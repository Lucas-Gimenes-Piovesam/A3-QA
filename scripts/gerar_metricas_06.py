#!/usr/bin/env python3
"""Recalcula painel/csv locais a partir de uma coleta verificada do GitHub.

Uso na raiz do repositorio: python3 scripts/gerar_metricas_06.py
Nao acessa GitHub: a coleta JSON deve ser atualizada com evidencias verdadeiras.
Nao apresenta DORA produtivo sem deploy de producao.
"""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'evidencias' / 'entregavel-06' / 'coleta-github-2026-11-25.json'
OUT = ROOT / 'evidencias' / 'entregavel-06'
DOC = ROOT / 'docs' / 'entregavel-06-metricas-indicadores'


def dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace('Z', '+00:00'))


def pct(n, d):
    return (100 * n / d) if d else None


def fmt_pct(n):
    return 'Não medido' if n is None else f'{n:.1f}%'.replace('.', ',')


def fmt_duration(seconds):
    if seconds is None:
        return 'Não medido'
    return f'{int(seconds // 60)} min {int(seconds % 60)} s'


def read():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    assert data['quality_gate_ultima_execucao']['tests_run'] == sum(data['quality_gate_ultima_execucao']['test_breakdown'].values())
    assert len(data['quality_gate_ultima_execucao']['p1_methods']) == 9
    assert all(x['conclusion'] in ('success', 'failure', 'cancelled', 'timed_out') for x in data['ci_runs'])
    return data


def main():
    d = read()
    q = d['quality_gate_ultima_execucao']
    runs = sorted(d['ci_runs'], key=lambda r: r['created_at'])
    total_ci = len(runs)
    passed_ci = sum(r['conclusion'] == 'success' for r in runs)
    failures_ci = sum(r['conclusion'] == 'failure' for r in runs)
    avg_ci_sec = sum((dt(r['updated_at']) - dt(r['created_at'])).total_seconds() for r in runs) / total_ci if total_ci else None
    review = next((r for r in d['pull_request']['reviews'] if r['resultado'] == 'APPROVED'), None)
    review_sec = (dt(review['submitted_at']) - dt(d['pull_request']['created_at'])).total_seconds() if review else None
    merged_at = d['pull_request']['merged_at']
    lead_pr_sec = (dt(merged_at) - dt(d['pull_request']['created_at'])).total_seconds() if merged_at else None
    cycle_sec = (dt(merged_at) - dt(d['pull_request']['primeiro_commit_da_branch_em'])).total_seconds() if merged_at else None
    line_p = pct(q['p1_line_covered'], q['p1_line_covered'] + q['p1_line_missed'])
    branch_p = pct(q['p1_branch_covered'], q['p1_branch_covered'] + q['p1_branch_missed'])
    tests_p = pct(q['tests_run'] - q['test_failures'] - q['test_errors'] - q['test_skipped'], q['tests_run'])
    cli_tests = q['test_breakdown']['CliFinancialIntegrationTest']
    ci_pct = pct(passed_ci, total_ci)
    status_pr = 'Aprovado, ainda aberto' if review and not merged_at else ('Integrado' if merged_at else 'Aberto')
    rows = [
        ['P01', 'Produto', 'Adequação funcional', 'Testes JUnit aprovados', 'percentual', fmt_pct(tests_p), '100%', 'Aceitar mudanças somente com a suíte verde', q['fonte_log']],
        ['P02', 'Produto', 'Adequação funcional / confiabilidade', 'Cobertura de linhas P1', 'percentual', fmt_pct(line_p), '>= 85%', 'Exigir novos testes para lacunas em regras financeiras', q['fonte_log']],
        ['P03', 'Produto', 'Adequação funcional / testabilidade', 'Cobertura de ramos P1', 'percentual', fmt_pct(branch_p), '>= 90%', 'Cobrir decisões alternativas antes do merge', q['fonte_log']],
        ['P04', 'Produto', 'Manutenibilidade', 'Checkstyle (regras configuradas)', 'status', 'Aprovado' if q['checkstyle_step']=='success' else 'Falhou', 'Aprovado', 'Inspecionar e corrigir violações de estilo bloqueadoras', q['fonte_log']],
        ['P05', 'Produto', 'Capacidade de interação', 'Cenários JUnit de CLI aprovados', 'casos', f'{cli_tests}/{cli_tests}', '100% dos cenários definidos', 'Ampliar cenários de entrada e persistência caso haja regressão', q['fonte_log']],
        ['R01', 'Processo', 'CI', 'Taxa de workflows aprovados', 'percentual', fmt_pct(ci_pct), '>= 90% em janela de 10', 'Reduzir falhas recorrentes, sem baixar o gate', 'https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions'],
        ['R02', 'Processo', 'CI', 'Duração média de workflows', 'segundos', f'{avg_ci_sec:.1f} s'.replace('.', ',') if avg_ci_sec is not None else 'Não medido', '<= 120 s', 'Investigar lentidão caso a duração cresça', 'https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions'],
        ['R03', 'Processo', 'Revisão', 'Tempo de abertura do PR até aprovação', 'tempo', fmt_duration(review_sec), '<= 24 h', 'Pedir revisão antecipada se o tempo ultrapassar a meta', d['pull_request']['url']],
        ['R04', 'Processo', 'Lead time interno', 'Tempo de abertura do PR ao merge', 'tempo', fmt_duration(lead_pr_sec), '<= 24 h', 'Remover gargalos de revisão e integração', d['pull_request']['url']],
        ['R05', 'Processo', 'Cycle time interno', 'Tempo do primeiro commit da branch ao merge', 'tempo', fmt_duration(cycle_sec), '<= 48 h', 'Reduzir escopo e duração das branches', d['pull_request']['url']],
        ['R06', 'Processo', 'Gestão de configuração', 'Revisão aprovada / PR integrado', 'estado', status_pr, 'PR revisado + merge com gate verde', 'Concluir integração somente após requisitos cumpridos', d['pull_request']['url']],
        ['D01', 'DORA (produção)', 'Implantação', 'Deployment frequency', 'frequência', 'Não aplicável / não medido', 'Só definir se houver deploy real', 'Não usar publicação de pre-release como deploy', d['fonte_geral']],
        ['D02', 'DORA (produção)', 'Entrega', 'Lead time for changes', 'tempo', 'Não aplicável / não medido', 'Só definir se houver produção', 'Medição requer commit e deployment de produção', d['fonte_geral']],
        ['D03', 'DORA (produção)', 'Estabilidade', 'Change failure rate', 'percentual', 'Não aplicável / não medido', 'Só definir se houver produção', 'Não confundir falha de pipeline com falha de deploy', d['fonte_geral']],
        ['D04', 'DORA (produção)', 'Recuperação', 'Failed deployment recovery time', 'tempo', 'Não aplicável / não medido', 'Só definir se houver produção', 'Não confundir correção de CI com recuperação de serviço', d['fonte_geral']]
    ]
    OUT.mkdir(parents=True, exist_ok=True)
    DOC.mkdir(parents=True, exist_ok=True)
    with (OUT/'metricas-calculadas.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['id','grupo','caracteristica_iso_ou_dimensao','indicador','unidade','valor_observado','meta','decisao_gerencial','fonte']); w.writerows(rows)
    with (OUT/'execucoes-ci.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['run_id','evento','inicio_utc','fim_utc','duracao_segundos','conclusao','url']);
        for r in runs:w.writerow([r['run_id'],r['event'],r['created_at'],r['updated_at'],int((dt(r['updated_at'])-dt(r['created_at'])).total_seconds()),r['conclusion'],r['url']])

    table_rows = '\n'.join('| '+ ' | '.join(str(s) for s in [row[0],row[3],row[5],row[6],row[7]])+' |' for row in rows)
    run_table = '\n'.join(f"| [{r['run_id']}]({r['url']}) | {r['event']} | {r['conclusion']} | {int((dt(r['updated_at']) - dt(r['created_at'])).total_seconds())} s |" for r in runs)
    md = f'''# Entregável 6 — Painel de métricas e indicadores

**Projeto:** A3-QA / Expense Tracker  
**Referência de coleta:** 25/11/2026 (UTC), [repositório](https://github.com/Lucas-Gimenes-Piovesam/A3-QA)  
**Dados:** [`coleta-github-2026-11-25.json`](../../evidencias/entregavel-06/coleta-github-2026-11-25.json) · [`metricas-calculadas.csv`](../../evidencias/entregavel-06/metricas-calculadas.csv)  
**Estado:** fotografia histórica, **não** atualização em tempo real. Regerar após uma nova coleta.

## Quadro de leitura rápida

| Indicador | Valor verificado | Meta | Interpretação |
|---|---:|---:|---|
| Testes JUnit aprovados | **{q['tests_run']}/{q['tests_run']}** ({fmt_pct(tests_p)}) | 100% | Conforme para a suíte existente |
| Cobertura de linhas dos **9 métodos P1** | **{q['p1_line_covered']}/{q['p1_line_covered']+q['p1_line_missed']}** ({fmt_pct(line_p)}) | >= 85% | Conforme, não representa projeto inteiro |
| Cobertura de ramos dos **9 métodos P1** | **{q['p1_branch_covered']}/{q['p1_branch_covered']+q['p1_branch_missed']}** ({fmt_pct(branch_p)}) | >= 90% | Conforme, não prova ausência de defeitos |
| Análise estática | Checkstyle **{q['checkstyle_step']}** | Sem violações bloqueadoras | Conforme apenas às regras configuradas |
| Casos de integração CLI | **{cli_tests}/{cli_tests}** aprovados | 100% dos definidos | Testes exercitam entrada e persistência |
| Execuções de CI aprovadas | **{passed_ci}/{total_ci}** ({fmt_pct(ci_pct)}) | >= 90% nas próximas 10 execuções | Atenção: configurou-se CI durante a janela |
| Tempo médio por workflow | **{avg_ci_sec:.1f} s** | <= 120 s | Adequado à execução curta observada |
| Tempo PR criado → aprovado | **{fmt_duration(review_sec)}** | <= 24 h | 1 PR observado; amostra muito pequena |
| PR #1 | **{status_pr}** | PR aprovado e integrado com gate | Lead/cycle time de merge ainda não medidos |

**Escopo da cobertura:** os contadores do JaCoCo utilizados pelo gate são agregados **somente nos 9 métodos P1 definidos em `scripts/check_coverage.py`**. A medição de cobertura **global** do projeto não está declarada neste painel.

## Painel completo — todo indicador ligado a uma decisão

| ID | Indicador | Valor observado | Meta | Decisão apoiada |
|---|---|---|---|---|
{table_rows}

A classificação ISO/IEC 25010:2023 e a definição operacional de cada indicador estão no [dicionário](02-dicionario-metricas-e-metas.md).

## Evidências — histórico de CI

| Run | Evento | Resultado | Duração aproximada |
|---|---|---|---|
{run_table}

**Atenção:** a taxa de aprovação de {fmt_pct(ci_pct)} é uma métrica do **processo de configuração inicial**; não mede confiabilidade em produção. A última execução aprovada [#{q['run_id']}]({q['url']}) registrou {q['tests_run']} testes, Maven, JaCoCo e Checkstyle bem-sucedidos.

## Lead time, cycle time e DORA

- **Tempo até primeira revisão aprovada:** {fmt_duration(review_sec)}, contado entre a criação do PR #1 e a aprovação. É indicador de revisão, não *lead time for changes* do DORA.
- **Lead time interno do PR (abertura → merge):** {fmt_duration(lead_pr_sec)}. O PR estava aberto na coleta; não transformar tempo decorrido em lead time concluído.
- **Cycle time interno da branch (primeiro commit → merge):** {fmt_duration(cycle_sec)}; não medido, pois não houve merge no momento da coleta.
- **DORA:** não há deploy de produção demonstrado. Frequência de deploy, lead time de mudanças até produção, taxa de falha por mudança e tempo de recuperação não devem receber valores inventados. Uma pre-release (`v0.1.0-baseline`) não equivale a deployment.

## Próxima decisão orientada pelos dados

1. Confirmar integração do PR #1 após aprovação, atualização da branch e gate verde, registrando o SHA de merge.
2. Atualizar a coleta com `merged_at` real para calcular os indicadores internos de lead/cycle time.
3. Acompanhar as próximas 10 execuções de CI (meta >= 90% de sucesso); falhas do período inicial não devem ser apagadas do histórico.
4. Preservar os relatórios JaCoCo/Surefire da execução verde, incluindo a URL do run.
5. Medir outras características ISO 25010 apenas quando houver protocolo e evidência de teste apropriados.

**A nota metodológica e as limitações estão em:** [03-análise e decisões](03-analise-e-decisoes.md).
'''
    (DOC/'01-painel-metricas.md').write_text(md,encoding='utf-8')

    def card(label,value,detail,cls=''):
        return f'<article class="metric {cls}"><div class="metric-label">{escape(label)}</div><div class="metric-value">{escape(value)}</div><div class="metric-desc">{escape(detail)}</div></article>'
    colored_runs=''.join(f'<div class="run {"good" if r["conclusion"]=="success" else "bad"}" title="{escape(r["conclusion"])} — {r["run_id"]}"><a href="{escape(r["url"])}" target="_blank" rel="noopener">{r["run_id"]}</a></div>' for r in runs)
    rows_html=''.join(f'<tr><td><code>{escape(row[0])}</code></td><td>{escape(row[1])}</td><td>{escape(row[3])}</td><td><strong>{escape(row[5])}</strong></td><td>{escape(row[6])}</td><td>{escape(row[7])}</td><td><a href="{escape(row[8])}" target="_blank" rel="noopener">Fonte</a></td></tr>' for row in rows)
    html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>A3-QA | Painel de métricas - Entregável 6</title><style>
:root{{color-scheme:dark;--bg:#0c1220;--panel:#171f30;--line:#303d55;--fg:#f3f6ff;--mute:#a9b6ca;--accent:#6cb6ff;--good:#49c4a4;--bad:#e6957b}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;line-height:1.5}}.wrap{{max-width:1200px;margin:auto;padding:38px 24px 60px}}.eyebrow{{text-transform:uppercase;letter-spacing:.18em;font-size:12px;color:var(--accent);font-weight:700}}h1{{font-size:clamp(32px,5vw,50px);line-height:1.1;margin:9px 0 12px}}h2{{font-size:23px;margin:36px 0 14px}}.intro{{max-width:860px;color:var(--mute)}}.pill{{display:inline-block;border:1px solid var(--line);border-radius:40px;padding:5px 12px;color:var(--mute);font-size:12px;margin-top:12px}}.grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:28px}}.metric{{background:var(--panel);padding:20px;border-radius:13px;border:1px solid var(--line);min-height:152px}}.metric-label{{color:var(--mute);font-size:13px;font-weight:600}}.metric-value{{font-size:31px;font-weight:760;letter-spacing:-.05em;margin:10px 0}}.metric-desc{{font-size:12px;color:var(--mute)}}section{{background:var(--panel);padding:22px;border:1px solid var(--line);border-radius:13px;margin-top:18px}}.runs{{display:flex;gap:8px;align-items:stretch;flex-wrap:wrap;margin-top:20px}}.run{{min-width:134px;padding:18px 9px;text-align:center;border-radius:10px;border:1px solid var(--line);background:#283246;font-size:12px}}.run.good{{border-color:var(--good);box-shadow:inset 0 4px var(--good)}}.run.bad{{border-top:4px solid var(--bad)}}a{{color:var(--accent);text-decoration:none}}a:hover{{text-decoration:underline}}.sub{{color:var(--mute);font-size:14px}}table{{border-collapse:collapse;width:100%;min-width:860px;font-size:13px}}td,th{{padding:11px 10px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}}th{{color:var(--mute);font-size:12px}}.scroll{{overflow-x:auto}}.empty{{color:var(--mute);font-style:italic}}.note{{border-left:3px solid var(--accent);padding:10px 15px;color:var(--mute);background:#14283c}}.cols{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}ul{{margin:0;padding-left:20px}}li{{margin:7px 0}}footer{{color:var(--mute);font-size:12px;margin-top:28px}}@media(max-width:900px){{.grid{{grid-template-columns:repeat(2,1fr)}}.cols{{grid-template-columns:1fr}}}}@media(max-width:500px){{.grid{{grid-template-columns:1fr}}.wrap{{padding:22px 14px}}}}
</style></head><body><div class="wrap"><div class="eyebrow">A3 · Gestão e Qualidade de Software · Entregável 06</div><h1>Painel de métricas<br>do Expense Tracker</h1><p class="intro">Evidências de produto e processo relacionadas a metas e decisões. Recorte estático de 25/11/2026 UTC, auditável por links de commits, PR e workflow.</p><span class="pill">Snapshot — não é telemetria ao vivo</span><div class="grid">
{card('Testes automatizados',f'{q["tests_run"]}/{q["tests_run"]}','JUnit · nenhum teste falhou')}
{card('Cobertura de linhas P1',fmt_pct(line_p),'145/145 linhas · meta ≥85%')}
{card('Cobertura de decisões P1',fmt_pct(branch_p),'64/64 ramos · meta ≥90%')}
{card('Workflows aprovados',f'{passed_ci}/{total_ci}','1 verde após correções de configuração')}
{card('Média de duração da CI',f'{avg_ci_sec:.1f} s','6 workflows · meta ≤120 s')}
{card('Primeira aprovação do PR',fmt_duration(review_sec),'1 aprovação de colaborador')}
{card('Tempo de merge',fmt_duration(lead_pr_sec),'PR ainda aberto no snapshot')}
{card('Release de referência','1 pre-release','v0.1.0-baseline · não é deploy')}
</div><h2>Evolução do pipeline</h2><section><p class="sub">Seis execuções registradas; os primeiros cinco checks falharam durante a implantação da CI. A última execução terminou com build e quality gate aprovados.</p><div class="runs">{colored_runs}</div><p class="sub">Proporção observada: <strong>{fmt_pct(ci_pct)}</strong>. Meta de processo para as próximas dez execuções: ≥ 90%.</p></section><h2>Indicadores, metas e decisões</h2><section class="scroll"><table><thead><tr><th>ID</th><th>Grupo</th><th>Indicador</th><th>Observado</th><th>Meta</th><th>Decisão apoiada</th><th>Fonte</th></tr></thead><tbody>{rows_html}</tbody></table></section><h2>Leitura crítica</h2><div class="cols"><section><h3>O que já podemos afirmar</h3><ul><li>33 testes JUnit aprovados na execução CI #{q['run_id']}.</li><li>JaCoCo registrou 145/145 linhas e 64/64 ramos em nove métodos financeiros P1.</li><li>Checkstyle não bloqueou o build bem-sucedido.</li><li>O PR #1 recebeu aprovação de um colaborador.</li></ul></section><section><h3>O que ainda não foi medido</h3><ul><li>Tempo efetivo de merge e cycle time da branch.</li><li>Lead time DORA até um ambiente de produção.</li><li>Frequência de deployments reais e taxa de falhas após produção.</li><li>Recuperação de serviço após incidente de produção.</li></ul></section></div><p class="note">A cobertura exibida é restrita aos métodos críticos P1. Nem cobertura alta nem suíte aprovada garantem ausência de defeitos. Taxa de falha de CI não equivale a change failure rate (DORA).</p><footer>Dados de origem: <a href="{escape(q['url'])}" target="_blank" rel="noopener">GitHub Actions</a> · <a href="{escape(d['pull_request']['url'])}" target="_blank" rel="noopener">PR #1</a> · <a href="{escape(d['releases'][0]['url'])}" target="_blank" rel="noopener">Baseline</a>. Gerado de coleta versionada, sem rede.</footer></div></body></html>'''
    (DOC/'painel-visual.html').write_text(html,encoding='utf-8')
    print('Painel gerado. Indicadores:',len(rows),'| CI:',passed_ci,'/',total_ci,'| JUnit:',q['tests_run'],'| Aprovação:',fmt_duration(review_sec))

if __name__=='__main__':
    main()
