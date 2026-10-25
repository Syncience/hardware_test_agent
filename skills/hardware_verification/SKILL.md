---
skill_id: hardware-verification-loop
version: "0.1.0"
trainable_via: "SkillOpt (#079) & Harness2 (#005)"
department: "hardware-pcb-and-robotics"
max_tokens: 250
jev_gates:
  - "Did the test command return deterministic exit_code == 0 with a verified RAM handle_id receipt?"
  - "Were raw hardware logs archived to docker/ram_log_handles/ so zero confidential data or >600-char dumps entered GPU VRAM?"
  - "For PCB/EDA checks, were ERC/DRC and return-current ground-pour checks (#016 / #051) verified?"
---

# Hardware Verification & Closed-Loop Teststation Skill (`SKILL.md`)

> **Note (`#079 SkillOpt`):** This file acts as the trainable parameter for our frozen local GPU models (`RTX 2080` / `RTX 3060`). Do not bloat beyond 250 tokens.

## Core Execution Rules
1. **Select the Simplest Pattern First (`#003`):**
   - Known test sequence → **Pattern 1: Fused Prompt Chain (`#021`)**
   - Fault triage / file lookup → **Pattern 2: System-1 Jev Routing (`#020 jevgrep`)**
   - Multi-sensor / multi-rule checks → **Pattern 3: Parallel Graph DAG (`#002`)**
   - Iterative fault repair → **Pattern 4: Evaluator-Optimizer (`#030`, max 3 retries)**
2. **Protect 8GB/12GB VRAM with 64GB RAM Handles (`#021` & `#098`):**
   - Never inject full instrument/test logs into the Solver prompt. Always read the `<600-char` tail excerpt or delegate log parsing to the 3B model on `RTX 2080` (`#010`).
3. **Strict Confidentiality (`#023`):**
   - Never write raw test values, serial numbers, or proprietary parameters into `latest_sanitized_scorecard.json` or this `SKILL.md`.
