int main(){
	int z = 1;
	int const *y = &z;
	int const * const *x = &y;
	int const * const * xyz = x;
}
