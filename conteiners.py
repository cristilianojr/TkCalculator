from tkinter import *

class Display(Frame):
    def __init__(self, master, **kargs):
        super(Display, self).__init__(master, kargs)

        self.display = Label(self, 
        text="0", 
        background='#262626', 
        foreground='#e6e6e6', 
        font='Arial 30',
        height='2',
        padx='10',
        anchor='e')
        self.display.pack(fill=BOTH)


class Keyboard(Frame):
    def __init__(self, master, connect, **kargs):
        super(Keyboard, self).__init__(master, kargs)
        self.fontsize = 28
        #Connector será responsável por receber um display e modificar seu Texto!
        self.connector = connect

        # Lista com todos os botões 
        self.keyboard = [
            Button(self, 
            text="C", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=10,
            command=self.cleaner_all),

            Button(self, 
            text="⌫", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=self.backspace),

            Button(self, 
            text="✚", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.sum_sub_values('+')),

            Button(self, 
            text="7", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('7')),

            Button(self, 
            text="8", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('8')),

            Button(self, 
            text="9", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('9')),

            Button(self, 
            text="━", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.sum_sub_values('-')),

            Button(self, 
            text="4", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('4')),

            Button(self, 
            text="5", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('5')),

            Button(self, 
            text="6", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('6')),

            Button(self, 
            text="✖", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=self.multply_value),

            Button(self, 
            text="1", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('1')),

            Button(self, 
            text="2", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('2')),

            Button(self, 
            text="3", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('3')),

            Button(self, 
            text="╱", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('/')),

            Button(self, 
            text="0", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=10,
            command=lambda: self.set_value('0')),

            Button(self, 
            text=",", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=self.dot_value),

            Button(self, 
            text="=", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=self.equal_to),

            Button(self, 
            text="(", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value('(')),

            Button(self, 
            text=")", 
            background='#262626', 
            foreground='#e6e6e6', 
            font=f'Arial {self.fontsize}',
            cursor='hand2',
            width=5,
            command=lambda: self.set_value(')')),
            ]
       
        # Construtor dos Botões
        self.keyboard[0].grid(row=0,column=0, columnspan=2, sticky=W+N+E+S)
        self.keyboard[1].grid(row=0,column=2, sticky=W+N+E+S)
        self.keyboard[2].grid(row=0,column=3, sticky=W+N+E+S)
        self.keyboard[3].grid(row=1,column=0, sticky=W+N+E+S)
        self.keyboard[4].grid(row=1,column=1, sticky=W+N+E+S)
        self.keyboard[5].grid(row=1,column=2, sticky=W+N+E+S)
        self.keyboard[6].grid(row=1,column=3, sticky=W+N+E+S)
        self.keyboard[7].grid(row=2,column=0, sticky=W+N+E+S)
        self.keyboard[8].grid(row=2,column=1, sticky=W+N+E+S)
        self.keyboard[9].grid(row=2,column=2, sticky=W+N+E+S)
        self.keyboard[10].grid(row=2,column=3, sticky=W+N+E+S)
        self.keyboard[11].grid(row=3,column=0, sticky=W+N+E+S)
        self.keyboard[12].grid(row=3,column=1, sticky=W+N+E+S)
        self.keyboard[13].grid(row=3,column=2, sticky=W+N+E+S)
        self.keyboard[14].grid(row=3,column=3, sticky=W+N+E+S)
        self.keyboard[15].grid(row=4,column=0, rowspan=2, columnspan=2, sticky=W+N+E+S)
        self.keyboard[16].grid(row=5,column=2, sticky=W+N+E+S)
        self.keyboard[17].grid(row=5,column=3, sticky=W+N+E+S)
        self.keyboard[18].grid(row=4,column=2, sticky=W+N+E+S, columnspan=1)
        self.keyboard[19].grid(row=4,column=3, sticky=W+N+E+S, columnspan=1)

    def set_value(self, value):
        try:
            if self.connector.display['text'] == '0':
                self.connector.display['text'] = value
            elif self.connector.display['text'] == 'Valor Inválido':
                self.connector.display['text'] = value    
            else:
                self.connector.display['text'] += value
        except Exception as error:
            print(f'{error}')

    def dot_value(self):
        if self.connector.display['text'] == '0':
                self.connector.display['text'] = '0,'
        else: 
            self.connector.display['text'] += ','

    def multply_value(self):
        value = self.connector.display['text']
        if self.connector.display['text'] == '0':
            self.connector.display['text'] = '0*'
        elif self.connector.display['text'][len(value)-1] == '*':
            self.connector.display['text'] = f'{value[:-1]}^'
        else: 
            self.connector.display['text'] += '*'

    def backspace(self):
        """
        Esta função será responsável por:
            1 - Checa se o texto do display é igual à 0, se verdadeiro, o valor não irá ser modificado.
            2 - Checa se o tamanho da str do display é igual a 1, se verdadeiro, seta o valor como 0
            3 - Apaga o ultimo caractere do display  
        """
        if self.connector.display['text'] == '0':
            pass
        elif self.connector.display['text'] == 'Valor Inválido':
            self.connector.display['text'] = '0'
        elif len(self.connector.display['text']) == 1:
            self.connector.display['text'] = '0'
        else:
            self.connector.display['text'] = self.connector.display['text'][:-1] 

    def sum_sub_values(self, value):
        string = self.connector.display['text']
        try:
            if self.connector.display['text'] == '0':
                self.connector.display['text'] = value
            elif self.connector.display['text'] == 'Valor Inválido':
                self.connector.display['text'] = value    
            elif self.connector.display['text'][len(string)-1] == value:
                self.connector.display['text'] = f'{string[:-1]}{value}'
            else:
                self.connector.display['text'] += value
        except Exception as error:
            print(f'{error}')

    def equal_to(self):
        try:
            value = eval(self.connector.display['text'].replace(',', '.').replace('^', '**'))
            self.connector.display['text'] = str(value).replace('.', ',')
        except Exception as error:
            self.connector.display['text'] = 'Valor Inválido'

    def cleaner_all(self):
        if self.connector.display['text'] == '0':
            pass
        else: 
            self.connector.display['text'] = '0'



