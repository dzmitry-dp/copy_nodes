import config

class Node_Template:
    def __init__(self, name: str, meter: int) -> None:
        self.meter = meter
        self.set_btn_text = {
                                "id": f"2a90beba.57d05{self.meter}",
                                "type": "function",
                                "z": "8389bbf5.5d9f78",
                                "name": "set_btn_text",
                                "func": "var start_flag = global.get('start_flag')||0;\nvar if_lang_code = global.get('if_lang_code')||1;\n\nif (if_lang_code == 1){\n    msg.lang_label = \"set_name\";\n}\nelse{\n    msg.lang_label = \"set_name_FR\";\n}\nreturn msg;".replace('set_name', str(name)),
                                "outputs": 1,
                                "noerr": 0,
                                "x": 150,
                                "y": 380 + 200*self.meter,
                                "wires": [
                                    [
                                        f"1db388a.5abe07{self.meter}"
                                    ]
                                ]
                            }

        self.main_logo = {
                            "id": f"1db388a.5abe07{self.meter}",
                            "type": "ui_button",
                            "z": "8389bbf5.5d9f78",
                            "name": f"{name}",
                            "group": "bf9559aa.54ab88",
                            "order": 3,
                            "width": 6,
                            "height": 1,
                            "passthru": False,
                            "label": "{{msg.lang_label}}",
                            "tooltip": "",
                            "color": "silver",
                            "bgcolor": "",
                            "icon": "",
                            "payload": "",
                            "payloadType": "str",
                            "topic": "",
                            "x": 160,
                            "y": 260 + 200*self.meter,
                            "wires": [
                                []
                            ]
                        }

        # первая строка
        self.hint_btn = {
                            "id": f"cbdcd6f8.4de79{self.meter}",
                            "type": "ui_button",
                            "z": "8389bbf5.5d9f78",
                            "name": f"h1_{name}",
                            "group": "bf9559aa.54ab88",
                            "order": 1,
                            "width": 1,
                            "height": 1,
                            "passthru": False,
                            "label": "",
                            "tooltip": "",
                            "color": "silver",
                            "bgcolor": "",
                            "icon": "fa-comment-o fa-2x",
                            "payload": "true",
                            "payloadType": "bool",
                            "topic": "",
                            "x": 380,
                            "y": 240 + 200*self.meter,
                            "wires": [
                                [
                                    f"9b15f2bf.5680{self.meter}",
                                    f"c7ac71ba.89f9{self.meter}"
                                ]
                            ]
                        }

        self.link_out = {
                            "id": f"c7ac71ba.89f9{self.meter}",
                            "type": "link out",
                            "z": "8389bbf5.5d9f78",
                            "name": "",
                            "links": [
                                "1f1f3cbf.8a3e93"
                            ],
                            "x": 495,
                            "y": 180 + 200*self.meter,
                            "wires": []
                        }

        self.check_lang = {
                            "id": f"9b15f2bf.5680{self.meter}",
                            "type": "function",
                            "z": "8389bbf5.5d9f78",
                            "name": "check_lang",
                            "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                            "outputs": 1,
                            "noerr": 0,
                            "x": 650,
                            "y": 240 + 200*self.meter,
                            "wires": [
                                [
                                    f"d72833b6.4ec5{self.meter}"
                                ]
                            ]
                        }

        self.delay =  {
                            "id": f"d72833b6.4ec5{self.meter}",
                            "type": "delay",
                            "z": "8389bbf5.5d9f78",
                            "name": "",
                            "pauseType": "delay",
                            "timeout": "500",
                            "timeoutUnits": "milliseconds",
                            "rate": "1",
                            "nbRateUnits": "1",
                            "rateUnits": "second",
                            "randomFirst": "1",
                            "randomLast": "5",
                            "randomUnits": "seconds",
                            "drop": False,
                            "x": 850,
                            "y": 240 + 200*self.meter,
                            "wires": [
                                [
                                    f"5f841428.1461e{self.meter}"
                                ]
                            ]
                        }

        self.mp3_win = {
                            "id": f"5f841428.1461e{self.meter}",
                            "type": "python-function",
                            "z": "8389bbf5.5d9f78",
                            "name": "mp3_win",
                            "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name 1.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name 1.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(name)),
                            "outputs": 1,
                            "x": 1040,
                            "y": 280 + 200*self.meter,
                            "wires": [
                                []
                            ]
                        }

        # вторая строка
        self.hint_btn_ = {
                        "id": f"8ea9804f.cb00{self.meter}",
                        "type": "ui_button",
                        "z": "8389bbf5.5d9f78",
                        "name": f"h2_{name}",
                        "group": "bf9559aa.54ab88",
                        "order": 2,
                        "width": 1,
                        "height": 1,
                        "passthru": False,
                        "label": "",
                        "tooltip": "",
                        "color": "silver",
                        "bgcolor": "",
                        "icon": "fa-commenting-o fa-2x",
                        "payload": "true",
                        "payloadType": "bool",
                        "topic": "",
                        "x": 380,
                        "y": 280 + 200*self.meter,
                        "wires": [
                            [
                                f"dd1b90ab.92cb{self.meter}",
                                f"e3072c77.8513{self.meter}"
                            ]
                        ]
                    }

        self.link_out_ = {
                        "id": f"e3072c77.8513{self.meter}",
                        "type": "link out",
                        "z": "8389bbf5.5d9f78",
                        "name": "",
                        "links": [
                            "1f1f3cbf.8a3e93"
                        ],
                        "x": 495,
                        "y": 340 + 200*self.meter,
                        "wires": []
                    }

        self.check_lang_ = {
                        "id": f"dd1b90ab.92cb{self.meter}",
                        "type": "function",
                        "z": "8389bbf5.5d9f78",
                        "name": "check_lang",
                        "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                        "outputs": 1,
                        "noerr": 0,
                        "x": 650,
                        "y": 280 + 200*self.meter,
                        "wires": [
                            [
                                f"dacd4ab0.ca513{self.meter}"
                            ]
                        ]
                    }

        self.delay_ = {
                    "id": f"dacd4ab0.ca513{self.meter}",
                    "type": "delay",
                    "z": "8389bbf5.5d9f78",
                    "name": "",
                    "pauseType": "delay",
                    "timeout": "500",
                    "timeoutUnits": "milliseconds",
                    "rate": "1",
                    "nbRateUnits": "1",
                    "rateUnits": "second",
                    "randomFirst": "1",
                    "randomLast": "5",
                    "randomUnits": "seconds",
                    "drop": False,
                    "x": 850,
                    "y": 280 + 200*self.meter,
                    "wires": [
                        [
                            f"92853d2b.1544{self.meter}"
                        ]
                    ]
                }

        self.mp3_win_ = {
                        "id": f"92853d2b.1544{self.meter}",
                        "type": "python-function",
                        "z": "8389bbf5.5d9f78",
                        "name": "mp3_win",
                        "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name 2.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name 2.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(name)),
                        "outputs": 1,
                        "x": 1040,
                        "y": 280 + 200*self.meter,
                        "wires": [
                            []
                        ]
                    }

        # json для групп и таблиц dashboard
        self.group = {
                    "id": "bf9559aa.54ab88",
                    "type": "ui_group",
                    "name": config.DASHBOARD_GROUP_NAME,
                    "tab": "7fcf911a.2daa8",
                    "order": 3,
                    "disp": True,
                    "width": 8,
                    "collapse": True
                }
        
        self.tab = {
                "id": "7fcf911a.2daa8",
                "type": "ui_tab",
                "name": config.DASHBOARD_TAB_NAME,
                "icon": "fa-bars",
                "order": 1,
                "disabled": False,
                "hidden": False
            }

class Node(Node_Template):
    def __init__(self, name, meter) -> None:
        super().__init__(name, meter)
        self._hints = None

    @property
    def hints(self):
        if self._hints == None:
            self._hints = self._get_hints_json()
        return self._hints

    def _get_hints_json(self):
        return [
            self.set_btn_text, 
            self.main_logo,
            self.hint_btn,
            self.link_out,
            self.check_lang,
            self.delay,
            self.mp3_win,
            self.hint_btn_,
            self.link_out_,
            self.check_lang_,
            self.delay_,
            self.mp3_win_,
        ]
