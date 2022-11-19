#!/bin/bash
rm -rf .nojekyll
rm -rf correct_built_html_files.py
rm -rf entrypoint.sh
rm -rf generate_src_rst_files.py
rm -rf ivy_modules.txt
rm -rf make.bat
rm -rf _make_docs.sh
rm -rf Makefile
rm -rf sphinx-build.py
rm -rf build/array/array_methods
rm -rf build/container/container_methods
rm -rf ../ivy/array/array_methods.py
rm -rf ../ivy/container/container_methods.py
rm -rf ../ivy/array/experimental.py
rm -rf ../ivy/container/experimental.py
rm -rf ../ivy/functional/ivy/experimental.py
rm -rf supported_devices.py
cd partial_source || exit
rm -rf _static
cd images || exit
rm -rf ivy_libraries.png
rm -rf ivy_libraries.svg
cd ..
if [ -z "$(ls -A images)" ]; then
   rm -rf images
fi
cd logos || exit
rm -rf supported
rm -rf doc_builder_logo.png
rm -rf doc_builder_logo.svg
cd ..
if [ -z "$(ls -A logos)" ]; then
   rm -rf logos
fi
rm -rf contributing/building_the_docs.rst
rm -rf conf.py
rm -rf supported_frameworks.rst