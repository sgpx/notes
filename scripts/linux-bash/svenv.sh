alias tsvenv="if [ \"\$(ls | grep venv)\" = \"\" ]; then echo creating venv; virtualenv venv --python=python3; fi; source venv/bin/activate"
