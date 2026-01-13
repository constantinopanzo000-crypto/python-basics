"""
Roob IA: Minha primeira assistente em Python
Criada por: Constantino Panzo Tula
Origem: SMART-CODE Universo
Data do início: 13/01/2026
Obrigrado pela contribuição
"""

#Importação do código funcional
import sys
import os
import datetime
import random
import subprocess
#Importação da GUI
import qtawesome as qta
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation

# ---------------- RESOURCE PATH ----------------
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ---------------- JANELA ----------------
class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("Roob.ui"), self)

        #Tornar fixaa a janela
        self.setFixedSize(self.width(), self.height())

        #CSS interno
        self.setStyleSheet("""
            QMainWindow{
                font-family: segoe UI;
            }
            QPushButton#btnEnviarNome{
                border: none
            }
            QPushButton#btnTentarNovamente{
                border: none
            }
            QPushButton#btnAvancar{
                border: none
            }
        """)

        #Ícone do botão
        icoEnviar = qta.icon('fa5s.paper-plane', color='black')
        self.btnEnviarNome.setIcon(icoEnviar)
        self.btnEnviarNome.setIconSize(QtCore.QSize(32, 32))
        icoHome = qta.icon('fa5s.home', color='black')
        self.btnHome.setIcon(icoHome)
        self.btnHome.setIconSize(QtCore.QSize(32, 32))
        icoUser = qta.icon('fa5s.user', color='black')
        self.btnUser.setIcon(icoUser)
        self.btnUser.setIconSize(QtCore.QSize(32, 32))
        icoSingOut= qta.icon('fa5s.sign-out-alt', color='black')
        self.btnSingOut.setIcon(icoSingOut)
        self.btnSingOut.setIconSize(QtCore.QSize(18, 18))
        icoAbout = qta.icon('fa5s.info-circle', color='black')
        self.btnAbout.setIcon(icoAbout)
        self.btnAbout.setIconSize(QtCore.QSize(32, 32))
        icoRefresh = qta.icon('fa5s.sync', color='black')
        self.btnTentarNovamente.setIcon(icoRefresh)
        self.btnTentarNovamente.setIconSize(QtCore.QSize(32, 32))
        icoNext = qta.icon('fa5s.arrow-right', color='black')
        self.btnAvancar.setIcon(icoNext)
        self.btnAvancar.setIconSize(QtCore.QSize(32, 32))
        icoKeyboard = qta.icon('fa5s.keyboard', color='black')
        self.btnTeclado.setIcon(icoKeyboard)
        self.btnTeclado.setIconSize(QtCore.QSize(18, 18))

        #Colocar Tooltip nos bobões e label
        self.lblImagem.setToolTip("Roob-Assistente de cálculo")
        self.lblImagem.setStyleSheet("""
                    QToolTip{
                        background-color: #1e1e1e;
                        color: white;
                        border: 1px solid #555;
                        padding: 6px;
                        border-radius: 4px
                    }
                """)
        self.btnHome.setToolTip("Início")
        self.btnHome.setStyleSheet("""
                            QToolTip{
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid #555;
                                padding: 6px;
                                border-radius: 4px
                            }
                        """)
        self.btnUser.setToolTip("Usuários")
        self.btnUser.setStyleSheet("""
                            QToolTip{
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid #555;
                                padding: 6px;
                                border-radius: 4px
                            }
                        """)
        self.btnSingOut.setToolTip("Sair")
        self.btnSingOut.setStyleSheet("""
                            QToolTip{
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid #555;
                                padding: 6px;
                                border-radius: 4px
                            }
                        """)
        self.btnAbout.setToolTip("Sobre Mim")
        self.btnAbout.setStyleSheet("""
                            QToolTip{
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid #555;
                                padding: 6px;
                                border-radius: 4px
                            }
                        """)
        self.btnEnviarNome.setToolTip("Enviar pra Roob")
        self.btnEnviarNome.setStyleSheet("""
                            QToolTip{
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid #555;
                                padding: 6px;
                                border-radius: 4px
                            }
                        """)
        self.btnAvancar.setToolTip("Avançar")
        self.btnAvancar.setStyleSheet("""
                                    QToolTip{
                                        background-color: #1e1e1e;
                                        color: white;
                                        border: 1px solid #555;
                                        padding: 6px;
                                        border-radius: 4px
                                    }
                                """)
        self.btnTentarNovamente.setToolTip("Enviar nome novamente")
        self.btnTentarNovamente.setStyleSheet("""
                                    QToolTip{
                                        background-color: #1e1e1e;
                                        color: white;
                                        border: 1px solid #555;
                                        padding: 6px;
                                        border-radius: 4px
                                    }
                                """)
        self.btnTeclado.setToolTip("Abrir teclado virtual")
        self.btnTeclado.setStyleSheet("""
                                            QToolTip{
                                                background-color: #1e1e1e;
                                                color: white;
                                                border: 1px solid #555;
                                                padding: 6px;
                                                border-radius: 4px
                                            }
                                        """)

        #Chamar função diretemante
        self.bem_vindo()
        self.removerbotaoEscolha()
        #self.lblMensagemInicial.setVisible(False)

        #Conectar funções aos botões
        self.btnHome.clicked.connect(self.bem_vindo)
        self.btnSingOut.clicked.connect(self.fechar_app)
        self.btnEnviarNome.clicked.connect(self.responder_nome)
        self.txtNome.returnPressed.connect(self.responder_nome)
        self.btnTeclado.clicked.connect(self.abrir_teclado)

        #imagens no label menu
        self.lblImagem.setPixmap(QPixmap(resource_path("imagem.png")).scaled(self.lblImagem.width(), self.lblImagem.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    #Remover visibilidade
    def removerbotaoEscolha(self):
        self.botaoEscolha.setVisible(False)
    #Mostrar visibilidade

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

    #Função abrir teclado
    def abrir_teclado(self):
        subprocess.Popen("osk", shell=True)

    #Função saudar pro periodo
    def saudacao(self):
        data = datetime.datetime.now()
        hora = data.hour
        if hora < 12:
            return "bom dia!"
        elif hora > 12 and hora < 18:
            return "boa tarde!"
        else:
            return "boa noite!"

    #Função da mensagem de boas-vindas
    def bem_vindo(self):
        saudacao = self.saudacao()
        frases = [
            "Olá " + saudacao + " Seja bem-vindo(a)! Qual seu nome?",
            saudacao + " Vai ser um prazer ajudar você, Me diz seu nome?",
            saudacao + " Como te chamas?"
        ]
        frases = random.choice(frases).capitalize()
        self.lblMensagemInicial.setText(frases)
        efeito = QGraphicsOpacityEffect(self.lblMensagemInicial)
        self.lblMensagemInicial.setGraphicsEffect(efeito)

        anim = QPropertyAnimation(efeito, b"opacity", self.botaoEscolha)
        anim.setDuration(900)  # tempo em ms
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)

        self.lblMensagemInicial.setVisible(True)
        anim.start()

        self._anim_botaoEscolha = anim  # evita o garbage collector

    #Função pra fechar o programa
    def fechar_app(self):
        self.close()

    #Função pegar nome usuário
    def nomeUsuario(self):
        return self.txtNome.text().title()

    #Função pra escrever
    def escrever_texto(self, mensagem):
        try:
            self.temporizador.stop()
        except AttributeError:
            pass

        texto = mensagem
        velocidade = random.randint(50, 60)

        self.display.setText("")
        self.temporizador = QTimer(self)
        self.temporizador.indice = 0
        def intervalo():
            if self.temporizador.indice < len(texto):
                self.display.setText(self.display.toPlainText() + texto[self.temporizador.indice])
                self.temporizador.indice += 1
            else:
                self.temporizador.stop()
        self.temporizador.timeout.connect(intervalo)
        self.temporizador.start(velocidade)

    #Função responder
    def responder_nome(self):
        self.lblMensagemInicial.setVisible(False)
        nome = self.nomeUsuario()
        if nome == "":
            mensagem = [
                "Não podes enviar compo vazio como nome.",
                "Por favor envia seu nome usuário.",
                "Opha! Não consegui detectar seu nome."
            ]
            nome = "Desconhecido"
            mensagem = random.choice(mensagem)
        else:
            saudar = self.saudacao()
            mensagem = [
                "Olá " + nome + ", " + saudar + " Sou a Roob e estou aqui pra ajudar você.",
                "Oi " + nome + "! Muito prazer, eu sou a Roob.\nUma calculadora inteligente pronta a te ajudar.",
                nome + " Vai ser um prazer ajudar-te."
            ]
            mensagem = random.choice(mensagem)

        self.display.setText("...")
        self.txtNome.clear()
        intervalo = random.randint(1500, 2000)
        QTimer.singleShot(intervalo, lambda: self.escrever_texto(mensagem))
        QTimer.singleShot(5000, self.mostrabotaoEscolha)



# ---------------- EXECUÇÃO ----------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
