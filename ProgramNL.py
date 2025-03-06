import sys
import numpy as np
import sympy as sp
import re
from UI import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem

class logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.tombolBiseksi.clicked.connect(self.ubahkeBiseksi)
        self.tombolNewtonRaphson.clicked.connect(self.ubahkeNewtonRaphson)
        self.tombolRegulaFalsi.clicked.connect(self.ubahkeRegulaFalsi)
        self.tombolSecant.clicked.connect(self.ubahkeSecant)
        self.simpanFungsi.clicked.connect(self.fungsiTersimpan)
        self.cariHasilBiseksi.clicked.connect(self.hitungBiseksi)
        self.cariHasilRegulaFalsi.clicked.connect(self.hitungRegulaFalsi)
        self.cariHasilSecant.clicked.connect(self.hitungSecant)
        self.cariHasilNewtonRaphson.clicked.connect(self.hitungNewtonRaphson)
    
    def replacement(self, fungsi): 
        replacement = {
            r'\bsin\b': 'np.sin',
            r'\bcos\b': 'np.cos',
            r'\btan\b': 'np.tan',
            r'\be\b' : 'E',
            r'\^' : '**',        
        }
        for variabel, pengganti in replacement.items():
            fungsi = re.sub(variabel, pengganti, fungsi)
        return fungsi
    
    def fungsiTersimpan(self):
        self.fungsiStr = self.ketikFungsi.text()
        self.ketikFungsi.clear()
        
    def f(self, x):
        self.fungsiParsed = self.replacement(self.fungsiStr)
        try:
            x_symbol = sp.symbols('x')
            fungsi_expr = sp.parse_expr(self.fungsiParsed, transformations="all")
            fungsi_lambdified = sp.lambdify(x_symbol, fungsi_expr, modules=["numpy", {"e": sp.E}])
            return fungsi_lambdified(x)
        except (TypeError, SyntaxError):
            QMessageBox.warning(None, "Error Fungsi", "Fungsi tidak tepat.")
            return
        
    def fungsiDerivatif(self, x):
        try:
            x_symbol = sp.symbols('x')
            fungsi_string = self.replacement(self.fungsiStr)
            fungsi_symbol = sp.parse_expr(fungsi_string, transformations="all") 
            fungsi_derivatif = sp.diff(fungsi_symbol, x_symbol)
            turunanFungsi = sp.lambdify(x_symbol, fungsi_derivatif, modules=["numpy", {"e": sp.E}])
            return turunanFungsi(x)
        except (TypeError, SyntaxError):
            QMessageBox.warning(None, "Error Fungsi Turunan", "Fungsi gagal dikonversi ke turunan.")
            return

    def hitungMetodeTertentu(self, metode, a, b, e, tabel, isiTabel):
        for o in range(0,20):
            if metode == "Biseksi":
                x = (a + b) / 2
            elif metode == "RegulaFalsi":
                fb = self.f(b)
                fa = self.f(a)
                x = (fb * a - fa * b) / (fb - fa)
            fx = self.f(x)
            fa = self.f(a)
            fb = self.f(b)
            m = "Lanjut"
            if abs(fx) < e:
                m = "Berhenti"
                isiTabel(o, a, b, x, fx, fa, fb, m)
                break
            if fx * fa < 0:
                b = x
            else:
                a = x
            isiTabel(o, a, b, x, fx, fa, fb, m)

    def get_float_input(self, input_field, field_name):
        try:
            return float(input_field.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", f"Invalid input for {field_name}. Please enter a valid number.")
            return None

    def hitungBiseksi(self):
        self.tabelBiseksi.clearContents()
        a = self.get_float_input(self.aBiseksi, "a (Biseksi)")
        b = self.get_float_input(self.bBiseksi, "b (Biseksi)")
        e = self.get_float_input(self.toleransiBiseksi, "toleransi (Biseksi)")
        if a is not None and b is not None and e is not None:
            self.hitungMetodeTertentu("Biseksi", a, b, e, self.tabelBiseksi, self.isiTabelBiseksi)

    def hitungRegulaFalsi(self):
        self.tabelRegulaFalsi.clearContents()
        a = self.get_float_input(self.aRegulaFalsi, "a (Regula Falsi)")
        b = self.get_float_input(self.bRegulaFalsi, "b (Regula Falsi)")
        e = self.get_float_input(self.toleransiRegulaFalsi, "toleransi (Regula Falsi)")
        if a is not None and b is not None and e is not None:
            self.hitungMetodeTertentu("RegulaFalsi", a, b, e, self.tabelRegulaFalsi, self.isiTabelRegulaFalsi)

    def hitungSecant(self):
        self.tabelSecant.clearContents()
        x0 = self.get_float_input(self.x0Secant, "x0 (Secant)")
        x1 = self.get_float_input(self.x1Secant, "x1 (Secant)")
        e = self.get_float_input(self.toleransiSecant, "toleransi (Secant)")
        if x0 is not None and x1 is not None and e is not None:
            m = "Lanjut"
            for i in range(21):
                y0 = self.f(x0)  
                y1 = self.f(x1) 
                if abs(y0) < e:
                    m = "Berhenti"
                    self.isiTabelSecant(i, x0, y0, m)  
                    break
                self.isiTabelSecant(i, x0, y0, m)            
                x2 = x1 - y1 * ((x1 - x0) / (y1 - y0))
                x0, x1 = x1, x2

    def hitungNewtonRaphson(self):
        self.tabelNewtonRaphson.clearContents()
        x = self.get_float_input(self.xNewtonRaphson, "x (Newton Raphson)")
        e = self.get_float_input(self.toleransiNewtonRaphson, "toleransi (Newton Raphson)")
        if x is not None and e is not None:
            m = "Lanjut"
            for o in range(21):
                fx = self.f(x)
                fungsiDerr = self.fungsiDerivatif(x)
                if abs(fx) < e:
                    m = "Berhenti"
                    self.isiTabelNewtonRaphson(o, x, fx, fungsiDerr, m)
                    break
                self.isiTabelNewtonRaphson(o, x, fx, fungsiDerr, m)
                x = x - (fx / fungsiDerr)
            
    def ubahkeBiseksi(self):
        self.stackedWidget.setCurrentWidget(self.halamanBiseksi)
    def ubahkeNewtonRaphson(self):
        self.stackedWidget.setCurrentWidget(self.halamanNewtonRaphson)
    def ubahkeRegulaFalsi(self):
        self.stackedWidget.setCurrentWidget(self.halamanRegulaFalsi)
    def ubahkeSecant(self):
        self.stackedWidget.setCurrentWidget(self.halamanSecant)

    def isiTabelBiseksi(self, i, a, b, x, fx, fa, fb, status):
        self.tabelBiseksi.setItem(i, 0, QTableWidgetItem(str(i+1)))
        self.tabelBiseksi.setItem(i, 1, QTableWidgetItem(str(f"{a:.6f}")))
        self.tabelBiseksi.setItem(i, 2, QTableWidgetItem(str(f"{b:.6f}")))
        self.tabelBiseksi.setItem(i, 3, QTableWidgetItem(str(f"{x:.6f}")))
        self.tabelBiseksi.setItem(i, 4, QTableWidgetItem(str(f"{fx:.6f}")))
        self.tabelBiseksi.setItem(i, 5, QTableWidgetItem(str(f"{fa:.6f}")))
        self.tabelBiseksi.setItem(i, 6, QTableWidgetItem(str(f"{fb:.6f}")))
        self.tabelBiseksi.setItem(i, 7, QTableWidgetItem(str(status)))
    def isiTabelRegulaFalsi(self, i, a, b, x, fx, fa, fb, status):
        self.tabelRegulaFalsi.setItem(i, 0, QTableWidgetItem(str(i+1)))
        self.tabelRegulaFalsi.setItem(i, 1, QTableWidgetItem(str(f"{a:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 2, QTableWidgetItem(str(f"{b:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 3, QTableWidgetItem(str(f"{x:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 4, QTableWidgetItem(str(f"{fx:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 5, QTableWidgetItem(str(f"{fa:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 6, QTableWidgetItem(str(f"{fb:.6f}")))
        self.tabelRegulaFalsi.setItem(i, 7, QTableWidgetItem(str(status)))
    def isiTabelSecant(self, i, x, y, status):
        self.tabelSecant.setItem(i, 0, QTableWidgetItem(str(i)))
        self.tabelSecant.setItem(i, 1, QTableWidgetItem(str(f"{x:.6f}")))
        self.tabelSecant.setItem(i, 2, QTableWidgetItem(str(f"{y:.6f}")))
        self.tabelSecant.setItem(i, 3, QTableWidgetItem(str(status)))
    def isiTabelNewtonRaphson(self, i, x, fx, fxderivatif, status):
        self.tabelNewtonRaphson.setItem(i, 0, QTableWidgetItem(str(i)))
        self.tabelNewtonRaphson.setItem(i, 1, QTableWidgetItem(str(f"{x:.6f}")))
        self.tabelNewtonRaphson.setItem(i, 2, QTableWidgetItem(str(f"{fx:.6f}")))
        self.tabelNewtonRaphson.setItem(i, 3, QTableWidgetItem(str(f"{fxderivatif:.6f}")))
        self.tabelNewtonRaphson.setItem(i, 4, QTableWidgetItem(str(status)))
        

app = QApplication(sys.argv)
window = logic()
window.show()
app.exec()