# First-Journey-Audit

`First-Journey-Audit` is a tiny local prototype for auditing a landing page against a fixed click-to-activation rubric. It fetches a URL, extracts readable page content, optionally includes local onboarding notes, and prints a structured prompt you can paste into ChatGPT, Codex, or another LLM.

The project is intentionally narrow:

- one script
- one fixed rubric
- one fixed expert prompt
- no API calls
- no product surface beyond local command-line usage

## Install

Use Python 3 and install the minimal dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Basic usage:

```bash
python3 run_audit.py https://example.com
```

With optional onboarding notes:

```bash
python3 run_audit.py https://example.com --notes notes.txt
```

The script prints a combined audit prompt to stdout. Redirect it to a file if you want:

```bash
python3 run_audit.py https://example.com --notes notes.txt > audit_prompt.txt
```

## What The Karpathy-Style Loop Means Here

In this prototype, the loop is deliberately constrained:

1. Use a fixed rubric.
2. Extract a consistent page snapshot.
3. Ask for structured evaluation output.
4. Review the output.
5. Improve the landing page or onboarding.
6. Repeat with the same evaluation frame.

The goal is not to build a general-purpose growth platform. The goal is to create a small, inspectable evaluation loop where the prompt, rubric, and extracted input are stable enough to improve over time.

## Future Ideas

These are intentionally not included in v0:

- save outputs to JSON files automatically
- compare multiple page versions
- add screenshot support
- add lightweight batch auditing for multiple URLs
- add a small local scoring report or diff view
