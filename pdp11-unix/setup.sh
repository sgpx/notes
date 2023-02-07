#!/bin/bash
REPO_URL="https://github.com/qrush/unix"
PROJDIR="unix"
WDIR="$PWD/$PROJDIR"
P2DIR="$WDIR/P2DIR"

function get_dist_id(){
        if test -r /etc/os-release; then
                dist_id=$(grep -E "^ID=" /etc/os-release | sed -r "s/ID=(.+)/\1/")
                echo $dist_id
        else
                echo Unknown
        fi
}

function chk_sudo(){
        if test "$(whoami)" = "root"; then
                echo $@;
                $@;
        else
                echo sudo $@;
                sudo $@;
        fi
}


function deps_prep(){
	if [ "$(get_dist_id)" = "ubuntu" ]; then
		chk_sudo apt install -y python3 python3-pip gcc g++ make build-essential wget simh
	elif [ "$(get_dist_id)" = "arch" ]; then
		chk_sudo pacman -Sy python python-pip gcc make wget simh
	else
		echo distribution not supported
		exit
	fi
}

function symlink_simh(){
	if [ "$(get_dist_id)" = "ubuntu" ]; then
		ln -s /usr/bin/pdp11 ./tools/pdp11
	elif [ "$(get_dist_id)" = "arch" ]; then
		ln -s /usr/bin/simh-pdp11 ./tools/pdp11
	else
		echo distribution not supported
		exit
	fi
}

function install_python_2_7(){
        if [ ! -d "$P2DIR" ]; then
                mkdir -p $P2DIR
		mkdir tmp
		cd tmp_python2
                wget "https://www.python.org/ftp/python/2.7/Python-2.7.tgz" -O p27.tgz
                tar xf p27.tgz
                cd Python-2.7/
                nohup ./configure --prefix=$P2DIR
                nohup make -j5
                nohup make install
		cd ..
		rm -rfv tmp_python2
        fi
}

function clone_repo(){
	git clone $REPO_URL $PROJDIR
}

function manage_python(){
	if [ -v USE_PYTHON3 ]; then
		pip3 install 2to3
		2to3 -w tools/*.py
		sed -r "s/env python/env python3/g" -i.bak tools/*.py
	else
		install_python_2_7
		export PATH="$P2DIR/bin:$PATH"
	fi
}


function enter_project_dir(){
	cd $WDIR
}

function build_project(){
	enter_project_dir
	make
}

function patch_fp(){
	cd tools/apout
	cp -v fp.c fp.c.original
	sed -i.backup -r "s/AC/AXC/g" fp.c
	cd ../..
}

function make_tools(){
	cd $WDIR/tools
	make
	cd ..
}

function run_pdp11(){
	./simh.cfg
}

function make_image_dir(){
	mkdir -p images
}

function main(){
	deps_prep
	clone_repo
	enter_project_dir
	make_image_dir
	symlink_simh
	patch_fp
	make_tools
	manage_python
	build_project
	run_pdp11
}

main
