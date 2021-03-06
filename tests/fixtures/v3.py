"""Define fixtures related to v2 tests."""
import json

import aresponses
import pytest

from ..const import (
    TEST_ACCOUNT_ID,
    TEST_SUBSCRIPTION_ID,
    TEST_SYSTEM_ID,
    TEST_SYSTEM_SERIAL_NO,
    TEST_USER_ID,
)


@pytest.fixture()
def v3_server(
    api_token_json,
    auth_check_json,
    event_loop,
    v3_sensors_json,
    v3_settings_json,
    v3_subscriptions_json,
):
    """Return a ready-to-query mocked v2 server."""
    server = aresponses.ResponsesMockServer(loop=event_loop)
    server.add(
        "api.simplisafe.com",
        "/v1/api/token",
        "post",
        aresponses.Response(text=json.dumps(api_token_json), status=200),
    )
    server.add(
        "api.simplisafe.com",
        "/v1/api/authCheck",
        "get",
        aresponses.Response(text=json.dumps(auth_check_json), status=200),
    )
    server.add(
        "api.simplisafe.com",
        f"/v1/users/{TEST_USER_ID}/subscriptions",
        "get",
        aresponses.Response(text=json.dumps(v3_subscriptions_json), status=200),
    )
    server.add(
        "api.simplisafe.com",
        f"/v1/ss3/subscriptions/{TEST_SUBSCRIPTION_ID}/sensors",
        "get",
        aresponses.Response(text=json.dumps(v3_sensors_json), status=200),
    )
    server.add(
        "api.simplisafe.com",
        f"/v1/ss3/subscriptions/{TEST_SUBSCRIPTION_ID}/settings/pins",
        "get",
        aresponses.Response(text=json.dumps(v3_settings_json), status=200),
    )

    return server


@pytest.fixture()
def v3_sensors_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/sensors response."""
    return {
        "account": TEST_ACCOUNT_ID,
        "success": True,
        "sensors": [
            {
                "type": 5,
                "serial": "825",
                "name": "Fire Door",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 5,
                "serial": "14",
                "name": "Front Door",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 5,
                "serial": "185",
                "name": "Patio Door",
                "setting": {
                    "instantTrigger": True,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 13,
                "serial": "236",
                "name": "Basement",
                "setting": {
                    "alarmVolume": 3,
                    "doorChime": 0,
                    "exitBeeps": 0,
                    "entryBeeps": 2,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 3,
                "serial": "789",
                "name": "Front Door",
                "setting": {"alarm": 1},
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 3,
                "serial": "822",
                "name": "Master BR",
                "setting": {"alarm": 1},
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 1,
                "serial": "972",
                "name": "Kitchen",
                "setting": {"lowPowerMode": False, "alarm": 1},
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 8,
                "serial": "93",
                "name": "Upstairs",
                "setting": {},
                "status": {
                    "test": False,
                    "tamper": False,
                    "malfunction": False,
                    "triggered": False,
                },
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 8,
                "serial": "650",
                "name": "Downstairs",
                "setting": {},
                "status": {
                    "test": False,
                    "tamper": False,
                    "malfunction": False,
                    "triggered": False,
                },
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "491",
                "name": "Basement N",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "280",
                "name": "Mud Counter",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "430",
                "name": "Basement S",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 9,
                "serial": "129",
                "name": "Laundry",
                "setting": {"alarm": 1},
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 9,
                "serial": "975",
                "name": "Basement",
                "setting": {"alarm": 1},
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 9,
                "serial": "382",
                "name": "Fridge",
                "setting": {"alarm": 1},
                "status": {"triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 10,
                "serial": "320",
                "name": "Basement",
                "setting": {"highTemp": 95, "lowTemp": 41, "alarm": 1},
                "status": {"temperature": 67, "triggered": False},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 4,
                "serial": "785",
                "name": "Upstairs",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 0,
                    "home": 0,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 4,
                "serial": "934",
                "name": "Downstairs",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 0,
                    "home": 0,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "634",
                "name": "Landing",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "801",
                "name": "Living Room",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
            {
                "type": 6,
                "serial": "946",
                "name": "Eating Area",
                "setting": {
                    "instantTrigger": False,
                    "away2": 1,
                    "away": 1,
                    "home2": 1,
                    "home": 1,
                    "off": 0,
                },
                "status": {},
                "flags": {
                    "swingerShutdown": False,
                    "lowBattery": False,
                    "offline": False,
                },
            },
        ],
        "lastUpdated": 1534626361,
        "lastSynced": 1534626361,
        "lastStatusUpdate": 1534626358,
    }


@pytest.fixture()
def v3_settings_full_pins_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/settings/pins (full)."""
    return {
        "account": "12345012",
        "settings": {
            "normal": {
                "wifiSSID": "MY_WIFI",
                "alarmDuration": 240,
                "alarmVolume": 3,
                "doorChime": 2,
                "entryDelayAway": 30,
                "entryDelayAway2": 30,
                "entryDelayHome": 30,
                "entryDelayHome2": 30,
                "exitDelayAway": 60,
                "exitDelayAway2": 60,
                "exitDelayHome": 0,
                "exitDelayHome2": 0,
                "lastUpdated": "2019-07-03T03:24:20.999Z",
                "light": True,
                "voicePrompts": 2,
                "_id": "1197192618725121765212",
            },
            "pins": {
                "lastUpdated": "2019-07-04T20:47:44.016Z",
                "_id": "asd6281526381253123",
                "users": [
                    {"_id": "1271279d966212121124c7", "pin": "3456", "name": "Test 1"},
                    {"_id": "1271279d966212121124c6", "pin": "5423", "name": "Test 2"},
                    {"_id": "1271279d966212121124c5", "pin": "1289", "name": "Test 3"},
                    {"_id": "1271279d966212121124c4", "pin": "1099", "name": "Test 4"},
                ],
                "duress": {"pin": "9876"},
                "master": {"pin": "1234"},
            },
        },
        "basestationStatus": {
            "lastUpdated": "2019-07-15T15:28:22.961Z",
            "rfJamming": False,
            "ethernetStatus": 4,
            "gsmRssi": -73,
            "gsmStatus": 3,
            "backupBattery": 5293,
            "wallPower": 5933,
            "wifiRssi": -49,
            "wifiStatus": 1,
            "_id": "6128153715231t237123",
            "encryptionErrors": [],
        },
        "lastUpdated": 1562273264,
    }


@pytest.fixture()
def v3_settings_deleted_pin_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/settings/pins (deleted PIN)."""
    return {
        "account": "12345012",
        "settings": {
            "normal": {
                "wifiSSID": "MY_WIFI",
                "alarmDuration": 240,
                "alarmVolume": 3,
                "doorChime": 2,
                "entryDelayAway": 30,
                "entryDelayAway2": 30,
                "entryDelayHome": 30,
                "entryDelayHome2": 30,
                "exitDelayAway": 60,
                "exitDelayAway2": 60,
                "exitDelayHome": 0,
                "exitDelayHome2": 0,
                "lastUpdated": "2019-07-03T03:24:20.999Z",
                "light": True,
                "voicePrompts": 2,
                "_id": "1197192618725121765212",
            },
            "pins": {
                "lastUpdated": "2019-07-04T20:47:44.016Z",
                "_id": "asd6281526381253123",
                "users": [
                    {"_id": "1271279d966212121124c7", "pin": "3456", "name": "Test 1"},
                    {"_id": "1271279d966212121124c6", "pin": "", "name": ""},
                    {"_id": "1271279d966212121124c5", "pin": "", "name": ""},
                    {"_id": "1271279d966212121124c4", "pin": "", "name": ""},
                ],
                "duress": {"pin": "9876"},
                "master": {"pin": "1234"},
            },
        },
        "basestationStatus": {
            "lastUpdated": "2019-07-15T15:28:22.961Z",
            "rfJamming": False,
            "ethernetStatus": 4,
            "gsmRssi": -73,
            "gsmStatus": 3,
            "backupBattery": 5293,
            "wallPower": 5933,
            "wifiRssi": -49,
            "wifiStatus": 1,
            "_id": "6128153715231t237123",
            "encryptionErrors": [],
        },
        "lastUpdated": 1562273264,
    }


@pytest.fixture()
def v3_settings_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/settings/pins."""
    return {
        "account": "12345012",
        "settings": {
            "normal": {
                "wifiSSID": "MY_WIFI",
                "alarmDuration": 240,
                "alarmVolume": 3,
                "doorChime": 2,
                "entryDelayAway": 30,
                "entryDelayAway2": 30,
                "entryDelayHome": 30,
                "entryDelayHome2": 30,
                "exitDelayAway": 60,
                "exitDelayAway2": 60,
                "exitDelayHome": 0,
                "exitDelayHome2": 0,
                "lastUpdated": "2019-07-03T03:24:20.999Z",
                "light": True,
                "voicePrompts": 2,
                "_id": "1197192618725121765212",
            },
            "pins": {
                "lastUpdated": "2019-07-04T20:47:44.016Z",
                "_id": "asd6281526381253123",
                "users": [
                    {"_id": "1271279d966212121124c7", "pin": "3456", "name": "Test 1"},
                    {"_id": "1271279d966212121124c6", "pin": "5423", "name": "Test 2"},
                    {"_id": "1271279d966212121124c5", "pin": "", "name": ""},
                    {"_id": "1271279d966212121124c4", "pin": "", "name": ""},
                ],
                "duress": {"pin": "9876"},
                "master": {"pin": "1234"},
            },
        },
        "basestationStatus": {
            "lastUpdated": "2019-07-15T15:28:22.961Z",
            "rfJamming": False,
            "ethernetStatus": 4,
            "gsmRssi": -73,
            "gsmStatus": 3,
            "backupBattery": 5293,
            "wallPower": 5933,
            "wifiRssi": -49,
            "wifiStatus": 1,
            "_id": "6128153715231t237123",
            "encryptionErrors": [],
        },
        "lastUpdated": 1562273264,
    }


@pytest.fixture()
def v3_settings_new_pin_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/settings/pins (new pin)."""
    return {
        "account": "12345012",
        "settings": {
            "normal": {
                "wifiSSID": "MY_WIFI",
                "alarmDuration": 240,
                "alarmVolume": 3,
                "doorChime": 2,
                "entryDelayAway": 30,
                "entryDelayAway2": 30,
                "entryDelayHome": 30,
                "entryDelayHome2": 30,
                "exitDelayAway": 60,
                "exitDelayAway2": 60,
                "exitDelayHome": 0,
                "exitDelayHome2": 0,
                "lastUpdated": "2019-07-03T03:24:20.999Z",
                "light": True,
                "voicePrompts": 2,
                "_id": "1197192618725121765212",
            },
            "pins": {
                "lastUpdated": "2019-07-04T20:47:44.016Z",
                "_id": "asd6281526381253123",
                "users": [
                    {"_id": "1271279d966212121124c7", "pin": "3456", "name": "Test 1"},
                    {"_id": "1271279d966212121124c6", "pin": "5423", "name": "Test 2"},
                    {
                        "_id": "1271279d966212121124c5",
                        "pin": "1274",
                        "name": "whatever 3",
                    },
                    {"_id": "1271279d966212121124c4", "pin": "", "name": ""},
                ],
                "duress": {"pin": "9876"},
                "master": {"pin": "1234"},
            },
        },
        "basestationStatus": {
            "lastUpdated": "2019-07-15T15:28:22.961Z",
            "rfJamming": False,
            "ethernetStatus": 4,
            "gsmRssi": -73,
            "gsmStatus": 3,
            "backupBattery": 5293,
            "wallPower": 5933,
            "wifiRssi": -49,
            "wifiStatus": 1,
            "_id": "6128153715231t237123",
            "encryptionErrors": [],
        },
        "lastUpdated": 1562273264,
    }


@pytest.fixture()
def v3_state_away_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/state/away."""
    return {
        "success": True,
        "reason": None,
        "state": "AWAY",
        "lastUpdated": 1534725096,
        "exitDelay": 120,
    }


@pytest.fixture()
def v3_state_home_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/state/home."""
    return {
        "success": True,
        "reason": None,
        "state": "HOME",
        "lastUpdated": 1534725096,
        "exitDelay": 120,
    }


@pytest.fixture()
def v3_state_off_json():
    """Return a /v1/ss3/subscriptions/<SUBSCRIPTION_ID>/state/off."""
    return {
        "success": True,
        "reason": None,
        "state": "OFF",
        "lastUpdated": 1534725096,
        "exitDelay": 120,
    }


@pytest.fixture()
def v3_subscriptions_json():
    """Return a /v1/users/USER_ID/subscriptions response."""
    return {
        "subscriptions": [
            {
                "uid": TEST_USER_ID,
                "sid": TEST_SYSTEM_ID,
                "sStatus": 20,
                "activated": 1445034752,
                "planName": "24/7 Interactive Alarm Monitoring + Alerts",
                "pinUnlocked": True,
                "location": {
                    "sid": TEST_SYSTEM_ID,
                    "uid": TEST_USER_ID,
                    "account": TEST_ACCOUNT_ID,
                    "street1": "1234 Main Street",
                    "street2": "",
                    "locationName": "",
                    "city": "Atlantis",
                    "state": "UW",
                    "zip": "12345",
                    "county": "SEA",
                    "notes": "",
                    "residenceType": 2,
                    "numAdults": 2,
                    "numChildren": 0,
                    "safeWord": "panic",
                    "signature": "John Allen Doe",
                    "timeZone": 2,
                    "primaryContacts": [{"name": "John Doe", "phone": "1234567890"}],
                    "secondaryContacts": [{"name": "Jane Doe", "phone": "9876543210"}],
                    "copsOptIn": False,
                    "smashSafeOptIn": False,
                    "certificateUri": "https://simplisafe.com/account2/12345/alarm-certificate/",
                    "locationOffset": -360,
                    "nestStructureId": "",
                    "system": {
                        "serial": TEST_SYSTEM_SERIAL_NO,
                        "alarmState": "OFF",
                        "alarmStateTimestamp": 0,
                        "isAlarming": False,
                        "version": 3,
                        "temperature": 67,
                        "exitDelayRemaining": 60,
                        "cameras": [],
                        "stateUpdated": 1534625833,
                        "messages": [],
                    },
                },
                "currency": "USD",
                "country": "US",
                "data": "",
                "billDate": 1537187552,
                "features": {
                    "monitoring": True,
                    "alerts": True,
                    "online": True,
                    "hazard": False,
                    "video": False,
                },
                "creditCard": {"type": "Mastercard", "lastFour": "1234"},
                "pinUnlockedBy": "pin",
            }
        ]
    }
