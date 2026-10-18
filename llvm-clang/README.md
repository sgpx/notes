# compile for target architecture

set `-triple`

`clang -target x86_64-apple-darwin-macho a.c`

`clang -target x86_64-pc-linux-gnu a.c`

https://clang.llvm.org/docs/CrossCompilation.html

# building from source (mac) (make)

```
export LD_LIBRARY_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX12.1.sdk/usr/lib/
wget https://github.com/llvm/llvm-project/archive/refs/heads/main.zip
unzip main.zip # extracts to "llvm-project-main"
cd llvm-project-main
CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++ CMAKE_ASM_COMPILER=as CMAKE_MAKE_PROGRAM=make cmake -S llvm -B build-llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_PROJECTS=clang
cd build-llvm
cmake .
make -j20
make clang
```

```
# does not work

cd ..
brew install libedit
CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++ CMAKE_ASM_COMPILER=as CMAKE_MAKE_PROGRAM=make LLVM_DIR=build-llvm/ cmake -S clang -B build-clang -DCMAKE_BUILD_TYPE=Release
```

# building from source (mac) (ninja)

```
pip3 install ninja
wget https://github.com/llvm/llvm-project/archive/refs/heads/main.zip
mkdir -p llvm-proj/
unzip main.zip -d llvm-proj/
cd llvm-proj/llvm-project-main
CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++ CMAKE_ASM_COMPILER=as CMAKE_MAKE_PROGRAM=ninja  cmake -S llvm -B build-llvm -DCMAKE_BUILD_TYPE=Release
cd build
ninja
```

