import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from kzg.srs import srs_setup_real
from kzg.commit import commit, open_at, verify, r
from py_ecc.optimized_bls12_381 import G1, G2, add, multiply, neg
from viz.pairing_visuals import visualize_pairing

# --- Streamlit UI Setup ---
st.set_page_config(page_title="KZG Polynomial Commitment Visualizer", page_icon="📐")
st.title("KZG Polynomial Commitment Visualizer (BLS12-381)")

with st.expander("About", expanded=False):
    st.markdown(
        """
        **Educational demo** of Kate (KZG) polynomial commitments over **BLS12-381**.

        - Commit: \\(C = \\sum f_i (\\tau^i G_1) = g^{f(\\tau)}\\)
        - Witness at point \\(z\\): \\(q(x) = \\frac{f(x)-f(z)}{x-z}\\), \\(\\pi = \\text{Commit}(q)\\)
        - Verify: \\(e(C - yG_1, H) = e(\\pi, H_\\tau - zH)\\) where \\(y=f(z)\\).

        ⚠️ **Not for production.** The trusted setup here is local and insecure.
        """
    )

# --- Input Section ---
colA, colB = st.columns(2)
max_deg = colA.slider("Polynomial degree d", 1, 10, 3)
z = colB.number_input("Open point z", value=3, step=1)

coeffs = []
cols = st.columns(3)
for i in range(max_deg + 1):
    coeffs.append(cols[i % 3].number_input(f"c{i}", value=0, step=1))

# --- Compute & Verify ---
if st.button("Commit & Verify"):
    tau, G1_powers, H, H_tau = srs_setup_real(max_deg)
    C = commit(coeffs, G1_powers)
    pi, y = open_at(coeffs, z, G1_powers)
    ok = verify(C, y, z, pi, H, H_tau)

    st.subheader("Result")
    st.write(f"f(z) = **{y}**")

    if ok:
        st.success("✅ Pairing check PASSED")
    else:
        st.error("❌ Pairing check FAILED")

    # --- Visualization Section ---
    with st.expander("Pairing Equation Visualization", expanded=True):
        visualize_pairing(C, y, z, pi, H, H_tau, G1, G2, r, add, multiply, neg)

st.caption("© Educational demo • BLS12-381 via py-ecc • Sunny's KZG Visualizer")
