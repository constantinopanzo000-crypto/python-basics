import sys
import os
import psutil
from plyer import notification
from PyQt5 import uic, QtWidgets, QtCore, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication

#-----------------------Função de busca de recursos -------------------------
def resource_path(relative_path):
    """Pega o caminho absoluto do recurso, funcionando dentro do PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#----------------------Classe da Janela de diálogo--------------------------
class Sobre(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("sobre.ui"), self)

        self.setFixedSize(314, 304)
        self.posicionar_no_canto()

        icone = QIcon(resource_path("icone.png"))
        self.setWindowIcon(icone)



    def posicionar_no_canto(self):
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geo = screen.availableGeometry()

        janela_largura = self.frameGeometry().width()
        janela_altura = self.frameGeometry().height()

        x = screen_geo.x() + screen_geo.width() - janela_largura - 40
        y = screen_geo.y() + screen_geo.height() - janela_altura - 40

        self.move(x, y)

#----------------------Classe da Janela principal---------------------------
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("tela.ui"), self)

        # Aplicando estilo
        self.setStyleSheet("""
        QMainWindow { background-color: #0f172a; }
        #cardContainer { background-color: #1e293b; border-radius: 15px; padding: 20px; }
        QLabel { color: #e2e8f0; font-weight: bold; }
        #lblCPU { background-color: #1e293b; border-left: 6px solid #22c55e; padding: 10px; border-radius: 8px; font-size: 22px; }
        #lblRAM { background-color: #1e293b; border-left: 6px solid #3b82f6; padding: 10px; border-radius: 8px; font-size: 22px; }
        #lblDisco { background-color: #1e293b; border-left: 6px solid #f59e0b; padding: 10px; border-radius: 8px; font-size: 22px; }
        #lblVersao { color: gray; }
        #btnSobre { background-color: #0f172a; color: gray; border: none; }
        QMenuBar { background-color: #1e293b; color: #e2e8f0; }
        QMenuBar::item:selected { background: #334155; }
        QStatusBar { background-color: #1e293b; color: #94a3b8; }
        QMessageBox{background-color: #0f172a; color: white; font-weight: bold; }
        QTextEdit{border: none; font-size: 12px}
        """)

        self.setFixedSize(287, 224)

        # Inicializando recursos
        self.btnSobre.clicked.connect(self.abrir_tela_sobre)
        self.posicionar_no_canto()

        self.alerta_cpu = False
        self.alerta_ram = False
        self.alerta_disco = False

        # Inicializa histórico da CPU para psutil
        psutil.cpu_percent(interval=None)

        # Timer para atualizar os valores
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.verificar_sistema)
        self.timer.start(1000)  # 1 segundo

        # Ícone e tray
        icone = QIcon(resource_path("icone.png"))
        self.setWindowIcon(icone)
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(icone)
        self.tray.setVisible(True)

        # Menu do tray
        menu = QtWidgets.QMenu()
        abrir = menu.addAction("Abrir")
        abrir.triggered.connect(self.show)
        sair = menu.addAction("Sair")
        sair.triggered.connect(QtWidgets.QApplication.quit)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip("System Monitor\n\nClique no botão direito do mouse para abrir menu.")

        self.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray.showMessage(
            "System Monitor",
            "O app continua rodando em segundo plano",
            msecs=2000
        )

    # Sistema de alertas
    def perigo(self, cpu, ram, disco):
        if cpu > 89 and not self.alerta_cpu:
            notification.notify(title="⚠ Uso elevado de CPU",
                                message=f"A CPU está em {cpu}%",
                                app_name="System Monitor", timeout=5)
            self.alerta_cpu = True
        elif cpu <= 70:
            self.alerta_cpu = False

        if ram > 80 and not self.alerta_ram:
            notification.notify(title="⚠ Uso elevado de RAM",
                                message=f"A RAM está em {ram}%",
                                app_name="System Monitor", timeout=5)
            self.alerta_ram = True
        elif ram <= 60:
            self.alerta_ram = False

        if disco > 80 and not self.alerta_disco:
            notification.notify(title="⚠ Disco quase cheio",
                                message=f"Armazenamento em {disco}%",
                                app_name="System Monitor", timeout=5)
            self.alerta_disco = True
        elif disco <= 65:
            self.alerta_disco = False

    # Função principal do timer
    def verificar_sistema(self):
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        disco = psutil.disk_usage('/').percent

        self.lblCPU.setText(f"CPU: {cpu}%")
        self.lblRAM.setText(f"RAM: {ram}%")
        self.lblDisco.setText(f"Disco: {disco}%")

        self.perigo(cpu, ram, disco)



    def abrir_tela_sobre(self):
        self.dialogo = Sobre()
        self.dialogo.show()

    def posicionar_no_canto(self):
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geo = screen.availableGeometry()
        janela_largura = self.frameGeometry().width()
        janela_altura = self.frameGeometry().height()
        x = screen_geo.x() + screen_geo.width() - janela_largura - 40
        y = screen_geo.y() + screen_geo.height() - janela_altura - 40
        self.move(x, y)

#-----------------------Executar o programa-------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Main()
    janela.show()
    sys.exit(app.exec_())
