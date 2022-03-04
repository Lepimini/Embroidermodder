#!/bin/bash

LIBEMB_VERSION=0.1
VERSION=1.90.0

function get_dependencies () {

if command -v apt-get &> /dev/null
then
sudo apt-get update
sudo apt-get install --fix-missing \
    build-essential cmake libglu1-mesa-dev freeglut3-dev mesa-common-dev \
    pandoc
else

if command -v yum &> /dev/null
then
sudo yum install gdb gcc-c++ pandoc
else

if command -v brew &> /dev/null
then
brew install pandoc
else

cat <<EOF
Could not detect apt-get, yum or homebrew, at least
one of these should be present for automated installation of
the dependencies.

Try './build.sh --build-dependencies' instead.
EOF
fi
fi
fi
}

function make_docs () {
echo "Updating libembroidery"
git submodule init
git submodule update
cd libembroidery
git pull origin main
cd ..

echo "Building webpages"
cd docs
pandoc ../libembroidery/README.md -o temp.html
cat header.html temp.html footer.html > libembroidery.html

for i in index documentation contact about downloads
do
pandoc $i.md -o temp.html
cat header.html temp.html footer.html > $i.html
done
rm temp.html

echo "Building printed version"
pandoc ../libembroidery/README.md \
    -o libembroidery_${LIBEMB_VERSION}_manual.pdf
pandoc ../README.md -o embroidermodder_${VERSION}_developer_notes.pdf
pandoc documentation.md -o embroidermodder_${VERSION}_user_manual.pdf
cd ..
}

function install_to_userspace () {
echo "Preparing userspace..."

if [ $1 != "n" ]; then
if [ ":$PATH:" != *":~/.local/bin:"* ]; then
echo "~/.local/bin is not in your PATH"
echo ""
echo "If it is not added then you can call embroidermodder with"
echo "~/.local/bin/embroidermodder instead of embroidermodder."
echo ""
read -p "Should we add ~/.local/bin to your PATH? [Y,n]" doit
case $doit in
  n|N) echo "Okay." ;;
  y|Y|*) echo "export PATH=\"~/.local/bin:$PATH\"" >> ~/.bashrc ;;
esac
. ~/.bashrc
else
echo "~/.local/bin is in PATH."
fi
fi

cd build
cmake --install .
cd ..
}

function main_build () {
echo "Get internal dependencies."
git submodule init
git submodule update

echo "Do metaprogramming tasks."
python3 convert_json_to_c.py

echo "Build"
rm -fr build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
mv libembroidery/embroider .
rm -fr CMakeFiles CMakeCache.txt cmake_install.cmake Makefile
rm -fr libembroidery embroidermodder_autogen
cd ..
}

if [ $# -eq 0 ]; then
main_build
exit
fi

while true
do
    case $1 in
    --all)
      get_dependencies
      make_docs
      main_build
      install_to_userspace n
      shift
      ;;
    --get-dependencies)
      get_dependencies
      shift
      ;;
    --docs)
      make_docs
      shift
      ;;
    --build)
      main_build
      shift
      ;;
    --install)
      install_to_userspace
      shift
      ;;
    *)
      # echo "Unrecognised option: $1"
      break
      ;;
    esac
done

