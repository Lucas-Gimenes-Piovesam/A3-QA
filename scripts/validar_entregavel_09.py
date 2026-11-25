#!/usr/bin/env python3
"""Validação estática do pacote documental E9. Sem alterar o código Java."""
from pathlib import Path
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "entregavel-09-manutencao-evolucao"
EV = ROOT / "evidencias" / "entregavel-09"
REQUIRED = [
    DOC / "00-LEIA-ME.md", DOC / "01-inspecao-e-metodo.md",
    DOC / "02-matriz-solicitacoes-e-impactos.md",
    DOC / "03-adr-decisao-refatorar-modernizar-substituir.md",
    DOC / "04-plano-de-execucao-e-regressao.md",
    DOC / "05-evidencias-e-limitacoes.md", DOC / "06-checklist-e-aprovacao.md",
    DOC / "painel-manutencao.html", EV / "solicitacoes.csv",
    EV / "impactos.csv", EV / "decisao-alternativas.csv",
    EV / "inspecao-repositorio.json",
]


def load_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    errors = []
    for f in REQUIRED:
        if not f.is_file():
            errors.append(f"Arquivo ausente: {f.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors))
        return 1

    reqs = load_csv(EV / "solicitacoes.csv")
    ids = [r["id"] for r in reqs]
    if len(reqs) < 3 or len(set(ids)) != len(ids):
        errors.append("É obrigatório haver ao menos 3 IDs distintos")
    for r in reqs:
        if not (r["tipo"] and r["estado"] and r["prioridade"]):
            errors.append(f"Classificação incompleta: {r['id']}")
        p = ROOT / r["arquivo"]
        if not p.is_file():
            errors.append(f"Documento da CR ausente: {r['arquivo']}")
        if r["estado"] == "proposta" and not r["esforco_sp"]:
            errors.append(f"Sem estimativa relativa de tarefa proposta: {r['id']}")

    impacts = load_csv(EV / "impactos.csv")
    for r in impacts:
        if r["cr_id"] not in ids:
            errors.append("Impacto referencia ID inexistente: " + r["cr_id"])
    for id_ in ids:
        if not any(r["cr_id"] == id_ for r in impacts):
            errors.append("CR sem impacto documentado: " + id_)
    weights = load_csv(EV / "decisao-alternativas.csv")
    total_weight = sum(float(r["peso"]) for r in weights)
    if abs(total_weight - 1.0) > 1e-8:
        errors.append("Pesos da ADR não totalizam 100%")
    scores = {col: sum(float(r["peso"]) * int(r[col]) for r in weights)
              for col in ("refatorar_nota", "modernizar_nota", "substituir_nota")}
    if not (scores["refatorar_nota"] > scores["modernizar_nota"] > scores["substituir_nota"]):
        errors.append("Ranking da ADR mudou: revisar justificativa")
    inspection = json.loads((EV / "inspecao-repositorio.json").read_text(encoding="utf-8"))
    if len(inspection.get("commit_main_inspecionado", "")) != 40:
        errors.append("SHA inspecionado ausente ou incorreto")
    print(f"CRs: {len(reqs)}; impactos: {len(impacts)}; pesos: {total_weight:.2f}")
    print("Pontuação: " + ", ".join(f"{k.replace('_nota', '')}={v:.2f}" for k, v in scores.items()))
    if errors:
        for error in errors:
            print("ERRO:", error)
        return 1
    print("PASSOU: pacote documental e matriz coerentes (não equivale a execução de mudanças).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
