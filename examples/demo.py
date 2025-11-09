from kzg.srs import srs_setup_real
from kzg.commit import commit, open_at, verify, r

# Example polynomial: f(x) = 5 + 2x + 7x^2
coeffs = [5, 2, 7]
max_degree = len(coeffs) - 1

# Use a fixed tau for reproducibility in the demo
TAU = 123456789

if __name__ == "__main__":
    tau, G1_powers, H, H_tau = srs_setup_real(max_degree, tau=TAU)
    C = commit(coeffs, G1_powers)

    z = 42
    pi, y = open_at(coeffs, z, G1_powers)

    ok = verify(C, y, z, pi, H, H_tau)
    print(f"Verify @ z={z}: {ok}, y={y}")
