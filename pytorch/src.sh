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

function l() {
	bash next.sh
}

function er() {
	nano README.md
}

function c() {
        a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	chkgpt.sh ex$a.py
}

function nxt() {
	bash n4.sh --next
}

function chk() {
	bash n4.sh --check
}

function p() {
        a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
        ac ex$a.py
	echo copied
}

function py() {
	./venv/bin/python3
}

function stuck() {
	a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	printf "i am trying to solve this problem but i am stuck, what do i do next? tell me only the next step, not the whole code" > ~/tmp.txt
        cat ex$a.py >> ~/tmp.txt
	converse-gpt4o.sh -f ~/tmp.txt
	#oai-gpt41-nano.sh -i ~/tmp.txt
}

alias st=stuck

