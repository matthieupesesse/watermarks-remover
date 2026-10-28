"""Shared pytest fixtures for the watermarks-remover test suite.

This fork removed the Layer B rewrite (statistical-watermark evasion), so text
cleaning is Layer A only and needs no fixture.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "service" / "scripts"
sys.path.insert(0, str(SCRIPTS))
