import math

"""Calcula la nueva massa para el siguiente segundo"""
def actualizar_masa(V, T, m_antigua, avion):
    eta = avion.cf1 * (1 + V / avion.cf2)
    FF = eta * T

    m_nuevo = m_antigua + FF * 1

    return m_nuevo

