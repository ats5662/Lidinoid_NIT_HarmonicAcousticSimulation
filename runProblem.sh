#!/bin/sh
7z x LidinoidLinerMeshMeterTet4.7z
cfs -t8 -d Lidinoid_NIT_HarmonicAcousticSim_InputDeck
rm *.cdb
cp history/* .
rm -rf history
python postProcessResults.py
