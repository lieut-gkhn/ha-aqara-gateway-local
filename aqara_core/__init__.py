"""Aqara Gateway Local integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from ..custom_components.aqara_gateway_local.const import DOMAIN

AqaraConfigEntry = ConfigEntry


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AqaraConfigEntry,
) -> bool:
    """Set up from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = {}
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: AqaraConfigEntry,
) -> bool:
    """Unload a config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True