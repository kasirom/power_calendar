from datetime import datetime
import json
from pathlib import Path

try:
    from hijri_converter import Gregorian
except:
    Gregorian = None

EVENTS = {}
p = Path(__file__).with_name("events.json")
if p.exists():
    EVENTS = json.loads(p.read_text(encoding="utf8"))

def get_hijri(dt):
    if Gregorian:
        h = Gregorian(dt.year,dt.month,dt.day).to_hijri()
        return f"Hijriyah : {h.day}-{h.month}-{h.year}"
    return "Hijriyah : install hijri-converter"

def get_javanese(dt):
    pasaran = ["Legi","Pahing","Pon","Wage","Kliwon"]
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    base = datetime(2024,1,1)
    idx = (dt-base).days % 5
    return f"Weton Jawa : {hari[dt.weekday()]} {pasaran[idx]}"

def get_chinese(dt):
    return f"Kalender Cina : {dt.year} (placeholder lunar)"

def get_maya(dt):
    return "Kalender Maya : Long Count (placeholder)"

def get_syriac(dt):
    return f"Kalender Suryani : {dt.day}-{dt.month}-{dt.year+311}"

def get_events(dt):
    k = dt.strftime("%d-%m")
    return EVENTS.get(k, ["Tidak ada data"])
