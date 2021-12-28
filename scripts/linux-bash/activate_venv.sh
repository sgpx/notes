#!/bin/bash
if [ "$SHELL" = "/bin/zsh" ]; then
	target=".zshrc";
else
	target=".bashrc";
fi

echo target is $target

echo 'alias activate_venv=" a=$(2>/dev/null ls venv); if [ \"$a\" = \"\" ]; then echo creating venv; virtualenv venv --python=python3; fi; echo activating venv...; source venv/bin/activate; "' >> ~/$target
