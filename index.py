from tkinter import *
from tkinter import ttk
import random

# Função para gerar senha com base nos tipos selecionados
def gerar_senha(quantidade, usar_letras, usar_numeros, usar_simbolos):
    caracteres = ""
    if usar_letras:
        caracteres += 'abcdefghijklmnopqrstufwxyzABCDEFGHIFKLMNOPQRSTUVWXYZ'
    if usar_numeros:
        caracteres += '123456789'
    if usar_simbolos:
        caracteres += '!@#$%¨&*()_+,.;:/?\|'

    if not caracteres:
        return "Selecione pelo menos um tipo de caractere."
    
    return ''.join(random.choice(caracteres) for _ in range(quantidade))

# Função para gerar e exibir as senhas
def gerar_senhas():
    try:
        numero = int(entry_numero.get())
        quantidade = int(entry_quantidade.get())
        if numero <= 0 or quantidade <= 0:
            raise ValueError("Valores devem ser maiores que zero.")

        usar_letras = var_letras.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        resultado.delete(1.0, END) # Limpa o campo de texto

        for _ in range(numero):
            senha = gerar_senha(quantidade, usar_letras, usar_numeros, usar_simbolos)
            resultado.insert(END, senha + '\n')
    except ValueError:
        resultado.delete(1.0, END)
        resultado.insert(END, "Por favor, insira números válidos para ambos os campos")

# Criar a janela principal
root = Tk()
root.title("Gerador de Senhas")
root.geometry("500x400")

# Estilo com tkk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

# Rótulo e entrada para o número de senhas
label_numero = ttk.Label(root, text="Número de senhas:")
label_numero.pack(pady=5)

entry_numero = ttk.Entry(root, width=20)
entry_numero.pack(pady=5)

entry_quantidade = ttk.Label(root, text="Quantidade de caracteres por senha:")
entry_quantidade.pack(pady=5)

entry_quantidade = ttk.Entry(root, width=20)
entry_quantidade.pack(pady=5)

#Caixa de seleção para opções de caracteres
frame_opcoes = LabelFrame(root, text="Opções de Caracteres", padx=10, pady=10, font=("Arial", 10))
frame_opcoes.pack(pady=5)

var_letras = BooleanVar(value=True)
var_numeros = BooleanVar(value=True)
var_simbolos = BooleanVar(value=True)

chk_letras = ttk.Checkbutton(frame_opcoes, text="Letras (a - z, A - Z)", variable=var_letras)
chk_letras.grid(row=0, column=0, sticky=W)

chk_numeros = ttk.Checkbutton(frame_opcoes, text="Números (0 - 9)", variable=var_numeros)
chk_numeros.grid(row=1, column=0, sticky=W)

chk_simbolos = ttk.Checkbutton(frame_opcoes, text="Símbolos (!@#$)", variable=var_simbolos)
chk_simbolos.grid(row=2, column=0, sticky=W)

# Botão para gerar as senhas
botao_gerar = ttk.Button(root, text="Gerar Senhas", command=gerar_senhas)
botao_gerar.pack(pady=10)

# Área de texto para exibir as senhas geradas
resultado = Text(root, height=10, width=50, font=("Courier", 10), wrap=WORD)
resultado.pack(pady=10)

root.mainloop()
