import matplotlib
try:
    matplotlib.use("TkAgg")   # backend interactivo: necesario para que funcionen los botones (en PyCharm, el de "SciView" no los soporta)
except Exception:
    pass
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.ticker import FuncFormatter
from funcions import *
import numpy as np


class Aircraft:
    def __init__(self, name, mlw, max_weight, max_payload, s,
                 cd0_app, cd2_app, cd0_clean, cd2_clean,
                 hp_desc, ct_desc_high, ct_desc_low, ct_desc_app,
                 ct1, ct2, ct3, cf1, cf2):
        self.name = name
        self.mlw = mlw
        self.max_weight = max_weight
        self.max_payload = max_payload
        self.s = s
        self.cd0_app = cd0_app
        self.cd2_app = cd2_app
        self.cd0_clean = cd0_clean
        self.cd2_clean = cd2_clean
        self.hp_desc = hp_desc
        self.ct_desc_high = ct_desc_high
        self.ct_desc_low = ct_desc_low
        self.ct_desc_app = ct_desc_app
        self.ct1 = ct1
        self.ct2 = ct2
        self.ct3 = ct3
        self.cf1 = cf1
        self.cf2 = cf2

""" Decidí pasarlo directamente a la hora de añadirlos a la lista; en vez de hacer las funciones, será más eficiente"""

TON_TO_KG = 1000.0
FT_TO_M   = 0.3048
KT_TO_MS  = 0.514444
MIN_TO_S  = 60.0
KN_TO_N   = 1000.0

""" La lista de aviones con todos los datos en SI"""

aircraft_list = [
    Aircraft(
        name="B767-300ER",
        mlw=0.145150e3 * TON_TO_KG,
        max_weight=0.20410e3 * TON_TO_KG,
        max_payload=0.46500e2 * TON_TO_KG,
        s=0.28350e3,
        cd0_app=0.14000e-1,
        cd2_app=0.49000e-1,
        cd0_clean=0.17400e-1,
        cd2_clean=0.45900e-1,
        hp_desc=26418 * FT_TO_M,
        ct_desc_high=0.64359e-1,
        ct_desc_low=0.55988e-1,
        ct_desc_app=0.12475e0,
        ct1=0.35167e6,
        ct2=0.44673e5 * FT_TO_M,
        ct3=0.10129e-9 / (FT_TO_M ** 2),
        cf1=0.54005e0 / (MIN_TO_S * KN_TO_N),
        cf2=0.55782e3 * KT_TO_MS,
    ),
    Aircraft(
        name="B777-300",
        mlw=0.237680e3 * TON_TO_KG,
        max_weight=0.29930e3 * TON_TO_KG,
        max_payload=0.64900e2 * TON_TO_KG,
        s=0.42804e3,
        cd0_app=0.17300e-1,
        cd2_app=0.48400e-1,
        cd0_clean=0.15700e-1,
        cd2_clean=0.42000e-1,
        hp_desc=36122 * FT_TO_M,
        ct_desc_high=0.44239e-1,
        ct_desc_low=0.41065e-1,
        ct_desc_app=0.92921e-1,
        ct1=0.42577e6,
        ct2=0.48987e5 * FT_TO_M,
        ct3=0.66146e-10 / (FT_TO_M ** 2),
        cf1=0.87843e0 / (MIN_TO_S * KN_TO_N),
        cf2=0.36897e4 * KT_TO_MS,
    ),
    Aircraft(
        name="B737",
        mlw=0.51710e2 * TON_TO_KG,
        max_weight=0.70800e2 * TON_TO_KG,
        max_payload=0.16920e2 * TON_TO_KG,
        s=0.12465e3,
        cd0_app=0.27000e-1,
        cd2_app=0.44100e-1,
        cd0_clean=0.23500e-1,
        cd2_clean=0.44500e-1,
        hp_desc=30152 * FT_TO_M,
        ct_desc_high=0.36336e-1,
        ct_desc_low=0.53395e-1,
        ct_desc_app=0.16440e0,
        ct1=0.14573e6,
        ct2=0.55638e5 * FT_TO_M,
        ct3=0.14200e-10 / (FT_TO_M ** 2),
        cf1=0.94680e0 / (MIN_TO_S * KN_TO_N),
        cf2=0.10000e15 * KT_TO_MS,
    ),
    Aircraft(
        name="A320-212",
        mlw=0.64500e2 * TON_TO_KG,
        max_weight=0.77000e2 * TON_TO_KG,
        max_payload=0.21500e2 * TON_TO_KG,
        s=0.12260e3,
        cd0_app=0.24200e-1,
        cd2_app=0.46900e-1,
        cd0_clean=0.24000e-1,
        cd2_clean=0.37500e-1,
        hp_desc=12398 * FT_TO_M,
        ct_desc_high=0.45711e-1,
        ct_desc_low=0.27207e-1,
        ct_desc_app=0.13981e0,
        ct1=0.13605e6,
        ct2=0.52238e5 * FT_TO_M,
        ct3=0.26637e-10 / (FT_TO_M ** 2),
        cf1=0.94000e0 / (MIN_TO_S * KN_TO_N),
        cf2=0.10000e6 * KT_TO_MS,
    ),
    Aircraft(
        name="A319-131",
        mlw=0.61000e2 * TON_TO_KG,
        max_weight=0.70000e2 * TON_TO_KG,
        max_payload=0.17000e2 * TON_TO_KG,
        s=0.12260e3,
        cd0_app=0.28400e-1,
        cd2_app=0.37600e-1,
        cd0_clean=0.28000e-1,
        cd2_clean=0.31000e-1,
        hp_desc=27726 * FT_TO_M,
        ct_desc_high=0.83084e-1,
        ct_desc_low=0.51765e-1,
        ct_desc_app=0.14767e0,
        ct1=0.13900e6,
        ct2=0.58900e5 * FT_TO_M,
        ct3=0.57200e-14 / (FT_TO_M ** 2),
        cf1=0.68800e0 / (MIN_TO_S * KN_TO_N),
        cf2=0.16700e4 * KT_TO_MS,
    ),
]


"""
#Prueba funcion Presion
h = 10058
p_10058 = presion (h)
print(p_10058)

d_10058 = densidad(h)
print(d_10058)

# Prueba funcion Thrust de descenso
avion_prueba = aircraft_list[0] #escollim un avió qualsevol de la llista (B767-300ER)   |Tram alt>=8.052m, 8.052m<Tram mitjà<1828m
altura_prueba = 1000  # metres                                                                   26.418 peus                6000 peus

thrust_prueba = calcular_thrust_desc(altura_prueba, avion_prueba)
print(f"El Thrust de descenso para el {avion_prueba.name} a {altura_prueba} m es: {thrust_prueba:.3f} N")

"""
"""
# Este es el codigo inicial que realizamos para cumplir la gráfica del PowerPoint
resultados = {}

for aircraft in aircraft_list:
    for pct in [100, 80]:
        max_weight = aircraft.mlw * (pct / 100)
        x_vals, h_vals = simulador(aircraft, max_weight)

        key = f"{aircraft.name}_{pct}"
        resultados[key] = (x_vals, h_vals)

        plt.plot(x_vals, h_vals, label=f"{aircraft.name} [{pct}% MLW]")

plt.xlabel("x [m]")
plt.ylabel("h [m]")
plt.legend()
plt.show()
"""

#Lo siguiente es el codigo que hemos usado para sacar los datos para rellenar los cuadros de datos de los escenarios#

escenario_1 = [
    {"modelo": "B767-300ER", "star": "ALBER1Z", "pct_mlw": 80, "dist_km": 129.08},
    {"modelo": "B737", "star": "PUMAL1Z", "pct_mlw": 100, "dist_km": 94.45},
    {"modelo": "B777-300", "star": "MARTA3Z", "pct_mlw": 100, "dist_km": 178.35},
    {"modelo": "B767-300ER", "star": "MATEX3Z", "pct_mlw": 80, "dist_km": 190.02},
    {"modelo": "A319-131", "star": "LOBAR2W", "pct_mlw": 80, "dist_km": 151.31},
    {"modelo": "A320-212", "star": "CASPE2W", "pct_mlw": 100, "dist_km": 164.09}
]

aircraft_dict = {ac.name: ac for ac in aircraft_list}

resultados = {}

T_ENTRADA = 11 * 3600 + 45 * 60

# PLOT INICIAL (10 trayectorias)
trayectorias = {}
for ac in aircraft_list:
    for pct in [100, 80]:
        x_vals, h_vals, _, _ = simulador(ac, ac.mlw * pct / 100.0, 999)
        trayectorias[f"{ac.name} {pct}%"] = ([abs(x) for x in x_vals], h_vals)

# SCENARIO 1
# Antes aqui se dibujaba con plt.plot en cada vuelta; ahora solo se calculan y guardan los datos,
# y el dibujo se hace en vista_sc1() (boton de la interfaz).
# plt.figure(figsize=(10, 6))

for vuelo in escenario_1:
    ac = aircraft_dict[vuelo["modelo"]]
    max_weight = ac.mlw * (vuelo["pct_mlw"] / 100.0)

    x_vals, h_vals, t_entry, alt_entry = simulador(ac, max_weight, vuelo["dist_km"])

    vuelo["alt_entry"] = alt_entry                # Alt. at STAR entry WP [m]
    vuelo["t_entry"] = t_entry                    # Time STAR entry WP -> IAF [s]
    vuelo["toa_iaf"] = T_ENTRADA + t_entry        # ToA IAF [s]

    # Guardamos los vectores en el diccionario de resultados
    key = f"{ac.name}_{vuelo['pct_mlw']}_{vuelo['star']}"
    vuelo["key"] = key
    resultados[key] = (x_vals, h_vals)

    etiqueta = f"{vuelo['modelo']} [{vuelo['pct_mlw']}%] - {vuelo['star']}"
    vuelo["etiqueta"] = etiqueta
    # plt.plot(x_vals, h_vals, label=etiqueta)    # (version anterior, ahora en vista_sc1)

# Orden de secuencia y separación
orden = sorted(escenario_1, key=lambda v: v["toa_iaf"])
for i, v in enumerate(orden):
    v["seq"] = i + 1
    v["sep"] = None if i == 0 else v["toa_iaf"] - orden[i - 1]["toa_iaf"]

# Tabla Scenario 1 (consola)
print("\n=== SCENARIO 1: llegadas simultáneas a las 11:45:00 en el WP de entrada ===")
print(f"{'Aircraft':<11}|{'STAR':<8}|{'%MLW':<5}|{'Dist[km]':<9}|{'Alt[m]':<9}|{'t->IAF[s]':<10}|{'ToA IAF':<9}|{'Seq':<4}|{'Sep[s]'}")
for v in escenario_1:
    sep = "-" if v["sep"] is None else f"{v['sep']}"
    print(f"{v['modelo']:<11}|{v['star']:<8}|{v['pct_mlw']:<5}|{v['dist_km']:<9.2f}|"
          f"{v['alt_entry']:<9.1f}|{v['t_entry']:<10}|{segundos_a_hora(v['toa_iaf']):<9}|{v['seq']:<4}|{sep}")

# SCENARIO 2
# Separación exacta de 2 min en el IAF, mismo orden que Scenario 1, el primero no se ajusta
SEP_OBJETIVO = 120
toa_primero = orden[0]["toa_iaf"]

print("\n=== SCENARIO 2: separación de 2 min en el IAF ===")
print(f"{'Aircraft':<11}|{'STAR':<8}|{'%MLW':<5}|{'Alt[m]':<9}|{'ToA IAF S2':<11}|{'Delay[s]':<9}|{'ToA STAR entry S2'}")
for i, v in enumerate(orden):
    v["toa_iaf_s2"] = toa_primero + i * SEP_OBJETIVO
    v["toa_entry_s2"] = v["toa_iaf_s2"] - v["t_entry"]
    v["delay"] = v["toa_entry_s2"] - T_ENTRADA          # >0 retraso, <0 adelanto
    print(f"{v['modelo']:<11}|{v['star']:<8}|{v['pct_mlw']:<5}|{v['alt_entry']:<9.1f}|"
          f"{segundos_a_hora(v['toa_iaf_s2']):<11}|{v['delay']:<9}|{segundos_a_hora(v['toa_entry_s2'])}")

# PARTE 4
NM_TO_KM = 1.852
FL = lambda n: n * 100          # FL100 -> 10000 ft

# (WP, distancia del tramo anterior [NM] según AIP, altitud mínima "+" [ft], altitud máxima "-" [ft])
stars_aip = {
    "ALBER1Z": [("ALBER", 0, FL(110), FL(250)), ("CUTXE", 19.5, None, None), ("UTHAN", 22.4, None, None),
                ("ENJUC", 10.5, FL(80), None), ("UCREQ", 6.9, None, FL(100)), ("SLL", 10.4, 6000, None)],
    "PUMAL1Z": [("PUMAL", 0, FL(130), FL(250)), ("BERGA", 11.8, FL(120), None), ("KOSIT", 14.2, None, None),
                ("MAMUK", 5.9, FL(80), None), ("UCREQ", 8.7, None, FL(100)), ("SLL", 10.4, 6000, None)],
    "MARTA3Z": [("MARTA", 0, None, FL(240)), ("EBROX", 21.3, FL(100), None), ("RES", 26.3, None, None),
                ("VLA", 21.2, None, None), ("BL463", 17.5, None, FL(100)), ("SLL", 10.0, 6000, None)],
    "MATEX3Z": [("MATEX", 0, None, FL(280)), ("SENIA", 28.6, FL(100), None), ("RES", 25.3, None, None),
                ("VLA", 21.2, None, None), ("BL463", 17.5, None, FL(100)), ("SLL", 10.0, 6000, None)],
    "LOBAR2W": [("LOBAR", 0, None, FL(280)), ("PEKIS", 36.7, FL(160), FL(200)),
                ("BL461", 35.0, None, FL(100)), ("SLL", 10.0, 6000, None)],
    "CASPE2W": [("CASPE", 0, None, FL(280)), ("MECUH", 41.0, FL(160), FL(200)), ("VIBOK", 20.1, None, FL(150)),
                ("BL461", 17.5, None, FL(100)), ("SLL", 10.0, 6000, None)],
}

"""Formato de altitud para la tabla: FLxxx por encima de la altitud de transición (6000 ft)"""
def fmt_alt(ft):
    return f"{ft} ft" if ft <= 6000 else f"FL{ft // 100:03d}"

filas_parte4 = []      # filas de la tabla grafica
colores_parte4 = []    # color de la celda "Resultado" de cada fila

# Cada STAR se compara SOLO con su avion y su peso (los 6 casos de la tabla del SoW).
# Usamos la trayectoria que ya calculamos en el Scenario 1 (resultados[key]).
caso_por_star = {v["star"]: v for v in escenario_1}

for star, wps in stars_aip.items():
    v = caso_por_star[star]
    xs = [abs(x) for x in resultados[v["key"]][0]]      # distancia al IAF (positiva) [m]
    hs = resultados[v["key"]][1]                        # altura [m]
    total_nm = sum(leg for _, leg, _, _ in wps)
    print(f"\n=== {star}  ({v['modelo']}, {v['pct_mlw']}% MLW) ===")
    print(f"{'WP':<7}|{'Dist IAF[NM]':<13}|{'Alt CDO[ft]':<12}|{'Restriccion':<15}|Resultado")
    acum = 0
    for wp, leg, lo, hi in wps:
        acum += leg
        dist_nm = max(0.0, round(total_nm - acum, 3))      # evita el -0.0 por redondeo
        dist_m = dist_nm * NM_TO_KM * 1000
        alt_ft = np.interp(dist_m, xs, hs) / 0.3048        # altura de ESTE avion en el WP [ft]
        txt = (f">={lo} " if lo else "") + (f"<={hi}" if hi else "")

        # Comparacion con la restriccion (+ = no por debajo de lo, - = no por encima de hi)
        if not txt:
            res, res_g, color = "sin restriccion", "sin restricción", "#E7E6E6"
        elif hi and alt_ft > hi + 1:
            res = res_g = f"INCUMPLE: {alt_ft - hi:.0f} ft POR ENCIMA"
            color = "#FFC7CE"
        elif lo and alt_ft < lo - 1:
            res = res_g = f"INCUMPLE: {lo - alt_ft:.0f} ft POR DEBAJO"
            color = "#FFC7CE"
        else:
            res, res_g, color = "CUMPLE", "CUMPLE", "#C6EFCE"
        print(f"{wp:<7}|{dist_nm:<13.1f}|{alt_ft:<12.0f}|{txt or '-':<15}|{res}")

        # --- fila para la tabla grafica ---
        restr = " / ".join(([f"≥ {fmt_alt(lo)}"] if lo else []) + ([f"≤ {fmt_alt(hi)}"] if hi else [])) or "-"
        filas_parte4.append([f"{v['modelo']} ({v['pct_mlw']}%)", star, wp, f"{dist_nm:.1f}",
                             f"{alt_ft:.0f}", restr, res_g])
        colores_parte4.append(color)

# INTERFAZ GRÁFICA CON BOTONES
# Una sola ventana con 4 botones arriba; cada boton redibuja la zona de abajo:
#   1) Plot inicial  2) Scenario 1 (tabla + grafica)  3) Scenario 2 (tabla)  4) Parte 4 (tabla)
fig = plt.figure(figsize=(16, 9))
try:
    fig.canvas.manager.set_window_title("WP1 - CDO LEBL (RWY 24L)")
except Exception:
    pass

axes_contenido = []     # ejes de la vista actual (se borran al cambiar de boton)

def limpiar():
    for a in axes_contenido:
        a.remove()
    axes_contenido.clear()

def nuevo_eje(rect):
    a = fig.add_axes(rect)
    axes_contenido.append(a)
    return a

"""Dibuja una tabla que ocupa todo el eje. colores = {(fila, columna): color} para celdas concretas"""
def dibujar_tabla(ax, columnas, filas, fontsize=10, colores=None):
    ax.axis("off")
    tabla = ax.table(cellText=filas, colLabels=columnas, cellLoc="center", bbox=[0, 0, 1, 1])
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(fontsize)
    for (r, c), celda in tabla.get_celld().items():
        if r == 0:                                    # cabecera
            celda.set_facecolor("#4F81BD")
            celda.set_text_props(color="white", weight="bold")
        else:                                         # filas alternas
            celda.set_facecolor("#E9EDF4" if r % 2 else "white")
    for (r, c), color in (colores or {}).items():
        tabla[r, c].set_facecolor(color)

# ---------- Boton 1: plot inicial (el del PowerPoint) ----------
def vista_inicial(event=None):
    limpiar()
    ax = nuevo_eje([0.07, 0.07, 0.70, 0.80])
    for k, (xs, hs) in trayectorias.items():
        ax.plot([-x for x in xs], hs, label=k)       # x negativo = distancia antes del IAF
    ax.set_xlabel("x [m]")
    ax.set_ylabel("h [m]")
    ax.set_title("Perfiles de descenso CDO: 5 aviones x (100% y 80% MLW) = 10 trayectorias")
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1))
    ax.grid(True)
    fig.canvas.draw_idle()

# ---------- Boton 2: Scenario 1 (tabla + grafica de los 6 aviones) ----------
def vista_sc1(event=None):
    limpiar()
    ax_t = nuevo_eje([0.03, 0.55, 0.94, 0.32])
    columnas = ["Aircraft\nmodel", "STAR", "%MLW\nIAF", "Dist. STAR entry WP\nto IAF [km]",
                "Alt. at STAR\nentry WP [m]", "Time from STAR entry\nWP to IAF [s]", "ToA IAF",
                "Seq.\nOrder", "Sep. to previous\nat IAF [s]"]
    filas = [[v["modelo"], v["star"], v["pct_mlw"], f"{v['dist_km']:.2f}", f"{v['alt_entry']:.1f}",
              v["t_entry"], segundos_a_hora(v["toa_iaf"]), v["seq"],
              "-" if v["sep"] is None else v["sep"]] for v in escenario_1]
    dibujar_tabla(ax_t, columnas, filas)
    ax_t.set_title("SCENARIO 1: llegadas simultáneas al WP de entrada a las 11:45:00")

    ax_g = nuevo_eje([0.07, 0.07, 0.66, 0.40])
    for v in escenario_1:
        xs, hs = resultados[v["key"]]
        linea, = ax_g.plot(xs, hs, label=v["etiqueta"])
        # punto = WP de entrada de la STAR (altura de la tabla)
        ax_g.plot(-v["dist_km"] * 1000, v["alt_entry"], "o", color=linea.get_color())
    ax_g.set_xlabel("x [m]")
    ax_g.set_ylabel("h [m]")
    ax_g.set_title("Perfiles de descenso CDO - Escenario 1 (LEBL)   (● = WP de entrada de la STAR)")
    ax_g.legend(loc="upper left", bbox_to_anchor=(1.01, 1))
    ax_g.grid(True)
    fig.canvas.draw_idle()

# ---------- Boton 3: Scenario 2 (solo tabla) ----------
def vista_sc2(event=None):
    limpiar()
    ax_t = nuevo_eje([0.03, 0.40, 0.94, 0.47])
    columnas = ["Aircraft\nmodel", "STAR", "Weight\nat IAF", "Alt. at STAR\nentry WP [m]", "ToA IAF\nScenario 2",
                "Applied delay [s]\n(<0 = adelanto)", "ToA STAR entry WP\nScenario 2", "Seq.\nOrder"]
    filas = [[v["modelo"], v["star"], v["pct_mlw"], f"{v['alt_entry']:.1f}", segundos_a_hora(v["toa_iaf_s2"]),
              f"{v['delay']:+d}" if v["delay"] else "0", segundos_a_hora(v["toa_entry_s2"]), v["seq"]]
             for v in escenario_1]
    dibujar_tabla(ax_t, columnas, filas)
    ax_t.set_title("SCENARIO 2: separación exacta de 2 min en el IAF (mismo orden que Scenario 1)")

    fig.canvas.draw_idle()

# ---------- Boton 4: Parte 4 (restricciones de altitud de las STAR) ----------
def vista_parte4(event=None):
    limpiar()
    ax_t = nuevo_eje([0.02, 0.05, 0.96, 0.82])
    columnas = ["Aircraft (%MLW)", "STAR", "WP", "Dist. IAF [NM]", "Altitud CDO [ft]",
                "Restricción AIP", "Resultado"]     # cabecera en 1 linea (la tabla tiene muchas filas)
    colores = {(i + 1, 6): c for i, c in enumerate(colores_parte4)}      # color solo en la columna Resultado
    dibujar_tabla(ax_t, columnas, filas_parte4, fontsize=8, colores=colores)
    ax_t.set_title("PARTE 4: altitud de cada avion (CDO) en los WP de su STAR vs restricciones del AIP (LEBL)")
    fig.text(0.02, 0.015, "Verde = cumple | Rojo = incumple (se indica cuantos ft de desviacion) | Gris = sin restriccion en ese WP",
             fontsize=8)
    fig.canvas.draw_idle()

# ---------- Botones ----------
# (hay que guardar los Button en variables, si no matplotlib los borra y dejan de funcionar)
botones = []
for x0, texto, funcion in [(0.03, "1. Plot inicial", vista_inicial),
                           (0.27, "2. Scenario 1", vista_sc1),
                           (0.51, "3. Scenario 2", vista_sc2),
                           (0.75, "4. Parte 4: restricciones STAR", vista_parte4)]:
    b = Button(fig.add_axes([x0, 0.925, 0.22, 0.05]), texto)
    b.on_clicked(funcion)
    botones.append(b)

vista_inicial()      # vista por defecto al abrir la ventana
plt.show()