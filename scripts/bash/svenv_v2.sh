alias svenv="if [ ! -r venv ]; then virtualenv venv --python=python3; fi; source venv/bin/activate; if [ -r requirements.txt ]; then pip3 install -r requirements.txt; fi;"
