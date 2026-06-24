# Entry point for PowerCalendar ULTIMATE
#print('PowerCalendar ULTIMATE project scaffold')
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *

from datetime import datetime

from calendar_engine import CalendarEngine
from events_db import EventDatabase


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.engine = CalendarEngine()
        self.events = EventDatabase()

        self.setWindowTitle("POWER CALENDAR ULTIMATE")
        self.resize(700,80)

        self.build_ui()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # ==========================
        # KIRI (KALENDER)
        # ==========================
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        main_layout.addWidget(self.calendar, 3)

        # ==========================
        # KANAN
        # ==========================
        right = QVBoxLayout()

        self.info = QTextEdit()
        self.info.setReadOnly(True)
        right.addWidget(self.info, 3)

        # SEARCH
        search_group = QGroupBox("Pencarian Tanggal")
        search_layout = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("YYYY-MM-DD")

        btn = QPushButton("Cari")

        search_layout.addWidget(self.search)
        search_layout.addWidget(btn)

        search_group.setLayout(search_layout)
        right.addWidget(search_group)

        # BIODATA
        biodata_group = QGroupBox("Analisis Weton & Primbon")
        form = QFormLayout()

        self.nama_edit = QLineEdit()
        self.alamat_edit = QTextEdit()
        self.alamat_edit.setMaximumHeight(60)

        self.lahir_edit = QLineEdit()
        self.lahir_edit.setPlaceholderText("YYYY-MM-DD")

        form.addRow("Nama", self.nama_edit)
        form.addRow("Alamat", self.alamat_edit)
        form.addRow("Tanggal Lahir", self.lahir_edit)

        self.ramal_btn = QPushButton("Analisis")
        form.addRow(self.ramal_btn)

        biodata_group.setLayout(form)
        right.addWidget(biodata_group)

        self.ramal_output = QTextEdit()
        self.ramal_output.setReadOnly(True)
        right.addWidget(self.ramal_output, 2)

        main_layout.addLayout(right, 2)

        # CONNECT
        btn.clicked.connect(self.search_date)
        self.ramal_btn.clicked.connect(self.proses_ramal)
        self.calendar.selectionChanged.connect(self.update_info)

        self.update_info()

    def search_date(self):
        try:
            dt = datetime.strptime(self.search.text(), "%Y-%m-%d")
            self.calendar.setSelectedDate(QDate(dt.year, dt.month, dt.day))
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def update_info(self):
        q = self.calendar.selectedDate()
        dt = datetime(q.year(), q.month(), q.day())

        txt = []
        txt.append(f"Masehi : {dt:%d-%m-%Y}")
        txt.append(self.engine.hijri(dt))
        txt.append(self.engine.javanese(dt))
        txt.append(self.engine.chinese(dt))
        txt.append(self.engine.syriac(dt))
        txt.append(self.engine.maya(dt))

        txt.append("\nPERISTIWA")
        for event in self.events.find(dt):
            txt.append(f"• {event}")

        self.info.setText("\n".join(txt))
    def proses_ramal(self):
        try:
            nama = self.nama_edit.text()
            alamat = self.alamat_edit.toPlainText()
            dt = datetime.strptime(self.lahir_edit.text(), "%Y-%m-%d")

            hasil = self.engine.analisis_primbon(nama, alamat, dt)
            self.ramal_output.setText(hasil)

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))


app = QApplication(sys.argv)
app.setStyle("Fusion")

window = MainWindow()
window.show()

sys.exit(app.exec())