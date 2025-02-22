import sys
import numpy as np
import sympy as sp
import re
from UI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem

class logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            r'\be\b' : 'E',        }
        for variabel, pengganti in replacement.items():
            fungsi = re.sub(variabel, pengganti, fungsi)
        return fungsi
    
    def fungsiTersimpan(self):
        x = 0
        self.fungsiStr = self.ketikFungsi.text()
        self.ketikFungsi.clear()
        self.f(x)
        
    def f(self, x):
        self.fungsiParsed = self.replacement(self.fungsiStr)
        try:
            return eval(self.fungsiParsed, {"__builtins__": None}, {"x": x, "np": np, "E": np.e})
        except TypeError:
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
        except TypeError or fungsi_derivatif == 0:
            QMessageBox.warning(None, "Error Fungsi Turunan", "Fungsi gagal dikonversi ke turunan.")
            return

    def hitungBiseksi(self):
        a = float(self.aBiseksi.text())
        b = float(self.bBiseksi.text())
        e = float(self.toleransiBiseksi.text())
        self.tabelBiseksi.clearContents()
        for o in range(0, 20):
            x = (a+b)/2
            fx = self.f(x)
            fb = self.f(b)
            fa = self.f(a)
            m = "Lanjut"
            if abs(fx) < e:
                m = "Berhenti"
                self.isiTabelBiseksi(o,a,b,x,fx,fa,fb,m)
                break
            if fx * fa < 0:
                b = x
            else:
                a = x
            self.isiTabelBiseksi(o,a,b,x,fx,fa,fb,m)
            
    def hitungRegulaFalsi(self):
        a = float(self.aRegulaFalsi.text())
        b = float(self.bRegulaFalsi.text())
        e = float(self.toleransiRegulaFalsi.text())
        self.tabelRegulaFalsi.clearContents()
        for o in range(0, 20):
            a = a
            b = b
            fb = self.f(b)
            fa = self.f(a)
            x = float((fb*a-fa*b)/(fb-fa))
            fx = self.f(x)
            m = "Lanjut"
            if abs(fx)<e:
                m = "Berhenti"
                self.isiTabelRegulaFalsi(o, a, b, x, fx, fa, fb, m)
                break
            if fx * fa < 0:
                b = x
            else:
                a = x
            self.isiTabelRegulaFalsi(o,a,b,x,fx,fa,fb,m)
            
    def hitungSecant(self):
        x0 = float(self.x0Secant.text())
        x1 = float(self.x1Secant.text())
        e = float(self.toleransiSecant.text())
        m = "Lanjut"
        for i in range(0, 21):
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
        x = float(self.xNewtonRaphson.text())
        e = float(self.toleransiNewtonRaphson.text())
        m = "Lanjut"
        for o in range(0, 21):
            fx = self.f(x)
            fungsiDerr = self.fungsiDerivatif(x)
            if abs(fx)<e:
                m = "Berhenti"
                self.isiTabelNewtonRaphson(o, x, fx, fungsiDerr, m)
                break
            self.isiTabelNewtonRaphson(o, x, fx, fungsiDerr, m)
            x = x - (fx/fungsiDerr)
            
    def ubahkeBiseksi(self):
        self.stackedWidget.setCurrentWidget(self.halamanBiseksi)
    def ubahkeNewtonRaphson(self):
        self.stackedWidget.setCurrentWidget(self.halamanNewtonRaphson)
    def ubahkeRegulaFalsi(self):
        self.stackedWidget.setCurrentWidget(self.halamanRegulaFalsi)
    def ubahkeSecant(self):
        self.stackedWidget.setCurrentWidget(self.halamanSecant)

    def isiTabelBiseksi(self,i,a,b,x,fx,fa,fb,status):
        self.tabelBiseksi.setItem(i, 0, QTableWidgetItem(str(i+1)))
        self.tabelBiseksi.setItem(i, 1, QTableWidgetItem(str(f"{a:.6f}")))
        self.tabelBiseksi.setItem(i, 2, QTableWidgetItem(str(f"{b:.6f}")))
        self.tabelBiseksi.setItem(i, 3, QTableWidgetItem(str(f"{x:.6f}")))
        self.tabelBiseksi.setItem(i, 4, QTableWidgetItem(str(f"{fx:.6f}")))
        self.tabelBiseksi.setItem(i, 5, QTableWidgetItem(str(f"{fa:.6f}")))
        self.tabelBiseksi.setItem(i, 6, QTableWidgetItem(str(f"{fb:.6f}")))
        self.tabelBiseksi.setItem(i, 7, QTableWidgetItem(str(status)))
    def isiTabelRegulaFalsi(self,i, a, b, x, fx, fa, fb, status):
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
