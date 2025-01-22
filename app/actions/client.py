import logging
import pydantic

from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from app.services.state import IntegrationStateManager

DEFAULT_TIMEOUT = (3.1, 20)
DEFAULT_LOOKBACK_DAYS = 60

logger = logging.getLogger(__name__)
state_manager = IntegrationStateManager()


class OnyeshaDevice(BaseModel):
    nDeviceID: str
    strSpecialID: str
    dtCreated: datetime
    strSatellite: str


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
    return [OnyeshaDevice(nDeviceID = '89222', strSpecialID = '300434066112120', dtCreated = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150167', strSpecialID = '300434063388110', dtCreated = datetime.datetime(2022, 2, 23, 11, 49, 37, 350000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150181', strSpecialID = '300434063383130', dtCreated = datetime.datetime(2023, 1, 3, 16, 15, 31, 783000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150188', strSpecialID = '300434063387100', dtCreated = datetime.datetime(2023, 1, 3, 16, 15, 31, 847000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150705', strSpecialID = '300434066467530', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 307000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150706', strSpecialID = '300434066464540', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 323000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150707', strSpecialID = '300434066461470', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 323000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150708', strSpecialID = '300434066463540', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 340000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150709', strSpecialID = '300434066465530', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 340000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150710', strSpecialID = '300434066465520', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 353000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150711', strSpecialID = '300434066468520', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 370000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150712', strSpecialID = '300434066465560', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 370000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150713', strSpecialID = '300434066462530', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 387000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '150714', strSpecialID = '300434066461530', dtCreated = datetime.datetime(2022, 6, 16, 13, 41, 21, 387000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '152770', strSpecialID = '300434067188300', dtCreated = datetime.datetime(2024, 9, 24, 14, 39, 25, 223000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '152771', strSpecialID = '300434067187300', dtCreated = datetime.datetime(2024, 9, 24, 14, 39, 25, 423000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '152772', strSpecialID = '300434067180330', dtCreated = datetime.datetime(2024, 9, 24, 14, 39, 25, 457000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '155886', strSpecialID = '300434068741530', dtCreated = datetime.datetime(2024, 3, 7, 15, 2, 58, 413000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '155887', strSpecialID = '300434068747510', dtCreated = datetime.datetime(2024, 3, 7, 15, 2, 58, 443000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '155888', strSpecialID = '300434068740530', dtCreated = datetime.datetime(2024, 3, 7, 15, 2, 58, 477000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '155889', strSpecialID = '300434068744540', dtCreated = datetime.datetime(2024, 3, 7, 15, 2, 58, 507000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '155890', strSpecialID = '300434068749510', dtCreated = datetime.datetime(2024, 3, 7, 15, 2, 58, 537000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '156639', strSpecialID = '301434060726110', dtCreated = datetime.datetime(2024, 11, 6, 9, 1, 51, 210000), strSatellite = 'Iridium'),
            OnyeshaDevice(nDeviceID = '156950', strSpecialID = '301434060552790', dtCreated = datetime.datetime(2024, 11, 6, 9, 1, 51, 223000), strSatellite = 'Iridium')]