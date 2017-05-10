#!/bin/bash
read -n 1 -s -p "Make sure, that you have adjusted the jobscript_draft.sh file before. Then press any key to continue"

echo "Starting submission of datasets"

while read -r line; do
  export DATASETPATH=$line
  export DATASETNAME=HLT-$(basename $line)
  printf 'Current dataset: %s, %s\n' "$DATASETPATH" "$DATASETNAME"
  sed -e "s~##DATASETPATH##~${DATASETPATH}~g" ./TP2_exercise_cfg_draft.py > ./TP2_exercise_cfg_${DATASETNAME}_draft.py
  sed -e "s~##DATASETNAME##~${DATASETNAME}~g" ./TP2_exercise_cfg_${DATASETNAME}_draft.py > ./TP2_exercise_cfg_${DATASETNAME}.py
  sed -e "s~##DATASETNAME##~${DATASETNAME}~g" ./jobscript_draft.sh > ./jobscript_${DATASETNAME}.sh
  qsub -cwd -l os=sld6 -l arch=amd64 -l h_rt=00:25:00 ./jobscript_${DATASETNAME}.sh
done < "$1"
