function nc() {
	a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
	b=$((a+1))
	b=$(printf "%02d" $b)
	cp -v a$a.cpp a$b.cpp
	nano a$b.cpp
}

function n() {
	a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
	b=$((a+1))
	b=$(printf "%02d" $b)
	nano a$b.cpp
}

function r() {
	a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
	g++ a${a}.cpp
	./a.out
}

function e() {
	a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
	nano a${a}.cpp
}

function l() {
	bash next.sh
}

function ll() {
	a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
        b=$((a+1))
        bash next.sh | sed -r "s/\*/#/g" > a$b.cpp
        nano a$b.cpp
}

function er() {
	nano README.md
}

function p() {
	g++
}

function c() {
        a=$(ls a*.cpp | sed -r "s/a([0-9]+)\.cpp/\1/" | sort -n | tail -n1)
        chkgpt.sh a${a}.cpp
}

function lx() {
	bash lstatus.sh
}
