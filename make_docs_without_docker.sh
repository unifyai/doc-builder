#!/bin/bash
# file to setup documentation building pipeline without docker
# $1 : Path to the library being documented
# --no-cleanup disable the backup/cleanup procedure
# --git-add stage changed files before generating the docs

PROGNAME=$0

usage() {
  cat << EOF >&2
Usage: $PROGNAME [--no-cleanup] [--git-add] <project path>

--no-cleanup : Disable the backup/cleanup procedure
--git-add    : Stage changed files before generating the docs
EOF
  exit 0
}

cleanup=true
gitadd=false

while [ "${1:-}" != "" ]; do
  case "$1" in
    "-h" | "--help")
      usage
      ;;
    "--no-cleanup")
      cleanup=false
      shift
      ;;
    "--git-add")
      gitadd=true
      shift
      ;;
    *)
      break
      ;;
  esac
done

if [ $# -eq 0 ]
  then
    echo "Project directory is required"
    exit 1
fi

# install libraries for the doc-builder
pip install -r ./requirements.txt || exit 1

# Run a prebuild script if exists
[ -x $1/docs/prebuild.sh ] && $1/docs/prebuild.sh

if [ -d $1/requirements ]; then
  # install libraries for ivy
  pip install -r $1/requirements/requirements.txt || exit 1
  if [[ $(arch) == 'arm64' ]]; then
    pip install -r $1/requirements/optional_m1_1.txt || exit 1
    pip install -r $1/requirements/optional_m1_2.txt || exit 1
  else
    pip install -r $1/requirements/optional.txt || exit 1
  fi
else
    pip install -r $1/requirements.txt || exit 1
    [ -r $1/optional.txt ] && (pip install -r $1/optional.txt || exit 1)
fi

# delete any previously generated pages
rm -rf $1/docs/build

function cleanup {
  if [ $cleanup = true ]; then
    echo "Cleaning up"
    # Restore the original docs
    rm -rf $1/docs/
    mv $1/docs.old/ $1/docs/
  fi
  
  # Give read and write permissions to the docs folder, as docker root take ownership of 
  # the files
  echo "Fixing permissions"
  chmod -R a+rw $1/docs
}

function error_exit {
  echo "Error in building docs"
  cleanup $1
  exit 1
}

if [ $gitadd = true ]; then
  echo "Staging changed files"
  cd $1 && git add docs
  cd -
fi

if [ $cleanup = true ]; then
  echo "Creating backup"
  
  # Backing up the docs folder
  cp -r $1/docs/ $1/docs.old/ || exit 1
fi

# syncing ivy folder with the doc-builder folder
rsync -rav docs/ $1/docs/ || error_exit $1

sphinx-build -b html $1/docs $1/docs/build || error_exit $1

if [ $cleanup = true ]; then
  # Move the build to docs.old
  mv $1/docs/build $1/docs.old/build || error_exit $1
fi

cleanup $1
