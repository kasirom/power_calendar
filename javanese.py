# Weton, neptu, primbon
from datetime import datetime

PASARAN = [
    
    "Pahing",
    "Pon",
    "Wage",
    "Kliwon",
    "Legi"
]

HARI = [
    "Senin",
    "Selasa",
    "Rabu",
    "Kamis",
    "Jumat",
    "Sabtu",
    "Minggu"
]


def get_weton(dt):

    base = datetime(
        2024,
        1,
        1
    )

    diff = (
        dt - base
    ).days

    pasaran = PASARAN[
        diff % 5
    ]

    hari = HARI[
        dt.weekday()
    ]

    return (
        f"Weton Jawa : "
        f"{hari} {pasaran}"
    )