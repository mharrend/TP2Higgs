import FWCore.ParameterSet.Config as cms

hltSelectionAnalyzer = cms.EDAnalyzer(
    "HLTSelectionAnalyzer",
    OutTreeName = cms.string("TriggerResults")
)

