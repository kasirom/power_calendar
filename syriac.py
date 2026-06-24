# Syriac calendar
def syriac_date(dt):

    year = dt.year + 311

    return (
        f"Suryani : "
        f"{dt.day}-{dt.month}-{year}"
    )