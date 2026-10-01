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
    densidad_val = p / (R * T)

    return densidad_val


"""Calcula el Thrust de descenso (T_desc) en Newton"""

def calcular_thrust_desc(h_metros, avion):
    # 1. Calculamos T_max con la formula de las diapositivas
    t_max = avion.ct1 * (1 - (h_metros / avion.ct2) + avion.ct3 * (h_metros ** 2)) # Això dibuixa la corba de thrust max. disponible en funció de l'alçada actual.

    # 2. Determinamos qué coeficiente C_Tdesc usar según la altitud
    altitud_app_metros = 6000 * 0.3048 #de peus a metres

# per entendre els if elif else, tinguem en compte que avion.hp_desc és l'altitut de transició de descens de la taula que varia segons el model de l'avió
    if h_metros > avion.hp_desc: # Volant per sobre l'alçada de transició de l'avio utilitzem la configuració alta.
        c_tdesc = avion.ct_desc_high
    elif h_metros > altitud_app_metros: # Un cop sabem que està per sota aquella alçada preguntem si està per sobre dels 6000 peus
        c_tdesc = avion.ct_desc_low
    else: # si arriba aquí sabem que l'avió està per sota de 6000 peus
        c_tdesc = avion.ct_desc_app

    # 3. Calculamos el thrus real que tendrá el avión den ese momento dependiendo del coeficiente que hayamos usado
    t_desc = c_tdesc * t_max

    return t_desc

def calcular_Vmin_ROD(h, m, T, aircraft):

    g = 9.80665
    h_app = 6000 * 0.3048

    # 1. Elegir CD0 y CD2 según la fase (limpio o aproximación)
    if h > h_app:
        CD0, CD2 = aircraft.cd0_clean, aircraft.cd2_clean
    else:
        CD0, CD2 = aircraft.cd0_app, aircraft.cd2_app

    # 2. Calcular Vmin_ROD
    mg = m * g
    ratio = T / mg
    raiz_interna = (ratio ** 2 + 12 * CD0 * CD2) ** 0.5
    factor = (ratio + raiz_interna) / (3 * CD0)

    V = ((mg / (aircraft.s * densidad(h))) * factor) ** 0.5

    return V

def componentesV(V, h, m, T, aircraft):

    g = 9.80665
    h_app = 6000 * 0.3048
    rho = densidad(h)

    if h > h_app:
        CD0, CD2 = aircraft.cd0_clean, aircraft.cd2_clean
    else:
        CD0, CD2 = aircraft.cd0_app, aircraft.cd2_app

    CL = (m * g) / (0.5 * rho * V**2 * aircraft.s)
    CD = CD0 + CD2 * CL**2
    D = 0.5 * rho * V**2 * aircraft.s * CD

    gamma = math.asin((T - D) / (m * g))

    Vx = V * math.cos(gamma)
    Vh = -V * math.sin(gamma)   # negativo porque desciende

    return Vx, Vh
"""SIMULADOR"""
def simulador(aircraft, max_weight):
    h_iaf = 1828.8
    h_max = 12192.0
    dt = 1.0
    m = max_weight
    h = h_iaf
    x = 0.0

    x_list = [x]
    h_list = [h]

    while h < h_max:
        T_desc = calcular_thrust_desc(h, aircraft)
        V = calcular_Vmin_ROD(h, m, T_desc, aircraft)
        Vx, Vh = componentesV(V, h, m, T_desc, aircraft)

        m = actualizar_masa(V, T_desc, m, aircraft)

        x = x - Vx * dt
        h = h + Vh * dt      # <-- corregido

        x_list.append(x)
        h_list.append(h)

    return x_list, h_list