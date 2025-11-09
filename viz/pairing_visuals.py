from py_ecc.optimized_bls12_381 import pairing
import streamlit as st
import matplotlib.pyplot as plt


def visualize_pairing(C, y, z, pi, H, H_tau, G1, G2, r, add, multiply, neg):
    """
    Compute and display both sides of the pairing equation:
        e(C - yG1, H) ?= e(pi, Htau - zH)
    and visualize them in Streamlit.
    """

    # Compute both sides of the pairing equation
    left_g1 = add(C, neg(multiply(G1, y % r)))
    right_g2 = add(H_tau, neg(multiply(G2, z % r)))

    left_pair = pairing(H, left_g1)
    right_pair = pairing(right_g2, pi)

    equal = (left_pair == right_pair)

    # Display short pairing hash preview
    def short(x):
        s = str(x)
        return s[:80] + "..." if len(s) > 80 else s

    st.markdown("### 🔍 Pairing Equation Visualization")
    st.latex(r"e(C - yG_1, H) \stackrel{?}{=} e(\pi, H_\tau - zH)")

    col1, col2 = st.columns(2)
    col1.code(f"e(C - yG1, H)\n{short(left_pair)}")
    col2.code(f"e(pi, Htau - zH)\n{short(right_pair)}")

    if equal:
        st.success("✅ Pairings MATCH — verification passed")
    else:
        st.error("❌ Pairings differ — verification failed")

    # Optional visual projection of G1 points (for intuition only)
    st.markdown("### 📈 G1 Points Projection (approximate view)")
    fig, ax = plt.subplots()
    ax.scatter(C[0].n, C[1].n, color="blue", label="C")
    ax.scatter(pi[0].n, pi[1].n, color="orange", label="π (witness)")
    ax.set_xlabel("x-coordinate")
    ax.set_ylabel("y-coordinate")
    ax.legend()
    st.pyplot(fig)

    # Optional toggle to show full pairings
    if st.toggle("Show raw pairing elements"):
        st.json({
            "Left pairing (e(C - yG1, H))": str(left_pair),
            "Right pairing (e(pi, Htau - zH))": str(right_pair)
        })
