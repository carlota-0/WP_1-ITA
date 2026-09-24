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


aircraft_list = [
    Aircraft(
        name="B767-300ER",
        mlw=0.145150e3, max_weight=0.20410e3, max_payload=0.46500e2, s=0.28350e3,
        cd0_app=0.14000e-1, cd2_app=0.49000e-1,
        cd0_clean=0.17400e-1, cd2_clean=0.45900e-1,
        hp_desc=26418, ct_desc_high=0.64359e-1, ct_desc_low=0.55988e-1, ct_desc_app=0.12475e0,
        ct1=0.35167e6, ct2=0.44673e5, ct3=0.10129e-9,
        cf1=0.54005e0, cf2=0.55782e3,
    ),
    Aircraft(
        name="B777-300",
        mlw=0.237680e3, max_weight=0.29930e3, max_payload=0.64900e2, s=0.42804e3,
        cd0_app=0.17300e-1, cd2_app=0.48400e-1,
        cd0_clean=0.15700e-1, cd2_clean=0.42000e-1,
        hp_desc=36122, ct_desc_high=0.44239e-1, ct_desc_low=0.41065e-1, ct_desc_app=0.92921e-1,
        ct1=0.42577e6, ct2=0.48987e5, ct3=0.66146e-10,
        cf1=0.87843e0, cf2=0.36897e4,
    ),
    Aircraft(
        name="B737",
        mlw=0.51710e2, max_weight=0.70800e2, max_payload=0.16920e2, s=0.12465e3,
        cd0_app=0.27000e-1, cd2_app=0.44100e-1,
        cd0_clean=0.23500e-1, cd2_clean=0.44500e-1,
        hp_desc=30152, ct_desc_high=0.36336e-1, ct_desc_low=0.53395e-1, ct_desc_app=0.16440e0,
        ct1=0.14573e6, ct2=0.55638e5, ct3=0.14200e-10,
        cf1=0.94680e0, cf2=0.10000e15,
    ),
    Aircraft(
        name="A320-212",
        mlw=0.64500e2, max_weight=0.77000e2, max_payload=0.21500e2, s=0.12260e3,
        cd0_app=0.24200e-1, cd2_app=0.46900e-1,
        cd0_clean=0.24000e-1, cd2_clean=0.37500e-1,
        hp_desc=12398, ct_desc_high=0.45711e-1, ct_desc_low=0.27207e-1, ct_desc_app=0.13981e0,
        ct1=0.13605e6, ct2=0.52238e5, ct3=0.26637e-10,
        cf1=0.94000e0, cf2=0.10000e6,
    ),
    Aircraft(
        name="A319-131",
        mlw=0.61000e2, max_weight=0.70000e2, max_payload=0.17000e2, s=0.12260e3,
        cd0_app=0.28400e-1, cd2_app=0.37600e-1,
        cd0_clean=0.28000e-1, cd2_clean=0.31000e-1,
        hp_desc=27726, ct_desc_high=0.83084e-1, ct_desc_low=0.51765e-1, ct_desc_app=0.14767e0,
        ct1=0.13900e6, ct2=0.58900e5, ct3=0.57200e-14,
        cf1=0.68800e0, cf2=0.16700e4,
    ),
]

if __name__ == "__main__":
    for ac in aircraft_list:
        print(f"{ac.name}: MTOW={ac.max_weight} t, S={ac.s} m^2, CD0_clean={ac.cd0_clean}")
