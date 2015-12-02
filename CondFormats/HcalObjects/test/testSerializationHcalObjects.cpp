#include "CondFormats/Serialization/interface/Test.h"

#include "../src/headers.h"

int main()
{
    testSerialization<HcalCalibrationQIECoder>();
    //testSerialization<HcalCalibrationQIEData>(); no default constructor
    testSerialization<HcalChannelQuality>();
    testSerialization<HcalChannelStatus>();
    testSerialization<HcalCholeskyMatrices>();
    testSerialization<HcalCholeskyMatrix>();
    /* no default constructor
    testSerialization<HcalCondObjectContainer<HcalCalibrationQIECoder>>();
    testSerialization<HcalCondObjectContainer<HcalChannelStatus>>();
    testSerialization<HcalCondObjectContainer<HcalFlagHFDigiTimeParam>>();
    testSerialization<HcalCondObjectContainer<HcalGain>>();
    testSerialization<HcalCondObjectContainer<HcalGainWidth>>();
    testSerialization<HcalCondObjectContainer<HcalL1TriggerObject>>();
    testSerialization<HcalCondObjectContainer<HcalLUTCorr>>();
    testSerialization<HcalCondObjectContainer<HcalLongRecoParam>>();
    testSerialization<HcalCondObjectContainer<HcalZDCLowGainFraction>>();
    testSerialization<HcalCondObjectContainer<HcalLutMetadatum>>();
    testSerialization<HcalCondObjectContainer<HcalMCParam>>();
    testSerialization<HcalCondObjectContainer<HcalPFCorr>>();
    testSerialization<HcalCondObjectContainer<HcalPedestal>>();
    testSerialization<HcalCondObjectContainer<HcalPedestalWidth>>();
    testSerialization<HcalCondObjectContainer<HcalQIECoder>>();
    testSerialization<HcalCondObjectContainer<HcalRecoParam>>();
    testSerialization<HcalCondObjectContainer<HcalRespCorr>>();
    testSerialization<HcalCondObjectContainer<HcalTimeCorr>>();
    testSerialization<HcalCondObjectContainer<HcalTimingParam>>();
    testSerialization<HcalCondObjectContainer<HcalValidationCorr>>();
    testSerialization<HcalCondObjectContainer<HcalZSThreshold>>();
    */
    //testSerialization<HcalCondObjectContainerBase>(); protected constructor
    testSerialization<HcalCovarianceMatrices>();
    testSerialization<HcalCovarianceMatrix>();
    testSerialization<HcalDcsMap>();
    testSerialization<HcalDcsMap::Item>();
    testSerialization<HcalDcsValue>();
    testSerialization<HcalDcsValues>();
    testSerialization<HcalElectronicsMap>();
    testSerialization<HcalElectronicsMap::PrecisionItem>();
    testSerialization<HcalElectronicsMap::TriggerItem>();
    testSerialization<HcalFlagHFDigiTimeParam>();
    testSerialization<HcalFlagHFDigiTimeParams>();
    testSerialization<HcalGain>();
    testSerialization<HcalGainWidth>();
    testSerialization<HcalGainWidths>();
    testSerialization<HcalGains>();
    testSerialization<HcalL1TriggerObject>();
    testSerialization<HcalL1TriggerObjects>();
    testSerialization<HcalLUTCorr>();
    testSerialization<HcalLUTCorrs>();
    testSerialization<HcalLongRecoParam>();
    testSerialization<HcalLongRecoParams>();
    testSerialization<HcalZDCLowGainFraction>();
    testSerialization<HcalZDCLowGainFractions>();
    testSerialization<HcalLutMetadata>();
    testSerialization<HcalLutMetadata::NonChannelData>();
    testSerialization<HcalLutMetadatum>();
    testSerialization<HcalMCParam>();
    testSerialization<HcalMCParams>();
    testSerialization<HcalPFCorr>();
    testSerialization<HcalPFCorrs>();
    testSerialization<HcalPedestal>();
    testSerialization<HcalPedestalWidth>();
    testSerialization<HcalPedestalWidths>();
    testSerialization<HcalPedestals>();
    testSerialization<HcalQIECoder>();
    testSerialization<HcalQIEData>();
    testSerialization<HcalQIEType>();
    testSerialization<HcalQIETypes>();
    testSerialization<HcalRecoParam>();
    testSerialization<HcalRecoParams>();
    testSerialization<HcalRespCorr>();
    testSerialization<HcalRespCorrs>();
    testSerialization<HcalTimeCorr>();
    testSerialization<HcalTimeCorrs>();
    testSerialization<HcalTimingParam>();
    testSerialization<HcalTimingParams>();
    testSerialization<HcalValidationCorr>();
    testSerialization<HcalValidationCorrs>();
    testSerialization<HcalZSThreshold>();
    testSerialization<HcalZSThresholds>();
    testSerialization<std::pair<std::string, std::vector<HcalCalibrationQIECoder>>>();
    testSerialization<std::pair<std::string, std::vector<HcalChannelStatus>>>();
    testSerialization<std::pair<std::string, std::vector<HcalFlagHFDigiTimeParam>>>();
    testSerialization<std::pair<std::string, std::vector<HcalGain>>>();
    testSerialization<std::pair<std::string, std::vector<HcalGainWidth>>>();
    testSerialization<std::pair<std::string, std::vector<HcalL1TriggerObject>>>();
    testSerialization<std::pair<std::string, std::vector<HcalLUTCorr>>>();
    testSerialization<std::pair<std::string, std::vector<HcalLongRecoParam>>>();
    testSerialization<std::pair<std::string, std::vector<HcalLutMetadatum>>>();
    testSerialization<std::pair<std::string, std::vector<HcalMCParam>>>();
    testSerialization<std::pair<std::string, std::vector<HcalPFCorr>>>();
    testSerialization<std::pair<std::string, std::vector<HcalPedestal>>>();
    testSerialization<std::pair<std::string, std::vector<HcalPedestalWidth>>>();
    testSerialization<std::pair<std::string, std::vector<HcalQIECoder>>>();
    testSerialization<std::pair<std::string, std::vector<HcalQIEType>>>();
    testSerialization<std::pair<std::string, std::vector<HcalRecoParam>>>();
    testSerialization<std::pair<std::string, std::vector<HcalRespCorr>>>();
    testSerialization<std::pair<std::string, std::vector<HcalTimeCorr>>>();
    testSerialization<std::pair<std::string, std::vector<HcalTimingParam>>>();
    testSerialization<std::pair<std::string, std::vector<HcalValidationCorr>>>();
    testSerialization<std::pair<std::string, std::vector<HcalZSThreshold>>>();
    testSerialization<std::vector<HcalCalibrationQIECoder>>();
    testSerialization<std::vector<HcalChannelStatus>>();
    testSerialization<std::vector<HcalCholeskyMatrix>>();
    testSerialization<std::vector<HcalCovarianceMatrix>>();
    testSerialization<std::vector<HcalDcsMap::Item>>();
    testSerialization<std::vector<HcalDcsValue>>();
    testSerialization<std::vector<HcalElectronicsMap::PrecisionItem>>();
    testSerialization<std::vector<HcalElectronicsMap::TriggerItem>>();
    testSerialization<std::vector<HcalFlagHFDigiTimeParam>>();
    testSerialization<std::vector<HcalGain>>();
    testSerialization<std::vector<HcalGainWidth>>();
    testSerialization<std::vector<HcalL1TriggerObject>>();
    testSerialization<std::vector<HcalLUTCorr>>();
    testSerialization<std::vector<HcalLongRecoParam>>();
    testSerialization<std::vector<HcalZDCLowGainFraction>>();
    testSerialization<std::vector<HcalLutMetadatum>>();
    testSerialization<std::vector<HcalMCParam>>();
    testSerialization<std::vector<HcalPFCorr>>();
    testSerialization<std::vector<HcalPedestal>>();
    testSerialization<std::vector<HcalPedestalWidth>>();
    testSerialization<std::vector<HcalQIECoder>>();
    testSerialization<std::vector<HcalQIEType>>();
    testSerialization<std::vector<HcalRecoParam>>();
    testSerialization<std::vector<HcalRespCorr>>();
    testSerialization<std::vector<HcalTimeCorr>>();
    testSerialization<std::vector<HcalTimingParam>>();
    testSerialization<std::vector<HcalValidationCorr>>();
    testSerialization<std::vector<HcalZSThreshold>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalCalibrationQIECoder>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalChannelStatus>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalFlagHFDigiTimeParam>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalGain>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalGainWidth>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalL1TriggerObject>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalLUTCorr>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalLongRecoParam>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalZDCLowGainFraction>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalLutMetadatum>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalMCParam>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalPFCorr>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalPedestal>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalPedestalWidth>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalQIECoder>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalQIEType>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalRecoParam>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalRespCorr>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalTimeCorr>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalTimingParam>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalValidationCorr>>>>();
    testSerialization<std::vector<std::pair<std::string, std::vector<HcalZSThreshold>>>>();

    return 0;
}
