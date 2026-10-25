# 📋 SHIFT_NOTES.md — Anti-Hallucination Handoff & Verified State Ledger

> **Purpose (Pattern `#075` & `#032`):**
> This file is the **Single Source of Truth** across chat sessions. Any AI agent starting a new chat MUST read this file first to prevent hallucinating hardware capabilities, unimplemented drivers, or fictitious test results.

---

## 1. Verified Ground-Truth Hardware & Environment

| Environment | GPU & VRAM | System RAM | Interconnect | Assigned Role (Standard `#105` NECTEC HPC) |
| :--- | :--- | :---: | :--- | :--- |
| **1. Dev PC (Current Machine)** | `NVIDIA RTX 2080` (`8 GB VRAM`, No NVLink) | `64 GB RAM` | Local PCIe / LAN | • Build & validate Docker containers before cloning.<br>• In asymmetric cluster mode, runs **System-1 Local Jev (`3B-4B`) + 40:1 Cheap Test-Log Reader (`#010`)**. |
| **2. Confidential Teststation** | `NVIDIA RTX 3060` (`12 GB VRAM`) or `Dual RTX 3060` (`24 GB VRAM` pooled via PCIe Layer Split) | `64 GB RAM` | Air-Gapped (`internal: true`) | • Runs **100% offline confidential hardware testing (`#023`)**.<br>• Single 3060 runs `14B-Q4` Solver; Dual 3060 on same motherboard runs `32B-Q4` Solver via Pipeline Parallelism (`#105`). |

---

## 2. Verified Bookshelf Anchors (Do Not Re-Invent—Query via MCP)

All architectural decisions in this repository are grounded in [`Syncience/ohm-bookshelf`](https://github.com/Syncience/ohm-bookshelf):
* **`#015` (`bio-wetlab-agents/x-googleresearch-181399.md`):** Closed-loop physical/instrument verification (`Propose → Execute on Hardware → Capture Sensor/Test Readout → Update Policy`).
* **`#023` (`aidlc-inference-and-infra/x-googleresearch-357182.md`):** Confidential zero-leak execution—raw teststation logs never leave `docker/ram_log_handles/`; only sanitized scorecards and `SKILL.md` updates are exported.
* **`#021` (`aidlc-harness-and-loops/x-0xcodila-737913.md`) & `#010` (`x-undefinedki-156666.md`):** NVIDIA/MIT 2x Harness cost cut & Shopify 40:1 Reader split—fuse `edit + test`, archive full logs in **64GB System RAM**, and send only `<600-char` excerpts to GPU VRAM.
* **`#002` (`x-0xcodila-020996.md`), `#003` (`x-mdancho84-030484.md`), `#081` (`x-mdancho84-603355.md`):** Google's 21 Agentic Design Patterns & Pattern Selection Decision Tree (`Fused Chain → Jev Router → Parallel Graph DAG → Evaluator-Optimizer → Closed-Loop Harness²`).
* **`#005` (`x-sumanth_077-598588.md`), `#006` (`x-virgilxbt-482170.md`), `#079` (`x-dailydoseofds_-840124.md`):** Keep local GPU model weights frozen; treat `skills/hardware_verification/SKILL.md` as the trainable parameter optimized against a frozen held-out test set.
* **`#105` (`aidlc-inference-and-infra/web-nectec-ace-2026-high-performance-com.md`):** NECTEC-ACE 2026 HPC laws—never run synchronous Tensor Parallelism (`AllReduce`) across slow LAN; use Asymmetric Role Parallelism across PCs or Pipeline/Layer Splitting on the same motherboard.

---

## 3. Anti-Hallucination Ledger: What Exists vs. What Is Next

### ✅ Verified Implemented in This Repo (`v0.1.0`)
- [x] [`AGENTS.md`](./AGENTS.md) — Anti-Hallucination & Zero-Leak contract.
- [x] [`.mcp.json`](./.mcp.json) — MCP connection to `ohm-bookshelf`.
- [x] [`skills/hardware_verification/SKILL.md`](./skills/hardware_verification/SKILL.md) — Trainable `SkillOpt` (`#079`) hardware verification skill.
- [x] [`src/harness/profiles.py`](./src/harness/profiles.py) — 4 verified hardware profiles (`rtx2080_8gb`, `rtx3060_12gb`, `dual_rtx3060_24gb`, `hpc_asymmetric_cluster`).
- [x] [`src/harness/graph_loop.py`](./src/harness/graph_loop.py) — Pattern-aware closed-loop teststation runner (Fused execution, 64GB RAM log handle archiving, Local Jev `Noul` gating, and `#023` sanitized scorecard export).
- [x] [`docker/docker-compose.confidential.yml`](./docker/docker-compose.confidential.yml) & [`docker/Dockerfile.agent`](./docker/Dockerfile.agent) — Air-gapped container configuration (`internal: true`, `16gb` RAM `shm_size`, `q8_0` KV-cache).

### 🔜 Planned for Next Chat Session (Do Not Hallucinate as Already Built)
- [ ] **Specific Hardware Testbench Adapters (`src/adapters/`):** Connect `graph_loop.py` to your specific teststation instrument / serial / VISA / KiCad ERC-DRC / pytest runner (Ask user for exact teststation instrument or CLI command first!).
- [ ] **Held-Out Benchmark Suite (`benchmarks/held_out_scoring_set.json`):** Define the frozen test cases (`#006`) for grading `SkillOpt` (`#079`) updates.
- [ ] **Local Ollama / `llama.cpp` Model Pull Script (`scripts/preload_airgap_models.ps1`):** Script to pre-download GGUF weights on the RTX 2080 Dev PC before cloning the offline container to the air-gapped RTX 3060 teststation.

---

## 4. Copy-Paste Prompt to Start the New Chat Safely

```text
Read AGENTS.md and SHIFT_NOTES.md in hardware_test_agent. Verify the ground-truth state and help me build the next item in Section 3 (Planned for Next Chat Session) without hallucinating unimplemented hardware adapters.
```
