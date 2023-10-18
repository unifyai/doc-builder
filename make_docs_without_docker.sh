#!/bin/bash
# file to setup documentation building pipeline without docker
# $1 : Path to the library being documented
# --no-cleanup disable the backup/cleanup procedure
# --git-add stage changed files before generating the docs

PROGNAME=$0

usage() {
  cat << EOF >&2
Usage: $PROGNAME [options] <project path>

-h, --help                      : Show this help
-C, --no-cleanup                : Disable the backup/cleanup procedure
-g, --git-add                   : Stage changed files before generating the docs
-s, --skip-dependencies-install : Skip installing dependencies using pip
-j, --jobs N                    : Build in parallel with N processes where possible (special value "auto" will set N to cpu-count)
-D setting=value                : Override a setting in conf.py
EOF
  exit 0
}

cleanup=true
gitadd=false
installdependencies=true
build_args=""
doc_builder_dir=$(dirname $0)
dependency_installer="scripts/shell/install_dependencies.sh"

cd $doc_builder_dir

while [ "${1:-}" != "" ]; do
  case "$1" in
    "-h" | "--help")
      usage
      ;;
    "-C" | "--no-cleanup")
      cleanup=false
      shift
      ;;
    "-g" | "--git-add")
      gitadd=true
      shift
      ;;
    "-s" | "--skip-dependencies-install")
      installdependencies=false
      shift
      ;;
    "-j" | "--jobs")
      build_args="$build_args $1 $2"
      shift 2
      ;;
    "-D")
      build_args="$build_args $1 $2"
      shift 2
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

if [[ $1 == -* ]]; then
  echo "Unknown option $1"
  exit 1
fi

if [ $# -gt 1 ]
  then
    echo "Too many arguments, only one project directory is required"
    exit 1
fi

# If -j is not specified, use all available cores
if [[ $build_args != *"-j"* ]]; then
  build_args="$build_args -j auto"
fi

if [ $installdependencies = true ]; then
  # install libraries for the doc-builder
  pip install -r ./requirements.txt || exit 1

  # Run a prebuild script if exists
  [ -x $1/docs/prebuild.sh ] && $1/docs/prebuild.sh

  # run the dependency installer script
  (cd $1 && [ -x ./$dependency_installer ] && ./$dependency_installer)
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

sphinx-build -b html $build_args $1/docs $1/docs/build || error_exit $1

if [ $cleanup = true ]; then
  # Move the build to docs.old
  mv $1/docs/build $1/docs.old/build || error_exit $1
fi

cleanup $1
