from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import voluptuous as vol

from .const import DOMAIN  # Make sure you have a DOMAIN constant in your const.py
from . import RepsolLuzYGasAPI  # Import your API class


class RepsolConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Manage the Repsol Luz y Gas config flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, info):
        """Handle a flow initiated by the user."""
        errors = {}
        if info is not None:
            # Validate user input here and proceed to create the entry if valid
            return self.async_create_entry(title="Repsol Luz y Gas", data=info)

        # This is the schema for the form shown on the UI
        data_schema = vol.Schema(
            {
                vol.Required(
                    "username",
                    description="E-mail",
                ): str,
                vol.Required(
                    "password",
                    description="Password",
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
