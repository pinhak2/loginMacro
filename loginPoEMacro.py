import pyautogui
import time
import sys
import keyboard
import traceback
import random  # <--- Importa a biblioteca random

# --- Configurações ---
IMAGE_TO_FIND = 'login.png'
CONFIDENCE_LEVEL = 0.8  # 80% de certeza
PRESS_INTERVAL = 0.25   # Espera APÓS pressionar ENTER (250ms)
NO_IMAGE_INTERVAL = 1.0 # Espera se a imagem NÃO for encontrada (1s)
TOGGLE_KEY = 'k'        # Tecla para ligar/desligar
# --- Nova Configuração ---
MAX_RANDOM_DELAY = 0.2  # Valor máximo de atraso aleatório (0.2s)
# ---------------------

# --- Variáveis Globais de Controle ---
running = False
app_should_exit = False
# --------------------------------------

def handle_key_press(e):
    """
    Esta função é chamada quando a tecla 'k' é pressionada.
    - Se o script estiver parado, ele ATIVA.
    - Se o script já estiver ATIVADO, ele FINALIZA o programa.
    """
    global running, app_should_exit
    
    if e.name != TOGGLE_KEY:
        return

    if not running:
        running = True
        print(f"\n--- Script ATIVADO! --- Pressione '{TOGGLE_KEY}' novamente para FINALIZAR.")
    else:
        app_should_exit = True

# Registra a função para ser chamada quando 'k' for pressionada
keyboard.on_press(handle_key_press)

# Ativa o Fail-Safe: Mova o mouse para o canto superior esquerdo
pyautogui.FAILSAFE = True

print(f"Script iniciado. Pressione '{TOGGLE_KEY}' para ATIVAR.")
print(f"Pressione '{TOGGLE_KEY}' uma segunda vez para FINALIZAR.")
print("Mova o mouse para o canto superior esquerdo para PARAR (Fail-Safe).")
print("Pressione Ctrl+C no terminal para fechar.")

try:
    # Loop principal: Roda até 'k' ser pressionado pela segunda vez
    while not app_should_exit:
        
        # --- MUDANÇA ---
        # Gera um pequeno atraso aleatório a cada ciclo do loop
        random_delay = random.uniform(0, MAX_RANDOM_DELAY)
        
        # 1. Verifica se o script está ATIVADO
        if running:
            # 2. Tenta localizar a imagem na tela
            try:
                location = pyautogui.locateOnScreen(IMAGE_TO_FIND, confidence=CONFIDENCE_LEVEL)
            except pyautogui.ImageNotFoundException:
                location = None
            except Exception as e:
                # Captura outros erros do pyautogui (ex: falha de screenshot)
                print(f"\nErro ao tentar localizar imagem: {e}")
                location = None

            # 3. LÓGICA PRINCIPAL
            if location:
                # SE A IMAGEM ESTÁ NA TELA: Pressiona ENTER e espera 250ms + atraso
                print(f"Botão encontrado. Pressionando ENTER... (Pressione '{TOGGLE_KEY}' para finalizar)", end='\r')
                pyautogui.press('enter')
                # --- MUDANÇA ---
                time.sleep(PRESS_INTERVAL + random_delay)
            else:
                # SE A IMAGEM NÃO ESTÁ NA TELA: Espera 1 segundo + atraso
                print(f"Botão não encontrado. Aguardando 1s...   (Pressione '{TOGGLE_KEY}' para finalizar)", end='\r')
                # --- MUDANÇA ---
                time.sleep(NO_IMAGE_INTERVAL + random_delay)
        
        else:
            # 4. Script está DESATIVADO (esperando a primeira pressão de 'k')
            print(f"Script em espera. Pressione '{TOGGLE_KEY}' para iniciar...", end='\r')
            # --- MUDANÇA ---
            # Adiciona o atraso aleatório aqui também
            time.sleep(0.1 + random_delay) 

except KeyboardInterrupt:
    print("\nScript interrompido pelo usuário (Ctrl+C).")
except Exception as e:
    # --- MELHORIA NA DEPURAÇÃO DE ERROS ---
    print(f"\nOcorreu um erro inesperado e fatal: {e}")
    traceback.print_exc() # Imprime o log de erro completo
finally:
    print("\nEncerrando o script.")
    sys.exit()