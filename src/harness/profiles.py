"""
Verified Hardware & Multi-GPU HPC Profiles (`profiles.py`)
Grounded in `ohm-bookshelf` Note #105 (NECTEC-ACE 2026 HPC) & Note #098 (KV-Cache VRAM Management).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class HardwareProfile:
    key: str
    name: str
    vram_gb: int
    ram_gb: int
    interconnect: str
    hpc_strategy: str
    jev_model: str       # System-1 Reflex + 40:1 Log Reader (#010, #029)
    solver_model: str    # System-2 Frozen Solver (#005, #081)
    max_context_tokens: int


HARDWARE_PROFILES: Dict[str, HardwareProfile] = {
    "rtx2080_8gb": HardwareProfile(
        key="rtx2080_8gb",
        name="Dev PC (NVIDIA RTX 2080 8GB VRAM + 64GB RAM)",
        vram_gb=8,
        ram_gb=64,
        interconnect="Single-GPU PCIe + 16GB RAM shm_size",
        hpc_strategy="Time-shared 3B Jev + 7B Solver with Q8 KV-Cache",
        jev_model="qwen2.5:3b-instruct-q4_K_M",
        solver_model="qwen2.5-coder:7b-instruct-q4_K_M",
        max_context_tokens=4096,
    ),
    "rtx3060_12gb": HardwareProfile(
        key="rtx3060_12gb",
        name="Confidential Teststation (NVIDIA RTX 3060 12GB VRAM + 64GB RAM)",
        vram_gb=12,
        ram_gb=64,
        interconnect="Single-GPU PCIe (Air-Gapped internal:true)",
        hpc_strategy="14B Q4 Solver + 64GB RAM Handle Shield (#021, #023)",
        jev_model="qwen2.5:3b-instruct-q8_0",
        solver_model="qwen2.5-coder:14b-instruct-q4_K_M",
        max_context_tokens=8192,
    ),
    "dual_rtx3060_24gb": HardwareProfile(
        key="dual_rtx3060_24gb",
        name="Same-PC Dual GPU Teststation (2x NVIDIA RTX 3060 = 24GB Pooled VRAM + 64GB RAM)",
        vram_gb=24,
        ram_gb=64,
        interconnect="Motherboard PCIe 3.0/4.0 (No NVLink)",
        hpc_strategy="Pipeline / Layer Splitting (--split-mode layer) + Speculative Decoding (#095, #105)",
        jev_model="qwen2.5:3b-instruct-q8_0",
        solver_model="qwen2.5-coder:32b-instruct-q4_K_M",
        max_context_tokens=16384,
    ),
    "hpc_asymmetric_cluster": HardwareProfile(
        key="hpc_asymmetric_cluster",
        name="Two-PC Asymmetric HPC Cluster (PC1 RTX 2080 8GB + PC2 RTX 3060 12GB)",
        vram_gb=20,
        ram_gb=128,
        interconnect="Internal LAN JSON-RPC (<200-token messages only)",
        hpc_strategy="Asymmetric Role Parallelism: PC1=Jev+LogReader | PC2=14B Solver (Zero LAN Tensor Sync #105)",
        jev_model="node1-rtx2080/gero-4b-q4_K_M",
        solver_model="node2-rtx3060/qwen2.5-coder:14b-instruct-q4_K_M",
        max_context_tokens=16384,
    ),
}
