#!/usr/bin/env python3
"""Validação OFFLINE de consistência do Entregável 8.

Não acessa GitHub nem prova que as ações foram executadas: confere o pacote
contra seu snapshot e requisitos mínimos da rubrica interna.
"""
from pathlib import Path
import argparse, csv, json, sys

def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root)
    ev = root / "evidencias" / "entregavel-08"
    snap = json.loads((ev / "coleta-github-2026-11-25.json").read_text(encoding="utf-8"))
    rows = read_rows(ev / "matriz-diagnostico.csv")
    okrs = read_rows(ev / "roadmap-okrs.csv")
    actions = read_rows(ev / "plano-de-acoes.csv")
    assert len(rows) == 9, "O diagnóstico deve conter nove dimensões"
    assert all(int(x["pontuacao_interna"]) in (0, 1, 2) for x in rows)
    total = sum(int(x["pontuacao_interna"]) for x in rows)
    assert total == 11, f"Snapshot esperava 11/18, veio {total}/18"
    assert len(okrs) == 9 and len(set(x["kr_id"] for x in okrs)) == 9
    assert len(set(x["objetivo_id"] for x in okrs)) == 3
    assert len(actions) >= 3
    prs = snap["prs"]
    assert len(prs) == 3 and all(p["merged_at"] and p["reviewer_aprovador"] for p in prs)
    runs = snap["workflows"]
    s = sum(x["result"] == "success" for x in runs)
    assert (len(runs), s) == (11, 6)
    print(json.dumps({"status":"OK", "dimensoes":len(rows),"pontos_internos":total,
                      "maximo_interno":18,"objetivos":3,"krs":len(okrs),
                      "acoes":len(actions),"prs_integrados":len(prs),
                      "runs_ci":len(runs),"runs_verdes":s,
                      "observacao":"Verificacao do snapshot local, sem nova coleta"},
                     ensure_ascii=False, indent=2))
    return 0
if __name__ == "__main__":
    try: sys.exit(main())
    except (AssertionError, OSError, ValueError, KeyError) as e:
        print('INCONSISTENTE:', e, file=sys.stderr); sys.exit(1)
