#!/usr/bin/env python3
"""Gate de linhas e decisoes JaCoCo nos metodos financeiros P1.

Se o relatorio ou os metodos estiverem ausentes, falha (fail closed).
Nao confundir cobertura com deteccao efetiva de defeitos.
"""
import argparse
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

CRITICAL_CLASS = "Expense_Tracker/ExpenseTracker"
CRITICAL_METHODS = {
    "addExpense", "updateExpense", "viewSummary", "viewMonthlySummary",
    "filterByCategory", "viewCategorySummary", "manageBudget",
    "warnIfOverBudget", "monthTotal",
}
MIN_LINE = 0.85
MIN_BRANCH = 0.90


def evaluate(report_file: Path):
    tree = ET.parse(report_file)
    root = tree.getroot()
    classes = root.findall(".//class")
    target = next((cls for cls in classes if cls.get("name") == CRITICAL_CLASS), None)
    if target is None:
        raise ValueError(f"Classe critica ausente do JaCoCo: {CRITICAL_CLASS}")

    methods = {m.get("name"): m for m in target.findall("method")}
    missing = sorted(CRITICAL_METHODS - methods.keys())
    if missing:
        raise ValueError("Metodos criticos nao encontrados: " + ", ".join(missing))

    totals = {"LINE": {"covered": 0, "missed": 0}, "BRANCH": {"covered": 0, "missed": 0}}
    detail = {}
    for name in sorted(CRITICAL_METHODS):
        element = methods[name]
        row = {}
        for counter_name in totals:
            counter = next((c for c in element.findall("counter") if c.get("type") == counter_name), None)
            if counter is None:
                if counter_name == "BRANCH":
                    continue  # Um metodo sem ramos nao conta no denominador de decisoes.
                raise ValueError(f"Contador {counter_name} ausente no metodo: {name}")
            covered = int(counter.get("covered", "0"))
            missed = int(counter.get("missed", "0"))
            totals[counter_name]["covered"] += covered
            totals[counter_name]["missed"] += missed
            row[counter_name] = {"covered": covered, "missed": missed}
        detail[name] = row

    def ratio(typ):
        c = totals[typ]["covered"]
        m = totals[typ]["missed"]
        return c / (c + m) if c + m else None

    line, branch = ratio("LINE"), ratio("BRANCH")
    if line is None or branch is None:
        raise ValueError("Cobertura nao mensuravel: denominadores nulos")
    passed = line >= MIN_LINE and branch >= MIN_BRANCH
    return {
        "class": CRITICAL_CLASS,
        "methods": sorted(CRITICAL_METHODS),
        "line": {**totals["LINE"], "ratio": round(line, 6), "minimum": MIN_LINE},
        "branch": {**totals["BRANCH"], "ratio": round(branch, 6), "minimum": MIN_BRANCH},
        "passed": passed,
        "method_detail": detail,
        "note": "Indicador de cobertura nos metodos P1; nao prova ausencia de defeitos.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report", nargs="?", default="target/site/jacoco/jacoco.xml")
    ap.add_argument("--output", default="target/quality-gate.json")
    args = ap.parse_args()
    try:
        result = evaluate(Path(args.report))
    except (OSError, ET.ParseError, ValueError) as exc:
        result = {"passed": False, "error": str(exc)}

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
