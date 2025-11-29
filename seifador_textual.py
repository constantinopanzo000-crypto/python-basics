# seifador_textual_filedialog.py
# Autor: Constantino Panzo Tula
# Tema: SMART-CODE Preto + Azul
import os
import shutil
from pathlib import Path
from time import sleep
from tkinter import filedialog, Tk, messagebox

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Input, Label
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
from rich.markdown import Markdown

DEFAULT_PASSWORD = "1234"
MAX_ATTEMPTS = 5

# ---------------------------- TELAS ---------------------------- #

class LoginScreen(Static):
    attempts_left = reactive(MAX_ATTEMPTS)

    def compose(self) -> ComposeResult:
        yield Static(Markdown("# Seifador SMART-CODE"))
        yield Label("Digite a senha:")
        yield Input(password=True, placeholder="Senha", id="senha_input")
        yield Static(f"Tentativas restantes: {self.attempts_left}", id="hint")
        with Horizontal():
            yield Button("Entrar", id="btn_entrar")
            yield Button("Sair", id="btn_sair")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_sair":
            self.app.exit()
        else:
            self.try_login()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.try_login()

    def try_login(self):
        senha = self.query_one("#senha_input", Input).value or ""
        if senha == DEFAULT_PASSWORD:
            self.remove()
            self.app.show_menu()
        else:
            self.attempts_left -= 1
            self.query_one("#hint", Static).update(
                f"[red]Senha incorreta[/red] — Tentativas restantes: {self.attempts_left}"
            )
            if self.attempts_left <= 0:
                self.app.exit()

class MenuScreen(Static):
    def compose(self) -> ComposeResult:
        yield Static(Markdown("# Menu Principal"))
        yield Button("1 — Apagar Ficheiro", id="op_file")
        yield Button("2 — Apagar Pasta", id="op_folder")
        yield Button("3 — Sobre o Seifador", id="op_about")
        yield Button("0 — Sair", id="op_exit")

class AboutScreen(Static):
    def compose(self) -> ComposeResult:
        md = Markdown("""
# Sobre o Seifador

**Versão:** 1.5 Python  
**Criado por:** Constantino Panzo Tula  
**Origem:** SMART-CODE Universo  

> Aplicativo para remover permanentemente ficheiros e pastas.
**Atenção:** Os dados apagados não podem ser recuperados.
""")
        yield Static(md)
        yield Button("Voltar", id="btn_back")

class MessageBar(Static):
    def show_message(self, text: str) -> None:
        self.update(text)

# ---------------------------- APP ---------------------------- #

class SeifadorApp(App):
    CSS = """
Screen {
    background: black;
    color: white;
    align: center middle;
    padding: 1 2;
}
#main {
    width: 80%;
    height: 80%;
    border: round blue;
    padding: 1;
}
"""

    BINDINGS = [("q", "quit", "Sair")]

    def __init__(self):
        super().__init__()
        self.menu_screen = MenuScreen()
        self.about_screen = AboutScreen()
        self.message_bar = MessageBar()
        # variável auxiliar do tkinter
        self.root = Tk()
        self.root.withdraw()  # esconde a janela principal do Tk

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="main"):
            yield LoginScreen()
            yield self.message_bar
        yield Footer()

    # ---------------------- MENU ---------------------- #
    def show_menu(self):
        self.mount(self.menu_screen, after=self.message_bar)
        self.menu_screen.focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "op_file":
            self.select_file()
        elif btn_id == "op_folder":
            self.select_folder()
        elif btn_id == "op_about":
            self.menu_screen.remove()
            self.mount(self.about_screen, after=self.message_bar)
        elif btn_id == "op_exit":
            self.exit()
        elif btn_id == "btn_back":
            self.about_screen.remove()
            self.show_menu()

    # ---------------------- SELEÇÃO E DELETE ---------------------- #
    def select_file(self):
        caminho = filedialog.askopenfilename(
            title="Escolhe o ficheiro para apagar",
            filetypes=[("Todos ficheiros", "*.*")]
        )
        if caminho:
            if messagebox.askokcancel("Apagar", f"Deseja realmente apagar?\n{caminho}"):
                try:
                    os.remove(caminho)
                except Exception as e:
                    self.message_bar.show_message(f"[red]Erro: {e}[/red]")
                else:
                    self.message_bar.show_message(f"[green]{caminho} apagado com sucesso![/green]")
        else:
            self.message_bar.show_message("[red]Nenhum ficheiro selecionado[/red]")

    def select_folder(self):
        caminho = filedialog.askdirectory(title="Escolhe a pasta para apagar")
        if caminho:
            if messagebox.askokcancel("Apagar", f"Deseja realmente apagar?\n{caminho}"):
                try:
                    shutil.rmtree(caminho)
                except Exception as e:
                    self.message_bar.show_message(f"[red]Erro: {e}[/red]")
                else:
                    self.message_bar.show_message(f"[green]{caminho} apagado com sucesso![/green]")
        else:
            self.message_bar.show_message("[red]Nenhuma pasta selecionada[/red]")

if __name__ == "__main__":
    SeifadorApp().run()
