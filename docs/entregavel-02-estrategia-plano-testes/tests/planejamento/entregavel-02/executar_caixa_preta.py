#!/usr/bin/env python3
"""A3-QA: verificações black-box de planejamento (IA-assistidas; NAO braço humano).
Executar: python3 tests/planejamento/entregavel-02/executar_caixa_preta.py --src src/Expense_Tracker --out evidencias/entregavel-02
Usa apenas Python stdlib e JDK. Recria ambiente temporário por caso; NÃO altera src.
"""
import argparse, hashlib, json, platform, subprocess, tempfile, time
from datetime import datetime, timezone
from pathlib import Path


def add(amount, desc='Almoco', category='Alimentacao', date='2026-07-21'):
    return ['1',date,desc,str(amount),category]

def budget(amount,month='2026-07'):
    return ['8',month,str(amount)]

def run_script(cmds):
    return '\n'.join([*cmds,'0',''])

def case(id, group, technique, name, cmds, contains=(), excludes=(), file_contains=None, file_absent=(), rationale='', proposed=None):
    return dict(id=id, group=group, technique=technique, name=name, stdin=run_script(cmds), contains=list(contains), excludes=list(excludes), file_contains=file_contains or {}, file_absent=list(file_absent), rationale=rationale, proposed=proposed)

CASES = [
    case('CP-01','VAL','EP / BVA','Despesa R$ 0,01 válida',add('0.01'),['Expense added.'],['Amount must be greater than zero'], {'expenses.txt':'0.01'},rationale='valor positivo mínimo monetário escolhido'),
    case('CP-02','VAL','BVA','Despesa zero rejeitada',add('0'),['Amount must be greater than zero. Expense not added.'],['Expense added.'],{'expenses.txt':''},rationale='limite inferior inválido'),
    case('CP-03','VAL','BVA','Despesa negativa -0,01 rejeitada',add('-0.01'),['Amount must be greater than zero. Expense not added.'],['Expense added.'],rationale='imediatamente abaixo do zero'),
    case('CP-04','VAL','EP','Despesa positiva usual aceita',add('15.50'),['Expense added.'],file_contains={'expenses.txt':'15.5'},rationale='classe válida ordinária'),
    case('CP-05','VAL','EP','Texto alfabético rejeitado',add('abc'),['Invalid amount. Expense not added.'],['Expense added.'],rationale='classe de formato inválido'),
    case('CP-06','VAL','EP','NaN deve ser rejeitado',add('NaN'),['Invalid amount. Expense not added.'],['Expense added.'],rationale='pré-requisito proposto: somente reais finitos'),
    case('CP-07','VAL','EP','Infinity deve ser rejeitado',add('Infinity'),['Invalid amount. Expense not added.'],['Expense added.'],rationale='pré-requisito proposto: somente reais finitos'),
    case('CP-08','VAL','EP','-Infinity deve ser rejeitado',add('-Infinity'),excludes=['Expense added.'],rationale='classe especial negativa; mensagem pode ser de valor fora do intervalo'),
    case('CP-09','VAL','EP / BVA','Overflow numérico rejeitado',add('1e309'),['Invalid amount. Expense not added.'],['Expense added.'],rationale='overflow para infinito deve ser inválido'),
    case('CP-10','DATE','EP','Data bissexta válida 2024-02-29',add('1.00',date='2024-02-29'),['Expense added.'],file_contains={'expenses.txt':'2024-02-29'},rationale='classe data real válida'),
    case('CP-11','DATE','EP / BVA','Data impossível 2025-02-29', ['1','2025-02-29',''], ['Invalid date format. Please use YYYY-MM-DD.'],['Expense added.'],rationale='fevereiro não bissexto'),
    case('CP-12','DATE','EP','Mês inválido 2026-13', ['6','2026-13',''], ['Invalid month format. Please use YYYY-MM.'],rationale='partição de meses fora do intervalo'),
    case('CP-13','BUDGET','BVA','Orçamento zero permitido',budget('0'),['Budget for 2026-07 set to 0.0'],file_contains={'budgets.txt':'2026-07,0.0'},rationale='requisito proposto: orçamento não negativo, zero permite teto zero'),
    case('CP-14','BUDGET','BVA','Orçamento mínimo positivo',budget('0.01'),['Budget for 2026-07 set to 0.01'],file_contains={'budgets.txt':'2026-07,0.01'},rationale='valor imediatamente acima de zero'),
    case('CP-15','BUDGET','BVA','Orçamento negativo rejeitado',budget('-0.01'),['Invalid amount.'],['Budget for 2026-07 set to'],rationale='requisito proposto: orçamento não negativo'),
    case('CP-16','BUDGET','EP','Orçamento NaN rejeitado',budget('NaN'),['Invalid amount.'],['Budget for 2026-07 set to'],rationale='valor não numérico finito'),
    case('CP-17','BUDGET','EP','Orçamento Infinity rejeitado',budget('Infinity'),['Invalid amount.'],['Budget for 2026-07 set to'],rationale='valor não numérico finito'),
    case('CP-18','BUDGET','EP','Orçamento com texto rejeitado',budget('abc'),['Invalid amount.'],['Budget for 2026-07 set to'],rationale='formato inválido'),
    case('CP-19','BUDGET','BVA','Gasto abaixo do orçamento não alerta', [*budget('10'),*add('9.99')],['Expense added.'],['Warning: expenses for 2026-07'],rationale='limite inferior ao teto'),
    case('CP-20','BUDGET','BVA','Gasto igual ao orçamento não alerta', [*budget('10'),*add('10.00')],['Expense added.'],['Warning: expenses for 2026-07'],rationale='igualdade ao teto'),
    case('CP-21','BUDGET','BVA','Gasto acima do orçamento alerta', [*budget('10'),*add('10.01')],['Warning: expenses for 2026-07'],rationale='limite superior ao teto'),
    case('CP-22','SUMMARY','EP','Resumo soma valores corretamente', [*add('10.25'),*add('2.75'),'5'],['Total expenses: 13.00'],rationale='duas despesas válidas e total'),
    case('CP-23','SUMMARY','EP','Resumo do mês exclui mês distinto', [*add('10',date='2026-07-21'),*add('5',date='2026-08-21'),'6','2026-07'],['Total for 2026-07: 10.00'],rationale='partição pertence/não pertence ao mês'),
    case('CP-24','CATEGORY','EP','Filtro de categoria ignora maiúsculas', [*add('7',category='Food'),'7','food'],["Total for category 'food': 7.00"],rationale='comparação case-insensitive do filtro'),
    case('CP-25','DELETE','BVA','Índice -1 rejeitado', ['3','-1'],['Invalid index.'],rationale='índice abaixo do mínimo'),
    case('CP-26','DELETE','BVA','Índice 0 exclui registro', [*add('7'),'3','0','5'],['Expense deleted.','Total expenses: 0.00'],rationale='primeiro índice válido com um registro'),
    case('CP-27','UPDATE','BVA','Alteração de valor zero rejeitada', [*add('7'),'2','0','2026-07-21','Atualizada','0','5'],['Amount must be greater than zero. Expense not updated.','Total expenses: 7.00'],rationale='limite inferior em edição'),
    case('CP-28','UPDATE','EP','Alteração de valor NaN rejeitada', [*add('7'),'2','0','2026-07-21','Atualizada','NaN','5'],['Invalid amount. Expense not updated.','Total expenses: 7.00'],rationale='classe de valor especial inválido em edição'),
    case('CP-29','EXPORT','EP','Exportar descrição com vírgula mantém aspas', [*add('12.5',desc='cafe, bolo'),'9'],['Expenses exported to expenses_export.csv'],file_contains={'expenses_export.csv':'"cafe, bolo"'},rationale='serialização de CSV em integração'),
    case('CP-30','MENU','EP','Opção de menu fora do intervalo rejeitada', ['99'],['Invalid choice. Please try again.'],rationale='controle de opção de menu'),
]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--src',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args()
    src=a.src.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
    if not src.is_dir() or not list(src.glob('*.java')): raise SystemExit('Informe --src src/Expense_Tracker do repositório')
    with tempfile.TemporaryDirectory(prefix='a3_e2_build_') as td:
        build=Path(td);cmd=['javac','-encoding','UTF-8','-d',str(build),*[str(p) for p in sorted(src.glob('*.java'))]]
        start=time.perf_counter();cp=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30);btime=time.perf_counter()-start
        if cp.returncode!=0:raise SystemExit('Erro compilação:\n'+cp.stderr)
        records=[]
        for c in CASES:
            with tempfile.TemporaryDirectory(prefix=f'a3_e2_{c["id"]}_') as temp:
                t0=time.perf_counter();pr=subprocess.run(['java','-cp',str(build),'Expense_Tracker.ExpenseTracker'],input=c['stdin'],text=True,cwd=temp,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=12);elapsed=time.perf_counter()-t0
                output=pr.stdout+pr.stderr
                checks=[]
                for v in c['contains']:checks.append(dict(item=f'Contém {v!r}',ok=v in output))
                for v in c['excludes']:checks.append(dict(item=f'Não contém {v!r}',ok=v not in output))
                for filename,v in c['file_contains'].items():
                    p=Path(temp)/filename; content=p.read_text(errors='replace') if p.exists() else None
                    checks.append(dict(item=f'{filename} contém {v!r}' if v else f'{filename} existe',ok=(content is not None and v in content)))
                checks.append(dict(item='Código de saída 0',ok=pr.returncode==0))
                records.append({**c,'status':'PASSOU' if all(x['ok'] for x in checks) else 'FALHOU','checks':checks,'stdout':output,'returncode':pr.returncode,'duration_ms':round(elapsed*1000,1)})
    result={'gerado_em_utc':datetime.now(timezone.utc).isoformat(),'fonte_de_codigo':str(src),'sha256_fontes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(src.glob('*.java'))},'observacao':'Execução sobre cópia reconstruída do código; reproduzir no clone oficial identificado por SHA para evidência final','ambiente':{'java':subprocess.run(['java','-version'],capture_output=True,text=True).stderr.splitlines()[0],'python':platform.python_version(),'plataforma':platform.platform()},'compilacao_s':round(btime,4),'total':len(records),'passaram':sum(r['status']=='PASSOU' for r in records),'falharam':sum(r['status']=='FALHOU' for r in records),'casos':records}
    (out/'resultado_30_casos_caixa_preta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    md=['# Evidência — execução dos casos de caixa-preta (Entregável 2)','',f'**Data UTC:** {result["gerado_em_utc"]}  ',f'**Ambiente:** {result["ambiente"]["java"]}  ',f'**Compilação:** {btime:.3f} s  ',f'**Resultados:** {result["passaram"]}/{result["total"]} casos com todos os oráculos satisfeitos; {result["falharam"]} divergências.','','> Não confundir falha no oráculo com defeito confirmado sem validação da regra de negócio. Os casos são especificações inicialmente elaboradas com assistência de IA; não são a amostra manual independente da comparação do A3.','', '| Caso | Método | Cenário | Resultado |','|---|---|---|---|']
    for r in records: md.append(f'| {r["id"]} | {r["technique"]} | {r["name"]} | **{r["status"]}** |')
    md+=['','## Divergências','']
    for r in records:
        if r['status']=='FALHOU':
            md.append(f'### {r["id"]} — {r["name"]}')
            for ch in r['checks']:
                if not ch['ok']:md.append(f'- Critério não satisfeito: {ch["item"]}')
            md.append(f'- Comportamento observado (trecho): `{r["stdout"].strip().splitlines()[-1][:180] if r["stdout"].strip() else "sem saída"}`')
            md.append('')
    md+=['## Limitações','','- Executado sem alterações no programa e com dados isolados por cenário.', '- Regras de domínio propostas para valores financeiros finitos e orçamento não negativo exigem aprovação humana.', '- O relatório não contém cobertura JaCoCo e não fornece comparação com testes desenvolvidos manualmente.', '- Validar no repositório original fixado por commit SHA antes de utilizar como evidência final.', '']
    (out/'relatorio_execucao_30_casos.md').write_text('\n'.join(md),encoding='utf8')
    print(f"Casos: {result['total']}; passaram: {result['passaram']}; falharam: {result['falharam']}")
    print('Falharam:',', '.join(r['id'] for r in records if r['status']=='FALHOU'))
    return 0

if __name__=='__main__':raise SystemExit(main())
