# AGENTS.md — Anti-Hallucination Contract for `Syncience/hardware_test_agent`

> **CRITICAL RULE FOR AI AGENTS (Antigravity, Claude Code, Cursor, Local LLM):**
> This repository builds a **Confidential Local AI Hardware Testing Agent** running on **NVIDIA RTX 2080 (8GB VRAM)** and **RTX 3060 (12GB / 24GB Dual VRAM) + 64GB System RAM**.
> **Zero hallucination is permitted.** Follow the 4 mandatory rules below on every turn.

---

## 🛡️ 1. The 4 Anti-Hallucination Rules (Pattern `#032` & `#075`)

1. **Read `SHIFT_NOTES.md` First (Turn 1 Mandatory Step):**
   Before proposing plans or writing code in a new chat session, read [`SHIFT_NOTES.md`](./SHIFT_NOTES.md) to verify **Ground-Truth Hardware Specs**, **What Is Already Implemented**, and **What Is Still Planned**. Never assume a hardware driver, instrument interface, or model endpoint exists unless it is listed under `Verified Implemented Files` in `SHIFT_NOTES.md`.

2. **Consult the `ohm-bookshelf` Specialist Teachers (Zero Guessing):**
   Do not invent agentic patterns or HPC configurations from memory. Query the linked [`Syncience/ohm-bookshelf`](https://github.com/Syncience/ohm-bookshelf) MCP Gateway:
   ```powershell
   # Stage 1: Consult the Jev Dean Router
   python -m src.plugins.mcp_server --cli dean --query "<hardware test or agent task>"
   # Stage 2: Retrieve <200-token micro-skills from the Specialist Teacher
   python -m src.plugins.mcp_server --cli teacher --dept hardware-pcb-and-robotics --query "<specific problem>"
   ```

3. **Evidence-Grounded Execution Only (Pattern `#021` & `#030`):**
   * Never claim a test, ERC/DRC check, or container build succeeded without executing it via `src.harness.graph_loop` and citing the deterministic `exit_code` and `handle_id` receipt in `docker/ram_log_handles/`.
   * Never dump raw >1KB hardware logs into the LLM prompt; always archive raw logs into the **64GB System RAM handle store** (`#021`) and pass only the `<600-char` excerpt to protect 8GB/12GB GPU VRAM (`#098`).

4. **Confidentiality Standard `#023` (Zero Data Leak):**
   * Raw teststation waveforms, proprietary schematics, and full failure logs must stay strictly inside `docker/ram_log_handles/` (git-ignored and air-gapped via `internal: true` in Docker).
   * Only sanitized pass/fail scorecards (`latest_sanitized_scorecard.json`) and generalized `skills/hardware_verification/SKILL.md` rule weights (`#079 SkillOpt`) may be committed or synced back to the Dev PC.
