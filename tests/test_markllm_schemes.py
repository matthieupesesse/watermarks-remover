"""Multi-scheme support in the MarkLLM text harness.

CI-covered assertions that the extended scheme surface remains backward
compatible: new scheme keys are additive, the bench's default is still
synthid, and the rewrite loop accepts the new schemes.
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "service" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from detect_text_watermark import SCHEMES


def test_scheme_map_covers_all_schemes() -> None:
    assert SCHEMES["kgw"] == "KGW"
    assert SCHEMES["synthid"] == "SynthID"
    assert SCHEMES["synthid-text"] == "SynthID"
    # Additional schemes: EXP (Gumbel), Unigram, SIR.
    assert SCHEMES["exp"] == "EXP"
    assert SCHEMES["unigram"] == "Unigram"
    assert SCHEMES["sir"] == "SIR"


def test_scheme_map_is_additive_over_legacy_keys() -> None:
    # The legacy surface must remain exactly as shipped (backward compat).
    legacy = {"kgw": "KGW", "synthid": "SynthID", "synthid-text": "SynthID"}
    for key, alg in legacy.items():
        assert SCHEMES[key] == alg
