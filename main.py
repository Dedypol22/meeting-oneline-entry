"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the winning one-liner to ``entry.txt`` in MAKEFUN_OUTPUT_DIR
(default ``/output/entry.txt``), with no trailing newline.

Candidate scoring (each criterion scored 1-5; criteria in judge priority
order: 1 = one sentence that could replace a pointless meeting, unmistakably
office humor; 2 = kills the meeting outright; 3 = relatable to anyone who
has sat through a useless meeting; 4 = lands as a joke, turn/sting;
5 = stands alone with no context):

| # | Candidate (chars) | C1 | C2 | C3 | C4 | C5 | Total |
|---|-------------------|----|----|----|----|----|-------|
| 1 | This meeting could have been an email, and this sentence is that email. (71) | 5 | 5 | 5 | 4 | 5 | 24 |
| 2 | Good news: this meeting could have been an email, and this sentence is the email. (81) | 5 | 5 | 5 | 5 | 5 | 25 |
| 3 | This meeting could have been an email, and congratulations, this sentence is that email. (88) | 5 | 5 | 5 | 5 | 5 | 25 |
| 4 | We've all already agreed, so this hour is just us watching each other nod. (74) | 4 | 4 | 5 | 4 | 5 | 22 |
| 5 | The update is that nothing has changed, which is why this meeting didn't need to happen. (88) | 4 | 3 | 5 | 3 | 5 | 20 |
| 6 | This 'quick sync' has now lasted longer than the project it was about. (70) | 4 | 3 | 5 | 5 | 5 | 22 |
| 7 | Nobody in this room has new information, so we're all free to go back to work. (80) | 4 | 5 | 5 | 3 | 5 | 22 |
| 8 | We scheduled a meeting to decide whether to have a meeting, and the answer is no. (81) | 4 | 4 | 4 | 5 | 5 | 22 |
| 9 | Our only action item is to never schedule this meeting again. (61) | 4 | 4 | 4 | 4 | 5 | 21 |
| 10 | The decision was made before we sat down; this meeting is just the applause. (76) | 4 | 4 | 4 | 5 | 4 | 21 |
| 11 | This meeting exists because someone was afraid to send an email, so consider this the email. (92) | 5 | 4 | 4 | 4 | 5 | 22 |
| 12 | The agenda has one item: cancel every future meeting about this. (64) | 4 | 4 | 4 | 4 | 5 | 21 |
| 13 | We've spent an hour deciding nothing, so here's the decision: we're done. (73) | 4 | 4 | 5 | 4 | 5 | 22 |

Winner: candidate #2 (25/25, tied with #3 on score, wins the tie-break on
fewer bytes: 81 vs 88). Why it wins:

- It IS the replacement: the sentence literally is the email the meeting
  should have been, so after it there is nothing left to meet about (C1, C2).
- "Could have been an email" is the most universal pointless-meeting
  experience there is (C3).
- The deadpan "Good news:" opener is the turn: it delivers the kill as
  cheerful news, which is funnier than merely stating the fact (C4).
- It needs no setup, no agenda, no names — one sentence, done (C5).
- Runner-up #1 (24/25) is the same idea without the opener; it loses the
  joke's sting, which is why #2 beats it on C4. #3 ties #2 on score but is
  7 bytes longer, so it loses the byte tie-break.
"""

import os
import re

LINE = "Good news: this meeting could have been an email, and this sentence is the email."

_SENTENCE_END = re.compile(r"[.!?]")


def output_path() -> str:
    """Resolve the output file from the environment, never from the cwd."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate(line: str) -> None:
    """The gate: UTF-8 text, 1-200 chars, not only whitespace, one sentence."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 cap")
    if len(_SENTENCE_END.findall(line)) != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")


def main() -> None:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
