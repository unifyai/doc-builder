#!/bin/bash
IFS='/' read -r -a working_directory <<< "$PWD"
user="${working_directory[2]}"
cd "/home/$user/project" || exit
pip3 install -r requirements.txt
cd "docs" || exit
rsync -rav /home/"$user"/global_docs/* .
./_make_docs.sh "$@"
./remove_files.sh
rm -rf remove_files.sh