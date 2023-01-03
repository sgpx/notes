# building from source (mac) (ninja)

```
pip3 install ninja
wget https://github.com/llvm/llvm-project/archive/refs/heads/main.zip
mkdir -p llvm-build/
unzip main.zip -d llvm-build/
cd llvm-build/llvm-project-main
CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++ CMAKE_ASM_COMPILER=as CMAKE_MAKE_PROGRAM=ninja  cmake -S llvm -B build -DCMAKE_BUILD_TYPE=Release
cd build
ninja
```
