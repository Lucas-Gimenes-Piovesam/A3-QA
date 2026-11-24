#!/usr/bin/env python3
"""Testes exploratorios externos: nao altera a aplicacao original.
Executar depois de compilar: python3 evidencias/testar_linha_base.py
"""
import csv
import json
import os
from pathlib import Path
import re
import statistics
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT/'src'
BUILD = ROOT/'build'
EV = ROOT/'evidencias'
EV.mkdir(exist_ok=True)

runs=[]
for i in range(7):
    with tempfile.TemporaryDirectory(prefix='a3_build_') as d:
        start=time.perf_counter()
        p=subprocess.run(['javac','-encoding','UTF-8','-d',d, *[str(p) for p in sorted((SRC/'Expense_Tracker').glob('*.java'))]],capture_output=True,text=True)
        elapsed=time.perf_counter()-start
        runs.append(round(elapsed, 4))
        if p.returncode:
            raise RuntimeError('Falha na compilacao: '+p.stderr)

res=[]
def run_case(name, input_lines, expected, expect_file=None, expect_csv=None, observation=None):
    with tempfile.TemporaryDirectory(prefix='a3_case_') as d:
        data='\n'.join(input_lines)+'\n'
        t0=time.perf_counter()
        p=subprocess.run(['java','-cp',str(BUILD),'Expense_Tracker.ExpenseTracker'],cwd=d,input=data,capture_output=True,text=True,timeout=10)
        duration=round(time.perf_counter()-t0,4)
        checks=[s in p.stdout for s in expected]
        filetext=None
        if expect_file is not None:
            fp=Path(d)/'expenses.txt'
            filetext=fp.read_text() if fp.exists() else ''
            checks.append(expect_file in filetext)
        exported_rows=None
        if expect_csv is not None:
            fp=Path(d)/'expenses_export.csv'
            if fp.exists():
                with open(fp,encoding='UTF-8',newline='') as f: exported_rows=list(csv.reader(f))
            checks.append(exported_rows == expect_csv)
        item={'cenario':name, 'status':'CONFORME' if all(checks) and p.returncode==0 else 'DIVERGENCIA',
            'esperado':expected, 'encontrado':p.stdout.strip(), 'codigo_saida':p.returncode,
            'duracao_s':duration,'observacao':observation,
            'arquivo_despesas':filetext, 'csv_exportado':exported_rows}
        res.append(item)
        return item

run_case('01 - Sair do programa vazio', ['0'], ['Expenses saved. Exiting...'])
run_case('02 - Adicionar despesa valida', ['1','2026-11-05','Cafe','15.50','Food','5','0'], ['Expense added.','Total expenses: 15.50'], expect_file='2026-11-05,Cafe,15.5,Food')
run_case('03 - Rejeitar valor zero', ['1','2026-11-05','Teste','0','5','0'], ['Amount must be greater than zero. Expense not added.','Total expenses: 0.00'])
run_case('04 - Rejeitar valor negativo', ['1','2026-11-05','Teste','-10','5','0'], ['Amount must be greater than zero. Expense not added.','Total expenses: 0.00'])
run_case('05 - Rejeitar valor nao numerico', ['1','2026-11-05','Teste','abc','5','0'], ['Invalid amount. Expense not added.','Total expenses: 0.00'])
run_case('06 - Rejeitar data invalida e pedir outra', ['1','2026-02-30','2026-02-28','A','2','Food','0'], ['Invalid date format. Please use YYYY-MM-DD.','Expense added.'])
run_case('07 - Somatorio mensal', ['1','2026-11-05','A','10','Food','1','2026-10-05','B','5','Food','6','2026-11','0'], ['Total for 2026-11: 10.00'])
run_case('08 - Indice de exclusao invalido', ['3','99','0'], ['Invalid index.'])
run_case('09 - Atualizar despesa', ['1','2026-11-05','A','10','Food','2','0','2026-11-05','B','20','Food','5','0'], ['Expense updated.','Total expenses: 20.00'])
run_case('10 - Exportar CSV com virgula e aspas', ['1','2026-11-05','Cafe, "bom"','8','Food','9','0'], ['Expenses exported to expenses_export.csv'], expect_csv=[['date','description','amount','category'],['2026-11-05','Cafe, "bom"','8.0','Food']])
run_case('11 - Aviso de orçamento estourado', ['8','2026-11','50','1','2026-11-05','A','60','Food','0'], ['Budget for 2026-11 set to 50.0','Warning: expenses for 2026-11 total 60.00, exceeding the budget of 50.00.'])
run_case('12 - Agrupar categorias sem diferenciar caixa', ['1','2026-11-05','A','10','Food','1','2026-11-06','B','20','food','10','0'], ['Food: 30.00 (2 expenses)','Total expenses: 30.00'])
run_case('13 - Valor NaN aceito no cadastro', ['1','2026-11-05','A','NaN','Food','5','0'], ['Expense added.','Total expenses: NaN'], expect_file='2026-11-05,A,NaN,Food', observation='Comportamento de risco: Java aceita NaN como double; total deixa de representar valor financeiro.')
run_case('14 - Valor Infinity aceito no cadastro', ['1','2026-11-05','A','Infinity','Food','5','0'], ['Expense added.','Total expenses: Infinity'], expect_file='2026-11-05,A,Infinity,Food', observation='Comportamento de risco: Java aceita Infinity como double; total deixa de representar valor financeiro.')
run_case('15 - Orcamento negativo aceito', ['8','2026-11','-100','0'], ['Budget for 2026-11 set to -100.0'], observation='Risco possivel: orcamento negativo e aceito, requer especificacao de negocio.')
run_case('16 - Orcamento NaN aceito', ['8','2026-11','NaN','0'], ['Budget for 2026-11 set to NaN'], observation='Risco: limite financeiro nao finito e aceito, prejudica comparacoes.')
run_case('17 - Despesa com descricao vazia aceita', ['1','2026-11-05','','5','Food','0'], ['Expense added.'], observation='A definir: descricao vazia e permitida pelas regras?')

p=subprocess.run(['java','-cp',str(BUILD),'Expense_Tracker.CsvUtilTest'],capture_output=True,text=True,timeout=10)
native_test={'resultado':p.stdout.strip(),'codigo_saida':p.returncode,'cenarios_no_codigo':4}

metrics={
  'data_analise':'2026-11-24',
  'origem':'Codigo-fonte publico consultado em github.com/chaudhary-lakshay/Expense-Tracker main; copia local manual das seis classes; nao e git clone',
  'jdk':'OpenJDK 21',
  'arquivos_java':len(list((SRC/'Expense_Tracker').glob('*.java'))),
  'linhas_fonte_java':sum(len(p.read_text().splitlines()) for p in (SRC/'Expense_Tracker').glob('*.java')),
  'compilacao':{'sucessos':len(runs),'amostras_s':runs,'media_s':round(statistics.mean(runs),3),'mediana_s':round(statistics.median(runs),3),'min_s':round(min(runs),3),'max_s':round(max(runs),3)},
  'teste_nativo_csv': native_test,
  'exploratorios': {'total':len(res),'cenarios_sem_divergencia_de_expectativa':sum(i['status']=='CONFORME' for i in res), 'observacoes_risco':sum(bool(i['observacao']) for i in res)},
  'cobertura_percentual':'NAO MEDIDA - projeto nao inclui agente de cobertura e ambiente sem JaCoCo',
  'lead_time':'NAO MEDIDO - sem metadados confiaveis do fluxo de trabalho do grupo',
  'pipeline_ci':'Nao identificado no repositorio consultado',
  'observacao_metodologica':'CONFORME significa que comportamento esperado pelo script ocorreu, nao que seja requisito de negocio correto. Casos 13-16 sao observacoes de riscos; o codigo original nao foi alterado.'
}
(EV/'resultados_cenarios.json').write_text(json.dumps(res,indent=2,ensure_ascii=False),encoding='utf-8')
(EV/'metricas_linha_base.json').write_text(json.dumps(metrics,indent=2,ensure_ascii=False),encoding='utf-8')
(EV/'saida_teste_nativo.txt').write_text(p.stdout+('\n'+p.stderr if p.stderr else ''),encoding='utf-8')
print(json.dumps(metrics,ensure_ascii=False,indent=2))
