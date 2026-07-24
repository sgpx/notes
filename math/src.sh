function nc() {
	a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	b=$((a+1))
	cp -v ex${a}*.md ex$b.md
        nano ex$b.md
}

function n() {
	a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	b=$((a+1))
	nano ex$b.md
}

function r() {
	a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	./venv/bin/python3 ex${a}.md
}

function e() {
	a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	nano ex${a}*.md
}

function l() {
	bash next.sh
}

function er() {
	nano README.md
}

function c() {
        a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	chkgpt.sh ex$a*.md
}

function nxt() {
	bash n4.sh --next
}

function chk() {
	bash n4.sh --check
}

function p() {
        a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
        ac ex$a*.md
	echo copied
}

function py() {
	./venv/bin/python3
}

function stuck() {
	a=$(ls ex*.md | sed -r "s/ex([0-9]{2,3}).*\.md/\1/" | sort -n | tail -n1)
	echo $a
	printf "i am trying to solve this problem but i am stuck, what do i do next? tell me only the next step, not the whole code\n\n" > ~/tmp.txt
        cat ex$a*.md >> ~/tmp.txt
	#converse-gpt4o.sh -f ~/tmp.txt
	#oai-gpt41-nano.sh -i ~/tmp.txt
	nvidia-nemotron-ultra.sh -i ~/tmp.txt
}

alias st=stuck

