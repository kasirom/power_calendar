from datetime import datetime
from hijri_converter import Gregorian
from lunardate import LunarDate

from javanese import get_weton
from maya import maya_long_count
from syriac import syriac_date


class CalendarEngine:

    def hijri(self, dt):
        h = Gregorian(dt.year, dt.month, dt.day).to_hijri()
        return f"Hijriyah : {h.day}-{h.month}-{h.year}"

    def javanese(self, dt):
        return get_weton(dt)

    def chinese(self, dt):
        lunar = LunarDate.fromSolarDate(dt.year, dt.month, dt.day)
        return f"Cina Lunar : {lunar.day}/{lunar.month}/{lunar.year}"

    def syriac(self, dt):
        return syriac_date(dt)

    def maya(self, dt):
        return maya_long_count(dt)

    # 🔥 RAMALAN PRIMBON
    def analisis_primbon(self, nama, alamat, dt):
        weton = get_weton(dt)

        hasil = []
        hasil.append("=== HASIL ANALISIS PRIMBON ===")
        hasil.append(f"Nama : {nama}")
        hasil.append(f"Alamat : {alamat}")
        hasil.append(f"Lahir : {dt:%d-%m-%Y}")
        hasil.append("")
        hasil.append(weton)
        hasil.append("")

        # contoh logika sederhana
        hari = dt.weekday()

        sifat = [
            "Pemimpin alami",
            "Bijaksana dan tenang",
            "Kreatif tinggi",
            "Emosional tapi kuat",
            "Pekerja keras",
            "Cerdas & analitis",
            "Spiritual kuat"
        ]

        hasil.append(f"Sifat Dominan : {sifat[hari]}")

        hasil.append("\nRezeki : Lancar jika konsisten")
        hasil.append("Jodoh : Cocok dengan karakter sabar")
        hasil.append("Karier : Bagus di bidang teknologi / bisnis")

        return "\n".join(hasil)