#!/usr/bin/env python3
"""Reexecuta os 10 mesmos casos IA-01..IA-10 na baseline e no HEAD.

Execucao offline: --baseline-root e --after-root apontam para pastas com src/Expense_Tracker.
Execucao clonada: git show <ref>:src/... conserva revisoes exatas.
NÃO mede esforço humano de criar/revisar testes ou validação independente de oráculos.
"""
from __future__ import annotations
import argparse
import csv
import json
import hashlib
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

NAMES = ['ExpenseTracker.java','Expense.java','ExpenseStorage.java','BudgetStorage.java','CsvUtil.java','CsvUtilTest.java']
SCENARIOS = [
 {'id':'IA-01','name':'Despesa válida positiva','menu':['1','2026-11-05','A','15.50','Food','0'],'expected':['Expense added.'],'forbidden':[]},
 {'id':'IA-02','name':'Despesa zero rejeitada','menu':['1','2026-11-05','A','0','0'],'expected':['Expense not added.'],'forbidden':[]},
 {'id':'IA-03','name':'Despesa negativa rejeitada','menu':['1','2026-11-05','A','-10','0'],'expected':['Expense not added.'],'forbidden':[]},
 {'id':'IA-04','name':'Despesa não numérica rejeitada','menu':['1','2026-11-05','A','x','0'],'expected':['Invalid amount.'],'forbidden':[]},
 {'id':'IA-05','name':'Despesa NaN deve ser rejeitada (regra proposta)','menu':['1','2026-11-05','A','NaN','Food','0'],'expected':['Expense not added.'],'forbidden':[]},
 {'id':'IA-06','name':'Despesa Infinity deve ser rejeitada (regra proposta)','menu':['1','2026-11-05','A','Infinity','Food','0'],'expected':['Expense not added.'],'forbidden':[]},
 {'id':'IA-07','name':'Orçamento NaN deve ser rejeitado (regra proposta)','menu':['8','2026-11','NaN','0'],'expected':[],'forbidden':['set to NaN']},
 {'id':'IA-08','name':'Orçamento negativo deve ser rejeitado (regra proposta)','menu':['8','2026-11','-100','0'],'expected':[],'forbidden':['set to -100.0']},
 {'id':'IA-09','name':'Aviso quando gastos excedem orçamento','menu':['8','2026-11','50','1','2026-11-05','A','60','Food','0'],'expected':['Warning: expenses for 2026-11 total 60.00'],'forbidden':[]},
 {'id':'IA-10','name':'Soma mensal correta','menu':['1','2026-11-05','A','10','Food','1','2026-10-05','B','5','Food','6','2026-11','0'],'expected':['Total for 2026-11: 10.00'],'forbidden':[]},
]

def command(args, cwd=None, timeout=25):
    return subprocess.run(args,text=True,capture_output=True,cwd=cwd,timeout=timeout)

def get_git(reporoot, ref, relpath):
    p=command(['git','show',f'{ref}:{relpath}'],cwd=reporoot)
    if p.returncode: raise RuntimeError(f'git show {ref}:{relpath} falhou: {p.stderr.strip()}')
    return p.stdout

def snapshot(reporoot, ref, direct_root, dst):
    src=dst/'src'/'Expense_Tracker'; src.mkdir(parents=True,exist_ok=True)
    n=0
    hashes={}
    for name in NAMES+['FinancialRules.java']:
        if direct_root is not None:
            source=direct_root/'src'/'Expense_Tracker'/name
            if not source.is_file():
                if name=='FinancialRules.java': continue
                raise FileNotFoundError(source)
            data=source.read_text(encoding='utf-8')
        else:
            try: data=get_git(reporoot,ref,'src/Expense_Tracker/'+name)
            except RuntimeError:
                if name=='FinancialRules.java': continue
                raise
        encoded=data.encode('utf-8')
        (src/name).write_bytes(encoded);n+=1
        hashes[name]={'sha256': hashlib.sha256(encoded).hexdigest(),
          'git_blob_sha1': hashlib.sha1(b'blob '+str(len(encoded)).encode()+b'\0'+encoded).hexdigest()}
    return n,hashes

def compile_java(stage):
    build=stage/'classes';build.mkdir()
    src=stage/'src'/'Expense_Tracker'
    paths=sorted(str(p) for p in src.glob('*.java'))
    start=time.perf_counter()
    p=command(['javac','-encoding','UTF-8','-d',str(build),*paths],timeout=35)
    elapsed=time.perf_counter()-start
    if p.returncode: raise RuntimeError('Erro de compilacao: '+p.stderr[-4500:])
    return build,elapsed

def execute(build, scenario):
    with tempfile.TemporaryDirectory(prefix='a3_e10_caso_') as work:
        start=time.perf_counter()
        p=subprocess.run(['java','-cp',str(build),'Expense_Tracker.ExpenseTracker'],
                         input='\n'.join(scenario['menu'])+'\n',text=True,
                         capture_output=True,cwd=work,timeout=15)
        secs=time.perf_counter()-start
        passed=(p.returncode==0 and all(t in p.stdout for t in scenario['expected'])
                and all(t not in p.stdout for t in scenario['forbidden']))
        snippets=[line.strip() for line in p.stdout.splitlines() if any(w in line for w in
                  ['Expense added.','Expense not added.','Invalid amount.','set to ','Warning:',
                   'Total for ','Budget for ','Expenses saved.'])]
        return {'id':scenario['id'],'name':scenario['name'],'passed':passed,
                'return_code':p.returncode,'runtime_seconds':round(secs,5),
                'relevant_output':snippets,'stderr':p.stderr[-300:]}

def run_version(repo,ref,source,stage):
    files,hashes=snapshot(repo,ref,source,stage)
    build,compile_sec=compile_java(stage)
    cases=[execute(build,s) for s in SCENARIOS]
    return {'ref':ref if source is None else str(source),'source_files_compiled':files,'source_file_hashes':hashes,
            'compile_seconds':round(compile_sec,4),'tests_passed':sum(c['passed'] for c in cases),
            'total_tests':len(cases),'tests':cases,
            'tests_runtime_seconds':round(sum(c['runtime_seconds'] for c in cases),4)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',default='.',help='Repositorio clonado com baseline tag e branch')
    ap.add_argument('--baseline-ref',default='v0.1.0-baseline')
    ap.add_argument('--after-ref',default='HEAD')
    ap.add_argument('--baseline-label',default=None,help='Rotulo auditavel da baseline local')
    ap.add_argument('--after-label',default=None,help='Rotulo auditavel da versao posterior local')
    ap.add_argument('--baseline-root',type=Path,help='Opcional: fonte local para rodar sem git')
    ap.add_argument('--after-root',type=Path,help='Opcional: fonte local para rodar sem git')
    ap.add_argument('--out',type=Path,default=Path('evidencias/entregavel-10'))
    args=ap.parse_args()
    repo=Path(args.repo).resolve();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='a3_e10_snapshots_') as temp:
        work=Path(temp)
        before=run_version(repo,args.baseline_ref,args.baseline_root,work/'baseline')
        after=run_version(repo,args.after_ref,args.after_root,work/'after')
    if args.baseline_label: before['ref']=args.baseline_label
    if args.after_label: after['ref']=args.after_label
    rows=[]
    for a,b in zip(before['tests'],after['tests']):
        assert a['id']==b['id']
        effect=('corrigido' if not a['passed'] and b['passed'] else 'regressao'
                if a['passed'] and not b['passed'] else 'mantido_aprovado'
                if a['passed'] else 'ainda_divergente')
        rows.append({'id':a['id'],'name':a['name'],'before':a['passed'],
                     'after':b['passed'],'effect':effect,
                     'before_runtime_seconds':a['runtime_seconds'],
                     'after_runtime_seconds':b['runtime_seconds']})
    obj={'experiment':'E10 – comparacao antes/depois de oraculos predefinidos com IA',
        'measured_at_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'10 cenarios do piloto IA, mesmos comandos e mesmos oraculos',
        'baseline':before,'after':after,
        'comparison':{'before_pass':before['tests_passed'],'after_pass':after['tests_passed'],
          'resolved_case_ids':[x['id'] for x in rows if x['effect']=='corrigido'],
          'regression_case_ids':[x['id'] for x in rows if x['effect']=='regressao'],
          'cases':rows},
        'validity':'Mudanca de software e de testes nao prova superioridade de IA sobre teste humano. Regras propostas devem ser validadas por um humano. Tempos apenas de execucao de 10 casos, nunca de criacao/revisao. '
        'Versao local usada, quando --baseline-root/--after-root, deve ser conferida contra os SHAs Git.'}
    (out/'resultado_comparativo.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    with (out/'resultado_casos.csv').open('w',encoding='utf8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['id','name','before','after','effect',
                    'before_runtime_seconds','after_runtime_seconds']);writer.writeheader();writer.writerows(rows)
    print(json.dumps({'baseline':before['tests_passed'],'after':after['tests_passed'],
        'resolved':obj['comparison']['resolved_case_ids'],
        'regressions':obj['comparison']['regression_case_ids']},ensure_ascii=False))
    return 0

if __name__=='__main__':
    try: raise SystemExit(main())
    except (FileNotFoundError,RuntimeError,subprocess.TimeoutExpired) as exc:
        print('E10 FALHA: '+str(exc),file=sys.stderr);raise SystemExit(2)
