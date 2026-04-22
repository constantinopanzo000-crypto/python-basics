"""
Roob IA: Minha primeira assistente em Python
Criada por: Constantino Panzo Tula
Origem: SMART-CODE Universo
Data do início: 13/01/2026
Obrigrado pela contribuição!
"""

# Importação dos componentes do script
import sys
import os
import datetime
import random
import subprocess
import math

# Importação da GUI
import qtawesome as qta
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QPoint


# ---------------- RESOURCE PATH ----------------
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# ---------------- JANELA QDIALOG QUADRADO ----------------
def add_tooltip_global(widget, texto):
    widget.setToolTip(texto)
    widget.setStyleSheet("""
            QToolTip{
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #555;
                padding: 6px;
                border-radius: 4px;
            }
        """)


class InformacaoQuadrado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacoes_quadrado.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)


class InformacaoTriangulo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacoes_triangulo.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditTriangulo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditTriangulo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditTriangulo.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditTriangulo.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoCirculo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacoes_circulo.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)


class InformacaoRectangulo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacoes_rectangulo.ui"), self)

        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditRectangulo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditRectangulo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditRectangulo.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditRectangulo.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoCilindro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacoes_cilindro.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditCilindro.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditCilindro.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditCilindro.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditCilindro.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoLosango(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacao_losango.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditLosango.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditLosango.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditLosango.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditLosango.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoSeno(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_imformacoes_seno.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditSeno.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditSeno.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditSeno.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditSeno.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoSeno(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_imformacoes_seno.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditSeno.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditSeno.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditSeno.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditSeno.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoCosseno(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacao_cosseno.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditCosseno.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditCosseno.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditCosseno.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditCosseno.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoTangente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacao_tangente.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditTangente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditTangente.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditTangente.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditTangente.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


class InformacaoCotangente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path("tela_informacao_cotangente.ui"), self)

        # Removendo o ponto de interrogação da janela
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # Estado do scroll
        self.rolando = True

        # Configurar o timer para rolar o texto
        self.scroll_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rolar_texto)
        self.timer.start(120)

        self.textEditCotangente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEditCotangente.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Conectar botão (já existente no .ui)
        self.btnControlarScroll.clicked.connect(self.controlar_scroll)
        self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
        add_tooltip_global(self.btnControlarScroll, "Parar o texto")

    def rolar_texto(self):
        """Rola o texto para cima lentamente, estilo créditos."""
        self.scroll_value += 1
        self.textEditCotangente.verticalScrollBar().setValue(self.scroll_value)

        # Quando chegar ao final, reinicia
        if self.scroll_value >= self.textEditCotangente.verticalScrollBar().maximum():
            self.scroll_value = 0

    def controlar_scroll(self):
        if self.rolando:
            self.timer.stop()
            self.btnControlarScroll.setIcon(qta.icon('fa5s.play'))
            add_tooltip_global(self.btnControlarScroll, "Continuar o texto")
        else:
            self.timer.start(120)
            self.btnControlarScroll.setIcon(qta.icon('fa5s.pause'))
            add_tooltip_global(self.btnControlarScroll, "Parar o texto")

        self.rolando = not self.rolando


# ---------------- JANELA ----------------
class MinhaJanela(QMainWindow):
    # ---------------- FUNÇÃO DE INICIALIZAÇÃO ----------------
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("Roob.ui"), self)

        self.setWindowTitle("Roob - Calculadora")
        self.setWindowIcon(QIcon(resource_path("roob.png")))
        self.setFixedSize(self.width(), self.height())

        # CSS interno
        self.setStyleSheet("""
            QMainWindow{
                font-family: Segoe UI;
            }
            QPushButton{
                border: none
            }
            QTableWidget#tabela{
                background-color: #a0a0a0;
                color: black;
                gridline-color: #1e293b;
                font-size: 14px;
                selection-background-color: #2563eb;
                selection-color: white;
                padding:-6px
            }
        """)

        # Ícone do botão
        self.set_icone_botao(self.btnEnviarNome, 'fa5s.paper-plane', 32)
        self.set_icone_botao(self.btnHome, 'fa5s.comment-medical', 32)
        self.set_icone_botao(self.btnUser, 'fa5s.user', 32)
        self.set_icone_botao(self.btnSingOut, 'fa5s.sign-out-alt', 18)
        self.set_icone_botao(self.btnAbout, 'fa5s.info-circle', 32)
        self.set_icone_botao(self.btnTentarNovamente, 'fa5s.sync', 18)
        self.set_icone_botao(self.btnAvancar, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnTeclado, 'fa5s.keyboard', 18)
        self.set_icone_botao(self.btnVoltarTabela, 'fa5s.arrow-left', 18)
        self.set_icone_botao(self.btnVoltarSobre, 'fa5s.arrow-left', 18)
        self.set_icone_botao(self.btnVoltarTelaOpcao, 'fa5s.arrow-left', 18)
        self.set_icone_botao(self.btnVoltarGeometria, 'fa5s.arrow-left', 18)
        self.set_icone_botao(self.btnAvancarTabela, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnAvancarSobre, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnAvancarTelaOpcao, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnAvancarGeometria, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnVoltarQuadrado, 'fa5s.arrow-left', 18)
        self.set_icone_botao(self.btnAvancarQuadrado, 'fa5s.arrow-right', 18)
        self.set_icone_botao(self.btnLimparQuadrado, 'fa5s.trash', 18)
        self.set_icone_botao(self.btnLimpaTriangulo, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarTriangulo, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarTriangulo, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnAvancarCirculo, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarCirculo, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaCirculo, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarRectangulo, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarRectangulo, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaRectangulo, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarCilindro, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarCilindro, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaCilindro, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarLosango, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarLosango, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaLosango, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarTrigonometria, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarOpTrigonometria, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnAvancarSeno, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarSeno, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaSeno, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarCosseno, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarCosseno, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaCosseno, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarTangente, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarTangente, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaTangente, "fa5s.trash", 18)
        self.set_icone_botao(self.btnAvancarCotangente, "fa5s.arrow-right", 18)
        self.set_icone_botao(self.btnVoltarCotangente, "fa5s.arrow-left", 18)
        self.set_icone_botao(self.btnLimpaCotangente, "fa5s.trash", 18)

        # ---------------- TOOLTIP ----------------
        self.add_tooltip(self.lblImagem, "Roob-Assistente de cálculo")
        self.add_tooltip(self.btnHome, "Nova seção")
        self.add_tooltip(self.btnUser, "Usuários")
        self.add_tooltip(self.btnSingOut, "Sair")
        self.add_tooltip(self.btnAbout, "Sobre Mim")
        self.add_tooltip(self.btnEnviarNome, "Enviar pra Roob")
        self.add_tooltip(self.btnAvancar, "Avançar")
        self.add_tooltip(self.btnTentarNovamente, "Enviar nome novamente")
        self.add_tooltip(self.btnTeclado, "Abrir teclado virtual")
        self.add_tooltip(self.btnVoltarTabela, "Voltar")
        self.add_tooltip(self.btnAvancarSobre, "Avançar")
        self.add_tooltip(self.btnVoltarSobre, "Voltar")
        self.add_tooltip(self.btnVoltarTelaOpcao, "Voltar")
        self.add_tooltip(self.btnVoltarGeometria, "Voltar")
        self.add_tooltip(self.btnVoltarQuadrado, "Voltar")
        self.add_tooltip(self.btnAvancarTelaOpcao, "Avançar")
        self.add_tooltip(self.btnAvancarGeometria, "Avançar")
        self.add_tooltip(self.btnAvancarQuadrado, "Avançar")
        self.add_tooltip(self.btnLimparQuadrado, "Limpar")
        self.add_tooltip(self.imagem_quadrado, "Figura Quadrado")
        self.add_tooltip(self.btnAvancarTriangulo, "Avançar")
        self.add_tooltip(self.btnVoltarTriangulo, "Voltar")
        self.add_tooltip(self.btnLimpaTriangulo, "Limpar")
        self.add_tooltip(self.imagem_triangulo, "Figura Triângulo")
        self.add_tooltip(self.btnAvancarCirculo, "Avançar")
        self.add_tooltip(self.btnVoltarCirculo, "Voltar")
        self.add_tooltip(self.btnLimpaCirculo, "Limpar")
        self.add_tooltip(self.imagem_circulo, "Figura Circunferência")
        self.add_tooltip(self.btnAvancarRectangulo, "Avançar")
        self.add_tooltip(self.btnVoltarRectangulo, "Voltar")
        self.add_tooltip(self.btnLimpaRectangulo, "Limpar")
        self.add_tooltip(self.imagem_rectangulo, "Figura Rectângulo")
        self.add_tooltip(self.btnAvancarCilindro, "Avançar")
        self.add_tooltip(self.btnVoltarCilindro, "Voltar")
        self.add_tooltip(self.btnLimpaCilindro, "Limpar")
        self.add_tooltip(self.imagem_cilindron, "Figura Cilindro")
        self.add_tooltip(self.btnAvancarLosango, "Avançar")
        self.add_tooltip(self.btnVoltarLosango, "Voltar")
        self.add_tooltip(self.btnLimpaLosango, "Limpar")
        self.add_tooltip(self.imagem_losango, "Figura Losango")
        self.add_tooltip(self.btnAvancarTrigonometria, "Avançar")
        self.add_tooltip(self.btnVoltarOpTrigonometria, "Voltar")
        self.add_tooltip(self.btnAvancarSeno, "Avançar")
        self.add_tooltip(self.btnVoltarSeno, "Voltar")
        self.add_tooltip(self.btnLimpaSeno, "Limpar")
        self.add_tooltip(self.btnAvancarCosseno, "Avançar")
        self.add_tooltip(self.btnVoltarCosseno, "Voltar")
        self.add_tooltip(self.btnLimpaCosseno, "Limpar")
        self.add_tooltip(self.btnAvancarTangente, "Avançar")
        self.add_tooltip(self.btnVoltarTangente, "Voltar")
        self.add_tooltip(self.btnLimpaTangente, "Limpar")
        self.add_tooltip(self.btnAvancarCotangente, "Avançar")
        self.add_tooltip(self.btnVoltarCotangente, "Voltar")
        self.add_tooltip(self.btnLimpaCotangente, "Limpar")

        # Tela dos Menus
        self.btnOpGeometria.clicked.connect(lambda: self.mudar_tela(self.telaOpcaoGeometria))
        self.btnOpTrigonometria.clicked.connect(lambda: self.mudar_tela(self.telaOpTrigonometria))

        # Mudar de tela
        self.btnHome.clicked.connect(lambda: self.mudar_tela(self.telaInicio))
        self.btnUser.clicked.connect(lambda: self.mudar_tela(self.telaUser))
        self.btnAbout.clicked.connect(lambda: self.mudar_tela(self.telaAbout))
        self.btnAvancar.clicked.connect(lambda: self.mudar_tela(self.telaOpcao))
        # Opção Geometria
        self.btnQuadrado.clicked.connect(lambda: self.mudar_tela(self.telaOpQuadrado))
        self.btnTriangulo.clicked.connect(lambda: self.mudar_tela(self.telaTriangulo))
        self.btnCirculo.clicked.connect(lambda: self.mudar_tela(self.telaCirculo))
        self.btnRectangulo.clicked.connect(lambda: self.mudar_tela(self.telaRectangulo))
        self.btnCilindro.clicked.connect(lambda: self.mudar_tela(self.telaCilindro))
        self.btnLosango.clicked.connect(lambda: self.mudar_tela(self.telaLosango))
        # Opção Trigonometria
        self.btnSeno.clicked.connect(lambda: self.mudar_tela(self.telaSeno))
        self.btnCosseno.clicked.connect(lambda: self.mudar_tela(self.telaCosseno))
        self.btnTangente.clicked.connect(lambda: self.mudar_tela(self.telaTangente))
        self.btnCotangente.clicked.connect(lambda: self.mudar_tela(self.telaCotangente))

        # Voltar tela
        self.btnVoltarTelaOpcao.clicked.connect(self.voltar_tela)
        self.btnVoltarTabela.clicked.connect(self.voltar_tela)
        self.btnVoltarSobre.clicked.connect(self.voltar_tela)
        # Voltar Geometria
        self.btnVoltarGeometria.clicked.connect(self.voltar_tela)
        self.btnVoltarQuadrado.clicked.connect(self.voltar_tela)
        self.btnVoltarTriangulo.clicked.connect(self.voltar_tela)
        self.btnVoltarCirculo.clicked.connect(self.voltar_tela)
        self.btnVoltarRectangulo.clicked.connect(self.voltar_tela)
        self.btnVoltarCilindro.clicked.connect(self.voltar_tela)
        self.btnVoltarLosango.clicked.connect(self.voltar_tela)
        self.btnVoltarOpTrigonometria.clicked.connect(self.voltar_tela)
        # Voltar Trigonometria
        self.btnVoltarSeno.clicked.connect(self.voltar_tela)
        self.btnVoltarCosseno.clicked.connect(self.voltar_tela)
        self.btnVoltarTangente.clicked.connect(self.voltar_tela)
        self.btnVoltarCotangente.clicked.connect(self.voltar_tela)

        # Conectar botão mudar e escrever
        self.btnAvancar.clicked.connect(self.escrever_tela_opcao)
        self.btnUser.clicked.connect(self.escrever_tela_tabela)
        self.btnOpGeometria.clicked.connect(self.escrever_tela_geometria)
        self.btnOpTrigonometria.clicked.connect(self.escrever_tela_trigonometria)

        # Conectar botões de avançar
        self.btnAvancarTelaOpcao.clicked.connect(self.avancar_tela)
        self.btnAvancarTabela.clicked.connect(self.avancar_tela)
        self.btnAvancarSobre.clicked.connect(self.avancar_tela)
        # Avançar Geometria
        self.btnAvancarGeometria.clicked.connect(self.avancar_tela)
        self.btnAvancarQuadrado.clicked.connect(self.avancar_tela)
        self.btnAvancarTriangulo.clicked.connect(self.avancar_tela)
        self.btnAvancarCirculo.clicked.connect(self.avancar_tela)
        self.btnAvancarRectangulo.clicked.connect(self.avancar_tela)
        self.btnAvancarCilindro.clicked.connect(self.avancar_tela)
        self.btnAvancarLosango.clicked.connect(self.avancar_tela)
        self.btnAvancarTrigonometria.clicked.connect(self.avancar_tela)
        # Avançar Trigonometria
        self.btnAvancarSeno.clicked.connect(self.avancar_tela)
        self.btnAvancarCosseno.clicked.connect(self.avancar_tela)
        self.btnAvancarTangente.clicked.connect(self.avancar_tela)
        self.btnAvancarCotangente.clicked.connect(self.avancar_tela)

        # Botão limpar tela
        # Geometria
        self.btnLimparQuadrado.clicked.connect(self.limpar)
        self.btnLimpaTriangulo.clicked.connect(self.limparTriangulo)
        self.btnLimpaCirculo.clicked.connect(self.limparCirculo)
        self.btnLimpaRectangulo.clicked.connect(self.limparRectangulo)
        self.btnLimpaCilindro.clicked.connect(self.limparCilindro)
        self.btnLimpaLosango.clicked.connect(self.limparLosango)
        # Trigonomeria
        self.btnLimpaSeno.clicked.connect(self.limparSeno)
        self.btnLimpaCosseno.clicked.connect(self.limparCosseno)
        self.btnLimpaTangente.clicked.connect(self.limparTangente)

        # Chamar função diretemante
        self.bem_vindo()
        self.removerbotaoEscolha()

        # Mudar Automaticament
        # Geometria
        self.txtArea.textEdited.connect(self.mudar_texto_da_figura)
        self.txtArea.textEdited.connect(self.calcula_quadadro)
        self.txtLadoA.textEdited.connect(self.mudar_texto_figura_ladoA)
        self.txtLadoB.textEdited.connect(self.mudar_texto_figura_ladoB)
        self.txtLadoC.textEdited.connect(self.mudar_texto_figura_ladoC)
        self.txtLadoA.textEdited.connect(self.calcular_triagulo)
        self.txtLadoB.textEdited.connect(self.calcular_triagulo)
        self.txtLadoC.textEdited.connect(self.calcular_triagulo)
        self.txtBase.textEdited.connect(self.calcular_trangulo_normal)
        self.txtRaio.textEdited.connect(self.mudar_texto_figura_circulo)
        self.txtRaio.textEdited.connect(self.calcular_circulo)
        self.txtAlturaRect.textEdited.connect(self.mudar_texto_figura_rectangulo_altura)
        self.txtBaseRect.textEdited.connect(self.mudar_texto_figura_rectangulo_base)
        self.txtBaseRect.textEdited.connect(self.calcular_rectangulo)
        self.txtAlturaRect.textEdited.connect(self.calcular_rectangulo)
        self.txtRaioCilindro.textEdited.connect(self.mudar_texto_figura_cilindro_raio)
        self.txtAlturaCilindro.textEdited.connect(self.mudar_texto_figura_cilindro_altura)
        self.txtAlturaCilindro.textEdited.connect(self.calcular_cilindro)
        self.txtRaioCilindro.textEdited.connect(self.calcular_cilindro)
        self.txtDiagonalMaior.textEdited.connect(self.mudar_texto_figura_losango_lblDigonalMaior)
        self.txtDiagonalMenor.textEdited.connect(self.mudar_texto_figura_losango_lblDiagonalMenor)
        self.txtLadoLosango.textEdited.connect(self.mudar_texto_figura_losango_lblLadoLosango)
        self.txtDiagonalMaior.textEdited.connect(self.calcular_area_logango)
        self.txtDiagonalMenor.textEdited.connect(self.calcular_area_logango)
        self.txtLadoLosango.textEdited.connect(self.calcular_perimetro_losango)
        # Trigonometria
        self.txtSeno.textEdited.connect(self.mudar_texto_seno)
        self.txtSeno.textEdited.connect(self.calcular_seno)
        self.txtCosseno.textEdited.connect(self.mudar_texto_cosaseno)
        self.txtCosseno.textEdited.connect(self.calcular_cosseno)
        self.txtTangente.textEdited.connect(self.mudar_texto_tangente)
        self.txtTangente.textEdited.connect(self.calcular_tangente)
        self.txtCotangente.textEdited.connect(self.mudar_texto_cotangente)
        self.txtCotangente.textEdited.connect(self.calcular_cotangente)

        # Conectar funções aos botões
        self.btnHome.clicked.connect(self.bem_vindo)
        self.btnSingOut.clicked.connect(self.fechar_app)
        self.btnEnviarNome.clicked.connect(self.responder_nome)
        self.txtNome.returnPressed.connect(self.responder_nome)
        self.btnTeclado.clicked.connect(self.abrir_teclado)
        self.btnQuestaoVersao.clicked.connect(self.escrever_tela_sobre_minhaVersao)
        self.btnQuestaoFuncao.clicked.connect(self.escrever_tela_sobre_minhaFuncionalidade)
        self.btnQuestaoFalarSobreMim.clicked.connect(self.escrever_tela_sobre_falarSobeMim)
        self.btnQuestaoQuemTeCriou.clicked.connect(self.escrever_tela_sobre_quemTeCriou)
        self.btnHome.clicked.connect(self.apagar_texto_display)

        # Telas de dialogo
        # Geometria
        self.btnInformacaoQuadrado.clicked.connect(self.tela_dialogo_quadrado)
        self.btnInformacaoTriangulo.clicked.connect(self.tela_dialogi_triangulo)
        self.btnInformacaoCirculo.clicked.connect(self.tela_dialogo_circulo)
        self.btnInformacaoRectangulo.clicked.connect(self.tela_dialogo_rectangulo)
        self.btnInformacaoCilindro.clicked.connect(self.tela_dialogo_cilindro)
        self.btnInformacaoLosango.clicked.connect(self.tela_dialogi_losango)
        # Trigonometria
        self.btnInformacaoSeno.clicked.connect(self.tela_dialogo_seno)
        self.btnInformacaoCosseno.clicked.connect(self.tela_dialogo_cosseno)
        self.btnInformacaoTangente.clicked.connect(self.tela_dialogo_tangente)
        self.btnInformacaoCotangete.clicked.connect(self.tela_dialogo_cotangente)

        self.btnTentarNovamente.clicked.connect(self.refresh)

        # Ajustar a tabela
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # imagens no label menu
        self.lblImagem.setPixmap(
            QPixmap(resource_path("roob.png")).scaled(self.lblImagem.width(), self.lblImagem.height(),
                                                      Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_quadrado.setPixmap(
            QPixmap(resource_path("imagens/Image_quadrado.png")).scaled(self.imagem_quadrado.width(),
                                                                        self.imagem_quadrado.height(),
                                                                        Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_triangulo.setPixmap(
            QPixmap(resource_path("imagens/image_triangulo.png")).scaled(self.imagem_triangulo.width(),
                                                                         self.imagem_triangulo.height(),
                                                                         Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_circulo.setPixmap(
            QPixmap(resource_path("imagens/image_circulo.png")).scaled(self.imagem_circulo.width(),
                                                                       self.imagem_circulo.height(),
                                                                       Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_rectangulo.setPixmap(
            QPixmap(resource_path("imagens/image_retactanglo.png")).scaled(self.imagem_rectangulo.width(),
                                                                           self.imagem_rectangulo.height(),
                                                                           Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_cilindron.setPixmap(
            QPixmap(resource_path("imagens/image_cilindro.png")).scaled(self.imagem_cilindron.width(),
                                                                        self.imagem_cilindron.height(),
                                                                        Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imagem_losango.setPixmap(
            QPixmap(resource_path("imagens/image_losango.png")).scaled(self.imagem_losango.width(),
                                                                       self.imagem_losango.height(),
                                                                       Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # Histório de navegação
        self.historico_telas_voltar = []
        self.historico_telas_avancar = []

        # Desabilitar botão
        # Geometria
        self.btnLimparQuadrado.setEnabled(False)
        self.btnLimpaTriangulo.setEnabled(False)
        self.btnLimpaCirculo.setEnabled(False)
        self.btnLimpaRectangulo.setEnabled(False)
        self.btnLimpaCilindro.setEnabled(False)
        self.btnLimpaLosango.setEnabled(False)
        # Trigonometria
        self.btnLimpaSeno.setEnabled(False)
        self.btnLimpaCosseno.setEnabled(False)
        self.btnLimpaTangente.setEnabled(False)

        # Mudar tela interna triangulo
        self.estado_formula = "normal"
        self.btnMudarFormula.clicked.connect(self.alterar_formula)

        self.ultimo_texto = {}

    # ---------------- FUNÇÃO DE NAVEGAÇÃO ----------------
    def mudar_tela(self, widget):
        atual = self.telas.currentWidget()
        if atual == widget:
            return

        if atual:
            self.historico_telas_voltar.append(atual)
            self.historico_telas_avancar.clear()  # Limpa histórico avançar ao navegar nova tela

        largura = self.telas.width()
        widget.move(largura, 0)
        self.telas.setCurrentWidget(widget)

        anim_in = QPropertyAnimation(widget, b"pos", widget)
        anim_in.setDuration(300)
        anim_in.setStartValue(QPoint(largura, 0))
        anim_in.setEndValue(QPoint(0, 0))

        anim_out = QPropertyAnimation(atual, b"pos", atual)
        anim_out.setDuration(300)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-largura, 0))

        anim_in.start()
        anim_out.start()
        self._anim_in = anim_in
        self._anim_out = anim_out

    def voltar_tela(self):
        if not self.historico_telas_voltar:
            return
        atual = self.telas.currentWidget()
        widget_anterior = self.historico_telas_voltar.pop()
        self.historico_telas_avancar.append(atual)
        largura = self.telas.width()

        widget_anterior.move(-largura, 0)
        self.telas.setCurrentWidget(widget_anterior)

        anim_in = QPropertyAnimation(widget_anterior, b"pos", widget_anterior)
        anim_in.setDuration(300)
        anim_in.setStartValue(QPoint(-largura, 0))
        anim_in.setEndValue(QPoint(0, 0))

        anim_out = QPropertyAnimation(atual, b"pos", atual)
        anim_out.setDuration(300)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(largura, 0))

        anim_in.start()
        anim_out.start()
        self._anim_back_in = anim_in
        self._anim_back_out = anim_out

    def avancar_tela(self):
        if not self.historico_telas_avancar:
            return
        atual = self.telas.currentWidget()
        widget_avancar = self.historico_telas_avancar.pop()
        self.historico_telas_voltar.append(atual)
        largura = self.telas.width()

        widget_avancar.move(largura, 0)
        self.telas.setCurrentWidget(widget_avancar)

        anim_in = QPropertyAnimation(widget_avancar, b"pos", widget_avancar)
        anim_in.setDuration(300)
        anim_in.setStartValue(QPoint(largura, 0))
        anim_in.setEndValue(QPoint(0, 0))

        anim_out = QPropertyAnimation(atual, b"pos", atual)
        anim_out.setDuration(300)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-largura, 0))

        anim_in.start()
        anim_out.start()
        self._anim_forward_in = anim_in
        self._anim_forward_out = anim_out

    # ---------------- FUNÇÃO DE COMPORTAMENTO DA CALCULADORA ----------------
    def apagar_texto_display(self):
        self.display.setVisible(False)

    def set_icone_botao(self, botao, nome_icone, tamanho):
        ico = qta.icon(nome_icone, color='black')
        botao.setIcon(ico)
        botao.setIconSize(QtCore.QSize(tamanho, tamanho))

    def add_tooltip(self, widget, texto):
        widget.setToolTip(texto)
        widget.setStyleSheet("""
            QToolTip{
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #555;
                padding: 6px;
                border-radius: 4px;
            }
        """)

    def nomeUsuario(self):
        return self.txtNome.text().title()

    def removerbotaoEscolha(self):
        self.botaoEscolha.setVisible(False)

    def mostrabotaoEscolha(self):
        efeito = QGraphicsOpacityEffect(self.botaoEscolha)
        self.botaoEscolha.setGraphicsEffect(efeito)

        anim = QPropertyAnimation(efeito, b"opacity", self.botaoEscolha)
        anim.setDuration(700)  # tempo em ms
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)

        self.botaoEscolha.setVisible(True)
        anim.start()

        self._anim_botaoEscolha = anim  # evita o garbage collector

    def abrir_teclado(self):
        subprocess.Popen("start osk", shell=True)

    def saudacao(self):
        data = datetime.datetime.now()
        hora = data.hour
        if hora < 12:
            return "bom dia!"
        elif hora >= 12 and hora < 18:
            return "boa tarde!"
        else:
            return "boa noite!"

    def bem_vindo(self):
        saudacao = self.saudacao()
        frases = [
            "Olá " + saudacao + " Seja bem-vindo(a)! Qual é o seu nome?",
            saudacao.capitalize() + " Vai ser um prazer ajudar você, por favor, me diga seu nome.",
            saudacao.capitalize() + " Como você se chama?"
        ]
        frases = random.choice(frases)
        self.lblMensagemInicial.setText(frases)
        efeito = QGraphicsOpacityEffect(self.lblMensagemInicial)
        self.lblMensagemInicial.setGraphicsEffect(efeito)

        anim = QPropertyAnimation(efeito, b"opacity", self.botaoEscolha)
        anim.setDuration(900)  # tempo em ms
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)

        self.removerbotaoEscolha()
        self.display.setText("")
        self.lblMensagemInicial.setVisible(True)
        anim.start()

        self._anim_botaoEscolha = anim  # evita o garbage collector

    def fechar_app(self):
        self.close()

    def escrever_texto(self, mensagem):
        try:
            self.temporizador_display.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.display.setText("")
        self.temporizador_display = QTimer(self)
        self.temporizador_display.indice = 0

        def intervalo():
            if self.temporizador_display.indice < len(texto):
                self.display.setText(self.display.toPlainText() + texto[self.temporizador_display.indice])
                self.temporizador_display.indice += 1
            else:
                self.temporizador_display.stop()

        self.temporizador_display.timeout.connect(intervalo)
        self.temporizador_display.start(velocidade)

    def escrever_texto_tabela(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.lblMensagemTabela.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0

        def intervalo():
            if self.temporizador.indice < len(texto):
                self.lblMensagemTabela.setText(self.lblMensagemTabela.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()

        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    def escrever_texto_sobre(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.display_sobre.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0

        def intervalo():
            if self.temporizador.indice < len(texto):
                self.display_sobre.setText(self.display_sobre.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()

        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    def escrever_texto_opcao(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.display_opcao.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0

        def intervalo():
            if self.temporizador.indice < len(texto):
                self.display_opcao.setText(self.display_opcao.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()

        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    def escrever_texto_geometria(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.display_geometria.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0

        def intervalo():
            if self.temporizador.indice < len(texto):
                self.display_geometria.setText(self.display_geometria.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()

        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    def escrever_texto_trigonometria(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(20, 30)

        self.display_trigonometria.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0

        def intervalo():
            if self.temporizador.indice < len(texto):
                self.display_trigonometria.setText(
                    self.display_trigonometria.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()

        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    def responder_nome(self):
        self.enviar_tabela()
        self.display.setVisible(True)
        self.lblMensagemInicial.setVisible(False)
        nome = self.nomeUsuario()
        intervalo = random.randint(1500, 2000)
        if nome == "":
            emojis = ["🤷", "️❌", "✖️,", "😐", "😑", "🤷"]
            emojis = self.escolher_texto_sem_repetir("emojis", emojis)
            mensagem = [
                f"O campo de nome não pode ficar vazio.{emojis}",
                f"Por favor, insira o seu nome.",
                f"Ops! Não consegui identificar o nome.{emojis}",
                f"Insira seu nome.",
                f"Qual seu nome?"
            ]
            mensagem = random.choice(mensagem)
            QTimer.singleShot(intervalo, lambda: self.escrever_texto(mensagem))
        else:
            emojis = ['✌️', '😀', '🙋', '️💪', '🖐️', '🤘', '🖖', '👋', '👊', '🔥', '⚡',
                      '❤', '️🧡', '💞😂', '😂', '🤣🤣', '✌️✌', '️😊😉', '🙌👍', '🙋🙋', '️🖖🖖', '💪💪🖐', '️🖐️',
                      '👋👋']
            emojis = random.choice(emojis)
            mensagem = [
                f"Olá {nome}!{emojis} Prazer em conhecê-lo(a). Sou a Roob, sua calculadora.",
                f"Olá, Muito gosto {nome}! {emojis} O meu nome é Roob, e vai ser um prazer ajuda-lo(a).",
                f"Oi {nome}!{emojis} Muito prazer, eu sou a Roob.\n\nMinha função é fazer cálculos pra si, como uma calculadora inteligente.",
                f"Oi {nome}!{emojis} Prazer! Sou a Roob, e posso ajudá-lo(a) a fazer cálculos inteligentes.",
                f"Será um prazer ajudá-lo(a), {nome}.",
                f"Oi {nome}! Estou pronta!"
            ]
            mensagem = random.choice(mensagem)
            emojis_sub = ['🏃‍', '️🏃‍️💨', '🏃💨', '🏁🏃‍️💨']
            emojis_sub = random.choice(emojis_sub)
            texto_sub = [
                f"\n\nPara continuar, clique na seta à direita."
                f"\n\nVamos começar!",
                f"\n\nVamos lá!{emojis_sub} trabalhar. Clica em avançar.",
                f"\n\nVamos lá!{emojis_sub} Clique em avançar para continuar.",
                f"\n\nEstou sempre pronta para ajudar no que for possível."
            ]
            texto_sub = random.choice(texto_sub)
            QTimer.singleShot(intervalo, lambda: self.escrever_texto(mensagem + texto_sub))

        self.display.setText("...")
        self.txtNome.clear()
        QTimer.singleShot(3000, self.mostrabotaoEscolha)

    def refresh(self):
        textos = [
            "Por favor, envie novamente o seu nome.",
            "Aguardando a inserção de um novo nome...",
            "Digite um nome válido.",
            "Digite outro nome para iniciar a sessão."
        ]

        texto = random.choice(textos)
        QTimer.singleShot(1000, lambda: self.display.setText("..."))
        pensar = random.randint(1500, 2000)
        QTimer.singleShot(pensar, lambda: self.escrever_texto(texto))

    def enviar_tabela(self):
        nome = self.nomeUsuario()
        data = datetime.datetime.now()
        formatarData = data.strftime("%H:%M - %d/%m/%Y")
        if nome == "":
            nome = "desconhecido".capitalize()
            linha = self.tabela.rowCount()
            self.tabela.insertRow(linha)
            self.tabela.setItem(linha, 0, QTableWidgetItem(nome))
            self.tabela.setItem(linha, 1, QTableWidgetItem(formatarData))
        else:
            linha = self.tabela.rowCount()
            self.tabela.insertRow(linha)
            self.tabela.setItem(linha, 0, QTableWidgetItem(nome))
            self.tabela.setItem(linha, 1, QTableWidgetItem(formatarData))

            # Função pra escrever na tela de tabela

    def escolher_texto_sem_repetir(self, chave, lista_textos):
        if chave in self.ultimo_texto and self.ultimo_texto[chave] in lista_textos:
            lista_filtrada = [t for t in lista_textos if t != self.ultimo_texto[chave]]
        else:
            lista_filtrada = lista_textos

        texto = random.choice(lista_filtrada)
        self.ultimo_texto[chave] = texto
        return texto

    def escrever_tela_tabela(self):
        textos = [
            "Nesta tabela estão todos os usuários que fizeram login hoje.",
            "Cada vez que uma sessão é iniciada, o nome e a data são registrados nesta tabela.",
            "Esta é a tabela de registros. Todas as sessões ficam registradas aqui.",
            "As suas sessões são registradas aqui."
        ]

        texto = self.escolher_texto_sem_repetir("tabela", textos)

        self.lblMensagemTabela.setText("")
        QTimer.singleShot(1200, lambda: self.lblMensagemTabela.setText("..."))

        pensar = random.randint(1500, 2000)
        QTimer.singleShot(pensar, lambda: self.escrever_texto_tabela(texto))

    def escrever_tela_sobre_minhaVersao(self):
        self.lblMensagemInicialSobre.setVisible(False)
        self.nome = self.nomeUsuario()

        textos = [
            "Nesse momento estou na versão 1.5 Ling. Python.",
            "Versão atual: 1.5, tecnoligia Python3",
            "Versão atual é 1.5 Ling. Python.",
            "1.5 Ling. Python, é a minha versão atual.",
            "A Roob está na versão 1.5 Ling. Python.",
            "Versão 1.5, linguagem Python.",
            "Versão 1.5 Ling. Python."
        ]

        texto = self.escolher_texto_sem_repetir("versao", textos)

        pensar = random.randint(1500, 2000)
        self.display_sobre.setText("...")
        QTimer.singleShot(pensar, lambda: self.escrever_texto_sobre(texto))

    def escrever_tela_sobre_minhaFuncionalidade(self):
        self.lblMensagemInicialSobre.setVisible(False)

        emojis_lista = ["✔️", "👉", "✅", "💠", "➡️", "☑️"]
        emoji = random.choice(emojis_lista)

        textos = [
            "Sou uma calculadora, minha função é fazer cálculos pra você. Pode ser sobre:\n\n" +
            f"{emoji}Aritimética\n{emoji}Trigometria\n{emoji}Álgebra\n{emoji}Geometria\n\nTambém faço alguns cálculos de:\n\n{emoji}Física\n" +
            f"{emoji}Química\n{emoji}Estatística\n\nE muito mais.",

            "Super calculadora, posso calcular diversos tipos de operações, matemáticas, de física, química e muito mais.",

            "Sobre a minha funcionalidade. Bom, eu sou uma calculadora, realizo cálculos pra você, são diversos tipos de " +
            "cálculos: álgebra, geometria, aritmética e outros."
        ]

        texto = self.escolher_texto_sem_repetir("funcionalidade", textos)

        pensar = random.randint(1500, 2000)
        self.display_sobre.setText("...")
        QTimer.singleShot(pensar, lambda: self.escrever_texto_sobre(texto))

    def escrever_tela_sobre_falarSobeMim(self):
        self.lblMensagemInicialSobre.setVisible(False)

        textos = [
            "Fui desenvolvida na SMART-CODE pelo programador Constantino Panzo Tula. Sou uma calculadora.\n" +
            "Sou capaz de realizar diversos cálculos pra si. Tenho algumas limitações quanto ao meu funcionamento, mas o objectivo do meu criador é melhorar e superar.",

            "Meu nome é Roob, sou uma calculadora avançada, posso calcular temas como álgebra, trigonometria.\n\n" +
            "Estou na versão 1.5, o meu código fonte foi criado com Python por Constantino Panzo Tula.",

            "Olá eu sou a Roob sua calculadora super, fui criada pra te ajudar em cálculos do básico ao intermediário.",

            "Sou uma calculadora criada pra te ajudar onde puder."
        ]

        texto = self.escolher_texto_sem_repetir("sobre_mim", textos)

        self.display_sobre.setText("...")
        pensar = random.randint(1500, 2000)
        QTimer.singleShot(pensar, lambda: self.escrever_texto_sobre(texto))

    def escrever_tela_sobre_quemTeCriou(self):
        self.lblMensagemInicialSobre.setVisible(False)

        textos = [
            "O meu processo de construção foi feito na SMART-CODE pelo Dev Constantino Panzo Tula.",
            "Foi a SMART-CODE que construiu o meu código-fonte.",
            "Fui criada por Constantino Panzo Tula.",
            "O meu código-fonte foi feito por Constantino Panzo Tula."
        ]

        texto = self.escolher_texto_sem_repetir("criador", textos)

        self.display_sobre.setText("...")
        pensar = random.randint(1500, 2000)
        QTimer.singleShot(pensar, lambda: self.escrever_texto_sobre(texto))

    def escrever_tela_opcao(self):
        textos = [
            "Seleciona uma opção para prosseguir.",
            "Qual assunto vamos calcular hoje?",
            "Qual será o caso a calcular?",
            "No que vamos trabalhar hoje?",
            "Clica em uma das opções a baixo.",
            "Qual a sua opção?",
            "O que desejas calcular agora?"
        ]

        texto = self.escolher_texto_sem_repetir("opcao", textos)

        QTimer.singleShot(800, lambda: self.display_opcao.setText("..."))

        pensar = random.randint(1500, 2000)
        QTimer.singleShot(pensar, lambda: self.escrever_texto_opcao(texto))

    def escrever_tela_geometria(self):
        textos = [
            "Ok, agora já podes escolher o tema que vamos trabalhar hoje.",
            "Muito bem, qual será o nosso tema de hoje?",
            "Você escolheu a opção Geometria. Agora me diz o tema que você quer calcular?",
            "Escolha um tema para calcular."
        ]

        texto = self.escolher_texto_sem_repetir("geometria", textos)

        pensar = random.randint(1500, 1600)
        QTimer.singleShot(800, lambda: self.display_geometria.setText("..."))
        QTimer.singleShot(pensar, lambda: self.escrever_texto_geometria(texto))

    def escrever_tela_trigonometria(self):
        textos = [
            "Vamos continuar. Escolha uma das opções.",
            "Qual tema você quer trabalhar hoje?",
            "Seleciona uma das opções a baixo:",
        ]

        texto = self.escolher_texto_sem_repetir("opcao", textos)

        QTimer.singleShot(800, lambda: self.display_trigonometria.setText("..."))

        pensar = random.randint(1500, 1600)
        QTimer.singleShot(pensar, lambda: self.escrever_texto_trigonometria(texto))

    # ---------------- FUNÇÃO DE COMPORTAMENTO DE CÁLCULOS ----------------

    # Função de calcula da opção Geometria
    # <<<<<<<<<Calcular Quadrado<<<<<<<<<<<<<<<
    def peger_valor_area_quadrado(self):
        return self.txtArea.text()

    def mudar_texto_da_figura(self):
        valor = self.peger_valor_area_quadrado()
        self.lblArea1.setText(valor + " cm")
        self.lblArea2.setText(valor + " cm")
        self.lblArea3.setText(valor + " cm")
        self.lblArea4.setText(valor + " cm")

    def calcula_quadadro(self):
        texto = self.peger_valor_area_quadrado().strip()

        self.btnLimparQuadrado.setEnabled(True)

        if texto == "":
            self.lblResultadoArea.setText("0")
            self.lblResultadoPerimetro.setText("0")
            self.lblArea1.setText("L")
            self.lblArea2.setText("L")
            self.lblArea3.setText("L")
            self.lblArea4.setText("L")

            self.btnLimparQuadrado.setEnabled(False)

            return

        try:
            valor = float(texto)
        except ValueError:
            return

        area = valor ** 2
        perimetro = 4 * valor

        if valor % 1 == 0:
            self.lblResultadoArea.setText(str(int(area)) + " cm²")
            self.lblResultadoPerimetro.setText(str(int(perimetro)) + " cm")
        else:
            self.lblResultadoArea.setText(str(area) + " cm²")
            self.lblResultadoPerimetro.setText(str(perimetro) + " cm")

    def limpar(self):
        self.txtArea.clear()
        self.lblResultadoArea.setText("0")
        self.lblResultadoPerimetro.setText("0")
        self.lblArea1.setText("L")
        self.lblArea2.setText("L")
        self.lblArea3.setText("L")
        self.lblArea4.setText("L")

    def tela_dialogo_quadrado(self):
        modal = InformacaoQuadrado(parent=self)
        modal.exec_()

    # <<<<<<<<<Calcular Triangulo<<<<<<<<<<<<<<<

    def pegar_texto_trianguloLadoA(self):
        return self.txtLadoA.text().strip()

    def pegar_texto_trianguloLadoB(self):
        return self.txtLadoB.text().strip()

    def pegar_texto_trianguloLadoC(self):
        return self.txtLadoC.text().strip()

    def mudar_texto_figura_ladoA(self):
        a = self.pegar_texto_trianguloLadoA()
        self.btnLimpaTriangulo.setEnabled(True)

        if a == "":
            self.lblLadoA.setText("A")
        else:
            self.lblLadoA.setText(a + " cm")

    def mudar_texto_figura_ladoB(self):
        b = self.pegar_texto_trianguloLadoB()

        if b == "":
            self.lblLadoB.setText("B")
        else:
            self.lblLadoB.setText(b + " cm")

    def mudar_texto_figura_ladoC(self):
        c = self.pegar_texto_trianguloLadoC()

        if c == "":
            self.lblLadoC.setText("C")
        else:
            self.lblLadoC.setText(c + " cm")

    def pegar_texto_base(self):
        return self.txtBase.text().strip()

    def peger_texto_altura(self):
        return self.txtAltura.text().strip()

    # 🔵 Área com base e altura
    def calcular_trangulo_normal(self):
        altura = self.peger_texto_altura()
        base = self.pegar_texto_base()

        self.btnLimpaTriangulo.setEnabled(True)

        if base == "" and altura == "":
            self.lblResultadoAreaTriagulo.setText("0")
            self.btnLimpaTriangulo.setEnabled(False)

        try:
            base = float(base)
            altura = float(altura)
        except ValueError:
            return

        area = (base * altura) / 2
        if area % 1 == 0:
            self.lblResultadoAreaTriagulo.setText("{} cm²".format(int(area)))
        else:
            self.lblResultadoAreaTriagulo.setText("{} cm²".format(area))

    # 🔵 Área (Heron) + Perímetro
    def calcular_triagulo(self):
        a = self.pegar_texto_trianguloLadoA()
        b = self.pegar_texto_trianguloLadoB()
        c = self.pegar_texto_trianguloLadoC()

        if a == "" and b == "" and c == "":
            self.lblResultadoAreaTriagulo.setText("0")
            self.lblResultadoPerimetroTriangulo.setText("0")
            self.btnLimpaTriangulo.setEnabled(False)
            return

        self.btnLimpaTriangulo.setEnabled(True)

        try:
            valorA = float(a)
            valorB = float(b)
            valorC = float(c)
        except ValueError:
            return

        # 🔴 Verificar se é um triângulo válido
        if (valorA + valorB <= valorC or
                        valorA + valorC <= valorB or
                        valorB + valorC <= valorA):
            self.lblResultadoAreaTriagulo.setText("Inválido")
            self.lblResultadoPerimetroTriangulo.setText("Inválido")
            return

        # ✅ Perímetro correto
        perimetro = valorA + valorB + valorC

        # ✅ Semi-perímetro (Heron)
        s = perimetro / 2

        # ✅ Área
        area = math.sqrt(s * (s - valorA) * (s - valorB) * (s - valorC))

        if area % 1 == 0:
            self.lblResultadoAreaTriagulo.setText("{} cm²".format(int(area)))
        else:
            self.lblResultadoAreaTriagulo.setText("{} cm²".format(area))
        if perimetro % 1 == 0:
            self.lblResultadoPerimetroTriangulo.setText("{} cm".format(int(perimetro)))
        else:
            self.lblResultadoPerimetroTriangulo.setText("{} cm".format(perimetro))

    # 🔵 Alternar fórmulas
    def alterar_formula(self):
        if self.estado_formula == "normal":
            self.formulas.setCurrentIndex(0)
            self.btnMudarFormula.setText("Mudar para fórmula base")
            self.estado_formula = "alternativa"
        else:
            self.formulas.setCurrentIndex(1)
            self.btnMudarFormula.setText("Mudar para fórmula heron")
            self.estado_formula = "normal"

        # Limpar campos
        self.txtBase.setText("")
        self.txtAltura.setText("")
        self.txtLadoA.setText("")
        self.txtLadoB.setText("")
        self.txtLadoC.setText("")

        # Reset labels
        self.lblLadoA.setText("A")
        self.lblLadoB.setText("B")
        self.lblLadoC.setText("C")

        self.lblResultadoAreaTriagulo.setText("0")
        self.lblResultadoPerimetroTriangulo.setText("0")

        self.btnLimpaTriangulo.setEnabled(False)

    def limparTriangulo(self):
        self.txtLadoA.setText("")
        self.txtLadoB.setText("")
        self.txtLadoC.setText("")

        self.txtBase.setText("")
        self.txtAltura.setText("")

        self.lblLadoA.setText("A")
        self.lblLadoB.setText("B")
        self.lblLadoC.setText("C")

        self.lblResultadoAreaTriagulo.setText("0")
        self.lblResultadoPerimetroTriangulo.setText("0")

        self.btnLimpaTriangulo.setEnabled(False)

    def tela_dialogi_triangulo(self):
        modal = InformacaoTriangulo(parent=self)
        modal.exec_()

    # <<<<<<<<<Calcular Circulo<<<<<<<<<<<<<<<
    def pegar_texto_circulo(self):
        return self.txtRaio.text().strip()

    def mudar_texto_figura_circulo(self):
        raio = self.pegar_texto_circulo()
        self.btnLimpaCirculo.setEnabled(True)

        if raio == "":
            self.lblRaio.setText("r")
        else:
            self.lblRaio.setText(raio + " cm")

    def calcular_circulo(self):
        raio = self.pegar_texto_circulo()

        if raio == "":
            self.lblAreaCirculo.setText("0")
            self.lblPerimetroCirculo.setText("0")
            self.btnLimpaCirculo.setEnabled(False)
            return

        try:
            r = float(raio)
        except ValueError:
            return

        area = 3.14 * r * r
        perimetro = 2 * 3.14 * r

        if area % 1 == 0:
            self.lblAreaCirculo.setText("{} cm²".format(int(area)))
        else:
            self.lblAreaCirculo.setText("{} cm²".format(area))
        if perimetro % 1 == 0:
            self.lblPerimetroCirculo.setText("{} cm".format(int(perimetro)))
        else:
            self.lblPerimetroCirculo.setText("{} cm".format(perimetro))

    def limparCirculo(self):
        self.txtRaio.setText("")
        self.lblRaio.setText("r")
        self.lblAreaCirculo.setText("0")
        self.lblPerimetroCirculo.setText("0")
        self.btnLimpaCirculo.setEnabled(False)

    def tela_dialogo_circulo(self):
        modal = InformacaoCirculo(parent=self)
        modal.exec_()

        # <<<<<<<<<Calcular Quadrado<<<<<<<<<<<<<<<

    def pegar_texto_txtAlturaRect(self):
        return self.txtAlturaRect.text().strip()

    def pegar_texto_txtBaseRect(self):
        return self.txtBaseRect.text().strip()

    def mudar_texto_figura_rectangulo_altura(self):
        altura = self.pegar_texto_txtAlturaRect()

        if altura == "":
            self.lblAlturaRect.setText("h")
        else:
            self.lblAlturaRect.setText(altura + " cm")

    def mudar_texto_figura_rectangulo_base(self):
        base = self.pegar_texto_txtBaseRect()

        if base == "":
            self.lblBaseRect.setText("b")
        else:
            self.lblBaseRect.setText(base + " cm")

    def calcular_rectangulo(self):
        altura = self.pegar_texto_txtAlturaRect()
        base = self.pegar_texto_txtBaseRect()
        self.btnLimpaRectangulo.setEnabled(True)

        if altura == "" and base == "":
            self.lblAreaRectangulo.setText("0")
            self.lblPerimetroRectangulo.setText("0")
            self.btnLimpaRectangulo.setEnabled(False)

        try:
            base = float(base)
            altura = float(altura)
        except ValueError:
            return
        area = base * altura
        perimetro = 2 * (base + altura)

        if area % 1 == 0:
            self.lblAreaRectangulo.setText("{} cm²".format(int(area)))
        else:
            self.lblAreaRectangulo.setText("{} cm²".format(area))

        if perimetro % 1 == 0:
            self.lblPerimetroRectangulo.setText("{} cm".format(int(perimetro)))
        else:
            self.lblPerimetroRectangulo.setText("{} cm".format(perimetro))

    def limparRectangulo(self):
        self.txtBaseRect.setText("")
        self.txtAlturaRect.setText("")
        self.lblAreaRectangulo.setText("0")
        self.lblPerimetroRectangulo.setText("0")
        self.lblAlturaRect.setText("h")
        self.lblBaseRect.setText("b")
        self.btnLimpaRectangulo.setEnabled(False)

    def tela_dialogo_rectangulo(self):
        modal = InformacaoRectangulo(parent=self)
        modal.exec_()

    # <<<<<<<<<Calcular Circulo<<<<<<<<<<<<<<<
    def pegar_texto_txtRaioCilindro(self):
        return self.txtRaioCilindro.text().strip()

    def pegar_texto_txtAlturaCilindro(self):
        return self.txtAlturaCilindro.text().strip()

    def mudar_texto_figura_cilindro_raio(self):
        raio = self.pegar_texto_txtRaioCilindro()

        if raio == "":
            self.lblRaioCilindro.setText("r")
        else:
            self.lblRaioCilindro.setText(raio + " cm")

    def mudar_texto_figura_cilindro_altura(self):
        altura = self.pegar_texto_txtAlturaCilindro()

        if altura == "":
            self.lblAlturaCilindro.setText("h")
        else:
            self.lblAlturaCilindro.setText(altura + " cm")

    def calcular_cilindro(self):
        raio = self.pegar_texto_txtRaioCilindro()
        altura = self.pegar_texto_txtAlturaCilindro()

        self.btnLimpaCilindro.setEnabled(True)

        if raio == "" and altura == "":
            self.lblResultadoVolumeCilidro.setText("0")
            self.lblResulatdoAreaCilindro.setText("0")
            self.btnLimpaCilindro.setEnabled(False)
        try:
            raio = float(raio)
            altura = float(altura)
        except ValueError:
            return

        volume = math.pi * raio ** 2 * altura
        area = 2 * math.pi * raio * (raio + altura)

        if volume % 1 == 0:
            self.lblResultadoVolumeCilidro.setText("{} cm³".format(int(volume)))
        else:
            self.lblResultadoVolumeCilidro.setText("{} cm³".format(volume))
        if area % 1 == 0:
            self.lblResulatdoAreaCilindro.setText("{} cm²".format(int(area)))
        else:
            self.lblResulatdoAreaCilindro.setText("{} cm²".format(area))

    def limparCilindro(self):
        self.lblResultadoVolumeCilidro.setText("0")
        self.lblResulatdoAreaCilindro.setText("0")

        self.lblRaioCilindro.setText("r")
        self.lblAlturaCilindro.setText("h")

        self.txtAlturaCilindro.setText("")
        self.txtRaioCilindro.setText("")

        self.btnLimpaCilindro.setEnabled(False)

    def tela_dialogo_cilindro(self):
        modal = InformacaoCilindro(parent=self)
        modal.exec_()

    # <<<<<<<<<Calcular Losango<<<<<<<<<<<<<<<
    def pegar_texto_txtDiagonalMaior(self):
        return self.txtDiagonalMaior.text().strip()

    def pegar_texto_txtDiagonalMenor(self):
        return self.txtDiagonalMenor.text().strip()

    def pegar_texto_txtLadoLosango(self):
        return self.txtLadoLosango.text().strip()

    def mudar_texto_figura_losango_lblDigonalMaior(self):
        dMaior = self.pegar_texto_txtDiagonalMaior()
        if dMaior == "":
            self.lblDigonalMaior.setText("D")
        else:
            self.lblDigonalMaior.setText(dMaior + " cm")

    def mudar_texto_figura_losango_lblDiagonalMenor(self):
        dMenor = self.pegar_texto_txtDiagonalMenor()

        if dMenor == "":
            self.lblDiagonalMenor.setText("d")
        else:
            self.lblDiagonalMenor.setText(dMenor + " cm")

    def mudar_texto_figura_losango_lblLadoLosango(self):
        ladoLosango = self.pegar_texto_txtLadoLosango()

        if ladoLosango == "":
            self.lblLadoLosango.setText("L")
        else:
            self.lblLadoLosango.setText(ladoLosango + " cm")

    def calcular_area_logango(self):
        dMaior = self.pegar_texto_txtDiagonalMaior()
        dMenor = self.pegar_texto_txtDiagonalMenor()

        self.btnLimpaLosango.setEnabled(True)

        if dMaior == "" and dMenor == "":
            self.lblResulatdoAreaLosango.setText("0")
            self.btnLimpaLosango.setEnabled(False)
        try:
            dMaior = float(dMaior)
            dMenor = float(dMenor)
        except ValueError:
            return

        area = (dMaior * dMenor) / 2

        if area % 1 == 0:
            self.lblResulatdoAreaLosango.setText("{} cm³".format(int(area)))
        else:
            self.lblResulatdoAreaLosango.setText("{} cm".format(area))

    def calcular_perimetro_losango(self):
        lado = self.pegar_texto_txtLadoLosango()
        dMaior = self.pegar_texto_txtDiagonalMaior()
        dMenor = self.pegar_texto_txtDiagonalMenor()

        self.btnLimpaLosango.setEnabled(True)

        if lado == "" and dMaior == "" and dMenor == "":
            self.btnLimpaLosango.setEnabled(False)
        if lado == "":
            self.lblResultadoPerimetroLosango.setText("0")

        try:
            lado = float(lado)
        except ValueError:
            return
        perimetro = 4 * lado

        if perimetro % 1 == 0:
            self.lblResultadoPerimetroLosango.setText("{} cm".format(int(perimetro)))
        else:
            self.lblResultadoPerimetroLosango.setText("{} cm".format(perimetro))

    def limparLosango(self):
        self.txtDiagonalMaior.setText("")
        self.txtDiagonalMenor.setText("")
        self.txtLadoLosango.setText("")

        self.lblDigonalMaior.setText("D")
        self.lblDiagonalMenor.setText("d")
        self.lblLadoLosango.setText("L")

        self.lblResulatdoAreaLosango.setText("0")
        self.lblResultadoPerimetroLosango.setText("0")

        self.btnLimpaLosango.setEnabled(False)

    def tela_dialogi_losango(self):
        modal = InformacaoLosango(parent=self)
        modal.exec_()

    # Função de calculo da opção Trigonometria
    # <<<<<<<<<Calcular Losango<<<<<<<<<<<<<<<
    def pegar_texto_seno(self):
        return self.txtSeno.text().strip()

    def mudar_texto_seno(self):
        angulo = self.pegar_texto_seno()

        if angulo == "":
            self.lblSeno.setText("0°")
        else:
            self.lblSeno.setText("{}°".format(angulo))

    # <<<<<<<<<Calcular Seno<<<<<<<<<<<<<<<
    def calcular_seno(self):
        angulo = self.pegar_texto_seno()

        self.btnLimpaSeno.setEnabled(True)

        if angulo == "":
            self.btnLimpaSeno.setEnabled(False)
            self.lblSeno.setText("0°")
            self.lblResultadoSeno.setText("Resultado")
            return

        try:
            angulo = float(angulo)
        except ValueError:
            return

        anguloRadiano = math.radians(angulo)

        resultado = math.sin(anguloRadiano)

        resultado_formatado = "{:.4f}".format(resultado)

        self.lblResultadoSeno.setText(resultado_formatado)

    def limparSeno(self):
        self.txtSeno.setText("")
        self.lblSeno.setText("0°")
        self.lblResultadoSeno.setText("Resultado")
        self.btnLimpaSeno.setEnabled(False)

    def tela_dialogo_seno(self):
        modal = InformacaoSeno(parent=self)
        modal.exec_()

    # <<<<<<<<<Calcular Cosseno<<<<<<<<<<<<<<<
    def pegar_texto_cosseno(self):
        return self.txtCosseno.text().strip()

    def mudar_texto_cosaseno(self):
        angulo = self.pegar_texto_cosseno()

        if angulo == "":
            self.lblCosseno.setText("0°")
        else:
            self.lblCosseno.setText("{}°".format(angulo))

    def calcular_cosseno(self):
        angulo = self.pegar_texto_cosseno()

        self.btnLimpaCosseno.setEnabled(True)

        if angulo == "":
            self.btnLimpaCosseno.setEnabled(False)
            self.lblResultadoCosseno.setText("Resultado")
            self.lblCosseno.setText("0°")
            return
        try:
            angulo = float(angulo)
        except ValueError:
            return
        anguloRadiano = math.radians(angulo)

        resultado = math.cos(anguloRadiano)

        resultado_formatado = "{:.4f}".format(resultado)

        self.lblResultadoCosseno.setText(resultado_formatado)

    def limparCosseno(self):
        self.btnLimpaCosseno.setEnabled(False)
        self.lblResultadoCosseno.setText("Resultado")
        self.lblCosseno.setText("0°")
        self.txtCosseno.setText("")

    def tela_dialogo_cosseno(self):
        modal = InformacaoCosseno(parent=self)
        modal.exec_()

    def pegar_texto_tangente(self):
        return self.txtTangente.text().strip()

    def mudar_texto_tangente(self):
        angulo = self.pegar_texto_tangente()

        if angulo == "":
            self.lblTangente.setText("0°")
        else:
            self.lblTangente.setText("{}°".format(angulo))

    def calcular_tangente(self):
        angulo = self.pegar_texto_tangente()

        self.btnLimpaTangente.setEnabled(True)

        if angulo == "":
            self.btnLimpaTangente.setEnabled(False)
            self.lblTangente.setText("0°")
            self.lblResultadoTangente.setText("Resultado")
            return
        try:
            angulo = float(angulo)
        except ValueError:
            return
        anguloRadiano = math.radians(angulo)

        resultado = math.tan(anguloRadiano)
        resultado_grau = math.tan(angulo)

        resultado_formatado = "{:.4f}".format(resultado)

        self.lblResultadoTangente.setText(resultado_formatado)

    def limparTangente(self):
        self.txtTangente.setText("")
        self.btnLimpaTangente.setEnabled(False)
        self.lblTangente.setText("0°")
        self.lblResultadoTangente.setText("Resultado")

    def tela_dialogo_tangente(self):
        modal = InformacaoTangente(parent=self)
        modal.exec_()

    def pegar_texto_cotangente(self):
        return self.txtCotangente.text().strip()

    def mudar_texto_cotangente(self):
        angulo = self.pegar_texto_cotangente()

        self.btnLimpaCotangente.setEnabled(True)

        if angulo == "":
            self.lblCotangente.setText("0°")
        else:
            self.lblCotangente.setText("{}°".format(angulo))

    def calcular_cotangente(self):
        angulo = self.pegar_texto_cotangente()

        self.btnLimpaCotangente.setEnabled(True)

        if angulo == "":
            self.btnLimpaCotangente.setEnabled(False)
            self.lblCotangente.setText("0°")
            self.lblCot.setText("cot(θ) =")
            self.lblResultadoCotangente.setText("Resultado")
            return

        try:
            angulo = float(angulo)
        except ValueError:
            return

        anguloRadiano = math.radians(angulo)

        sin_val = math.sin(anguloRadiano)
        cos_val = math.cos(anguloRadiano)

        if abs(sin_val) < 1e-10:
            self.lblResultadoCotangente.setText("Erro! sin(θ) = 0.")
            self.lblCot.setText("")
        else:
            resultado = cos_val / sin_val
            self.lblCot.setText("cot(θ) =")
            self.lblResultadoCotangente.setText("{:.4f}".format(resultado))

    def tela_dialogo_cotangente(self):
        modal = InformacaoCotangente(parent=self)
        modal.exec_()

# ---------------- EXECUÇÃO ----------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
