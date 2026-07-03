#!/bin/bash
export HOMEBREW_NO_AUTO_UPDATE=1
# Exit immediately if any command fails
set -e

echo "=== 1. Checking Homebrew installation ==="
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Please install it first from https://brew.sh/"
    exit 1
fi

echo "=== 2. Installing Dependencies (PostgreSQL 17 & LLVM) ==="
# Install PostgreSQL 17, git, and LLVM/Clang tools
brew install postgresql@17



echo "Using compiler: $CC"
$CC --version | head -n 1

echo "=== 4. Locate PostgreSQL Configuration Utilities ==="
# Ensure the correct pg_config is targeted so the extension lands in the right directory
PG_PREFIX=$(brew --prefix postgresql@17)
export PATH="${PG_PREFIX}/bin:$PATH"
export PG_CONFIG="${PG_PREFIX}/bin/pg_config"

echo "Using pg_config at: $PG_CONFIG"

echo "=== 5. Cloning and Compiling pgvector ==="
# Clean up any old build attempts
rm -rf /tmp/pgvector

# Clone the repository
git clone --branch v0.8.3 https://github.com/pgvector/pgvector.git /tmp/pgvector
cd /tmp/pgvector

# Compile and install the extension
make clean
make -j5
make install

echo "=== 6. Cleanup ==="
rm -rf /tmp/pgvector

echo "=== 🎉 Success! pgvector has been compiled and installed! ==="
echo "To complete the setup, execute the following commands:"
echo "1. Start Postgres:  brew services start postgresql@17"
echo "2. Access DB:        psql -d postgres"
echo "3. Run SQL query:   CREATE EXTENSION vector;"

