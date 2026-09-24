# Python Foundations Lab

A production-minded foundation in Python: typed domain code, explicit errors, unit tests, and small composable modules.

## What this demonstrates

- Object-oriented design with dataclasses
- Type hints and validation
- Deterministic business logic
- Unit testing with `pytest`
- A maintainable package layout

## Run

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
pytest
```

## Project standard

Every feature is introduced with a small design note, tests for expected behavior, and explicit handling of invalid input.
