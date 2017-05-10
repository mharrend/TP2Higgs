import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTSelectionAnalysis")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000000)

#process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff') 
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
print "Using global tag: %s" % process.GlobalTag.globaltag

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        "##DATASETPATH##"
    )
)

# from Alignment.CommonAlignmentProducer.hltSelectionAnalyzer_cfi import hltSelectionAnalyzer
# process.analysis = hltSelectionAnalyzer.clone()
process.analysis=cms.EDAnalyzer("HLTSelectionAnalyzer",OutTreeName = cms.string("TriggerResults"))


process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("##DATASETNAME##")
)

process.p = cms.Path(
    process.analysis
)
