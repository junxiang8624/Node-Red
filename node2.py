[
    {
        "id": "63544989.8907b8",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "acb6e3be.0bc5a",
        "type": "inject",
        "z": "63544989.8907b8",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 124,
        "y": 163,
        "wires": [
            [
                "4aefaee9.78312",
                "93b130ab.2b504"
            ]
        ]
    },
    {
        "id": "4aefaee9.78312",
        "type": "function",
        "z": "63544989.8907b8",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"h7sAgYWy3nkEheiL\"\n    };\n    msg.payload=\"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 321,
        "y": 187,
        "wires": [
            [
                "dec7345.ca798c8"
            ]
        ]
    },
    {
        "id": "93b130ab.2b504",
        "type": "function",
        "z": "63544989.8907b8",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"h7sAgYWy3nkEheiL\"\n    };\n    msg.payload=\"Humidity,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 240,
        "wires": [
            [
                "a055f6b1.416228"
            ]
        ]
    },
    {
        "id": "dec7345.ca798c8",
        "type": "http request",
        "z": "63544989.8907b8",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DC0BCQVV/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 490,
        "y": 180,
        "wires": [
            [
                "635e7533.31761c",
                "d532845a.138378"
            ]
        ]
    },
    {
        "id": "a055f6b1.416228",
        "type": "http request",
        "z": "63544989.8907b8",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DC0BCQVV/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 490,
        "y": 240,
        "wires": [
            [
                "635e7533.31761c",
                "d532845a.138378"
            ]
        ]
    },
    {
        "id": "635e7533.31761c",
        "type": "http response",
        "z": "63544989.8907b8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 662,
        "y": 183,
        "wires": []
    },
    {
        "id": "d532845a.138378",
        "type": "debug",
        "z": "63544989.8907b8",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 730,
        "y": 340,
        "wires": []
    }
]
