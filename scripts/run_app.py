import os
import sys

# Adiciona o diretório principal ao sys.path para permitir importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import main

if __name__ == "__main__":
    main()

