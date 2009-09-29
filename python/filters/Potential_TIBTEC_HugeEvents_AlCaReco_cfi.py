import FWCore.ParameterSet.Config as cms

PotentialTIBTECHugeEvents = cms.EDFilter('EventWithHistoryEDFilter',
                               commonConfiguration = cms.untracked.PSet(
                                 historyProduct             = cms.untracked.InputTag("ConsecutiveHEs"),
                                 APVPhaseLabel              = cms.untracked.string("apvPhases"),
                                 partitionName              = cms.untracked.string("TM")
                               ),
                               filterConfigurations = cms.untracked.VPSet(
                                 cms.PSet(
                                    partitionName              = cms.untracked.string("TI"),
                                    absBXInCycleRangeLtcyAware = cms.untracked.vint32(8,11)
                                 ),
                                 cms.PSet(
                                    partitionName              = cms.untracked.string("TO"),
                                    absBXInCycleRangeLtcyAware = cms.untracked.vint32(8,11)
                                 ),
                                 cms.PSet(
                                    partitionName              = cms.untracked.string("TP"),
                                    absBXInCycleRangeLtcyAware = cms.untracked.vint32(8,11)
                                 ),
                                 cms.PSet(
                                    partitionName              = cms.untracked.string("TM"),
                                    absBXInCycleRangeLtcyAware = cms.untracked.vint32(8,11)
                                 )
                               )
                             )
