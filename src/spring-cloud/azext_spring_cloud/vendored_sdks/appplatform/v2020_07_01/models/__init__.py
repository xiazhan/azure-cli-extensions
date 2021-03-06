# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AppResource
    from ._models_py3 import AppResourceProperties
    from ._models_py3 import AvailableRuntimeVersions
    from ._models_py3 import BindingResource
    from ._models_py3 import BindingResourceProperties
    from ._models_py3 import CertificateProperties
    from ._models_py3 import CertificateResource
    from ._models_py3 import ClusterResourceProperties
    from ._models_py3 import ConfigServerGitProperty
    from ._models_py3 import ConfigServerProperties
    from ._models_py3 import ConfigServerResource
    from ._models_py3 import ConfigServerSettings
    from ._models_py3 import ConfigServerSettingsErrorRecord
    from ._models_py3 import ConfigServerSettingsValidateResult
    from ._models_py3 import CustomDomainProperties
    from ._models_py3 import CustomDomainResource
    from ._models_py3 import CustomDomainValidatePayload
    from ._models_py3 import CustomDomainValidateResult
    from ._models_py3 import DeploymentInstance
    from ._models_py3 import DeploymentResource
    from ._models_py3 import DeploymentResourceProperties
    from ._models_py3 import DeploymentSettings
    from ._models_py3 import Error
    from ._models_py3 import GitPatternRepository
    from ._models_py3 import LogFileUrlResponse
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagedIdentityProperties
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import MonitoringSettingProperties
    from ._models_py3 import MonitoringSettingResource
    from ._models_py3 import NameAvailability
    from ._models_py3 import NameAvailabilityParameters
    from ._models_py3 import NetworkProfile
    from ._models_py3 import NetworkProfileOutboundIPs
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationProperties
    from ._models_py3 import PersistentDisk
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegenerateTestKeyRequestPayload
    from ._models_py3 import RequiredTraffic
    from ._models_py3 import Resource
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuRestrictionInfo
    from ._models_py3 import ResourceSkuRestrictions
    from ._models_py3 import ResourceSkuZoneDetails
    from ._models_py3 import ResourceUploadDefinition
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Sku
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SupportedRuntimeVersion
    from ._models_py3 import TemporaryDisk
    from ._models_py3 import TestKeys
    from ._models_py3 import TrackedResource
    from ._models_py3 import UserSourceInfo
except (SyntaxError, ImportError):
    from ._models import AppResource
    from ._models import AppResourceProperties
    from ._models import AvailableRuntimeVersions
    from ._models import BindingResource
    from ._models import BindingResourceProperties
    from ._models import CertificateProperties
    from ._models import CertificateResource
    from ._models import ClusterResourceProperties
    from ._models import ConfigServerGitProperty
    from ._models import ConfigServerProperties
    from ._models import ConfigServerResource
    from ._models import ConfigServerSettings
    from ._models import ConfigServerSettingsErrorRecord
    from ._models import ConfigServerSettingsValidateResult
    from ._models import CustomDomainProperties
    from ._models import CustomDomainResource
    from ._models import CustomDomainValidatePayload
    from ._models import CustomDomainValidateResult
    from ._models import DeploymentInstance
    from ._models import DeploymentResource
    from ._models import DeploymentResourceProperties
    from ._models import DeploymentSettings
    from ._models import Error
    from ._models import GitPatternRepository
    from ._models import LogFileUrlResponse
    from ._models import LogSpecification
    from ._models import ManagedIdentityProperties
    from ._models import MetricDimension
    from ._models import MetricSpecification
    from ._models import MonitoringSettingProperties
    from ._models import MonitoringSettingResource
    from ._models import NameAvailability
    from ._models import NameAvailabilityParameters
    from ._models import NetworkProfile
    from ._models import NetworkProfileOutboundIPs
    from ._models import OperationDetail
    from ._models import OperationDisplay
    from ._models import OperationProperties
    from ._models import PersistentDisk
    from ._models import ProxyResource
    from ._models import RegenerateTestKeyRequestPayload
    from ._models import RequiredTraffic
    from ._models import Resource
    from ._models import ResourceSku
    from ._models import ResourceSkuCapabilities
    from ._models import ResourceSkuLocationInfo
    from ._models import ResourceSkuRestrictionInfo
    from ._models import ResourceSkuRestrictions
    from ._models import ResourceSkuZoneDetails
    from ._models import ResourceUploadDefinition
    from ._models import ServiceResource
    from ._models import ServiceSpecification
    from ._models import Sku
    from ._models import SkuCapacity
    from ._models import SupportedRuntimeVersion
    from ._models import TemporaryDisk
    from ._models import TestKeys
    from ._models import TrackedResource
    from ._models import UserSourceInfo
from ._paged_models import AppResourcePaged
from ._paged_models import BindingResourcePaged
from ._paged_models import CertificateResourcePaged
from ._paged_models import CustomDomainResourcePaged
from ._paged_models import DeploymentResourcePaged
from ._paged_models import OperationDetailPaged
from ._paged_models import ResourceSkuPaged
from ._paged_models import ServiceResourcePaged
from ._app_platform_management_client_enums import (
    ProvisioningState,
    TrafficDirection,
    ManagedIdentityType,
    ConfigServerState,
    MonitoringSettingState,
    TestKeyType,
    AppResourceProvisioningState,
    UserSourceType,
    RuntimeVersion,
    DeploymentResourceProvisioningState,
    DeploymentResourceStatus,
    SkuScaleType,
    ResourceSkuRestrictionsType,
    ResourceSkuRestrictionsReasonCode,
    SupportedRuntimeValue,
    SupportedRuntimePlatform,
)

__all__ = [
    'AppResource',
    'AppResourceProperties',
    'AvailableRuntimeVersions',
    'BindingResource',
    'BindingResourceProperties',
    'CertificateProperties',
    'CertificateResource',
    'ClusterResourceProperties',
    'ConfigServerGitProperty',
    'ConfigServerProperties',
    'ConfigServerResource',
    'ConfigServerSettings',
    'ConfigServerSettingsErrorRecord',
    'ConfigServerSettingsValidateResult',
    'CustomDomainProperties',
    'CustomDomainResource',
    'CustomDomainValidatePayload',
    'CustomDomainValidateResult',
    'DeploymentInstance',
    'DeploymentResource',
    'DeploymentResourceProperties',
    'DeploymentSettings',
    'Error',
    'GitPatternRepository',
    'LogFileUrlResponse',
    'LogSpecification',
    'ManagedIdentityProperties',
    'MetricDimension',
    'MetricSpecification',
    'MonitoringSettingProperties',
    'MonitoringSettingResource',
    'NameAvailability',
    'NameAvailabilityParameters',
    'NetworkProfile',
    'NetworkProfileOutboundIPs',
    'OperationDetail',
    'OperationDisplay',
    'OperationProperties',
    'PersistentDisk',
    'ProxyResource',
    'RegenerateTestKeyRequestPayload',
    'RequiredTraffic',
    'Resource',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuLocationInfo',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'ResourceSkuZoneDetails',
    'ResourceUploadDefinition',
    'ServiceResource',
    'ServiceSpecification',
    'Sku',
    'SkuCapacity',
    'SupportedRuntimeVersion',
    'TemporaryDisk',
    'TestKeys',
    'TrackedResource',
    'UserSourceInfo',
    'ServiceResourcePaged',
    'AppResourcePaged',
    'BindingResourcePaged',
    'CertificateResourcePaged',
    'CustomDomainResourcePaged',
    'DeploymentResourcePaged',
    'OperationDetailPaged',
    'ResourceSkuPaged',
    'ProvisioningState',
    'TrafficDirection',
    'ManagedIdentityType',
    'ConfigServerState',
    'MonitoringSettingState',
    'TestKeyType',
    'AppResourceProvisioningState',
    'UserSourceType',
    'RuntimeVersion',
    'DeploymentResourceProvisioningState',
    'DeploymentResourceStatus',
    'SkuScaleType',
    'ResourceSkuRestrictionsType',
    'ResourceSkuRestrictionsReasonCode',
    'SupportedRuntimeValue',
    'SupportedRuntimePlatform',
]
