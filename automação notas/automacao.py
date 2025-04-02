import pyautogui as pa
import time
import tkinter as tk
from tkinter import simpledialog

# Configuração do tempo de pausa entre os comandos
pa.PAUSE = 0.2

def obter_nome_cliente():
    """ Criar uma janela de entrada para o nome do cliente """
    root = tk.Tk()
    root.withdraw()
    nome_cliente = simpledialog.askstring("Entrada", "Digite o nome do cliente:")
    return nome_cliente

def obter_opcao():
    """ Pergunta ao usuário qual opção deseja usar para a quantidade de ESC """
    root = tk.Tk()
    root.withdraw()
    opcao = simpledialog.askinteger("Entrada", "Digite 1 (1 ESC), 2 (2 ESC), 3 (3 ESC) ou 4 (NENHUM ESC):", minvalue=1, maxvalue=4)
    return opcao

def realizar_automacao(nome_cliente, opcao):
    if nome_cliente:
        pa.click(x=648, y=745)
        
        if opcao == 1:
            pa.press('esc')
        elif opcao == 2:
            pa.press('esc')
            pa.press('esc')
        elif opcao == 3:
            pa.press('esc')
            pa.press('esc')
            pa.press('esc')
        
        pa.press('p')
        pa.write(nome_cliente)
        pa.press('enter')
        pa.press('enter')
        pa.press('x')
        pa.press('d')
        pa.press('d')
        pa.click(x=448, y=179)
        pa.click(x=494, y=247)
    else:
        print("Nome do cliente não fornecido!")

def main():
    while True:
        nome_cliente = obter_nome_cliente()
        if nome_cliente is None:
            print("Programa encerrado.")
            break
        opcao = obter_opcao()
        if opcao is None:
            print("Programa encerrado.")
            break
        realizar_automacao(nome_cliente, opcao)
        time.sleep(1)

if __name__ == "__main__":
    main()
