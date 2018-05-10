import json
from utils.eq import eq_services
from utils.utils import parseStorage
from escore.core import ESCore
from escore.pyQueryConstructor import QueryConstructor
import sys
from tqdm import tqdm

data = json.load(open('aws_services.json'))

print(data.keys())
# sys.exit()
indexable = []
for services in eq_services['supported_services']:
    # print(data[services]['products'].keys())
    for k, v in data[services]['products'].items():
        tisd = {}
        try:
            if k in data[services]['terms']['OnDemand'].keys():
                for kk, vv in data[services]['terms']['OnDemand'][k].items():
                    # print(vv['priceDimensions'])
                    for kkk, vvv in vv['priceDimensions'].items():
                        print(vvv['description'])
                        tisd['description'] = vvv['description']
                        print(vvv['appliesTo'])
                        tisd['appliesTo'] = vvv['appliesTo']
                        # print(vvv['beginRange'])
                        # print(vvv['endRange'])
                        print(vvv['pricePerUnit'])
                        tisd['pricePerUnit'] = vvv['pricePerUnit']
                        print(vvv['unit'])
                        tisd['unit'] = vvv['unit']
                        tisd['terms'] = 'OnDemand'
                        print('{}->{}'.format(kkk, vvv))
            elif k in data[services]['terms']['Reserved'].keys():
                for kk, vv in data[services]['terms']['Reserved'][k].items():
                    # print(vv['priceDimensions'])
                    for kkk, vvv in vv['priceDimensions'].items():
                        print(vvv['description'])
                        tisd['description'] = vvv['description']
                        print(vvv['appliesTo'])
                        tisd['appliesTo'] = vvv['appliesTo']
                        # print(vvv['beginRange'])
                        # print(vvv['endRange'])
                        print(vvv['pricePerUnit'])
                        tisd['pricePerUnit'] = vvv['pricePerUnit']
                        print(vvv['unit'])
                        tisd['unit'] = vvv['unit']
                        tisd['terms'] = 'Reserved'
                        print('{}->{}'.format(kkk, vvv))
        except Exception as inst:
            print('&'*100)
            print(services)
            # print(data[services]['terms']['OnDemand'].keys())
            print(data[services]['terms']['Reserved'].keys())
            print(inst.args)
            print(data[services]['terms']['OnDemand'].keys())
            print('&' * 100)
            # pass
            sys.exit()
        if 'clockSpeed' in v['attributes']:
            # print(v['attributes']['clockSpeed'])
            tisd['clockSpeed'] = v['attributes']['clockSpeed']
        if 'requestType' in v['attributes']:
            # print(v['attributes']['requestType'])  # todo: add as comment
            tisd['requestType'] = v['attributes']['requestType']
        if 'location' in v['attributes']:
            # print(v['attributes']['location'])
            tisd['location'] = v['attributes']['location']
        if 'usagetype' in v['attributes']:
            # print(v['attributes']['usagetype'])
            tisd['usagetype'] = v['attributes']['usagetype']
        if 'minimumStorageVolume' in v['attributes']:
            # print(v['attributes']['minimumStorageVolume'])
            tisd['minimumStorageVolume'] = v['attributes']['minimumStorageVolume']
        if 'instanceCapacity2xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity2xlarge'])  # todo: add as comment
        if 'enhancedNetworkingSupported' in v['attributes']:
            # print(v['attributes']['enhancedNetworkingSupported'])
            tisd['enhancedNetworkingSupported'] = v['attributes']['enhancedNetworkingSupported']
        if 'cacheEngine' in v['attributes']:
            print(v['attributes']['cacheEngine'])  # todo: add as comment
        if 'deploymentLocation' in v['attributes']:
            # print(v['attributes']['deploymentLocation'])
            tisd['deploymentLocation'] = v['attributes']['deploymentLocation']
        if 'directorySize' in v['attributes']:
            print(v['attributes']['directorySize'])  # todo: add as comment
        if 'license' in v['attributes']:
            # print(v['attributes']['license'])
            tisd['license'] = v['attributes']['license']
        if 'directoryType' in v['attributes']:
            print(v['attributes']['directoryType'])  # todo: add as comment
        if 'videoCodec' in v['attributes']:
            print(v['attributes']['videoCodec'])  # todo: add as comment
        if 'meteringType' in v['attributes']:
            # print(v['attributes']['meteringType'])
            tisd['meteringType'] = v['attributes']['meteringType']
        if 'vqSetting' in v['attributes']:
            print(v['attributes']['vqSetting'])  # todo: add as comment
        if 'countsAgainstQuota' in v['attributes']:
            print(v['attributes']['countsAgainstQuota'])  # todo: add as comment
        if 'supportedModes' in v['attributes']:
            print(v['attributes']['supportedModes'])  # todo: add as comment
        if 'origin' in v['attributes']:
            print(v['attributes']['origin'])  # todo: add as comment
        if 'maximumStorageVolume' in v['attributes']:
            # print(v['attributes']['maximumStorageVolume'])
            tisd['maximumStorageVolume'] = v['attributes']['maximumStorageVolume']
        if 'instanceStorageGb' in v['attributes']:
            # print(v['attributes']['instanceStorageGb'])
            tisd['instanceStorageGb'] = v['attributes']['instanceStorageGb']
        if 'operatingSystem' in v['attributes']:
            # print(v['attributes']['operatingSystem'])
            tisd['operatingSystem'] = v['attributes']['operatingSystem']
        if 'machineLearningProcess' in v['attributes']:
            # print(v['attributes']['machineLearningProcess'])
            tisd['machineLearningProcess'] = v['attributes']['machineLearningProcess']
        if 'instanceCapacity8xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity8xlarge'])  # todo: add as comment
        if 'description' in v['attributes']:
            print(v['attributes']['description'])  # todo: add as comment
        if 'programmaticCaseManagement' in v['attributes']:
            print(v['attributes']['programmaticCaseManagement'])  # todo: add as comment
        if 'memoryGib' in v['attributes']:
            # print(v['attributes']['memoryGib'])
            tisd['memoryGib'] = v['attributes']['memoryGib']
        if 'customerServiceAndCommunities' in v['attributes']:
            print(v['attributes']['customerServiceAndCommunities'])  # todo: add as comment
        if 'recipient' in v['attributes']:
            print(v['attributes']['recipient'])  # todo: add as comment
        if 'softwareIncluded' in v['attributes']:
            print(v['attributes']['softwareIncluded'])  # todo: add as comment
        if 'subscriptionType' in v['attributes']:
            print(v['attributes']['subscriptionType'])  # todo: add as comment
        if 'operationsSupport' in v['attributes']:
            print(v['attributes']['operationsSupport'])  # todo: add as comment
        if 'planType' in v['attributes']:
            print(v['attributes']['planType'])  # todo: add as comment
        if 'computeType' in v['attributes']:
            # print(v['attributes']['computeType'])
            tisd['computeType'] = v['attributes']['computeType']
        if 'mailboxStorage' in v['attributes']:
            print(v['attributes']['mailboxStorage'])  # todo: add as comment
        if 'upfrontCommitment' in v['attributes']:
            print(v['attributes']['upfrontCommitment'])  # todo: add as comment
        if 'normalizationSizeFactor' in v['attributes']:
            print(v['attributes']['normalizationSizeFactor'])  # todo: add as comment
        if 'tier' in v['attributes']:
            print(v['attributes']['tier'])  # todo: add as comment
        if 'licenseType' in v['attributes']:
            # print(v['attributes']['licenseType'])
            tisd['licenseType'] = v['attributes']['licenseType']
        if 'whoCanOpenCases' in v['attributes']:
            print(v['attributes']['whoCanOpenCases'])  # todo: add as comment
        if 'instanceFamily' in v['attributes']:
            # print(v['attributes']['instanceFamily'])
            tisd['instanceFamily'] = v['attributes']['instanceFamily']
        if 'storageMedia' in v['attributes']:
            # print(v['attributes']['storageMedia'])
            tisd['storageMedia'] = v['attributes']['storageMedia']
        if 'dedicatedEbsThroughput' in v['attributes']:
            # print(v['attributes']['dedicatedEbsThroughput'])
            tisd['dedicatedEbsThroughput'] = v['attributes']['dedicatedEbsThroughput']
        if 'maximumExtendedStorage' in v['attributes']:
            # print(v['attributes']['maximumExtendedStorage'])
            tisd['maximumExtendedStorage'] = v['attributes']['maximumExtendedStorage']
        if 'instanceCapacity12xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity12xlarge'])  # todo: add as comment
        if 'executionFrequency' in v['attributes']:
            print(v['attributes']['executionFrequency'])  # todo: add as comment
        if 'durability' in v['attributes']:
            print(v['attributes']['durability'])  # todo: add as comment
        if 'trialProduct' in v['attributes']:
            print(v['attributes']['trialProduct'])  # todo: add as comment
        if 'servicename' in v['attributes']:
            print(v['attributes']['servicename'])  # todo: add as comment
        if 'bundle' in v['attributes']:
            print(v['attributes']['bundle'])  # todo: add as comment
        if 'frameRate' in v['attributes']:
            print(v['attributes']['frameRate'])  # todo: add as comment
        if 'videoResolution' in v['attributes']:
            print(v['attributes']['videoResolution'])  # todo: add as comment
        if 'caseSeverityresponseTimes' in v['attributes']:
            print(v['attributes']['caseSeverityresponseTimes'])  # todo: add as comment
        if 'instanceCapacityXlarge' in v['attributes']:
            print(v['attributes']['instanceCapacityXlarge'])  # todo: add as comment
        if 'brokerEngine' in v['attributes']:
            print(v['attributes']['brokerEngine'])  # todo: add as comment
        if 'thirdpartySoftwareSupport' in v['attributes']:
            # print(v['attributes']['thirdpartySoftwareSupport'])
            tisd['thirdpartySoftwareSupport'] = v['attributes']['thirdpartySoftwareSupport']
        if 'storageDescription' in v['attributes']:
            print(v['attributes']['storageDescription'])  # todo: add as comment
        if 'groupDescription' in v['attributes']:
            print(v['attributes']['groupDescription'])  # todo: add as comment
        if 'cacheMemorySizeGb' in v['attributes']:
            print(v['attributes']['cacheMemorySizeGb'])  # todo: add as comment
        if 'memory' in v['attributes']:
            # print(v['attributes']['memory'])
            memval = v['attributes']['memory']
            if memval == "NA":
                tisd['memory'] = float(-1)
            elif "GB" in memval:
                tisd['memory'] = parseStorage(memval)
            # elif "1GB" in memval or "2GB" in memval or "0.5GB" in memval or "8GB" in memval:
            #     print("Not handeled yet")   #  TODO: IMPORTANT
            else:
                try:
                    if "," in memval:
                        memValCast = float(memval.split(" ")[0].replace(",", "."))
                    else:
                        memValCast = float(memval.split(" ")[0])
                    tisd['memory'] = memValCast  # cast to float
                except:
                    print("------>{}".format(v['attributes']['memory']))
                    sys.exit(3)
        if 'standardStorageRetentionIncluded' in v['attributes']:
            print(v['attributes']['standardStorageRetentionIncluded'])  # todo: add as comment
        if 'operation' in v['attributes']:
            print(v['attributes']['operation'])  # todo: add as comment
        if 'locationType' in v['attributes']:
            # print(v['attributes']['locationType'])
            tisd['locationType'] = v['attributes']['locationType']
        if 'deviceOs' in v['attributes']:
            # print(v['attributes']['deviceOs'])
            tisd['deviceOs'] = v['attributes']['deviceOs']
        if 'instanceCapacity24xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity24xlarge'])  # todo: add as comment
        if 'fromLocationType' in v['attributes']:
            print(v['attributes']['fromLocationType'])  # todo: add as comment
        if 'includedServices' in v['attributes']:
            # print(v['attributes']['includedServices'])
            tisd['includedServices'] = v['attributes']['includedServices']
        if 'toLocationType' in v['attributes']:
            print(v['attributes']['toLocationType'])  # todo: add as comment
        if 'servicecode' in v['attributes']:
            print(v['attributes']['servicecode'])  # todo: add as comment
        if 'version' in v['attributes']:
            print(v['attributes']['version'])  # todo: add as comment
        if 'currentGeneration' in v['attributes']:
            # print(v['attributes']['currentGeneration'])
            tisd['currentGeneration'] = v['attributes']['currentGeneration']
        if 'launchSupport' in v['attributes']:
            print(v['attributes']['launchSupport'])  # todo: add as comment
        if 'processorFeatures' in v['attributes']:
            # print(v['attributes']['processorFeatures'])
            tisd['processorFeatures'] = v['attributes']['processorFeatures']
        if 'softwareType' in v['attributes']:
            # print(v['attributes']['softwareType'])
            tisd['softwareType'] = v['attributes']['softwareType']
        if 'transcodingResult' in v['attributes']:
            print(v['attributes']['transcodingResult'])  # todo: add as comment
        if 'inputMode' in v['attributes']:
            print(v['attributes']['inputMode'])  # todo: add as comment
        if 'instanceCapacity9xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity9xlarge'])  # todo: add as comment
        if 'protocol' in v['attributes']:
            # print(v['attributes']['protocol'])
            tisd['protocol'] = v['attributes']['protocol']
        if 'instanceCapacity10xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity10xlarge'])  # todo: add as comment
        if 'instanceCapacityLarge' in v['attributes']:
            print(v['attributes']['instanceCapacityLarge'])  # todo: add as comment
        if 'intelTurboAvailable' in v['attributes']:
            # print(v['attributes']['intelTurboAvailable'])
            tisd['intelTurboAvailable'] = v['attributes']['intelTurboAvailable']
        if 'feeDescription' in v['attributes']:
            print(v['attributes']['feeDescription'])  # todo: add as comment
        if 'maxIopsBurstPerformance' in v['attributes']:
            print(v['attributes']['maxIopsBurstPerformance'])  # todo: add as comment
        if 'cloudSearchVersion' in v['attributes']:
            print(v['attributes']['cloudSearchVersion'])  # todo: add as comment
        if 'maxVolumeSize' in v['attributes']:
            # print(v['attributes']['maxVolumeSize'])
            tisd['maxVolumeSize'] = v['attributes']['maxVolumeSize']
        if 'enhancedNetworkingSupport' in v['attributes']:
            # print(v['attributes']['enhancedNetworkingSupport'])
            tisd['enhancedNetworkingSupport'] = v['attributes']['enhancedNetworkingSupport']
        if 'tenancy' in v['attributes']:
            print(v['attributes']['tenancy'])  # todo: add as comment
        if 'networkPerformance' in v['attributes']:
            # print(v['attributes']['networkPerformance'])
            tisd['networkPerformance'] = v['attributes']['networkPerformance']
        if 'proactiveGuidance' in v['attributes']:
            print(v['attributes']['proactiveGuidance'])  # todo: add as comment
        if 'availability' in v['attributes']:
            print(v['attributes']['availability'])  # todo: add as comment
        if 'directoryTypeDescription' in v['attributes']:
            print(v['attributes']['directoryTypeDescription'])  # todo: add as comment
        if 'storageType' in v['attributes']:
            # print(v['attributes']['storageType'])
            tisd['storageType'] = v['attributes']['storageType']
        if 'group' in v['attributes']:
            print(v['attributes']['group'])  # todo: add as comment
        if 'elasticGpuType' in v['attributes']:
            # print(v['attributes']['elasticGpuType'])
            tisd['elasticGpuType'] = v['attributes']['elasticGpuType']
        if 'storageclass' in v['attributes']:
            # print(v['attributes']['storageclass'])
            tisd['storageclass'] = v['attributes']['storageclass']
        if 'dataAction' in v['attributes']:
            print(v['attributes']['dataAction'])  # todo: add as comment
        if 'singleOrDualPass' in v['attributes']:
            print(v['attributes']['singleOrDualPass'])  # todo: add as comment
        if 'preInstalledSw' in v['attributes']:
            # print(v['attributes']['preInstalledSw'])
            tisd['preInstalledSw'] = v['attributes']['preInstalledSw']
        if 'freeTrial' in v['attributes']:
            print(v['attributes']['freeTrial'])  # todo: add as comment
        if 'includedEvents' in v['attributes']:
            print(v['attributes']['includedEvents'])  # todo: add as comment
        if 'instanceCapacity18xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity18xlarge'])  # todo: add as comment
        if 'jobnshipp' in v['attributes']:
            print(v['attributes']['jobnshipp'])  # todo: add as comment
        if 'vcpu' in v['attributes']:
            # print(v['attributes']['vcpu'])
            tisd['vcpu'] = float(v['attributes']['vcpu'])
        if 'accountAssistance' in v['attributes']:
            print(v['attributes']['accountAssistance'])  # todo: add as comment
        if 'instanceCapacityMedium' in v['attributes']:
            print(v['attributes']['instanceCapacityMedium'])  # todo: add as comment
        if 'volumeType' in v['attributes']:
            # print(v['attributes']['volumeType'])
            tisd['volumeType'] = v['attributes']['volumeType']
        if 'technicalSupport' in v['attributes']:
            print(v['attributes']['technicalSupport'])  # todo: add as comment
        if 'dataTransferQuota' in v['attributes']:
            # print(v['attributes']['dataTransferQuota'])
            tisd['dataTransferQuota'] = v['attributes']['dataTransferQuota']
        if 'usageFamily' in v['attributes']:
            print(v['attributes']['usageFamily'])  # todo: add as comment
        if 'country' in v['attributes']:
            # print(v['attributes']['country'])
            tisd['country'] = v['attributes']['country']
        if 'callingType' in v['attributes']:
            print(v['attributes']['callingType'])  # todo: add as comment
        if 'databaseEngine' in v['attributes']:
            print(v['attributes']['databaseEngine'])  # todo: add as comment
        if 'routingType' in v['attributes']:
            print(v['attributes']['routingType'])  # todo: add as comment
        if 'gpu' in v['attributes']:
            # print(v['attributes']['gpu'])
            tisd['gpu'] = v['attributes']['gpu']
        if 'toLocation' in v['attributes']:
            # print(v['attributes']['toLocation'])
            tisd['toLocation'] = v['attributes']['toLocation']
        if 'freeQueryTypes' in v['attributes']:
            print(v['attributes']['freeQueryTypes'])  # todo: add as comment
        if 'videoFrameRate' in v['attributes']:
            print(v['attributes']['videoFrameRate'])  # todo: add as comment
        if 'training' in v['attributes']:
            print(v['attributes']['training'])  # todo: add as comment
        if 'bestPractices' in v['attributes']:
            print(v['attributes']['bestPractices'])  # todo: add as comment
        if 'contentType' in v['attributes']:
            # print(v['attributes']['contentType'])
            tisd['contentType'] = v['attributes']['contentType']
        if 'fromLocation' in v['attributes']:
            # print(v['attributes']['fromLocation'])
            tisd['fromLocation'] = v['attributes']['fromLocation']
        if 'storageClass' in v['attributes']:
            # print(v['attributes']['storageClass'])
            tisd['storageClass'] = v['attributes']['storageClass']
        if 'instanceCapacity4xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity4xlarge'])  # todo: add as comment
        if 'withActiveUsers' in v['attributes']:
            print(v['attributes']['withActiveUsers'])  # todo: add as comment
        if 'deploymentOption' in v['attributes']:
            print(v['attributes']['deploymentOption'])  # todo: add as comment
        if 'frequencyMode' in v['attributes']:
            # print(v['attributes']['frequencyMode'])
            tisd['frequencyMode'] = v['attributes']['frequencyMode']
        if 'physicalProcessor' in v['attributes']:
            # print(v['attributes']['physicalProcessor'])
            tisd['physicalProcessor'] = v['attributes']['physicalProcessor']
        if 'availabilityZone' in v['attributes']:
            print(v['attributes']['availabilityZone'])  # todo: add as comment
        if 'engineCode' in v['attributes']:
            print(v['attributes']['engineCode'])  # todo: add as comment
        if 'routingTarget' in v['attributes']:
            print(v['attributes']['routingTarget'])  # todo: add as comment
        if 'edition' in v['attributes']:
            print(v['attributes']['edition'])  # todo: add as comment
        if 'bitRate' in v['attributes']:
            # print(v['attributes']['bitRate'])
            tisd['bitRate'] = v['attributes']['bitRate']
        if 'tenancySupport' in v['attributes']:
            print(v['attributes']['tenancySupport'])  # todo: add as comment
        if 'instance' in v['attributes']:
            # print(v['attributes']['instance'])
            tisd['instance'] = v['attributes']['instance']
        if 'virtualInterfaceType' in v['attributes']:
            print(v['attributes']['virtualInterfaceType'])  # todo: add as comment
        if 'minVolumeSize' in v['attributes']:
            print(v['attributes']['minVolumeSize'])  # todo: add as comment
        if 'freeTier' in v['attributes']:
            print(v['attributes']['freeTier'])  # todo: add as comment
        if 'output' in v['attributes']:
            print(v['attributes']['output'])  # todo: add as comment
        if 'snowballType' in v['attributes']:
            print(v['attributes']['snowballType'])  # todo: add as comment
        if 'feeCode' in v['attributes']:
            print(v['attributes']['feeCode'])  # todo: add as comment
        if 'codec' in v['attributes']:
            print(v['attributes']['codec'])  # todo: add as comment
        if 'intelAvxAvailable' in v['attributes']:
            # print(v['attributes']['intelAvxAvailable'])
            tisd['intelAvxAvailable'] = v['attributes']['intelAvxAvailable']
        if 'transferType' in v['attributes']:
            print(v['attributes']['transferType'])  # todo: add as comment
        if 'executionLocation' in v['attributes']:
            print(v['attributes']['executionLocation'])  # todo: add as comment
        if 'comments' in v['attributes']:
            # print(v['attributes']['comments'])
            tisd['comments'] = v['attributes']['comments']
        if 'messageDeliveryFrequency' in v['attributes']:
            print(v['attributes']['messageDeliveryFrequency'])  # todo: add as comment
        if 'databaseEdition' in v['attributes']:
            print(v['attributes']['databaseEdition'])  # todo: add as comment
        if 'architectureSupport' in v['attributes']:
            print(v['attributes']['architectureSupport'])
            tisd['architectureSupport'] = v['attributes']['architectureSupport']
        if 'computeFamily' in v['attributes']:
            print(v['attributes']['computeFamily'])  # todo: add as comment
        if 'processorArchitecture' in v['attributes']:
            print(v['attributes']['processorArchitecture'])
        if 'endpointType' in v['attributes']:
            print(v['attributes']['endpointType'])  # todo: add as comment
        if 'ecu' in v['attributes']:
            # print(v['attributes']['ecu'])
            tisd['ecu'] = v['attributes']['ecu']
        if 'releaseType' in v['attributes']:
            print(v['attributes']['releaseType'])  # todo: add as comment
        if 'operationType' in v['attributes']:
            print(v['attributes']['operationType'])  # todo: add as comment
        if 'resourceType' in v['attributes']:
            print(v['attributes']['resourceType'])  # todo: add as comment
        if 'outputMode' in v['attributes']:
            print(v['attributes']['outputMode'])  # todo: add as comment
        if 'alarmType' in v['attributes']:
            print(v['attributes']['alarmType'])  # todo: add as comment
        if 'provisioned' in v['attributes']:
            # print(v['attributes']['provisioned'])
            tisd['provisioned'] = v['attributes']['provisioned']
        if 'directConnectLocation' in v['attributes']:
            # print(v['attributes']['directConnectLocation'])
            tisd['directConnectLocation'] = v['attributes']['directConnectLocation']
        if 'overageType' in v['attributes']:
            print(v['attributes']['overageType'])  # todo: add as comment
        if 'requestDescription' in v['attributes']:
            print(v['attributes']['requestDescription'])  # todo: add as comment
        if 'queueType' in v['attributes']:
            print(v['attributes']['queueType'])  # todo: add as comment
        if 'instanceType' in v['attributes']:
            # print(v['attributes']['instanceType'])
            tisd['instanceType'] = v['attributes']['instanceType']
        if 'maxThroughputvolume' in v['attributes']:
            # print(v['attributes']['maxThroughputvolume'])
            tisd['maxThroughputvolume'] = v['attributes']['maxThroughputvolume']
        if 'instanceCapacity16xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity16xlarge'])  # todo: add as comment
        if 'videoQuality' in v['attributes']:
            print(v['attributes']['videoQuality'])  # todo: add as comment
        if 'freeUsageIncluded' in v['attributes']:
            print(v['attributes']['freeUsageIncluded'])  # todo: add as comment
        if 'maximumCapacity' in v['attributes']:
            print(v['attributes']['maximumCapacity'])
            tisd['maximumCapacity'] = v['attributes']['maximumCapacity']
        if 'maxIopsvolume' in v['attributes']:
            # print(v['attributes']['maxIopsvolume'])
            tisd['maxIopsvolume'] = v['attributes']['maxIopsvolume']
        if 'portSpeed' in v['attributes']:
            print(v['attributes']['portSpeed'])  # todo: add as comment
        if 'architecturalReview' in v['attributes']:
            print(v['attributes']['architecturalReview'])  # todo: add as comment
        if 'serverLocation' in v['attributes']:
            # print(v['attributes']['serverLocation'])
            tisd['serverLocation'] = v['attributes']['serverLocation']
        if 'input' in v['attributes']:
            print(v['attributes']['input'])  # todo: add as comment
        if 'gpuMemory' in v['attributes']:
            # print(v['attributes']['gpuMemory'])
            tisd['gpuMemory'] = v['attributes']['gpuMemory']
        if 'addonFeature' in v['attributes']:
            print(v['attributes']['addonFeature'])  # todo: add as comment
        if 'georegioncode' in v['attributes']:
            # print(v['attributes']['georegioncode'])
            tisd['georegioncode'] = v['attributes']['georegioncode']
        if 'licenseModel' in v['attributes']:
            # print(v['attributes']['licenseModel'])
            tisd['licenseModel'] = v['attributes']['licenseModel']
        if 'eventType' in v['attributes']:
            print(v['attributes']['eventType'])  # todo: add as comment
        if 'storage' in v['attributes']:
            # print(v['attributes']['storage'])
            storageVal = v['attributes']['storage']
            if storageVal.split(" ")[0] == "EBS":
                tisd['storage'] = float(-1)
            elif storageVal == "N/A":
                tisd['storage'] = float(-1)
            elif storageVal == "NA":
                tisd['storage'] = float(-1)
            elif storageVal == "Included" or storageVal == "Additional":
                tisd['storage'] = parseStorage(v['attributes']['maximumStorageVolume'])
            elif 'SSD' in storageVal:
                tisd['storage'] = parseStorage(v['attributes']['storage'].split(" ")[0])
                tisd['storageType'] = 'SSD'
            elif 'HDD' in storageVal:
                tisd['storage'] = parseStorage(v['attributes']['storage'].split(" ")[0])
                tisd['storageType'] = 'HDD'
            elif "GB" in storageVal:
                tisd['storage'] = parseStorage(storageVal)
            elif "Root" in storageVal or "above" in storageVal:
                print("Not handeled yet")  # TODO: IMPORTANT
            else:
                try:
                    tisd['storage'] = float(v['attributes']['storage'].split(" ")[0])
                except:
                    print("---->{}".format(v['attributes']['storage']))
                    sys.exit(1)
        if 'meterMode' in v['attributes']:
            print(v['attributes']['meterMode'])  # todo: add as comment
        if 'instanceCapacity32xlarge' in v['attributes']:
            print(v['attributes']['instanceCapacity32xlarge'])  # todo: add as comment
        if 'messageDeliveryOrder' in v['attributes']:
            print(v['attributes']['messageDeliveryOrder'])  # todo: add as comment
        if 'videoQualitySetting' in v['attributes']:
            print(v['attributes']['videoQualitySetting'])  # todo: add as comment
        if 'runningMode' in v['attributes']:
            print(v['attributes']['runningMode'])  # todo: add as comment
        if 'io' in v['attributes']:
            # print(v['attributes']['io'])
            tisd['io'] = v['attributes']['io']
        if 'freeOverage' in v['attributes']:
            print(v['attributes']['freeOverage'])  # todo: add as comment
        if 'resolution' in v['attributes']:
            print(v['attributes']['resolution'])  # todo: add as comment
        if 'resourceEndpoint' in v['attributes']:
            print(v['attributes']['resourceEndpoint'])  # todo: add as comment
        if 'intelAvx2Available' in v['attributes']:
            print(v['attributes']['intelAvx2Available'])  # todo: add as comment
        if 'executionMode' in v['attributes']:
            print(v['attributes']['executionMode'])  # todo: add as comment
        if 'ebsOptimized' in v['attributes']:
            # print(v['attributes']['ebsOptimized'])
            tisd['ebsOptimized'] = v['attributes']['ebsOptimized']
        if 'physicalCores' in v['attributes']:
            # print(v['attributes']['physicalCores'])
            tisd['physicalCores'] = v['attributes']['physicalCores']
        indexable.append(tisd)

# print(len(indexable))

testConnection = ESCore('194.102.63.78')
# print(testConnection.info())
# print(testConnection.clusterHealth())

# for d in tqdm(indexable):
#     print(d)

for d in tqdm(indexable):
    testConnection.pushData('maneuver', doc_type='d', body=d)
#
# queryBody = {
#     "query": {
#         "bool" : {
#             "must" : {
#                 "query_string" : {
#                     "query" : "*"
#                 }
#             }
#         }
#     }
# }

# newquery = QueryConstructor()
# queryBody = newquery.cequery("memory:\"7*\" AND vcpu:\"4\"")
# print(testConnection.mquery(queryBody=queryBody))