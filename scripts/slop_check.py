#!/usr/bin/env python3
"""
slop_check.py — universal AI-pattern linter.

Usage:
  python slop_check.py <file>           # check a file
  python slop_check.py -                # read stdin
  python slop_check.py --text "..."     # check inline text
  python slop_check.py --json <file>    # output JSON

Exit codes:
  0 — clean (no hard hits)
  1 — hard hits found (em-dash, banned closers/openers, scientific jargon, etc.)
  2 — only soft hits (adverbs, business jargon — informational)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Force UTF-8 stdout/stderr on Windows so Cyrillic + em-dashes render in cp1252 consoles
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HARD = "hard"
SOFT = "soft"

# In ad copy these work for competitors (Calm, Migraine Buddy), see anti-ai-patterns SKILL.md
AD_SOFT_PREFIXES = ("closing", "RU closing", "RU 'кто-нибудь", "AI opener", "RU AI opener")

# (severity, regex, label, suggest)
PATTERNS = [
    # ---- HARD: Zak's 6 rules + stop-slop critical ----
    (HARD, r"—", "em-dash", "Replace with comma/period/parens or rephrase"),
    (HARD, r"(?<=\w) – (?=\w)", "en-dash between words", "Use comma/period"),
    # Quotes around short phrases (3-6 words, no sentence punctuation inside)
    (HARD, r'"[A-Za-zА-Яа-яёЁ][\w\s\'\-]{2,40}?"(?!\s*[:,])',
     "quotes around short phrase (emphasis tell)",
     "Integrate phrase into sentence flow without quotes"),
    # Closing-question templates
    (HARD, r"\bI[' ]?m curious\b", "closing 'I'm curious' template",
     "Close on statement or trailing thought instead"),
    (HARD, r"\bI[' ]?d love to hear\b", "closing 'I'd love to hear' template",
     "Drop. Close on observation"),
    (HARD, r"\bI wonder if (anyone|other people|others)\b",
     "closing 'I wonder if others' template", "Close on statement"),
    (HARD, r"\bCurious what you think\b", "closing curiosity ping", "Drop"),
    (HARD, r"\bМне интересно (как|что)\b", "RU closing 'мне интересно'", "Закрой на утверждении"),
    (HARD, r"\bЛюбопытно (ваше|узнать)\b", "RU closing 'любопытно'", "Закрой на утверждении"),
    (HARD, r"\bКто-нибудь сталкивался\b", "RU 'кто-нибудь сталкивался'", "Перефразируй"),
    # Audience-targeting openers
    (HARD, r"(?im)^[\s>*-]*for (people|anyone) who\b",
     "AI opener 'for people/anyone who...'",
     "Replace: direct question / observational / personal-curiosity / question-as-title"),
    (HARD, r"(?im)^[\s>*-]*для тех,?\s*кто\b",
     "RU AI opener 'для тех, кто...'",
     "Вшей аудиторию в сам вопрос"),
    # Outsider-disclosure openers
    (HARD, r"(?im)^[\s>*-]*(i[' ]?m|i am) not (a |an )?\w+,? but\b",
     "outsider-disclosure opener 'I'm not X, but...'",
     "Lead with observation. Disclose context in paragraph 2-3"),
    (HARD, r"(?im)^[\s>*-]*i[' ]?m posting (this )?from outside\b",
     "outsider 'posting from outside' opener",
     "Lead with observation"),
    (HARD, r"(?im)^[\s>*-]*я не \w+,?\s*но\b",
     "RU outsider 'Я не X, но...'",
     "Веди наблюдением, контекст во 2-3 абзац"),
    (HARD, r"(?im)^[\s>*-]*пишу со стороны\b",
     "RU 'Пишу со стороны' opener",
     "Веди наблюдением"),
    # Throat-clearing openers (line-start)
    (HARD, r"(?im)^[\s>*-]*here[' ]?s (the thing|what|why|the problem)\b",
     "throat-clearing opener", "Cut. State the point directly"),
    (HARD, r"(?im)^[\s>*-]*(it turns out|the truth is|let me be clear)\b",
     "throat-clearing opener", "Cut"),
    (HARD, r"(?im)^[\s>*-]*(если честно,|на самом деле,|знаете что,)\s",
     "RU throat-clearing opener", "Режь, говори сразу"),
    # Scientific jargon in casual content
    (HARD, r"\bn\s*=\s*1\b", "scientific 'n=1' in casual content",
     "Use 'just my experience' / drop"),
    (HARD, r"\bexternal validation\b", "scientific 'external validation'",
     "Use 'no way to know if I'm right'"),
    (HARD, r"\bconfirmation bias\b", "scientific 'confirmation bias' disclaimer",
     "Use 'might be reading too much into it'"),
    (HARD, r"\banecdata\b", "scientific 'anecdata'", "Use 'just one story'"),
    (HARD, r"\bstatistically significant\b", "scientific 'statistically significant'",
     "Use 'noticeable' / 'real'"),
    # Binary contrast / dramatic structures
    (HARD, r"(?i)\bit[' ]?s not \w+[\.,]\s*it[' ]?s \w+", "binary contrast 'not X. it's Y'",
     "State Y directly"),
    (HARD, r"(?i)\bnot because \w[^.]{0,30}\.\s*because\b", "binary 'Not because X. Because Y.'",
     "State Y directly"),
    (HARD, r"(?im)^[\s>*-]*(и|и|but) that[' ]?s okay\.?\s*$",
     "permission-granting closer", "Drop"),
    (HARD, r"(?im)^[\s>*-]*и это нормально\.?\s*$", "RU permission closer", "Удалить"),

    # ---- SOFT: adverbs, business jargon ----
    (SOFT, r"\b(really|just|literally|genuinely|honestly|simply|actually|"
           r"deeply|truly|fundamentally|inherently|inevitably|crucially|importantly|"
           r"basically|essentially|ultimately|clearly|obviously)\b",
     "filler adverb", "Cut"),
    (SOFT, r"\b(буквально|реально|просто|очевидно|конечно)\b",
     "RU filler adverb", "Удали"),
    (SOFT, r"\b(navigate the|unpack the|lean into|game[- ]changer|double down|"
           r"deep dive|circle back|on the same page)\b",
     "business jargon", "Use plain language"),
    (SOFT, r"\b(прокачать|закрыть вопрос|вызовы|синергия|топовый|в моменте)\b",
     "RU business jargon", "Заменить простым"),
    # Filler phrases
    (SOFT, r"(?i)\b(at its core|in today[' ]?s|at the end of the day|"
           r"in a world where|the reality is|it[' ]?s worth noting)\b",
     "filler phrase", "Cut"),
    (SOFT, r"(?i)\b(по сути|в наше время|в конечном счёте|стоит отметить)\b",
     "RU filler", "Удалить"),
    # False agency (a few high-signal cases)
    (SOFT, r"\bthe (decision|conversation|culture|market) (emerges|moves|shifts|rewards)\b",
     "false agency (inanimate doing human action)", "Name the actor"),
    # Lazy extremes
    (SOFT, r"\b(everyone|everybody|nobody|always|never)\b",
     "lazy extreme", "Use specifics"),
    # Meta-commentary
    (SOFT, r"(?im)^[\s>*-]*(hint|plot twist|spoiler):", "meta-commentary marker", "Drop"),

    # ---- anti-ai-patterns rules 15, 17, 19, 20 (added 2026-10-14) ----
    (HARD, r"(?i)\b(week|day|step|session|phase|line|country|month|page) by \1\b",
     "X by X (rule 15)", "Name what the reader finds instead"),
    (HARD, r"(?i)\b(недел\w* за недел|шаг\w* за шаг|день за дн|месяц\w* за месяц|строк\w* за строк)\w*",
     "RU X за X (rule 15)", "Назови, что найдёт читатель"),
    (SOFT, r"(?i),\s+(highlighting|underscoring|emphasizing|showcasing|ensuring|reflecting|"
           r"cementing|solidifying|making it)\b",
     "significance tail (rule 17)", "Cut the tail or make it a real sentence"),
    (SOFT, r"(?i),\s+(подчёркивая|подчеркивая|обеспечивая|демонстрируя|что делает (его|её|их))\b",
     "RU significance tail (rule 17)", "Режь хвост"),
    (SOFT, r"(?i)\b(serves as|stands as|functions as|acts as a)\b",
     "copula avoidance (rule 19)", "is / has"),
    (SOFT, r"(?i)\b(является|являются|представляет собой|выступает в роли)\b",
     "RU copula avoidance (rule 19)", "это / есть"),
    (SOFT, r"(?i)\b(quietly|the quiet power|the honest answer|real trade-?offs|load-bearing|"
           r"doing a lot of (the )?(heavy lifting|work))\b",
     "trendy decoration (rule 20)", "Drop the decoration, state the claim"),
    (SOFT, r"(?i)(тихая сила|честный ответ)",
     "RU trendy decoration (rule 20)", "Убери украшение"),
]


def _scan(text: str) -> list[dict]:
    hits = []
    lines = text.splitlines()
    for severity, pattern, label, suggest in PATTERNS:
        rx = re.compile(pattern)
        for m in rx.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            col = m.start() - (text.rfind("\n", 0, m.start()) + 1) + 1
            snippet = lines[line_no - 1].strip() if line_no - 1 < len(lines) else ""
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            hits.append({
                "severity": severity,
                "line": line_no,
                "col": col,
                "label": label,
                "match": m.group(0),
                "snippet": snippet,
                "suggest": suggest,
            })
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="file path or - for stdin")
    ap.add_argument("--text", help="check inline text")
    ap.add_argument("--json", action="store_true", help="output JSON")
    ap.add_argument("--quiet", action="store_true", help="only print on hits")
    ap.add_argument("--ad", action="store_true",
                    help="ad copy mode: audience opener and closing question become soft (anti-ai-patterns, 2026-10-14)")
    args = ap.parse_args()

    if args.text is not None:
        text = args.text
        source = "<inline>"
    elif args.path == "-" or args.path is None and not sys.stdin.isatty():
        text = sys.stdin.read()
        source = "<stdin>"
    elif args.path:
        p = Path(args.path)
        if not p.exists():
            print(f"slop_check: file not found: {p}", file=sys.stderr)
            return 3
        text = p.read_text(encoding="utf-8", errors="replace")
        source = str(p)
    else:
        ap.print_help()
        return 3

    hits = _scan(text)
    if args.ad:
        for h in hits:
            if h["label"].startswith(AD_SOFT_PREFIXES):
                h["severity"] = SOFT
    hard = [h for h in hits if h["severity"] == HARD]
    soft = [h for h in hits if h["severity"] == SOFT]

    if args.json:
        print(json.dumps({"source": source, "hard": hard, "soft": soft}, ensure_ascii=False, indent=2))
    else:
        if not hits:
            if not args.quiet:
                print(f"[slop_check] {source}: CLEAN")
            return 0
        print(f"[slop_check] {source}: {len(hard)} HARD, {len(soft)} soft hits")
        for h in hard:
            print(f"  HARD L{h['line']}:{h['col']}  {h['label']!r}  match={h['match']!r}")
            print(f"    > {h['snippet']}")
            print(f"    fix: {h['suggest']}")
        if soft and not args.quiet:
            print("  --- soft (review):")
            for h in soft[:20]:
                print(f"  soft L{h['line']}  {h['label']!r}  match={h['match']!r}")
            if len(soft) > 20:
                print(f"  ... +{len(soft) - 20} more soft hits")

    if hard:
        return 1
    if soft:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
