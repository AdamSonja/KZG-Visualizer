import os
from typing import List, Tuple
from py_ecc.optimized_bls12_381 import (
    G1, G2, add, multiply, neg, pairing, Z1, Z2, curve_order,
    is_on_curve, b, b2
)

__all__ = [
    "srs_setup_real", "msm_g1", "curve_order", "G1", "G2",
    "add", "multiply", "neg", "pairing", "Z1", "Z2"
]

def srs_setup_real(max_degree: int, tau: int | None = None):
    """
    Build SRS: G1_powers[i] = (tau^i) * G1, and (H=G2, H_tau=tau*G2).
    """
    if tau is None:
        tau = int.from_bytes(os.urandom(32), "big") % curve_order or 1

    G1_powers = []
    for i in range(max_degree + 1):
        exp = pow(tau, i, curve_order)
        G1_powers.append(multiply(G1, exp))

    H = G2
    H_tau = multiply(G2, tau)
    # sanity
    assert is_on_curve(H, b2)
    assert is_on_curve(H_tau, b2)
    for i, P in enumerate(G1_powers):
        assert is_on_curve(P, b), f"G1_powers[{i}] not on curve"
    return tau, G1_powers, H, H_tau

def msm_g1(scalars: List[int], bases: List[Tuple[int, int, int]]):
    acc = Z1
    for s, bse in zip(scalars, bases):
        s_mod = s % curve_order
        if s_mod:
            acc = add(acc, multiply(bse, s_mod))
    return acc
