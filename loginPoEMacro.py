import pyautogui
import time
import sys
import traceback
import random
from pyautogui import ImageNotFoundException

# ==========================================
#        SELETOR DE JOGO (GLOBAL)
# ==========================================
# Mude este valor para alternar entre os jogos: "GAME1" ou "GAME2"
SELECTED_GAME = "GAME2"

# ==========================================
#        CONFIGURAÇÕES DOS JOGOS
# ==========================================
GAMES_CONFIG = {
    "GAME1": {
        "image_file": "login.png",
        # (Left, Top, Width, Height)
        "region": (1170, 640, 180, 100),
    },
    "GAME2": {
        "image_file": "login_game2.png",  # Nome da imagem do segundo jogo
        # Coloquei a tela cheia por padrão, ajuste para otimizar
        "region": (885, 885, 1080, 940),
    },
}

# --- Configurações Gerais ---
CONFIDENCE_LEVEL = 0.8  # 80% de certeza
PRESS_INTERVAL = 0.1  # Espera APÓS pressionar ENTER
NO_IMAGE_INTERVAL = 1.0  # Espera se a imagem NÃO for encontrada
MAX_RANDOM_DELAY = 0.2  # Atraso aleatório

# --- Carregamento das Configurações do Jogo Selecionado ---
try:
    current_config = GAMES_CONFIG[SELECTED_GAME]
    IMAGE_TO_FIND = current_config["image_file"]
    SEARCH_REGION = current_config["region"]
except KeyError:
    print(f"ERRO: O jogo '{SELECTED_GAME}' não existe no dicionário GAMES_CONFIG.")
    sys.exit()

# Ativa o Fail-Safe
pyautogui.FAILSAFE = True

print(f"Script iniciado para: {SELECTED_GAME}")
print(f"Procurando imagem: {IMAGE_TO_FIND}")
print(f"Região de busca: {SEARCH_REGION}")
print("Mova o mouse para o canto superior esquerdo para PARAR (Fail-Safe).")
print("Pressione Ctrl+C no terminal para fechar.")

try:
    # Loop principal
    while True:

        random_delay = random.uniform(0, MAX_RANDOM_DELAY)

        try:
            location = pyautogui.locateOnScreen(
                IMAGE_TO_FIND,
                confidence=CONFIDENCE_LEVEL,
                region=SEARCH_REGION,
                grayscale=True,
            )
        except ImageNotFoundException:
            location = None
        except Exception as e:
            print(f"\nErro ao tentar localizar imagem: {e}")
            location = None

        if location:
            print(f"Botão encontrado. Pressionando ENTER...", end="\r")
            pyautogui.press("enter")
            time.sleep(PRESS_INTERVAL + random_delay)
        else:
            print(f"Botão não encontrado. Aguardando 1s...", end="\r")
            time.sleep(NO_IMAGE_INTERVAL + random_delay)

except KeyboardInterrupt:
    print("\nScript interrompido pelo usuário (Ctrl+C).")
except Exception as e:
    print(f"\nOcorreu um erro inesperado e fatal: {e}")
    traceback.print_exc()
finally:
    print("\nEncerrando o script.")
    sys.exit()
