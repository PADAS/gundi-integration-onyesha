import logging
import pydantic

from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from app.services.state import IntegrationStateManager

DEFAULT_TIMEOUT = (3.1, 20)
DEFAULT_LOOKBACK_DAYS = 60

logger = logging.getLogger(__name__)
state_manager = IntegrationStateManager()


class OnyeshaPosition(BaseModel):
    ChannelStatus: str
    UploadTimeStamp: datetime
    Latitude: float
    Longitude: float
    Altitude: float
    ECEFx: int
    ECEFy: int
    ECEFz: int
    RxStatus: int
    PDOP: float
    MainV: float
    BkUpV: float
    Temperature: float
    FixDuration: int
    bHasTempVoltage: bool
    DevName: str
    DeltaTime: int
    FixType: int
    CEPRadius: int
    CRC: int
    DeviceID: int
    RecDateTime: datetime


def default_last_run():
    '''Default for a new configuration is to pretend the last run was 7 days ago'''
    return datetime.now(tz=timezone.utc) - timedelta(days=7)

class IntegrationState(pydantic.BaseModel):
    last_run: datetime = pydantic.Field(default_factory=default_last_run, alias='last_run')
    error: str = None

    @pydantic.validator("last_run")
    def clean_last_run(cls, v):
        if v is None:
            return default_last_run()
        if not v.tzinfo:
            return v.replace(tzinfo=timezone.utc)
        return v

async def get_token():
    response = {
        "grant_type": "token",
        "token": "dummy_token",
    }
    return response

async def get_devices(): # reutrn list of strings
    return [{
            "id": "1df7abf4-4315-4874-92c8-7910c498bc5f",
            "external_id": "150711",
            "status": "healthy",
            "provider": {
                "id": "08d231ff-70a2-4802-b447-74a347d6b275",
                "name": "Onyesha TEST [VH]",
                "owner": {
                    "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                    "name": "EarthRanger Team"
                },
                "type": {
                    "id": "9ccf842e-c63b-4625-8225-347024639d0c",
                    "name": "Onyesha",
                    "value": "Onyesha"
                },
                "base_url": "",
                "status": "disabled",
                "status_details": "Integration is disabled"
            },
            "destinations": [
                {
                    "id": "282e46af-4189-4330-94ed-2090a769af3e",
                    "name": "Gundi Dev Site",
                    "owner": {
                        "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                        "name": "EarthRanger Team"
                    },
                    "type": {
                        "id": "7c890e6d-162f-4f01-8fc8-386d5a56a5e5",
                        "name": "Earth Ranger",
                        "value": "earth_ranger"
                    },
                    "base_url": "https://gundi-dev.staging.pamdas.org/",
                    "status": "healthy",
                    "status_details": "No issues detected"
                }
            ],
            "routing_rules": [
                {
                    "id": "4606b5b0-6774-4494-806e-c17a817093cf",
                    "name": "Onyesha TEST Route"
                }
            ],
            "update_frequency": "unknown",
            "last_update": "unknown",
            "created_at": "2024-12-11T09:10:09.075168Z"
        },
        {
            "id": "c5c0b892-3a64-42c0-ad83-81813b455766",
            "external_id": "150713",
            "status": "healthy",
            "provider": {
                "id": "08d231ff-70a2-4802-b447-74a347d6b275",
                "name": "Onyesha TEST [VH]",
                "owner": {
                    "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                    "name": "EarthRanger Team"
                },
                "type": {
                    "id": "9ccf842e-c63b-4625-8225-347024639d0c",
                    "name": "Onyesha",
                    "value": "Onyesha"
                },
                "base_url": "",
                "status": "disabled",
                "status_details": "Integration is disabled"
            },
            "destinations": [
                {
                    "id": "282e46af-4189-4330-94ed-2090a769af3e",
                    "name": "Gundi Dev Site",
                    "owner": {
                        "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                        "name": "EarthRanger Team"
                    },
                    "type": {
                        "id": "7c890e6d-162f-4f01-8fc8-386d5a56a5e5",
                        "name": "Earth Ranger",
                        "value": "earth_ranger"
                    },
                    "base_url": "https://gundi-dev.staging.pamdas.org/",
                    "status": "healthy",
                    "status_details": "No issues detected"
                }
            ],
            "routing_rules": [
                {
                    "id": "4606b5b0-6774-4494-806e-c17a817093cf",
                    "name": "Onyesha TEST Route"
                }
            ],
            "update_frequency": "unknown",
            "last_update": "unknown",
            "created_at": "2024-12-11T09:10:33.356220Z"
        },
        {
            "id": "461a6edd-616d-410b-80b4-6dbd9344194a",
            "external_id": "152770",
            "status": "healthy",
            "provider": {
                "id": "08d231ff-70a2-4802-b447-74a347d6b275",
                "name": "Onyesha TEST [VH]",
                "owner": {
                    "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                    "name": "EarthRanger Team"
                },
                "type": {
                    "id": "9ccf842e-c63b-4625-8225-347024639d0c",
                    "name": "Onyesha",
                    "value": "Onyesha"
                },
                "base_url": "",
                "status": "disabled",
                "status_details": "Integration is disabled"
            },
            "destinations": [
                {
                    "id": "282e46af-4189-4330-94ed-2090a769af3e",
                    "name": "Gundi Dev Site",
                    "owner": {
                        "id": "f5a91774-fe2e-4b92-ad94-6f752bcc1409",
                        "name": "EarthRanger Team"
                    },
                    "type": {
                        "id": "7c890e6d-162f-4f01-8fc8-386d5a56a5e5",
                        "name": "Earth Ranger",
                        "value": "earth_ranger"
                    },
                    "base_url": "https://gundi-dev.staging.pamdas.org/",
                    "status": "healthy",
                    "status_details": "No issues detected"
                }
            ],
            "routing_rules": [
                {
                    "id": "4606b5b0-6774-4494-806e-c17a817093cf",
                    "name": " TEST Route"
                }
            ],
            "update_frequency": "unknown",
            "last_update": "unknown",
            "created_at": "2024-12-11T09:10:43.698599Z"
        }]


async def get_positions():
    return []