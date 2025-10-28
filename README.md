# Macro de Auto-ENTER por Imagem

Este script monitora a tela procurando pela imagem `login.png`. Ao encontrá-la, ele começa a pressionar "ENTER" repetidamente.

  * **Atalho**: Pressione `k` para ATIVAR ou DESATIVAR o script.
  * **Fail-Safe**: Mova o mouse para o canto superior esquerdo da tela para parar o script.

-----

## Aviso

  * A imagem `login.png` incluída no repositório é um **exemplo**. Você **deve substituí-la** pela sua própria imagem de login.
  * O script **requer permissão de Administrador** para funcionar, pois ele precisa ler suas teclas.

-----

## Guia de Instalação (Para um PC novo)

Siga estes 3 passos para configurar o macro pela primeira vez.

### Etapa 1: Instalar o Python 3.11

Este script não funciona com versões mais novas do Python (como 3.13+). Você deve usar a versão 3.11 ou 3.12.

1.  Acesse o site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  Baixe um instalador do **Python 3.11** (ex: 3.11.9).
3.  Execute o instalador. **IMPORTANTE:** Na primeira tela, marque a caixa **"Add python.exe to PATH"**.
4.  Conclua a instalação.

### Etapa 2: Baixar e Preparar o Macro

1.  Baixe este repositório (clique em "Code" \> "Download ZIP") e extraia-o em um local fácil (ex: `C:\Macro`).
2.  Entre na pasta.
3.  Delete o arquivo `login.png` de exemplo.
4.  Tire um print screen da imagem que você quer detectar (o botão de login, etc.).
5.  Salve esta nova imagem dentro da pasta do macro com o nome exato `login.png`.

### Etapa 3: Instalar as Bibliotecas

Este passo só precisa ser feito uma vez.

1.  No Menu Iniciar, digite `cmd` para abrir o "Prompt de Comando".
2.  Clique com o botão direito e selecione **"Executar como administrador"**.
3.  Navegue até a pasta do macro usando o comando `cd`:
    ```bash
    cd C:\Macro
    ```
4.  Crie o ambiente virtual (uma "caixa" para as bibliotecas do projeto):
    ```bash
    py -3.11 -m venv .venv
    ```
5.  Ative o ambiente:
    ```bash
    .\.venv\Scripts\activate
    ```
6.  Instale as bibliotecas necessárias (o `(.venv)` deve estar aparecendo no terminal):
    ```bash
    pip install pyautogui opencv-python keyboard
    ```
7.  Você pode fechar o terminal. A instalação está concluída.

-----

## Como Executar o Macro (Uso Diário)

Após ter feito a instalação (Etapa 1 a 3), você não precisa mais repetir aqueles passos.

Para ligar o macro:

1.  Vá até a pasta do projeto (ex: `C:\Macro`).
2.  Clique com o **botão direito** no arquivo `executar_macro.bat`.
3.  Selecione **"Executar como administrador"**.

O terminal aparecerá e o script estará rodando. Pressione `k` para ativá-lo.