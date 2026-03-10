# First-Journey-Audit# First Journey Audit

First Journey Audit is a lightweight prototype for evaluating the path from landing page to onboarding.

It analyzes the "first journey" a user takes — from first click to first meaningful action — and surfaces the highest-leverage friction points across:

- clarity of value proposition
- trust and credibility
- CTA motivation
- confusion and cognitive load
- onboarding momentum

The system produces structured audit recommendations designed to be **specific, practical, and implementation-ready**.

## Why this project exists

This repo is also an experiment in a **Karpathy-style improvement loop**.

Instead of asking AI for generic advice, the system uses:

- a **fixed audit rubric**
- a **constrained prompt**
- **structured output**
- a **narrow editable surface**

Over time, the audit logic can be iteratively improved while keeping the rubric stable.

The goal is to turn product judgment and conversion expertise into a **repeatable optimization loop**.

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
