import pyautogui as pa
import time
import tkinter as tk
from tkinter import simpledialog

# Configuração do tempo de pausa entre os comandos
pa.PAUSE = 0.2

# Função para criar a janela de entrada
def obter_nome_cliente():
    # Criar uma janela oculta
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Exibe um campo para o nome do cliente
    nome_cliente = simpledialog.askstring("Entrada", "Digite o nome do cliente:")
    
    return nome_cliente

# Função para realizar a automação com base no nome do cliente
def realizar_automacao(nome_cliente):
    if nome_cliente:
        pa.hotkey('alt', 'tab')
        pa.press('esc')
        pa.press('esc')
        pa.press('esc')
        pa.press('p')
        pa.write(nome_cliente)  # Usa o nome do cliente digitado
        pa.press('enter')
        pa.press('enter')
        pa.press('x')
        pa.press('d')
        pa.press('d')
        pa.click(x=448, y=179)
        pa.click(x=494, y=247)
    else:
        print("Nome do cliente não fornecido!")

# Criando a janela principal para o loop
def main():
    while True:
        nome_cliente = obter_nome_cliente()
        if nome_cliente is None:  # Caso o usuário feche a janela de entrada
            print("Programa encerrado.")
            break  # Encerra o loop e o programa
        realizar_automacao(nome_cliente)
        time.sleep(1)  # Aguarda um tempo antes de permitir uma nova entrada

# Executa o programa
if __name__ == "__main__":
    main()
