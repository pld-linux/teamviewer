#!/bin/sh
# Launch teamviewer 6 for Linux

rootdir=$(dirname $(readlink -f "$0"))

# Set the environment up
export PATH="$rootdir/.wine/bin":$PATH
export LD_LIBRARY_PATH="$rootdir/.wine/lib"
export WINEDLLPATH="$rootdir/.wine/lib/wine"
export WINELOADER="$rootdir/.wine/bin/wine"
export WINESERVER="$rootdir/.wine/bin/wineserver"
export WINEPREFIX="$rootdir/.wine"

if [ -n "$TV_WINEPREFIX" ] ; then
     # User specified a prefix in the environment, use it
     export WINEPREFIX="$TV_WINEPREFIX"
fi

exec "$rootdir/.wine/bin/wine" "$rootdir/.wine/drive_c/Program Files/TeamViewer/Version6/TeamViewer.exe"
