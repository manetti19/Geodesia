#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 09:47:50 2026

@author: roberto
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ``sph_harm`` was relocated/renamed in SciPy 1.17+: the old name
# used to be ``sph_harm`` and accepted arguments ``(m, l, theta,
# phi)``.  In the new release the equivalent function is called
# ``sph_harm_y`` and takes ``(n, m, theta, phi)`` where ``n`` is the
# degree (often denoted by ``l``) and ``m`` is the order.  To keep
# the rest of the code working regardless of the installed SciPy
# version we try the legacy import and fall back to the new name
# with a simple wrapper that swaps the first two arguments.
try:
    # new API (1.17+)
    from scipy.special import sph_harm_y as _sph_harm_impl
    def sph_harm(m, l, theta, phi, /, *args, **kwargs):
        # ``l`` (degree) corresponds to ``n`` in the new function.
        return _sph_harm_impl(l, m, theta, phi, *args, **kwargs)
except ImportError:
    # older SciPy still provides ``sph_harm`` directly
    from scipy.special import sph_harm


def plot_sph_harm(l=2, m=0, n_theta=200, n_phi=100, cmap=cm.seismic,
                  outfile="legendre_harmonico.png", show=True):
    r"""
    Plota a parte real de $Y_l^m(\theta, \phi)$ em uma esfera unitária.

    O código tenta ser compatível com múltiplas versões do SciPy.  Nas
    versões anteriores a 1.17 a função ``sph_harm`` aceitava os
    argumentos ``(m, l, theta, phi)``; na 1.17+ ela foi renomeada para
    ``sph_harm_y`` e espera ``(n, m, theta, phi)`` (``n`` é o grau,
    frequentemente chamado de ``l``).  O wrapper importado no topo do
    módulo unifica os dois formatos.

    âncoras: 
      - theta = longitude (azimute) âˆˆ [0, 2π]
      - phi   = colatitude (polar) âˆˆ [0, π]
    """

    # --- validação (essencial) ---
    if l < 0:
        raise ValueError("l deve ser >= 0.")
    if abs(m) > l:
        raise ValueError(f"Parâmetros inválidos: |m| <= l, mas m={m}, l={l}.")

    # Grade angular
    phi = np.linspace(0.0, np.pi, n_phi)            # colatitude
    theta = np.linspace(0.0, 2.0*np.pi, n_theta)    # longitude
    phi, theta = np.meshgrid(phi, theta)

    # Coordenadas cartesianas da esfera unitária
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    # Harmônico esférico (parte real)
    Y = sph_harm(m, l, theta, phi).real

    # Normalização robusta para [0,1]
    fmin = np.nanmin(Y)
    fmax = np.nanmax(Y)
    denom = fmax - fmin
    if np.isclose(denom, 0.0):
        fcolors = np.zeros_like(Y) + 0.5  # cor neutra se for constante
    else:
        fcolors = (Y - fmin) / denom

    # Plot
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(
        x, y, z,
        rstride=1, cstride=1,
        facecolors=cmap(fcolors),
        linewidth=0, antialiased=False, shade=False
    )

    # Esfera com aspecto correto
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    # Título opcional
    ax.set_title(rf"Parte real de $Y_{{{l}}}^{{{m}}}(\theta,\phi)$", pad=12)

    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)

if __name__ == "__main__":
    # Exemplo: escolha l e m válidos
    #funciona para qualquer l>=0 e m <=l

    plot_sph_harm(l=2, m=0, outfile="legendre_harmonico.png")