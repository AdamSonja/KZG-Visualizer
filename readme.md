# KZG Polynomial Commitment Visualizer

🔗 **Live Demo:** [https://adamsonja-kzg-visualizer-vizapp-streamlit-jwn8bg.streamlit.app/](https://adamsonja-kzg-visualizer-vizapp-streamlit-jwn8bg.streamlit.app/)

---

## Overview

This project is an **educational and research-oriented implementation of the KZG (Kate–Zaverucha–Goldberg) polynomial commitment scheme** over the **BLS12-381 elliptic curve**. It is designed to help build *deep intuition* about how polynomial commitments work internally, how opening proofs are constructed, and how pairing-based verification enforces correctness.

The project intentionally separates:

* **Toy algebraic intuition** (finite-field polynomials)
* **Real cryptographic implementation** (pairings on BLS12-381)

This separation follows standard cryptographic pedagogy and research practice.

---

## What This Project Demonstrates

### 1. Polynomial Commitments (KZG)

* Commitment to a polynomial using a Structured Reference String (SRS)
* Opening the commitment at a point `z`
* Verification using bilinear pairings

Mathematically:

* **Commit:**
  ( C = \sum_i f_i (\tau^i G_1) = g^{f(\tau)} )

* **Open at z:**
  ( q(x) = (f(x) - f(z)) / (x - z) ), witness ( \pi = Commit(q) )

* **Verify:**
  [ e(C - yG_1, H) = e(\pi, H_\tau - zH) ]

---

### 2. Toy Finite-Field Polynomial Visualization (Intuition Layer)

A *toy* visualization is included to build intuition about:

* Polynomial evaluation over finite fields
* Why division by `(x - z)` yields the witness polynomial

This uses **small finite fields** to make behavior observable and **is not cryptographic**.

⚠️ **Important:**

> This toy visualization is purely algebraic and does **not** represent elliptic curve geometry or cryptographic security.

---

### 3. Pairing-Based Verification (Cryptographic Layer)

* Real elliptic curve operations over **BLS12-381**
* Bilinear pairing checks using `py-ecc`
* Explicit construction of both sides of the pairing equation

The UI shows:

* The pairing equation
* Equality / inequality results
* Optional raw pairing element inspection

---

This project is **educational + research-oriented**, not security-hardened.

---

## Threat Model & Assumptions

### Assumptions

* Trusted setup is assumed to be honest
* The secret parameter ( \tau ) is unknown to adversaries
* No toxic waste leakage
* Correctness of elliptic curve and pairing operations

### Adversary Capabilities

* May choose arbitrary polynomials and evaluation points
* May attempt to forge incorrect openings

### Security Goals

* **Binding:** Commitments bind to a single polynomial
* **Correctness:** Valid openings always verify
* **Soundness:** Invalid openings are rejected

### Out of Scope

* Malicious trusted setup
* Batch or multi-point openings
* Aggregated proofs
* Side-channel attacks

---

## Implementation Breakdown (Clarifying Ownership)

This project uses external libraries **only for low-level cryptographic primitives**.

### Libraries Used

* `py-ecc`: elliptic curve & pairing primitives
* `numpy`, `matplotlib`: toy visualization
* `streamlit`: UI

### Implemented From Scratch

* Polynomial arithmetic over finite fields
* Synthetic division for witness construction
* Commitment logic (MSM over SRS)
* Opening proof generation
* Pairing equation assembly for verification
* Educational and visualization tooling

No existing KZG or SNARK library is used.

---

## Project Structure

```
KZG-Visualizer/
├── kzg/
│   ├── commit.py        # Commit, open, verify logic
│   ├── field_poly.py    # Polynomial arithmetic
│   └── srs.py           # Trusted setup (SRS)
│
├── viz/
│   ├── app_streamlit.py # Streamlit application entry point
│   └── pairing_visuals.py
│
├── requirements.txt
└── README.md
```

---

## Running Locally

### Requirements

* Python 3.10+ (or Python 3.8+ with `Optional[int]` typing)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run viz/app_streamlit.py
```

---

## Live Deployment

The project is deployed using **Streamlit Cloud**:

🔗 **Live App:** [https://adamsonja-kzg-visualizer-vizapp-streamlit-jwn8bg.streamlit.app/](https://adamsonja-kzg-visualizer-vizapp-streamlit-jwn8bg.streamlit.app/)

This demonstrates:

* Reproducibility
* End-to-end correctness
* Practical engineering maturity

---

## Limitations & Future Work

### Current Limitations

* Only single-point openings
* No batching or aggregation
* Trusted setup assumed
* No prover/verifier optimizations
* No comparison with other commitment schemes

### Possible Extensions

* Batch openings
* Proof aggregation
* Comparison with IPA / FRI
* Performance optimization & benchmarking

---

## Research Context

Polynomial commitments are a foundational primitive in modern cryptography and zero-knowledge proofs, including:

* Plonk-style SNARKs
* Ethereum’s EIP-4844 (data availability)

This project serves as a **conceptual bridge** between algebraic intuition and real pairing-based cryptographic systems.

---

## Author

**Sunny**
B.Tech CSE | Cryptography & Zero-Knowledge Proofs Enthusiast

---
