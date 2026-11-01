# PersonalLLM

A small English **decoder-only Transformer** language model trained from **randomly initialized weights**.

This repository is at milestone **M0: project foundation**. The tokenizer, model, training loop, and datasets are **not implemented yet**.

## What this project is

- An educational from-scratch language-model stack
- A long-term local AI core that later projects may reuse

## What M0 includes

- Project layout
- A project-local virtual environment on **Python 3.14.10**
- A tiny `personalllm` package that can load `configs/default.toml`
- Architecture and compatibility notes

## Requirements

- Windows
- Python **3.14.10** (64-bit). On this development machine the interpreter is at `C:\Python3.14\python.exe`; use an equivalent 3.14.10 install on other machines.
- Run all project commands from the **repository root** (the folder that contains `pyproject.toml`, `README.md`, and `src/`).

Do **not** use a global Python 3.15 default for this project.

## Environment

The project uses a **project-local** virtual environment at `.venv` under the repository root.

### Create the virtual environment (first clone / new machine)

From the repository root:

```powershell
# Adjust the Python path if your 3.14.10 install is elsewhere
C:\Python3.14\python.exe -m venv .venv
```

Confirm the venv reports **3.14.10**:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.version); print(sys.executable)"
```

### Activate (PowerShell)

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
```

If Windows blocks scripts, you can skip activation and call `.\.venv\Scripts\python.exe` by relative path (examples below).

### Verify the interpreter

From the repository root:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.version); print(sys.executable)"
.\.venv\Scripts\python.exe scripts\verify_environment.py
```

You should see Python **3.14.10** and an executable under this repository’s `.venv\` directory.

### Deactivate

```powershell
deactivate
```

## Installation

M0 installs **no** third-party packages. `pyproject.toml` currently has an empty `dependencies` list.

PyTorch CPU support for Python 3.14 on Windows appears available via official wheels, but **installation is waiting for approval**. See `docs/compatibility.md`.

After approval, the intended CPU install (from the repository root) is:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Do not run those commands until they are approved.

## Tests

Tests use the standard-library `unittest` runner (no pytest required in M0). From the repository root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Repository map

| Path | Purpose |
| --- | --- |
| `configs/default.toml` | Default CPU / model-target settings |
| `data/` | Future licensed datasets (empty placeholders) |
| `artifacts/` | Future checkpoints and generated files |
| `experiments/` | Future run notes |
| `docs/architecture.md` | Planned design and M0 boundary |
| `docs/compatibility.md` | PyTorch / Python 3.14 findings |
| `scripts/verify_environment.py` | Interpreter and config check |
| `src/personalllm/` | Python package scaffold |
| `tests/` | Scaffold tests |

## Out of scope for M0

Tokenizer, Transformer, training, dataset downloads, pretrained weights, RAG, chatbot, FastAPI, cloud training, other-project integrations, and git publishing.

## License / data policy

Use only **licensed** English text when data work begins. Do not place secrets or datasets in the repository.
