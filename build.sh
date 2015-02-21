#!/bin/sh
DEST="dist/plugin.video.bvbtotal-0.1.0"

mkdir -p ${DEST}
cp ./addon.xml ${DEST}/addon.xml
cp ./addon.py ${DEST}/addon.py
cp ./icon.png ${DEST}/icon.png
cp ./changelog.txt ${DEST}/changelog.txt
cp ./LICENSE.txt ${DEST}/LICENSE.txt
