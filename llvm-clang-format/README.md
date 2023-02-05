# setup 

see: building llvm-clang

# example

`clang-format --style=GNU a.c`

`clang-format --style=Microsoft a.c`

`clang-format --style=LLVM --verbose -i a.c`

`clang-format --style="{BasedOnStyle: llvm, IndentWidth: 4}" -i a.c`

# in place editing

`clang-format -i a.c`
