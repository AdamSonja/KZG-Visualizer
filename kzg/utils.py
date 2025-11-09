from typing import Iterable
from py_ecc.optimized_bls12_381 import is_on_curve, b


# Minimal helpers; extend as you wish.


def ensure_on_curve(point, group="G1"):
"""Raise if a point is not on the expected curve subgroup."""
if not is_on_curve(point, b if group == "G1" else None):
raise ValueError(f"Point not on {group} curve: {point}")