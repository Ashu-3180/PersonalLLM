# Dependency compatibility (M0 investigation)

PersonalLLM targets **Python 3.14.10** on **Windows AMD64**, CPU-only, using:

`C:\Python3.14\python.exe`

No third-party packages were installed during M0. This file records what was checked and the install plan that still needs approval.

## Interpreter

Verified locally:

- File: `C:\Python3.14\python.exe`
- Reported version: `3.14.10` (64-bit AMD64, MSC)
- Project virtual environment: `E:\Projects\PersonalLLM\.venv`

The global default Python 3.15.1 was not modified.

## PyTorch

### Official “Get Started” page (stale on Python versions)

- https://pytorch.org/get-started/locally/
- https://docs.pytorch.org/get-started/locally/

These pages still say that **PyTorch on Windows supports Python 3.9–3.12** and that the latest PyTorch requires **Python 3.9 or later**. They also describe a CPU (“No CUDA”) pip install selected from the OS / package / compute-platform chooser.

That 3.9–3.12 Windows range is **out of date** relative to published wheels (see below). M0 does **not** treat the prose range as the source of truth for Python 3.14.

### Official wheel indexes (evidence of CPU + Windows + cp314)

The official CPU wheel index lists Windows AMD64 CPython 3.14 wheels, including:

- `torch-2.12.1+cpu-cp314-cp314-win_amd64.whl`
- `torch-2.13.0+cpu-cp314-cp314-win_amd64.whl`

Index: https://download.pytorch.org/whl/torch

PyPI’s simple index also lists `cp314-cp314-win_amd64` wheels for recent torch versions (for example 2.9.1 through at least 2.13.0):

- https://pypi.org/simple/torch/
- https://pypi.org/project/torch/2.13.0/

Current PyPI torch requires `Python >=3.10` (project page for 2.13.0).

### Tracker issue

PyTorch issue [python 3.14 support](https://github.com/pytorch/pytorch/issues/156856) marks Windows 3.14 wheels as available for nightlies and the 2.9 release branch. That is project-tracker evidence, not a substitute for the wheel filenames above.

### CUDA vs CPU on Python 3.14

Issue [169929](https://github.com/pytorch/pytorch/issues/169929) reports that a default `pip install torch` on Python 3.14 can resolve to a **CPU** build (`2.9.1+cpu`) even when a GPU is present, and that older CUDA indexes (cu121/cu124) lack cp314 wheels. That matches this project’s **CPU-first** choice. CUDA is not required for M0 or the first training milestone.

Windows **ARM64** + Python 3.14 CPU wheels are a separate, still-reported gap. This machine’s interpreter is **AMD64**, so that gap does not apply here.

### Proposed install (pending approval; not executed)

Prefer the official CPU index so pip does not silently pick a CUDA wheel later:

```powershell
E:\Projects\PersonalLLM\.venv\Scripts\python.exe -m pip install --upgrade pip
E:\Projects\PersonalLLM\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
```

After a future approved install, verify:

```powershell
E:\Projects\PersonalLLM\.venv\Scripts\python.exe -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Expected on this laptop: a `+cpu` version string and `False` for CUDA.

**Not verified in M0:** actually downloading or importing `torch`. Wheel **existence** is documented; runtime import on this machine is not.

## NumPy (PyTorch dependency)

NumPy 2.5.4 on PyPI requires `Python >=3.12`:

- https://pypi.org/project/numpy/2.5.4/

Search of published files indicates Windows `cp314` wheels exist (for example `numpy-*-cp314-cp314-win_amd64.whl`). M0 did not download NumPy. NumPy should arrive as a PyTorch dependency, not as a separate unused install.

## pytest (optional, not required for M0)

M0 tests use `unittest` from the standard library so they can run **without** installing pytest.

pytest documents official Python 3.14 support from 8.4.x onward:

- https://docs.pytest.org/en/stable/changelog.html (3.14 support; 8.4.2 annotation crash fix)
- Current pytest on PyPI requires `Python >=3.10` and classifiers include 3.14: https://pypi.org/project/pytest/

pytest is **not** listed in `pyproject.toml` dependencies until approved.

## Packages deliberately omitted

Not needed for M0 and not scheduled until a later, justified milestone:

- torchvision, torchaudio
- transformers, tokenizers, datasets
- FastAPI / uvicorn
- Jupyter stacks
- CUDA toolkits

## Unresolved concerns

1. The official Get Started **documentation** still lists Windows Python 3.9–3.12. Compatibility is inferred from **wheel filenames** and GitHub tracker status, not from an updated sentence on that page.
2. No `torch` import was executed on this machine.
3. Exact torch version that pip would select today (2.13.0 vs another stable) was not pinned by a dry-run install, because installs are postponed.
4. Python **3.14.10** specifically is newer than the 3.14.0 discussion on some GitHub threads. Wheels tagged `cp314` are ABI-stable for the 3.14 series, but this patch version was not individually certified by PyTorch docs.
5. `torch.compile` / Triton on Windows CPU is unused and untested; the first model should use eager PyTorch.

## Approval gate

Do not run the PyTorch pip command above until it is explicitly approved. M0 stopped after documenting the plan.
