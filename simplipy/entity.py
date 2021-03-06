"""Define a base SimpliSafe entity."""
from enum import Enum
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api import API  # pylint: disable=cyclic-import
    from .system import System  # pylint: disable=cyclic-import

_LOGGER: logging.Logger = logging.getLogger(__name__)


class EntityTypes(Enum):
    """Define entity types based on internal SimpliSafe ID number."""

    remote = 0
    keypad = 1
    keychain = 2
    panic_button = 3
    motion = 4
    entry = 5
    glass_break = 6
    carbon_monoxide = 7
    smoke = 8
    leak = 9
    temperature = 10
    camera = 12
    siren = 13
    unknown = 99


class Entity:
    """Define a base SimpliSafe entity."""

    def __init__(
        self, api: "API", system: "System", entity_type: EntityTypes, entity_data: dict
    ) -> None:
        """Initialize."""
        self._api: "API" = api
        self._system: "System" = system
        self._type: EntityTypes = entity_type
        self.entity_data: dict = entity_data

    @property
    def name(self) -> str:
        """Return the entity name."""
        return self.entity_data["name"]

    @property
    def serial(self) -> str:
        """Return the entity number."""
        return self.entity_data["serial"]

    @property
    def type(self) -> EntityTypes:
        """Return the entity type."""
        return self._type


class EntityV3(Entity):
    """Define a base SimpliSafe V3 entity."""

    @property
    def error(self) -> bool:
        """Return the entity's error status."""
        return self.entity_data["status"].get("malfunction", False)

    @property
    def low_battery(self) -> bool:
        """Return whether the entity's battery is low."""
        return self.entity_data["flags"]["lowBattery"]

    @property
    def offline(self) -> bool:
        """Return whether the entity is offline."""
        return self.entity_data["flags"]["offline"]

    @property
    def settings(self) -> dict:
        """Return the entity's settings."""
        return self.entity_data["setting"]
