[
    {
        "id": "1104a38b.38e51c",
        "type": "tab",
        "label": "Flow 3"
    },
    {
        "id": "4c5a45ce.befadc",
        "type": "inject",
        "z": "1104a38b.38e51c",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 150,
        "y": 160,
        "wires": [
            [
                "f40a1fa.d064fe",
                "d834058e.3f5898"
            ]
        ]
    },
    {
        "id": "f40a1fa.d064fe",
        "type": "function",
        "z": "1104a38b.38e51c",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"h7sAgYWy3nkEheiL\"\n    };\n    msg.payload=\"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 160,
        "wires": [
            [
                "fbfeea75.49ff18"
            ]
        ]
    },
    {
        "id": "d834058e.3f5898",
        "type": "function",
        "z": "1104a38b.38e51c",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"h7sAgYWy3nkEheiL\"\n    };\n    msg.payload=\"Humidity,,40\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 240,
        "wires": [
            [
                "cdb95734.da2a88"
            ]
        ]
    },
    {
        "id": "fbfeea75.49ff18",
        "type": "http request",
        "z": "1104a38b.38e51c",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DC0BCQVV/datapoints.csv",
        "tls": "",
        "x": 550,
        "y": 180,
        "wires": [
            [
                "3ef934c.9d561cc",
                "83ca598f.691338"
            ]
        ]
    },
    {
        "id": "cdb95734.da2a88",
        "type": "http request",
        "z": "1104a38b.38e51c",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DC0BCQVV/datapoints.csv",
        "tls": "",
        "x": 550,
        "y": 240,
        "wires": [
            [
                "83ca598f.691338",
                "3ef934c.9d561cc"
            ]
        ]
    },
    {
        "id": "3ef934c.9d561cc",
        "type": "http response",
        "z": "1104a38b.38e51c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 790,
        "y": 120,
        "wires": []
    },
    {
        "id": "83ca598f.691338",
        "type": "debug",
        "z": "1104a38b.38e51c",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 810,
        "y": 240,
        "wires": []
    }
]
