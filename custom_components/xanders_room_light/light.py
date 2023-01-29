"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = XandersRoomLight()
    add_entities([ent])


class XandersRoomLight(NewLight):
    """XandersRoom Light."""

    def __init__(self) -> None:
        """Initialize XandersRoom Light."""
        super(XandersRoomLight, self).__init__(
            "Xander's Room", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.xander_s_room_group"] = None
        # self.entities["light.xanders_room_top_group"] = None
        self.entities["light.xander_s_light_panel"] = None
        self.entities["light.xander_s_gradient_strip"] = None
        self.entities["light.xander_s_light_bar_e"] = None
        self.entities["light.xander_s_light_bar_w"] = None

        self.switch = "Xander's Room Switch"
