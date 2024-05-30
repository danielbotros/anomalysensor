# anomalysensor modular service

This module implements the [rdk sensor API](https://github.com/rdk/sensor-api) in a danielb:sensor:anomalysensor model.
With this model, you can...

## Requirements

_Add instructions here for any requirements._

``` bash
```

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `rdk:sensor:danielb:sensor:anomalysensor` model from the [`danielb:sensor:anomalysensor` module](https://app.viam.com/module/rdk/danielb:sensor:anomalysensor).

## Configure your sensor

> [!NOTE]  
> Before configuring your sensor, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `sensor` type, then select the `danielb:sensor:anomalysensor` model. 
Enter a name for your sensor and click **Create**.

On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

```json
{
  TODO: INSERT SAMPLE ATTRIBUTES
}
```

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `rdk:sensor:danielb:sensor:anomalysensor` sensors:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `todo1` | string | **Required** |  TODO |
| `todo2` | string | Optional |  TODO |

### Example Configuration

```json
{
  TODO: INSERT SAMPLE CONFIGURATION(S)
}
```

### Next Steps

_Add any additional information you want readers to know and direct them towards what to do next with this module._
_For example:_ 

- To test your...
- To write code against your...

## Troubleshooting

_Add troubleshooting notes here._
