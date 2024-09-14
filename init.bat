@echo off
REM Criar pastas principais
mkdir meu_projeto
cd meu_projeto
mkdir app
mkdir app\gui
mkdir app\database
mkdir app\tests
mkdir app\utils
mkdir docs
mkdir setup
mkdir dist
mkdir scripts
mkdir plugins
mkdir plugins\core
mkdir plugins\vendors
mkdir .vscode

REM Criar arquivos vazios
cd app
echo. > __init__.py
echo. > main.py
cd gui
echo. > __init__.py
echo. > main_window.py
echo. > widgets.py
cd ..\database
echo. > __init__.py
echo. > db_manager.py
echo. > models.py
cd ..\tests
echo. > __init__.py
echo. > test_gui.py
echo. > test_db.py
echo. > test_main.py
cd ..\utils
echo. > __init__.py
echo. > helpers.py
cd ..\..

cd docs
echo. > README.md
echo. > CHANGELOG.md
echo. > INSTALL.md
cd ..

cd setup
echo. > __init__.py
echo. > setup.py
echo. > requirements.txt
cd ..

cd scripts
echo. > run_app.py
echo. > run_tests.py
echo. > build_dist.py
cd ..

cd plugins\core
echo. > __init__.py
cd ..\..

cd plugins\vendors
echo. > __init__.py
cd ..\..

cd .vscode
echo {^
    "python.pythonPath": "path/to/your/python",^
    "editor.formatOnSave": true,^
    "editor.tabSize": 4,^
    "files.exclude": {^
        "**/__pycache__": true,^
        "**/*.pyc": true^
    }^
} > settings.json

echo {^
    "version": "0.2.0",^
    "configurations": [^
        {^
            "name": "Python: App",^
            "type": "python",^
            "request": "launch",^
            "program": "${workspaceFolder}/app/main.py",^
            "console": "integratedTerminal"^
        },^
        {^
            "name": "Python: Tests",^
            "type": "python",^
            "request": "launch",^
            "program": "${workspaceFolder}/scripts/run_tests.py",^
            "console": "integratedTerminal"^
        }^
    ]^
} > launch.json

echo {^
    "recommendations": [^
        "ms-python.python",^
        "ms-python.vscode-pylance",^
        "ms-toolsai.jupyter",^
        "esbenp.prettier-vscode"^
    ]^
} > extensions.json

cd ..

REM Criar arquivo .gitignore
echo. > .gitignore

REM Criar arquivo requirements.txt na raiz do projeto
echo. > requirements.txt

echo Estrutura de pastas e arquivos criada com sucesso!
pause
