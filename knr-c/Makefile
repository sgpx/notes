all:
	gcc a.c -lm
	./a.out

gdb:
	gcc -g a.c
	gdb ./a.out

vl:
	gcc a.c
	valgrind -s --leak-check=full --track-origins=yes --show-leak-kinds=all ./a.out


clean:
	rm -v a.out
