#!/usr/bin/env python3
"""Gera HTML estático do experimento E10 a partir do JSON medido."""
import html
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'evidencias/entregavel-10/resultado_comparativo.json').read_text(encoding='utf8'))
rows=data['comparison']['cases']
render='\n'.join(f'''<tr><td><code>{html.escape(x['id'])}</code></td><td>{html.escape(x['name'])}</td><td><span class="status {'ok' if x['before'] else 'fail'}">{'Conforme' if x['before'] else 'Divergente'}</span></td><td><span class="status {'ok' if x['after'] else 'fail'}">{'Conforme' if x['after'] else 'Divergente'}</span></td><td>{'Corrigido' if x['effect']=='corrigido' else 'Mantido'}</td></tr>''' for x in rows)
nb=data['baseline']['tests_passed'];na=data['after']['tests_passed']
page=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>A3 · Experimento de Inovação</title><style>
:root{{--bg:#f5f7fb;--ink:#1b2943;--muted:#5b6a80;--line:#dce3ec;--green:#007e68;--red:#b44352;--blue:#214775;--card:#fff}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}}
main{{max-width:1120px;margin:auto;padding:44px 24px 65px}}h1{{font-size:clamp(29px,4vw,43px);margin:8px 0 9px;line-height:1.16}}h2{{font-size:23px;margin:30px 0 10px}}
small,.muted{{color:var(--muted)}}.eyebrow{{letter-spacing:.12em;font-size:12px;color:var(--blue);font-weight:800;text-transform:uppercase}}
.lead{{max-width:750px;color:var(--muted);font-size:17px}}.metrics{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:15px;margin:30px 0}}
.card{{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:23px;box-shadow:0 4px 12px #20304409}}
.metric{{font-size:42px;font-weight:760;letter-spacing:-.04em;line-height:1.12;margin:4px 0}}.metric.bad{{color:var(--red)}}.metric.good{{color:var(--green)}}
.metricname{{font-size:13px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.035em}}.row{{display:flex;align-items:center;justify-content:space-between;gap:12px}}
.barbg{{background:#e2e8f0;height:11px;border-radius:30px;overflow:hidden;margin:17px 0 5px}}.bar{{height:100%;background:#b15a62;border-radius:30px}}.bar.green{{background:#079479}}
table{{width:100%;border-collapse:collapse;text-align:left;background:white}}th,td{{padding:11px 13px;border-bottom:1px solid var(--line);font-size:14px}}th{{background:#eff3f9;color:#334765;font-weight:700}}.tablewrap{{overflow:auto;border-radius:14px;border:1px solid var(--line)}}
code{{font-family:Consolas,Monaco,monospace;font-size:12px}}.status{{font-weight:700;white-space:nowrap}}.status.ok{{color:var(--green)}}.status.fail{{color:var(--red)}}
.info{{border-left:3px solid var(--blue);padding:11px 17px;background:#eaf0f8;border-radius:0 12px 12px 0;margin:22px 0}}.foot{{border-top:1px solid var(--line);margin-top:25px;padding-top:18px;font-size:13px;color:var(--muted)}}
a{{color:#14589d}}@media(max-width:750px){{.metrics{{grid-template-columns:1fr}}main{{padding:27px 14px}}.card{{padding:18px}}}}@media print{{body{{background:white}}.card{{box-shadow:none}}}}
</style></head><body><main>
<div class="eyebrow">A3 · Gestão e Qualidade de Software · Entregável 10</div>
<h1>IA a serviço da qualidade</h1>
<p class="lead">Uma comparação reproduzível dos mesmos 10 casos de teste no Expense Tracker antes e depois de correções nas regras financeiras.</p>
<div class="metrics">
<div class="card"><div class="metricname">Baseline · v0.1.0</div><div class="metric bad">{nb}/10</div><div class="barbg"><div class="bar" style="width:{nb*10}%"></div></div><small>Casos conformes · versão inicial</small></div>
<div class="card"><div class="metricname">Versão corrigida</div><div class="metric good">{na}/10</div><div class="barbg"><div class="bar green" style="width:{na*10}%"></div></div><small>Casos conformes · código posterior</small></div>
<div class="card"><div class="metricname">Efeito observado</div><div class="metric good">+4</div><p style="margin:10px 0 0">Casos corrigidos; <b>0 regressões</b> observadas nos outros seis.</p></div>
</div>
<h2>Mesmos casos, dois estados de código</h2>
<div class="tablewrap"><table><thead><tr><th>Caso</th><th>Verificação</th><th>Antes</th><th>Depois</th><th>Efeito</th></tr></thead><tbody>{render}</tbody></table></div>
<div class="info"><b>Resultado importante ≠ hipótese completamente comprovada.</b> Os resultados mostram melhora da conformidade do software nos dez cenários. Não há cronometria de criação/revisão manual independente; a hipótese de reduzir o esforço com IA em ≥20% permanece <b>inconclusiva</b>.</div>
<h2>Desenho do experimento</h2><div class="metrics" style="margin-top:13px"><div class="card"><b>Hipótese</b><p>IA reduz ≥20% o tempo de criação, revisão e execução de testes sem perder capacidade de detectar falhas.</p></div><div class="card"><b>Intervenção</b><p>Validação de despesas e orçamento, tratamento de entradas e persistência, testes automatizados e integração CI.</p></div><div class="card"><b>Próximo passo</b><p>Comparar duas suítes independentes, medir tempo humano real e registrar oráculos corretos, erros e alucinações após revisão.</p></div></div>
<div class="foot"><p><b>Rastreabilidade:</b> baseline <code>6b55f9d3</code> · versão corrigida <code>f4abe2da</code> · teste <code>scripts/experimento_10.py</code> · resultados <code>evidencias/entregavel-10/resultado_comparativo.json</code>.</p><p>Os oráculos contêm regras propostas que necessitam validação do grupo. Esta é uma fotografia experimental de 25/11/2026, não um painel em tempo real.</p></div>
</main></body></html>'''
path=ROOT/'docs/entregavel-10-experimento-inovacao/painel-experimento.html'
path.write_text(page,encoding='utf8');print(path)
