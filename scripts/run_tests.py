import pytest
import os

# Define o diretório dos testes
test_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'tests'))

# Executa os testes
pytest.main([test_dir])
