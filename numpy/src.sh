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

function er() {
	nano README.md
}

function c() {
        a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	chkgpt.sh a$a.py
}

function nxt() {
	bash n4.sh --next
}

function chk() {
	bash n4.sh --check
}

function p() {
        a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
        ac a$a.py
	echo copied
}

function py() {
	./venv/bin/python3
}

function stuck() {
	a=$(ls a*.py | sed -r "s/a([0-9]+)\.py/\1/" | sort -n | tail -n1)
	printf "i am trying to solve this problem but i am stuck, what do i do next? tell me only the next step, not the whole code\n\n" > ~/tmp.txt
        cat a$a.py >> ~/tmp.txt
	converse-gpt4o.sh -f ~/tmp.txt
	#nvidia-nemotron-ultra.sh -i ~/tmp.txt
}

alias st=stuck

