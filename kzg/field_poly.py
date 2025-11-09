from typing import List, Tuple


def poly_eval(coeffs: List[int], x: int, p: int) -> int:
    """Evaluate polynomial at x over Z_p using Horner's method.
    coeffs = [a0, a1, ..., ad] representing a0 + a1*x + ... + ad*x^d.
    """
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % p
    return acc


def poly_div_by_linear(coeffs: List[int], z: int, p: int) -> Tuple[List[int], int]:
    """
    Synthetic division of f(x) by (x - z) over Z_p.
    Returns (quotient_coeffs, remainder) with quotient length len(coeffs)-1.

    coeffs = [a0, a1, ..., ad]. We compute q(x) & remainder r = f(z) such that:
      f(x) = (x - z) * q(x) + r
    """
    n = len(coeffs) - 1
    if n < 0:
        return [], 0

    q_rev = []  # build quotient in reverse
    carry = coeffs[-1] % p
    for i in range(n - 1, -1, -1):
        q_rev.append(carry)
        carry = (coeffs[i] + carry * z) % p
    remainder = carry % p
    q = list(reversed(q_rev))  # length n
    return q, remainder


def poly_add(a: List[int], b: List[int], p: int) -> List[int]:
    """Add two polynomials modulo p."""
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out[i] = (ai + bi) % p
    return out


def poly_sub(a: List[int], b: List[int], p: int) -> List[int]:
    """Subtract polynomial b from a modulo p."""
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out[i] = (ai - bi) % p
    return out


def poly_mul(a: List[int], b: List[int], p: int) -> List[int]:
    """Multiply two polynomials modulo p."""
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out
