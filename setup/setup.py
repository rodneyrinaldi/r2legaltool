 
from setuptools import setup, find_packages

setup(
    name="meu_projeto",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "pymongo",
        "sqlite3",
        "pytest",
        "pyinstaller"
    ],
    entry_points={
        'console_scripts': [
            'run_app=scripts.run_app:main',
            'run_tests=scripts.run_tests:main',
            'build_dist=scripts.build_dist:main',
        ],
    },
)
