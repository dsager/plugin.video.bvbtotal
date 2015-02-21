#!/bin/sh
VERSION="0.1.0"
NAME="plugin.video.bvbtotal-${VERSION}"
DEST="dist/${NAME}"

mkdir -p "${DEST}"
cp ./addon.xml "${DEST}/addon.xml"
cp ./addon.py "${DEST}/addon.py"
cp ./icon.png "${DEST}/icon.png"
cp ./changelog.txt "${DEST}/changelog.txt"
cp ./LICENSE.txt "${DEST}/LICENSE.txt"
cd ./dist
zip -r "${NAME}.zip" "${NAME}"
