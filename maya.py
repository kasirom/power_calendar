# Maya calendar
from datetime import datetime

MAYA_EPOCH = datetime(
    2012,
    12,
    21
)


def maya_long_count(dt):

    days = (
        dt - MAYA_EPOCH
    ).days

    baktun = 13 + (
        days // 144000
    )

    return (
        f"Maya Long Count : "
        f"{baktun}"
    )