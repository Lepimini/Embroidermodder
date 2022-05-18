#!/bin/bash

case "$1" in
    "dev_install")
        python3 -m build
        python3 -m pip install -U dist/*.whl --force-reinstall
        ;;

    "test")
        cd src
        python3 tests.py
        emb_dev_install
        # We don't know if the user has added the command to their
        # PATH variable, so give the address from HOME.
        timeout 10 ~/.local/bin/embroidermodder
        ;;

    "lint")
        python3 -m pip install pylint
        pylint src/ > rating.txt
        pylint src/ -f json > triage.json
        python3 src/triage.py
        python3 src/make_button.py
        ;;

    "qa")
        python3 -m pip install pylint
        pylint src/ > rating.txt
        pylint src/ -f json > triage.json
        python3 src/triage.py
        python3 src/make_button.py
        cd src
        python3 tests.py
        emb_dev_install
        # We don't know if the user has added the command to their
        # PATH variable, so give the address from HOME.
        timeout 10 ~/.local/bin/embroidermodder
        ;;

    "install")
        python3 -m pip install embroidermodder
        ;;

    "dev_run")
        git submodule init
        git submodule update
        mkdir build
        cd build
        cmake ../src/libembroidery
        cmake --build .
        cd ..

        cd src/libembroidery
        python3 -m build
        python3 -m pip install -U dist/*.whl --force-reinstall
        cd ../..
        python3 -m build
        python3 -m pip install -U dist/*.whl --force-reinstall

        alias embroider="../build/embroider"
        cd src
        python3 -m embroidermodder
        ;;

    "run")
        python3 -m pip install libembroidery embroidermodder
        python3 -m embroidermodder
        ;;

    "clean")
        rm -fr dist src/embroidermodder.egg-info rating.txt triage.json
        ;;

    *)
        cat <<EOF
Please enter a command for EM2 from this list:
    install
    qa
    lint
    test
    dev_install
    run
    dev_run
    clean
EOF
        ;;
esac