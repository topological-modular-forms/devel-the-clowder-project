import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Create the index array n and define the amplitude A(n)
# --------------------------------------------------------
n = np.arange(603)  # n = 0, 1, 2, ..., 600
alpha = 0.01

# Smoothly decaying amplitude: from 1.5 at n=0 toward 1.0 as n→∞
amplitude = 1.0 + 1.0 * np.exp(-alpha * n)

# --------------------------------------
# 2. Define the sinusoidal sequence x_n
# --------------------------------------
x = amplitude * np.sin(2.0 * np.pi * n / 100.0)
x[601] = 1
x[602] = -1

# ------------------------------------------------------
# 3. Compute partial supremum and infimum for each n:
#    sup_{m >= n} x_m  and  inf_{m >= n} x_m
# ------------------------------------------------------
partial_sup = np.empty_like(x)
partial_inf = np.empty_like(x)
for i in range(len(n)):
    partial_sup[i] = np.max(x[i:])
    partial_inf[i] = np.min(x[i:])

# ----------------------------------------------
# 4. Plot everything:
#    - x(n): blue dots
#    - partial sup/inf: #d55e00 lines
#    - dashed lines for lim sup/inf = ±1.0
# ----------------------------------------------
plt.figure(figsize=(8,6))

# Plot x_n in blue dots
plt.plot(n, x, '.', color = '#0072b2', markersize=3, label=r'$x_n$')

# Plot partial sup (#d55e00) and partial inf (#d55e00) as step-like lines
plt.step(n, partial_sup, where='post', color='#d55e00', label=r'$\displaystyle\sup_{m \geq n}(x_m)$')
plt.step(n, partial_inf, where='post', color='#d55e00', label=r'$\displaystyle\inf_{m \geq n}(x_m)$')

# Horizontal dashed lines for lim sup = 1.0 and lim inf = -1.0
plt.axhline(y=1.0, color='k', linestyle='--', label=r'$\displaystyle\limsup_{n\to\infty}(x_n)$')
plt.axhline(y=-1.0, color='k', linestyle='--', label=r'$\displaystyle\liminf_{n\to\infty}(x_n)$')

# Decorate axes
plt.xlim(0, 600)
plt.ylim(-2, 2)
plt.xlabel(r'$n$')
plt.ylabel(r'$x_n$',rotation=0)
#plt.title('Sinusoidal sequence with smoothly decaying amplitude')

# (Optional) Annotate in the figure
plt.rc('text',usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{charter}\usepackage[charter]{newtxmath}')
plt.text(45, 1.6, r'$\displaystyle\sup_{m \geq n}(x_m)$', color='#d55e00')
plt.text(15, -1.65, r"$\displaystyle\inf_{m \geq n}(x_m)$", color='#d55e00')
plt.text(535, 1.15, r'$\displaystyle\limsup_{n\to\infty}(x_n)$')
plt.text(535, -1.15, r'$\displaystyle\liminf_{n\to\infty}(x_n)$')

# Combine legend items (avoid duplicates)
handles, labels = plt.gca().get_legend_handles_labels()
unique = dict(zip(labels, handles))
#plt.legend(unique.values(), unique.keys(), loc='upper right')

plt.tight_layout()
plt.savefig('liminf-limsup.pdf',transparent=True)
