from datetime import date


def mmyy_to_date(st: str):
    if not st:
        return None
    (mm, yy) = st.split(".")
    return date(int(yy), int(mm), 1)


def date_to_mmyy(dt: date):
    return dt.strftime("%m.%Y")

def yymmdd_to_date(st: str):
    if not st:
        return None
    (yy, mm, dd) = st.split(".")
    return date(int(yy), int(mm), int(dd))
