import time
from PIL import ImageGrab
import pytesseract

def capturar_texto_da_tela():
    """ Captura uma região da tela e tenta extrair texto usando OCR """
    time.sleep(3)  # Dá tempo para mudar de tela antes da captura
    x1, y1, x2, y2 = 100, 100, 600, 400  # Ajuste conforme necessário
    imagem = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    imagem.save("captura_tela.png")  # Salva a imagem para análise
    texto = pytesseract.image_to_string(imagem)
    print("Texto detectado:")
    print(texto)
    
if __name__ == "__main__":
    capturar_texto_da_tela()