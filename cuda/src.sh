function nc() {
	a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
	b=$((a+1))
	cp -v ex$a.cu ex$b.cu
        nano ex$b.cu
}

function n() {
	a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
	b=$((a+1))
	nano ex$b.cu
}

function r() {
	a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
	nvcc ex${a}.cu
	./a.out
	rm a.out
}

function e() {
	a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
	nano ex${a}.cu
}

function l() {
	bash next.sh
}

function er() {
	nano README.md
}

function c() {
        a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
	chkgpt.sh ex$a.cu
}

function nxt() {
	bash n4.sh --next
}

function chk() {
	bash n4.sh --check
}

function p() {
        a=$(ls ex*.cu | sed -r "s/ex([0-9]+)\.cu/\1/" | sort -n | tail -n1)
        ac ex$a.cu
	echo copied
}

