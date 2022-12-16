#!/bin/bash
arch=$(uname -i)
platform=$(uname -s)

function get_development_database_port(){
	if [ -r "$(which node)" &&  -r "./config.js" ]; then
		node --eval="console.log(require('./config').testDbPort)";
	else
		echo 5002;
	fi
}

function sub_sudo(){
	echo $@;
	if [ "$(whoami)" = "root" ]; then
		$@;
	else
		sudo $@;
	fi
}

if [ "$platform" = "Linux" ]; then
    if [ "$(which wget)" = "" ]; then
	sub_sudo apt update
        sub_sudo apt install -y wget
    fi

    if [ "$(which curl)" = "" ]; then
	sub_sudo apt update
        sub_sudo apt install -y curl
    fi

    if [ ! -r mdb.tgz ]; then
        url="https://fastdl.mongodb.org/linux/mongodb-linux-$arch-ubuntu2004-6.0.3.tgz";
        wget $url --output-document="mdb.tgz";
    fi

    if [ ! -r mongodb/ ]; then
        tar xvzf mdb.tgz;
        mv -v mongodb-*/ mongodb/
    fi

    if [ ! -d dbdata/ ]; then mkdir dbdata/; fi

    if [ ! -r start-development-database.sh ]; then
        echo "#!/bin/bash" > start-development-database.sh;
        echo "echo ./mongodb/bin/mongod --dbpath dbdata/ --bind_ip 0.0.0.0 --port $(get_development_database_port)" > start-development-database.sh;
        echo "./mongodb/bin/mongod --dbpath dbdata/ --bind_ip 0.0.0.0 --port $(get_development_database_port)" >> start-development-database.sh;
        chmod +x start-development-database.sh;
    fi

    if [ ! -d libcryptofix ]; then
        url="https://raw.githubusercontent.com/sgpx/notes/master/mongodb/libcrypto.so.1.1-not-found-fix.sh";
        mkdir libcryptofix/
        cd libcryptofix/
        wget $url --output-document="fix.sh";
        sub_sudo bash fix.sh; 
    fi
fi
