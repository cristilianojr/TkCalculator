"""
Programador: Cristiliano Machado
Tempo de desenvolvimento: 9 horas

"""

from tkinter import *
import sys
from conteiners import *

"""
    Classe princial da aplicação.
    Responsável por gerar a janela e os componentes.
"""
class TkCalculator(Tk):
    def __init__(self, master=None):
        super(TkCalculator, self).__init__(master)
        # Configurações gerais da aplicação!
        #   Dimensões
        self.width = 480
        self.height = 540

        #   Posições
        self.posx = 480
        self.posy = 50

        #   SetConfig 
        self.geometry(f'{self.width}x{self.height}+{self.posx}+{self.posy}')
        self.resizable(False, False) # Setar valores de tamanho da janela
        self.title('TkCalculadora') # Text da Janela
        self.iconbitmap('tkcalc_logo.ico') # Icone da janela
        self.configure(bg='#e6e6e6')

        # Declaração dos Widgets
        self.disp = Display(self)
        self.keyboard = Keyboard(self, self.disp)

        # Contrutor dos Widgets
        self.disp.pack(side=TOP, fill=X) # Display
        self.keyboard.pack(side=TOP, fill=BOTH, expand=True) # Keyboard

if __name__ == '__main__':
    sys.exit(TkCalculator().mainloop())
