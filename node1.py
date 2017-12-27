[
    {
        "id": "2a386acb.26e4d6",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "a6840fde.90f63",
        "type": "rpi-gpio in",
        "z": "2a386acb.26e4d6",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 110,
        "y": 340,
        "wires": [
            [
                "ea402485.7fb3a8"
            ]
        ]
    },
    {
        "id": "cda87a9b.6935c8",
        "type": "debug",
        "z": "2a386acb.26e4d6",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 670,
        "y": 240,
        "wires": []
    },
    {
        "id": "8b312441.35d6c8",
        "type": "change",
        "z": "2a386acb.26e4d6",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 430,
        "y": 400,
        "wires": [
            [
                "90bd20b1.151ca",
                "cda87a9b.6935c8"
            ]
        ]
    },
    {
        "id": "afb5fe64.5a97e",
        "type": "change",
        "z": "2a386acb.26e4d6",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 430,
        "y": 460,
        "wires": [
            [
                "90bd20b1.151ca",
                "cda87a9b.6935c8"
            ]
        ]
    },
    {
        "id": "ea402485.7fb3a8",
        "type": "switch",
        "z": "2a386acb.26e4d6",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 250,
        "y": 400,
        "wires": [
            [
                "8b312441.35d6c8"
            ],
            [
                "afb5fe64.5a97e"
            ]
        ]
    },
    {
        "id": "90bd20b1.151ca",
        "type": "rpi-gpio out",
        "z": "2a386acb.26e4d6",
        "name": "LED",
        "pin": "11",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 650,
        "y": 380,
        "wires": []
    }
]
