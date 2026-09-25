import math

"""Calcula la nueva massa para el siguiente segundo"""
def actualizar_masa(V, T, m_antigua, avion):
    eta = avion.cf1 * (1 + V / avion.cf2)
    FF = eta * T

    m_nuevo = m_antigua + FF * 1

    return m_nuevo


"""Calculo de la presion en funcion de la altura en m"""


def presion(h_metros):

    # Constantes a MSL
    p0 = 101325.0  # Pa (N/m^2)
    T0 = 288.15    # °K
    g = 9.80665    # m/sec^2
    R = 287.04     # m^2/(°K sec^2)

    # Constantes en la tropopausa
    h11 = 11000.0  # m
    p11 = 22632.0  # Pa (N/m^2)
    T11 = 216.65   # °K

    if h_metros <= h11:
        # Troposfera: La temperatura disminuye con la altitud
        presion = p0 * (1 - 0.0065 * (h_metros / T0)) ** 5.2561
    else:
        # Estratosfera: La temperatura es constante
        exponente = -(g / (R * T11)) * (h_metros - h11)
        presion = p11 * math.exp(exponente)

    return presion


"""Calculo de la densidad en funcion de la altura en m"""


def densidad(h_metros):
    # Constantes
    R = 287.04     # m^2/(°K sec^2)
    T0 = 288.15    # °K
    h11 = 11000.0  # m
    T11 = 216.65   # °K

    # Calculo de T en funcion de h
    if h_metros <= h11:
        # En la troposfera, la temperatura desciende con la altitud
        T = T0 - (0.0065 * h_metros)
    else:
        # Por encima de la tropopausa, la temperatura se mantiene constante
        T = T11

    # Calculamos la presion con la funcion anterior
    p = presion(h_metros)

    # Calculo final de la presion
    densidad = p / (R * T)

    return densidad