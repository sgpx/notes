function extall(){
	
}

mkdir cstinstall && mkdir cstinstall/bin cstinstall/lib cstinstall/lib64 cstinstall/include;
extall; # extract dependencies to folders
export myprefix="$HOME/cstinstall";
export PATH="$myprefix/bin:$PATH";
cd m4 && ./configure --prefix=$myprefix && make -j20 && make install && cd .. 
cd gmp && ./configure --prefix=$myprefix && make -j20 && make install && cd ..
cd mpfr && ./configure --prefix=$myprefix --with-gmp=$myprefix && make -j20 && make install && cd ..
cd mpc && ./configure --prefix=$myprefix --with-gmp=$myprefix --with-mpfr=$myprefix && make -j20 && make install && cd ..
cd gcc && ./configure --prefix=$myprefix --with-gmp=$myprefix --with-mpfr=$myprefix --with-mpc=$myprefix --disable-multilib && make -j20 && make install && cd ..

