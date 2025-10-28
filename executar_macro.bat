f@echo off
REM Este script deve ser executado como Administrador!

REM 1. Ativa o ambiente virtual
echo "Ativando o ambiente virtual..."
call .\.venv\Scripts\activate

REM 2. Executa o script Python
echo "Iniciando o script Python. Pressione 'k' para (des)ativar."
python loginPoEMacro.py

REM 3. Pausa no final para ver mensagens de erro
echo "Script encerrado. Pressione qualquer tecla para fechar."
pause