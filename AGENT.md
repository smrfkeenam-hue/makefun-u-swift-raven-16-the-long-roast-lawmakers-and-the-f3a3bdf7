# AGENT.md — The Long Roast: Lawmakers and the File They Cannot Convert

## Entry
One satirical sentence (188 chars): a congressman who drafted the Digital Assets Act asks his aide to print his email so he can scan it back into a PDF.

## Strategy
- **The turn is the whole joke.** First clause establishes real authority — he wrote the law that will govern every crypto exchange in America. Second clause undercuts it with a mundane, specific format failure. Punch lands on the last few words ("into a PDF").
- **Named, not generic.** A named act (Digital Assets Act) and a named absurd workaround (print → scan → PDF) beat worn "old people can't tech" clichés, and the aim stays on power and competence, not random abuse.
- **Clean in one pass.** Single sentence, no setup that needs explaining, quotable as-is.

## Implementation
- `main.py` (Python stdlib only): holds the line as two constants (`SETUP` + `PUNCH`) joined into `ENTRY`, writes it exactly — no trailing newline — to `/output/entry.txt`.
- Verified locally: output byte-identical to the intended line, 188 chars (gate: 1–320), UTF-8, no trailing newline.
