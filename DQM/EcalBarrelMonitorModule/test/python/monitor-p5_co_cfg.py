import FWCore.ParameterSet.Config as cms

process = cms.Process("ECALDQM")

process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerMapping_cfi")
process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerData_cfi")

import RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi
process.ecalUncalibHit2 = RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi.ecalFixedAlphaBetaFitUncalibRecHit.clone()

import RecoLocalCalo.EcalRecProducers.ecalWeightUncalibRecHit_cfi
process.ecalUncalibHit = RecoLocalCalo.EcalRecProducers.ecalWeightUncalibRecHit_cfi.ecalWeightUncalibRecHit.clone()

process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")

process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")

process.load("DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.preScaler = cms.EDFilter("Prescaler",
    prescaleFactor = cms.int32(1)
)

process.dqmInfoEB = cms.EDFilter("DQMEventInfo",
    subSystemFolder = cms.untracked.string('EcalBarrel')
)

process.dqmQTestEB = cms.EDFilter("QualityTester",
    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/EcalBarrelMonitorModule/test/data/EcalBarrelQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.dqmSaverEB = cms.EDFilter("DQMFileSaver",
    fileName = cms.untracked.string('EcalBarrel'),
    dirName = cms.untracked.string('.'),
    convention = cms.untracked.string('Online')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(150)
)
#process.source = cms.Source("NewEventStreamFileReader",
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(10),
#---
#    fileNames = cms.untracked.vstring('/store/users/dellaric/data/P5_Co.00002357.A.0.0.root')
#---
#    fileNames = cms.untracked.vstring('/store/users/dellaric/data/P5_Co.00031955.A.0.0.root')
#---
    fileNames = cms.untracked.vstring('/store/users/dellaric/data/P5_Co.00031961.A.0.0.root')
#---
)

process.EcalTrivialConditionRetriever = cms.ESSource("EcalTrivialConditionRetriever",
    adcToGeVEBConstant = cms.untracked.double(0.00875), ## 0.035
    pedWeights = cms.untracked.vdouble(0.333, 0.333, 0.333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    amplWeights = cms.untracked.vdouble(-0.333, -0.333, -0.333, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0),
    jittWeights = cms.untracked.vdouble(0.041, 0.041, 0.041, 0.0, 1.325, -0.05, -0.504, -0.502, -0.390, 0.0)
)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        EcalTBRawToDigiDccBlockSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiNumTowerBlocks = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        threshold = cms.untracked.string('WARNING'),
        noLineBreaks = cms.untracked.bool(True),
        EcalRawToDigiDevSRP = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiTpg = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDev = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemGain = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemBlock = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevDccBlockSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTriggerType = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTpg = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevNumTowerBlocks = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalBarrelMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalTBRawToDigiTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBInputService = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalTBRawToDigiGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        noTimeStamps = cms.untracked.bool(True),
        EcalRawToDigiDevChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigiTriggerType = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalRawToDigiDevTCC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalDCCHeaderRuntypeDecoder = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalTBRawToDigi = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        )
    ),
    categories = cms.untracked.vstring('EcalTBInputService', 
        'EcalTBRawToDigi', 
        'EcalTBRawToDigiTriggerType', 
        'EcalTBRawToDigiTpg', 
        'EcalTBRawToDigiNumTowerBlocks', 
        'EcalTBRawToDigiTowerId', 
        'EcalTBRawToDigiTowerSize', 
        'EcalTBRawToDigiChId', 
        'EcalTBRawToDigiGainZero', 
        'EcalTBRawToDigiGainSwitch', 
        'EcalTBRawToDigiDccBlockSize', 
        'EcalRawToDigiDev', 
        'EcalRawToDigiDevTriggerType', 
        'EcalRawToDigiDevTpg', 
        'EcalRawToDigiDevNumTowerBlocks', 
        'EcalRawToDigiDevTowerId', 
        'EcalRawToDigiDevTowerSize', 
        'EcalRawToDigiDevChId', 
        'EcalRawToDigiDevGainZero', 
        'EcalRawToDigiDevGainSwitch', 
        'EcalRawToDigiDevDccBlockSize', 
        'EcalRawToDigiDevMemBlock', 
        'EcalRawToDigiDevMemTowerId', 
        'EcalRawToDigiDevMemChId', 
        'EcalRawToDigiDevMemGain', 
        'EcalRawToDigiDevTCC', 
        'EcalRawToDigiDevSRP', 
        'EcalDCCHeaderRuntypeDecoder', 
        'EcalBarrelMonitorModule'),
    destinations = cms.untracked.vstring('cout')
)

process.ecalDataSequence = cms.Sequence(process.preScaler*process.ecalEBunpacker*process.ecalUncalibHit*process.ecalUncalibHit2*process.ecalRecHit)
process.ecalBarrelMonitorSequence = cms.Sequence(process.ecalBarrelMonitorModule*process.dqmInfoEB*process.ecalBarrelMonitorClient*process.dqmQTestEB*process.dqmSaverEB)

process.p = cms.Path(process.ecalDataSequence*process.ecalBarrelMonitorSequence)
process.q = cms.EndPath(process.ecalBarrelCosmicTasksSequence)

process.ecalUncalibHit2.MinAmplBarrel = 12.
process.ecalUncalibHit2.MinAmplEndcap = 16.
process.ecalUncalibHit2.EBdigiCollection = cms.InputTag("ecalEBunpacker","ebDigis")
process.ecalUncalibHit2.EEdigiCollection = cms.InputTag("ecalEBunpacker","eeDigis")

process.ecalUncalibHit.EBdigiCollection = cms.InputTag("ecalEBunpacker","ebDigis")
process.ecalUncalibHit.EEdigiCollection = cms.InputTag("ecalEBunpacker","eeDigis")

process.ecalRecHit.EBuncalibRecHitCollection = cms.InputTag("ecalUncalibHit2","EcalUncalibRecHitsEB")
process.ecalRecHit.EEuncalibRecHitCollection = cms.InputTag("ecalUncalibHit2","EcalUncalibRecHitsEE")

process.ecalBarrelCosmicTask.EcalUncalibratedRecHitCollection = cms.InputTag("ecalUncalibHit2","EcalUncalibRecHitsEB")
process.ecalBarrelLaserTask.EcalUncalibratedRecHitCollection = cms.InputTag("ecalUncalibHit2","EcalUncalibRecHitsEB")

process.ecalBarrelTimingTask.EcalUncalibratedRecHitCollection = cms.InputTag("ecalUncalibHit2","EcalUncalibRecHitsEB")

process.ecalBarrelMonitorClient.maskFile = 'maskfile-EB.dat'
process.ecalBarrelMonitorClient.location = 'P5_Co'
process.ecalBarrelMonitorClient.baseHtmlDir = '.'
#process.ecalBarrelMonitorClient.superModules = [34]

process.DQM.collectorHost = ''

