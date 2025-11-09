from typing import List
from py_ecc.optimized_bls12_381 import (
    G1, G2, add, multiply, neg, pairing, Z1, Z2, curve_order,
    is_on_curve, b, b2
)
from .srs import msm_g1
from .field_poly import poly_div_by_linear

r = curve_order

def _assert_g1(P, name="point"):
    if not is_on_curve(P, b):
        raise ValueError(f"{name} is not on G1")

def _assert_g2(Q, name="point"):
    if not is_on_curve(Q, b2):
        raise ValueError(f"{name} is not on G2")

def commit(coeffs: List[int], G1_powers):
    """C = sum f_i * (tau^i * G1)"""
    scalars = [c % r for c in coeffs]
    if len(scalars) > len(G1_powers):
        raise ValueError("Polynomial degree exceeds SRS size")
    C = msm_g1(scalars, G1_powers[: len(scalars)])
    _assert_g1(C, "C")
    return C

def open_at(coeffs: List[int], z: int, G1_powers):
    """
    Build q(x) = (f(x) - f(z)) / (x - z), then π = Commit(q).
    Returns (π, y=f(z)).
    """
    mod_coeffs = [c % r for c in coeffs]
    z_mod = z % r
    q, fz = poly_div_by_linear(mod_coeffs, z_mod, r)
    pi = commit(q, G1_powers)
    _assert_g1(pi, "pi")
    return pi, fz % r

def verify(C, y: int, z: int, pi, H, H_tau) -> bool:
    """Check e(C - y*G1, H) == e(pi, H_tau - z*H)."""
    _assert_g1(C, "C")
    _assert_g1(pi, "pi")
    _assert_g2(H, "H")
    _assert_g2(H_tau, "H_tau")

    left_g1 = add(C, neg(multiply(G1, y % r)))
    _assert_g1(left_g1, "C - y*G1")

    right_g2 = add(H_tau, neg(multiply(G2, z % r)))
    _assert_g2(right_g2, "H_tau - z*H")

    # py_ecc pairing signature: pairing(Q_in_G2, P_in_G1)
    return pairing(H, left_g1) == pairing(right_g2, pi)
