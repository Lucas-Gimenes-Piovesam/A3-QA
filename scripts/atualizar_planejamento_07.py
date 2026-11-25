#!/usr/bin/env python3
"""Recalcula o comparativo de escopo em Story Points do A3-QA.

Nao infere horas de trabalho a partir de commits, PRs ou execucoes do CI.
Usa somente o backlog de subtarefas, com indicadores de evidencia revisados.
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def calcular(root: Path):
    base = root / 'evidencias' / 'entregavel-07'
    origem = base / 'backlog_subtarefas.csv'
    with origem.open(newline='', encoding='utf-8-sig') as file:
        linhas = list(csv.DictReader(file))
    if not linhas:
        raise ValueError('Backlog vazio')
    resultado = defaultdict(lambda: {'estimado_sp': 0, 'evidenciado_sp': 0, 'tarefas': 0, 'tarefas_evidenciadas': 0})
    ids = set()
    for item in linhas:
        id_ = item['id_subtarefa'].strip()
        if id_ in ids:
            raise ValueError('Subtarefa duplicada: ' + id_)
        ids.add(id_)
        entrega = item['entrega'].strip()
        status = item['status'].strip().lower()
        if status not in {'verificado', 'pendente'}:
            raise ValueError('Status invalido no item ' + id_)
        pontos = int(item['pontos_estimados'])
        if pontos <= 0:
            raise ValueError('Pontos devem ser inteiros positivos: ' + id_)
        if status == 'verificado' and not item['url_evidencia'].strip():
            raise ValueError('Item verificado sem link: ' + id_)
        d = resultado[entrega]
        d['estimado_sp'] += pontos
        d['evidenciado_sp'] += pontos if status == 'verificado' else 0
        d['tarefas'] += 1
        d['tarefas_evidenciadas'] += int(status == 'verificado')
    total_est = sum(v['estimado_sp'] for v in resultado.values())
    total_evd = sum(v['evidenciado_sp'] for v in resultado.values())
    dados = []
    for entrega in sorted(resultado, key=lambda x: int(x)):
        d = resultado[entrega]
        dados.append({
            'entrega': entrega,
            **d,
            'fracao_escopo_evidenciado': round(d['evidenciado_sp']/d['estimado_sp'], 4)
        })
    csv_path = base / 'comparativo_sp.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        colunas = ['entrega', 'estimado_sp', 'evidenciado_sp', 'tarefas', 'tarefas_evidenciadas', 'fracao_escopo_evidenciado']
        w = csv.DictWriter(f, fieldnames=colunas)
        w.writeheader()
        w.writerows(dados)
    resumo = {
        'metodo': 'story points / escopo evidenciado, nao horas trabalhadas',
        'estimativa_registrada': '2026-11-25 UTC; entregas 1-6: retrospectiva; entregas 7-10: prospectiva',
        'quantidade_entregas': len(resultado),
        'estimado_total_sp': total_est,
        'evidenciado_total_sp': total_evd,
        'pendente_total_sp': total_est-total_evd,
        'fracao_escopo_evidenciado': round(total_evd/total_est, 4),
        'horas_reais': None,
        'motivo_horas_ausentes': 'Nenhum apontamento individual de tempo fornecido pelo grupo',
        'nota': 'Status de cada subtarefa e uma avaliacao preliminar com links; exige validacao do grupo. Pontos evidenciados nao sao SP de esforco consumido.',
        'entregas': dados,
    }
    (base/'resumo_planejamento.json').write_text(json.dumps(resumo, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f'Planejado: {total_est} SP; evidenciado: {total_evd} SP; pendente: {total_est-total_evd} SP')
    print(f'Progresso do escopo ponderado: {total_evd/total_est:.1%}; horas reais: nao medidas')
    return resumo

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Gera comparativo do Entregavel 7')
    p.add_argument('--root', type=Path, default=Path('.'))
    calcular(p.parse_args().root)
