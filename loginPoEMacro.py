import pyautogui
import time
import sys
import traceback
import random
from pyautogui import ImageNotFoundException  # Importa a exceção

# --- Configurações ---
IMAGE_TO_FIND = "login.png"
CONFIDENCE_LEVEL = 0.8  # 80% de certeza
PRESS_INTERVAL = 0.1  # Espera APÓS pressionar ENTER (100ms)
NO_IMAGE_INTERVAL = 1.0  # Espera se a imagem NÃO for encontrada (1s)
MAX_RANDOM_DELAY = 0.2  # Valor máximo de atraso aleatório (0.2s)

# --- CONFIGURAÇÃO DE OTIMIZAÇÃO ---
# !! IMPORTANTE !!
# Para otimizar, mude estes valores para criar uma pequena caixa
# exatamente onde o botão de login deve aparecer.
# Deixar (0, 0, 1920, 1080) funciona, mas NÃO otimiza.
SEARCH_LEFT = 1170
SEARCH_TOP = 640
SEARCH_WIDTH = 180
SEARCH_HEIGHT = 100
# ----------------------------------
SEARCH_REGION = (SEARCH_LEFT, SEARCH_TOP, SEARCH_WIDTH, SEARCH_HEIGHT)
# ----------------------------------

# Ativa o Fail-Safe: Mova o mouse para o canto superior esquerdo
pyautogui.FAILSAFE = True

print("Script iniciado. Procurando pela imagem...")
print(f"Região de busca definida para: {SEARCH_REGION}")
print("Mova o mouse para o canto superior esquerdo para PARAR (Fail-Safe).")
print("Pressione Ctrl+C no terminal para fechar.")

try:
    # Loop principal: Roda indefinidamente
    while True:

        # Gera um pequeno atraso aleatório a cada ciclo do loop
        random_delay = random.uniform(0, MAX_RANDOM_DELAY)

        # 1. Tenta localizar a imagem na tela
        try:
            # --- MUDANÇAS AQUI ---
            # Adicionamos 'region' e 'grayscale' para otimizar a busca
            location = pyautogui.locateOnScreen(
                IMAGE_TO_FIND,
                confidence=CONFIDENCE_LEVEL,
                region=SEARCH_REGION,  # <--- Procura SÓ nesta área
                grayscale=True,  # <--- Procura em preto e branco (mais rápido)
            )
        except ImageNotFoundException:
            location = None
        except Exception as e:
            # Captura outros erros do pyautogui (ex: falha de screenshot)
            print(f"\nErro ao tentar localizar imagem: {e}")
            location = None

        # 2. LÓGICA PRINCIPAL
        if location:
            # SE A IMAGEM ESTÁ NA TELA: Pressiona ENTER e espera 250ms + atraso
            print(f"Botão encontrado. Pressionando ENTER...", end="\r")
            pyautogui.press("enter")
            time.sleep(PRESS_INTERVAL + random_delay)
        else:
            # SE A IMAGEM NÃO ESTÁ NA TELA: Espera 1 segundo + atraso
            print(f"Botão não encontrado. Aguardando 1s...", end="\r")
            time.sleep(NO_IMAGE_INTERVAL + random_delay)

except KeyboardInterrupt:
    print("\nScript interrompido pelo usuário (Ctrl+C).")
except Exception as e:
    # --- MELHORIA NA DEPURAÇÃO DE ERROS ---
    print(f"\nOcorreu um erro inesperado e fatal: {e}")
    traceback.print_exc()  # Imprime o log de erro completo
finally:
    print("\nEncerrando o script.")
    sys.exit()
