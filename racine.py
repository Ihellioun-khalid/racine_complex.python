# !/usr/bin/python
# -*- coding : utf-8 -*-

def racine(a, b, c):
    """[summary]
    [la fonction qui résout les équations du second degré à coefficients complexes.]
    Arguments:
        a {[complexe]} -- [le coeff ]
        b {[complexe]} -- [description]
        c {[complexe]} -- [description]
    """
    from math import sin, cos, sqrt, atan2
    delta = b * b - 4 * a * c
    if delta.imag == 0:
        try:
            delta = delta.real
        except TypeError:
            pass
        if delta < 0:
            z1 = complex(-b, sqrt(- delta)) / (2 * a)
            return (z1, z1.conjugate())
        return (-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)
    else:
        t = atan2(delta.imag, delta.real) / 2
        rd = sqrt(abs(delta)) * complex(cos(t), sin(t))
    return ((-b + rd) / (2 * a), (-b - rd) / (2 * a))
