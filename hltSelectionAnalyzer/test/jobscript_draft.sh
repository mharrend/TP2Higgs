#!/bin/bash
# Load CMSSW 8_0_26_patch1
. /etc/profile.d/modules.sh
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cd /nfs/dust/cms/user/mharrend/triggertutorial/CMSSW_8_0_26_patch1/src
eval `scramv1 runtime -sh`

cmsRun $PWD/TP2_exercise_cfg_##DATASETNAME##.py
