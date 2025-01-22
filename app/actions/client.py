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
    return [OnyeshaDevice(lati = '89222', strSpecialID = '300434066112120', dtCreated = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), strSatellite = 'Iridium'),
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


async def get_positions():
    return [OnyeshaPosition(Latitude = '-22.688246', Longitude = '-72.432657', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '156950'),
            OnyeshaPosition(Latitude = '-11.553351', Longitude = '-22.765566', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '156639'),
            OnyeshaPosition(Latitude = '-51.445334', Longitude = '-34.667656', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '155890'),
            OnyeshaPosition(Latitude = '-54.688246', Longitude = '-54.704450', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '155886'),
            OnyeshaPosition(Latitude = '-14.543344', Longitude = '-45.321678', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '152770'),
            OnyeshaPosition(Latitude = '-61.123322', Longitude = '-72.645234', RecDateTime = datetime.datetime(2023, 1, 3, 16, 5, 56, 120000), DeviceID = '152771'),
            OnyeshaPosition(Latitude = '-11.543345', Longitude = '-77.123986', RecDateTime = datetime.datetime(2024, 11, 6, 9, 1, 51, 223000), DeviceID = '152772')]