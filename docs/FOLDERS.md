meu_projeto/
│
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── menu.py
│   │   ├── toolbar.py
│   │   └── icons/
│   │       ├── folder_icon.png
│   │       └── file_icon.png
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db_manager.py
│   │   └── models.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_gui.py
│   │   ├── test_db.py
│   │   └── test_main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── plugins/
│   │   ├── core/
│   │   │   └── __init__.py
│   │   └── vendors/
│   │       └── __init__.py
│
├── docs/
│   ├── README.md
│   ├── CHANGELOG.md
│   └── INSTALL.md
│
├── setup/
│   ├── __init__.py
│   ├── setup.py
│   └── requirements.txt
│
├── scripts/
│   ├── run_app.py
│   ├── run_tests.py
│   └── build_dist.py
│
├── dist/
│   └── (arquivos gerados pelo instalador)
│
└── .gitignore
