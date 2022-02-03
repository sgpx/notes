alias ave=" a=$(2>/dev/null ls venv); if [ \"$a\" = \"\" ]; then echo creating venv; virtualenv venv --python=python3; fi; echo activating venv...; source venv/bin/activate; "
