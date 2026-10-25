# 📋 SHIFT_NOTES.md — Anti-Hallucination Handoff & Verified State Ledger

> **Purpose (Pattern `#075` & `#032`):**
> This file is the **Single Source of Truth** across chat sessions. Any AI agent starting a new chat MUST read this file first to prevent hallucinating hardware capabilities, unimplemented drivers, or fictitious test results.

---

## 1. Verified Ground-Truth Hardware & Environment

| Environment | GPU & VRAM | System RAM | Interconnect | Assigned Role (Standard `#105` NECTEC HPC) |
| :--- | :--- | :---: | :--- | :--- |
| **1. Dev PC (Current Machine)** | `NVIDIA RTX 2080` (`8 GB VRAM`, No NVLink) | `64 GB RAM` | Local PCIe / LAN | • Build & validate Docker containers before cloning.<br>• Runs **Tier 1 Local Jev (`3B-4B`) + 40:1 Cheap Test-Log Reader (`#010`)**. |
| **2. Confidential Teststation** | `NVIDIA RTX 3060` (`12 GB VRAM`) or `Dual RTX 3060` (`24 GB VRAM` pooled via PCIe Layer Split) | `64 GB RAM` | Air-Gapped (`internal: true`) | • Runs **100% offline confidential hardware testing (`#023`)**.<br>• Single 3060 runs **Tier 2 `14B-Q4` Solver**; Dual 3060 runs **`32B-Q4` Solver** via Pipeline Parallelism (`#105`). |
| **3. Target DUT (`Video Adapter POC`)** | `NVIDIA Jetson NX` + `AMD/Xilinx Zynq UltraScale+ FPGA` + `STM32 MCU` | Board DDR | PCIe Slot (`100xG5` Switch in Prod) + `1/10G` & `10GBase-KR` Eth + `UART/USB` | • `I2C1`: Sensors + Circuit Breaker Control<br>• `I2C2`: Jetson NX RTC Drift Check<br>• `I2C3`: PMBus/SMBus Circuit Breaker ($V, I, P$)<br>• `4-Port SDI`: FPGA SerDes + STM32 SDI Crosspoint Mux |

---

## 2. Verified Bookshelf Anchors (Do Not Re-Invent—Query via MCP)

All architectural decisions in this repository are grounded in [`Syncience/ohm-bookshelf`](https://github.com/Syncience/ohm-bookshelf):
* **`#015` (`bio-wetlab-agents/x-googleresearch-181399.md`):** Closed-loop physical/instrument verification (`Propose → Execute on Hardware → Capture Sensor/Test Readout → Update Policy`).
* **`#023` (`aidlc-inference-and-infra/x-googleresearch-357182.md`):** Confidential zero-leak execution—raw teststation logs and internal document codes never leave `docker/ram_log_handles/`; only sanitized scorecards, `SKILL.md` updates, and redacted `antigravity_escalation_ticket.json` summaries are exported.
* **`#029` (`x-_avichawla-496464.md`) & `#034` (`x-sora_biz-120119.md`):** Hybrid 3-Tier System-1 Jev (`<5ms`, `$0` token `Choice`/`Score`/`Noul`) + Tier 2 Local GPU Solver (`7B`/`14B`/`32B`) + Tier 3 Sanitized Antigravity Frontier Escalation (`complexity >= 0.75`).
* **`#021` (`aidlc-harness-and-loops/x-0xcodila-737913.md`) & `#010` (`x-undefinedki-156666.md`):** NVIDIA/MIT 2x Harness cost cut & Shopify 40:1 Reader split—fuse `edit + test`, archive full logs in **64GB System RAM**, and send only `<600-char` excerpts to GPU VRAM.
* **`#005` (`x-sumanth_077-598588.md`), `#006` (`x-virgilxbt-482170.md`), `#079` (`x-dailydoseofds_-840124.md`):** Keep local GPU model weights frozen; treat `skills/hardware_verification/SKILL.md` as the trainable parameter optimized against a frozen held-out test set.
* **`#069` (`sdlc-architecture-and-craft/x-mattpocockuk-350655.md`) & `#103` (`x-alexxubyte-783459.md`):** Deep Modules (`src/adapters/__init__.py`, `src/harness/__init__.py`) + Security Policy Guard (non-shell execution, SCPI voltage/current safety interlocks, confidential SOP/SN/MAC/IP/Token redaction, rate-limiting, HMAC-SHA256 RPC signing).
* **`book-ti-dynamic-z-track-sluab20a` (`hardware-pcb-and-robotics/book-ti-dynamic-z-track-sluab20a.md` + `books/ti-dynamic-z-track-sluab20a/`):** Texas Instruments Application Note `SLUAB20A` (*Dynamic Z-Track™ Technology for `BQ41Z50` / `BQ41Z90`*). Broadband battery impedance modeling under dynamic pulsed loads (`10s 2C SPC` / `10ms 4C CPC`, `1C`–`1.75C` discharge) without requiring 10-minute OCV relaxation waits, keeping pulsed resistance error `<10%` and preventing `10%–60%` `RemCap` overestimation at the `3.0V` minimum system voltage cutoff.

---

## 3. Anti-Hallucination Ledger: What Exists vs. What Is Next

### ✅ Verified Implemented in This Repo (`v0.2.0`)
- [x] [`AGENTS.md`](./AGENTS.md) — Anti-Hallucination & Zero-Leak contract.
- [x] [`.mcp.json`](./.mcp.json) — Dual MCP configuration linking `mcp-server-1-ohm-bookshelf` (Knowledge Vault) and `mcp-server-2-hardware-test-agent` (64GB RAM Handle Vault & Hybrid Escalation Bridge).
- [x] [`skills/hardware_verification/SKILL.md`](./skills/hardware_verification/SKILL.md) — Trainable `SkillOpt` (`#079`) hardware verification skill.
- [x] [`src/harness/profiles.py`](./src/harness/profiles.py) — 4 verified hardware profiles (`rtx2080_8gb`, `rtx3060_12gb`, `dual_rtx3060_24gb`, `hpc_asymmetric_cluster`).
- [x] [`src/harness/security.py`](./src/harness/security.py) — Hardware Safety Interlocks (`max_voltage_v`, `max_current_a`), Command Injection & Zero-Egress Guard (`#023`, `#103`), Confidential Internal-SOP/SN/MAC/IP/Token Redactor, Sliding-Window Rate Limiter, and HMAC-SHA256 Cluster RPC Auth.
- [x] [`src/harness/jev_escalation.py`](./src/harness/jev_escalation.py) — Hybrid 3-Tier Jev Complexity Router (`tier_1_local_jev`, `tier_2_local_solver`, `tier_3_antigravity_frontier`) & Zero-Leak Antigravity Escalation Ticket generator (`#023`, `#029`, `#034`).
- [x] [`src/harness/mcp_bridge.py`](./src/harness/mcp_bridge.py) — MCP Server 2 CLI & Antigravity Hybrid Escalation Bridge.
- [x] [`src/adapters/`](./src/adapters/__init__.py) — Deep Module Pluggable Hardware Testbench Adapters:
  - [`src/adapters/scpi_visa_serial.py`](./src/adapters/scpi_visa_serial.py) (`ScpiSerialVisaAdapter`: PyVISA / PySerial + deterministic offline container simulation).
  - [`src/adapters/pytest_hil.py`](./src/adapters/pytest_hil.py) (`PytestHilAdapter`: `shell=False` safe subprocess & pytest HIL runner).
  - [`src/adapters/kicad_eda.py`](./src/adapters/kicad_eda.py) (`KicadEdaAdapter`: KiCad ERC, DRC & `#016`/`#051` return-current ground pour verification).
  - [`src/adapters/video_adapter_hil.py`](./src/adapters/video_adapter_hil.py) (`VideoAdapterCardHilAdapter`: Scientific Positive & Negative protocol checks for `I2C1`, `I2C2` RTC, `I2C3` PMBus $V/I/P$, `4-Port SDI` + `STM32` Mux, `PCIe` Endpoint/Switch, `10GBase-KR`/`1G`/`10G` Ethernet, and `UART/USB`).
- [x] [`docs/architecture/video_adapter_poc_testbench.drawio`](./docs/architecture/video_adapter_poc_testbench.drawio) & [`docs/architecture/zero_leak_planops_codeops_workflow.drawio`](./docs/architecture/zero_leak_planops_codeops_workflow.drawio) — Editable `draw.io` architecture diagrams (`Agents365-ai/drawio-skill`).
- [x] [`tests/test_adapters_and_security.py`](./tests/test_adapters_and_security.py) — 11 automated unit, security red-team, Video Adapter HIL, Hybrid Jev Escalation, Deep-Module boundary, and held-out benchmark tests.

### 🔜 Planned for Next Chat Session (Do Not Hallucinate as Already Built)
- [ ] **Physical Register / Slave Address Mapping (`config/video_adapter_poc.internal.json`):** Bind exact `I2C1`/`I2C2`/`I2C3` hex addresses and `STM32` SDI Mux UART/UDP opcodes (git-ignored via `*.internal.*`).
- [ ] **Local Gitea & Local FastAPI/Grafana Dashboard Services in Compose (`docker/docker-compose.confidential.yml`):** Add optional on-prem `gitea` and `local-dashboard` containers.
