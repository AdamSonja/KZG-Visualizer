# 📐 KZG Polynomial Commitment Visualizer (BLS12-381)

An **interactive cryptography simulator** for the **Kate–Zaverucha–Goldberg (KZG)** polynomial commitment scheme — the algebraic foundation behind **Ethereum’s zkEVM**, **EIP-4844 (Proto-Danksharding)**, and **Verkle Trees**.
This project implements the complete mathematical pipeline:
> **Commit → Open → Verify** using real **BLS12-381 pairings**,  
> visualized live with **Streamlit**.

---

## ✨ Features
- 🔒 **Full KZG workflow:** trusted setup → polynomial commit → witness → pairing-based verification  
- 🧮 **Real elliptic-curve operations:** built on `py_ecc.optimized_bls12_381`  
- 📊 **Interactive Streamlit UI:** sliders for coefficients, polynomial degree, and open point  
- 🔍 **Pairing Equation Visualization:** shows both sides of  
  \[
  e(C - yG_1, H) = e(\pi, H_\tau - zH)
  \]  
  with hash previews and 2D curve plots  
- 🧠 **Polynomial plot:** displays \( f(x) \) and its open point \( (z, f(z)) \)  
- ⚠️ **Educational demo only** – local trusted setup, not production-secure

---

## 🧱 Project Structure
