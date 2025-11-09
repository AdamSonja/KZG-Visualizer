import numpy as np
import matplotlib.pyplot as plt
from typing import List


from kzg.field_poly import poly_eval, poly_div_by_linear




def demo_toy_plot(coeffs: List[int], p: int, z: int):
xs = np.arange(0, min(p, 101))
ys = np.array([poly_eval(coeffs, int(x), p) for x in xs])
q, fz = poly_div_by_linear(coeffs, z % p, p)
y_line = fz * np.ones_like(xs)


plt.figure()
plt.title(f"Toy Field Plot mod {p} (z={z}, f(z)={fz})")
plt.plot(xs, ys, label="f(x) mod p")
plt.plot(xs, y_line, linestyle="--", label="y = f(z)")
plt.legend()
plt.xlabel("x")
plt.ylabel("value mod p")
plt.grid(True)
plt.show()