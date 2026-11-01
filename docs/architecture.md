# PersonalLLM architecture (planned)

This document describes the **intended** design. Milestone **M0** records the plan and project foundation only. It does **not** implement a tokenizer, model, trainer, dataset pipeline, or API.

## Purpose

PersonalLLM has two goals:

1. **Educational.** Implement a small English decoder-only Transformer language model from randomly initialized weights, so the training stack is understandable end to end.
2. **Long-term platform.** Grow a reusable local AI core that later projects (AidScout, ShopSphere, CampusConnect, and others) may call. Those integrations are out of scope until much later milestones.

Budget for development is ₹0. First training and verification use a laptop **CPU**. Paid APIs, paid cloud GPUs, and pretrained weights are not part of the design.

## Design principles

- Train from **scratch** (random initialization). Do not download pretrained model weights.
- Use **licensed English text** only. Do not scrape arbitrary websites or copy copyrighted corpora without a license.
- Keep the first model small enough to run locally on CPU.
- Prefer the Python standard library and a very small third-party set (primarily PyTorch, after approval).
- Separate data, configuration, source, tests, and generated artifacts.
- Treat checkpoints as resume-able training state, not as a substitute for source control.

## Planned pipeline

```text
licensed English text
        |
        v
  data/raw  -->  cleaning / split  -->  data/processed
        |
        v
  custom BPE tokenizer (vocab ~2,000–4,000)
        |
        v
  decoder-only Transformer (random weights)
        |
        v
  causal next-token training (CPU first; optional free GPU later)
        |
        +--> checkpoints in artifacts/ (save and resume)
        |
        v
  evaluation: train loss, val loss, perplexity, sample generation
        |
        v
  future local inference interface (not FastAPI in early milestones)
```

## Components (later milestones)

### 1. Licensed English text data pipeline

- Store originals in `data/raw/` and derived files in `data/processed/` and `data/interim/`.
- Record license, source, and split information with the data, not only in memory.
- Keep datasets out of source control.

### 2. Custom BPE tokenizer

- Train a Byte Pair Encoding tokenizer on the project corpus.
- Preliminary vocabulary size: about 2,000–4,000 tokens.
- Persist vocabulary and merge rules as artifacts, not as handwritten tables in source.

### 3. Decoder-only Transformer

- Causal (left-to-right) self-attention.
- Weights initialized randomly.
- Preliminary size: about **1–5 million** parameters, **2–4** layers, context length about **128** tokens.
- These numbers are planning targets, not M0 implementation requirements.

### 4. Training

- Objective: causal next-token prediction (standard language-modeling cross-entropy).
- First runs on local CPU.
- Optional later use of free cloud GPU if it stays within the ₹0 budget.
- Save checkpoints often enough that a crash does not lose a long CPU run.
- Resume from the latest valid checkpoint.

### 5. Evaluation

- Training loss and validation loss.
- Perplexity on held-out data.
- Qualitative sample generation from a prompt.

### 6. Future inference interface

- A small local interface so other projects can request completions.
- Not implemented in M0. FastAPI, RAG, and chat product features are explicitly out of scope for now.

## Repository layout

| Path | Role |
| --- | --- |
| `configs/` | Human-editable TOML settings |
| `data/` | Datasets (raw / processed / interim); not committed |
| `artifacts/` | Tokenizers, checkpoints, logs produced by later runs |
| `experiments/` | Run notes and experiment metadata |
| `docs/` | Architecture and compatibility notes |
| `scripts/` | Small operator scripts (environment checks, later training entry points) |
| `src/personalllm/` | Installable Python package |
| `tests/` | Tests for whatever exists in the current milestone |
| `pyproject.toml` | Project metadata; M0 has **no** installed third-party runtime deps |

## M0 scope (this milestone)

In scope:

- Project directories and ignore rules
- Local virtual environment on Python 3.14.10
- Package and test scaffold
- Default configuration file
- Architecture and compatibility documentation

Out of scope (do not start until a later prompt):

- Tokenizer implementation
- Transformer implementation
- Training loop
- Dataset download or collection
- Model weights or checkpoints
- RAG, chatbot UI, FastAPI
- Cloud training
- Integrations with other projects
- GitHub / git publishing
- Installing PyTorch until the installation plan is approved

## Configuration

`configs/default.toml` stores the preliminary model and runtime targets (`device = "cpu"`, BPE vocab size, layer count, context length). Loading this file does not train or allocate a model.
