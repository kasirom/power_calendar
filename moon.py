# Moon phase calculations
from datetime import datetime

def moon_phase(dt):

    known_new_moon = datetime(
        2000,
        1,
        6
    )

    days = (
        dt -
        known_new_moon
    ).days

    phase = (
        days % 29.53
    )

    return phase