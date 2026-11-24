#!/usr/bin/env python3
"""PILOTO DE IA para A3 - testes de regras de negocio sugeridas pelo assistente.
Nao altera codigo original. Os requisitos de finitude e nao-negatividade devem
ser validados pelo grupo/professor antes de chamar os desvios de defeitos confirmados.
"""
import json
import subprocess
import tempfile
from pathlib import Path
from time import perf_counter

HERE=Path(__file__).resolve().parent
BUILD=HERE.parent/'build'
scenarios=[
 {'id':'IA-01','nome':'Despesa válida positiva','menu':['1','2026-11-05','A','15.50','Food','0'],'aceita':['Expense added.']},
 {'id':'IA-02','nome':'Despesa zero rejeitada','menu':['1','2026-11-05','A','0','0'],'aceita':['Expense not added.']},
 {'id':'IA-03','nome':'Despesa negativa rejeitada','menu':['1','2026-11-05','A','-10','0'],'aceita':['Expense not added.']},
 {'id':'IA-04','nome':'Despesa não numérica rejeitada','menu':['1','2026-11-05','A','x','0'],'aceita':['Invalid amount.']},
 {'id':'IA-05','nome':'Despesa NaN deve ser rejeitada (regra proposta)','menu':['1','2026-11-05','A','NaN','Food','0'],'aceita':['Expense not added.']},
 {'id':'IA-06','nome':'Despesa Infinity deve ser rejeitada (regra proposta)','menu':['1','2026-11-05','A','Infinity','Food','0'],'aceita':['Expense not added.']},
 {'id':'IA-07','nome':'Orçamento NaN deve ser rejeitado (regra proposta)','menu':['8','2026-11','NaN','0'],'proibida':['set to NaN']},
 {'id':'IA-08','nome':'Orçamento negativo deve ser rejeitado (regra proposta)','menu':['8','2026-11','-100','0'],'proibida':['set to -100.0']},
 {'id':'IA-09','nome':'Aviso quando gastos excedem orçamento','menu':['8','2026-11','50','1','2026-11-05','A','60','Food','0'],'aceita':['Warning: expenses for 2026-11 total 60.00']},
 {'id':'IA-10','nome':'Soma mensal correta','menu':['1','2026-11-05','A','10','Food','1','2026-10-05','B','5','Food','6','2026-11','0'],'aceita':['Total for 2026-11: 10.00']},
]
results=[]
t0=perf_counter()
for s in scenarios:
    with tempfile.TemporaryDirectory(prefix='a3_piloto_ia_') as d:
        p=subprocess.run(['java','-cp',str(BUILD),'Expense_Tracker.ExpenseTracker'],input='\n'.join(s['menu'])+'\n',text=True,capture_output=True,cwd=d,timeout=10)
        passed=p.returncode==0 and all(x in p.stdout for x in s.get('aceita',[])) and all(x not in p.stdout for x in s.get('proibida',[]))
        results.append({'id':s['id'],'cenario':s['nome'],'resultado':'PASSOU' if passed else 'FALHOU','saida_relevante':[line.strip() for line in p.stdout.splitlines() if ('Expense added.' in line or 'Expense not added.' in line or 'set to ' in line or 'Warning:' in line or 'Total for ' in line or 'Invalid amount.' in line)]})
(EHERE:=HERE/'resultado_piloto_ia.json').write_text(json.dumps({'total':len(results),'passou':sum(r['resultado']=='PASSOU' for r in results),'falhou':sum(r['resultado']=='FALHOU' for r in results),'duracao_s':round(perf_counter()-t0,3),'ressalva':'Regras financeiras propostas, não especificação original; não compara com testes independentes do grupo','casos':results},ensure_ascii=False,indent=2),encoding='utf8')
print(EHERE.read_text())
