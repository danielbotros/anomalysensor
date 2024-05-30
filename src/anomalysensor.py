from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from viam.utils import SensorReading

from viam.components.sensor import Sensor
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.logging import getLogger

import time
import asyncio
import random
import numpy as np

LOGGER = getLogger(__name__)

class anomalysensor(Sensor, Reconfigurable):
    
    """
    An anomaly sensor represents a virtual sensing device that detects when anomalous readings occur (defined as occuring less
    than 5% of the time). Can be configured to include anomalous readings and/or update statistics based on new readings.
    """
 
    MODEL: ClassVar[Model] = Model(ModelFamily("danielb", "sensor"), "anomalysensor")

    mean: float
    std: float
    include_anomalies: bool
    update_statistics: bool
    readings: List[float] = []

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate(cls, config: ComponentConfig):
        if "mean" in config.attributes.fields:
            if not config.attributes.fields["mean"].HasField("number_value"):
                raise Exception("Mean must be a float.")

        if "std" in config.attributes.fields:
            if not config.attributes.fields["std"].HasField("number_value"):
                raise Exception("Standard Deviation must be a float.")
        
        if "include_anomalies" in config.attributes.fields:
            if not config.attributes.fields["include_anomalies"].HasField("bool_value"):
                raise Exception("Include anomalies must be a bool.")
        
        if "update_statistics" in config.attributes.fields:
            if not config.attributes.fields["update_statistics"].HasField("bool_value"):
                raise Exception("Update statistics must be a bool.")

        return []

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        if "mean" in config.attributes.fields:
            self.mean = config.attributes.fields["mean"].number_value
        if "std" in config.attributes.fields:
            self.std = config.attributes.fields["std"].number_value
        if "include_anomalies" in config.attributes.fields:
            self.include_anomalies = config.attributes.fields["include_anomalies"].bool_value
        if "update_statistics" in config.attributes.fields:
            self.update_statistics = config.attributes.fields["update_statistics"].bool_value


    """ Implement the methods the Viam RDK defines for the Sensor API (rdk:component:sensor) """
    
    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """
        Given a measurements/data from a sensor, determine if this is an anomalous reading. Underlying sensor 
        readings must be of type float or int. If one is not provided, a random reading [0,1000] is generated.

        Returns:
            Mapping[str, Any]: The measurements. Can be of any type.
        """
        sensor_reading: Optional[float] = None

        if extra and 'sensor_reading' in extra:
            sensor_reading = extra['sensor_reading']
            if not isinstance(sensor_reading, (int, float)):
                raise ValueError("sensor_reading must be a float")

        if sensor_reading:
            reading = sensor_reading
        else:
            reading = [random.randint(0, 1000)]

        anomaly = 1 if (np.mean(reading) > (self.mean + 2*self.std) or np.mean(reading) < (self.mean - 2*self.std)) else 0

        if not anomaly or self.include_anomalies:
            self.readings = self.readings + reading
        
        if self.update_statistics:
            self.mean = np.mean(self.readings)
            self.std = np.std(self.readings)

        return {"anomaly": anomaly, "reading": reading}
