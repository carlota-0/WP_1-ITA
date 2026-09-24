class Aircraft:
    name: str

    # Pesos y geometría
    mlw: float          # Max Landing Weight (tons)
    max_weight: float   # Max Weight (tons)
    max_payload: float  # Max Payload (tons)
    s: float            # Superficie alar S (m^2)

    # Coeficientes de arrastre - aproximación (flaps/gear out)
    cd0_app: float
    cd2_app: float

    # Coeficientes de arrastre - configuración limpia
    cd0_clean: float
    cd2_clean: float

    # Descenso
    hp_desc: float       # Altitud de transición de descenso (ft)
    ct_desc_high: float
    ct_desc_low: float
    ct_desc_app: float

    # Modelo de empuje (thrust)
    ct1: float   # N
    ct2: float   # ft
    ct3: float   # 1/ft^2

    # Modelo de consumo de combustible (fuel flow)
    cf1: float   # kg/(min*kN)
    cf2: float   # kt


aircraft_list = [
    Aircraft(
        name="B767-300ER",
        mlw=145.150, max_weight=204.10, max_payload=46.500, s=283.50,
        cd0_app=0.014000, cd2_app=0.049000,
        cd0_clean=0.017400, cd2_clean=0.045900,
        hp_desc=26418, ct_desc_high=0.064359, ct_desc_low=0.055988, ct_desc_app=0.12475,
        ct1=0.35167e6, ct2=0.44673e5, ct3=0.10129e-9,
        cf1=0.54005, cf2=0.55782e3,
    ),
    Aircraft(
        name="B777-300",
        mlw=237.680, max_weight=299.30, max_payload=64.900, s=428.04,
        cd0_app=0.017300, cd2_app=0.048400,
        cd0_clean=0.015700, cd2_clean=0.042000,
        hp_desc=36122, ct_desc_high=0.044239, ct_desc_low=0.041065, ct_desc_app=0.092921,
        ct1=0.42577e6, ct2=0.48987e5, ct3=0.66146e-10,
        cf1=0.87843, cf2=0.36897e4,
    ),
    Aircraft(
        name="B737",
        mlw=51.710, max_weight=70.80, max_payload=16.920, s=124.65,
        cd0_app=0.027000, cd2_app=0.044100,
        cd0_clean=0.023500, cd2_clean=0.044500,
        hp_desc=30152, ct_desc_high=0.036336, ct_desc_low=0.053395, ct_desc_app=0.16440,
        ct1=0.14573e6, ct2=0.55638e5, ct3=0.14200e-10,
        cf1=0.94680, cf2=0.10000e15,
    ),
    Aircraft(
        name="A320-212",
        mlw=64.500, max_weight=77.00, max_payload=21.500, s=122.60,
        cd0_app=0.024200, cd2_app=0.046900,
        cd0_clean=0.024000, cd2_clean=0.037500,
        hp_desc=12398, ct_desc_high=0.045711, ct_desc_low=0.027207, ct_desc_app=0.13981,
        ct1=0.13605e6, ct2=0.52238e5, ct3=0.26637e-10,
        cf1=0.94000, cf2=0.10000e6,
    ),
    Aircraft(
        name="A319-131",
        mlw=61.000, max_weight=70.00, max_payload=17.000, s=122.60,
        cd0_app=0.028400, cd2_app=0.037600,
        cd0_clean=0.028000, cd2_clean=0.031000,
        hp_desc=27726, ct_desc_high=0.083084, ct_desc_low=0.051765, ct_desc_app=0.14767,
        ct1=0.13900e6, ct2=0.58900e5, ct3=0.57200e-14,
        cf1=0.68800, cf2=0.16700e4,
    ),
]


if __name__ == "__main__":
    for ac in aircraft_list:
        print(f"{ac.name}: MTOW={ac.max_weight} t, S={ac.s} m^2, CD0_clean={ac.cd0_clean}")
