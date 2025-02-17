from app.actions.client import OnyeshaDevice
from .core import InternalActionConfiguration, PullActionConfiguration, AuthActionConfiguration
import pydantic

class AuthenticateConfig(AuthActionConfiguration):
    username: str
    password: pydantic.SecretStr = pydantic.Field(..., title = "Password", 
                                description = "Password for Onyesha account",
                                format="password")


class PullObservationsConfig(PullActionConfiguration):
    endpoint: str = "mobile/vehicles"

class PullObservationsFromDeviceBatch(InternalActionConfiguration):
    devices: list[OnyeshaDevice]