function nc() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	b=$((a+1))
	cp -v a$a.py a$b.py
        nano a$b.py
}

function n() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	b=$((a+1))
	nano a$b.py
}

function r() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	./venv/bin/python3 a${a}.py
}

function e() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	nano a${a}.py
}

function l() {
	bash next.sh
}

function ll() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
        b=$((a+1))
        bash next.sh | sed -r "s/\*/#/g" > a$b.py
        nano a$b.py
}

function er() {
	nano README.md
}

function p() {
	./venv/bin/python3
}

function c() {
        a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
        chkgpt.sh a${a}.py
}

function lx() {
	bash lstatus.sh
}
