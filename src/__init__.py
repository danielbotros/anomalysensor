"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .anomalysensor import anomalysensor

Registry.register_resource_creator(Sensor.SUBTYPE, anomalysensor.MODEL, ResourceCreatorRegistration(anomalysensor.new, anomalysensor.validate))
