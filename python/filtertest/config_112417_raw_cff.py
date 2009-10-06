import FWCore.ParameterSet.Config as cms

from DPGAnalysis.SiStripTools.filtertest.MessageLogger_cff import *

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(),
                            skipBadFiles = cms.untracked.bool(True)
                            )
from DPGAnalysis.SiStripTools.filtertest.raw_112417_debug_cff import fileNames
source.fileNames = fileNames

#---------------------------------------------------------------------
# Raw to Digi: TO BE TESTED !!
#---------------------------------------------------------------------

from DPGAnalysis.SiStripTools.filtertest.rawtodigi_cff import *

#-------------------------------------------------
# Global Tag
#-------------------------------------------------
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
GlobalTag.globaltag = "GR09_31X_V5P::All"

#-------------------------------------------------------------------------
from DPGAnalysis.SiStripTools.apvlatency.fakeapvlatencyessource_cff import *
fakeapvlatency.APVLatency = cms.untracked.int32(144)
#-------------------------------------------------------------------------

consecutiveHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                                l1ABCCollection=cms.InputTag("scalersRawToDigi")
                                )


#------------------------------------------------------------------------
# APV Cycle Phase Producer and monitor
#------------------------------------------------------------------------
from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1abc_GR09_cfi import *

#------------------------------------------------------------------------

sinit = cms.Sequence(scalersRawToDigi + consecutiveHEs + APVPhases )

from DPGAnalysis.SiStripTools.eventtimedistribution_cfi import *



