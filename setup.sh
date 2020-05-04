#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
pip install -U pip setuptools
pip install -r Requirements.txt
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter nbextension enable --py widgetsnbextension
deactivate

