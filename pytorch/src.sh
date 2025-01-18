function nc() {
	a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	b=$((a+1))
	cp -v ex$a.py ex$b.py
        nano ex$b.py
}

function n() {
	a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	b=$((a+1))
	nano ex$b.py
}

function r() {
	a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	./venv/bin/python3 ex${a}.py
}

function e() {
	a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	nano ex${a}.py
}
