class NodeTemplate:
    def __init__(self, name: str, hints_1: list, hints_2: list) -> None:
        self._name_hint_1 = name # элемент из списка config.HINTS_1
        # Из второго списка берем имя которое соответствует порядковому номеру первого списка
        self.__index = hints_1.index(self._name_hint_1) # порядковый номер
        self._name_hint_2 = hints_2[self.__index] # такой же по счету элемент, как и в 1м списке

        self.set_btn_text = {
                                "id": f"2a90beba.57d{self.__index}",
                                "type": "function",
                                "z": "8389bbf5.5d9f78",
                                "name": "set_btn_text",
                                "func": "var start_flag = global.get('start_flag')||0;\nvar if_lang_code = global.get('if_lang_code')||1;\n\nif (if_lang_code == 1){\n    msg.lang_label = \"set_name\";\n}\nelse{\n    msg.lang_label = \"set_name_FR\";\n}\nreturn msg;".replace('set_name', str(name)),
                                "outputs": 1,
                                "noerr": 0,
                                "x": 150,
                                "y": 380 + 200*self.__index,
                                "wires": []
                            }

        self.main_logo = {
                            "id": f"1db388a.5ab{self.__index}",
                            "type": "ui_button",
                            "z": "8389bbf5.5d9f78",
                            "name": f"{self._name_hint_1}",
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
                            "y": 260 + 200*self.__index,
                            "wires": []
                        }

        # первая строка
        self.hint_btn = {
                            "id": f"cbdcd6f8.4de{self.__index}",
                            "type": "ui_button",
                            "z": "8389bbf5.5d9f78",
                            "name": f"h1_{self._name_hint_1}",
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
                            "y": 240 + 200*self.__index,
                            "wires": []
                        }

        self.link_out = {
                            "id": f"c7ac71ba.89f{self.__index}",
                            "type": "link out",
                            "z": "8389bbf5.5d9f78",
                            "name": "",
                            "links": [
                                "1f1f3cbf.8a3e93"
                            ],
                            "x": 495,
                            "y": 180 + 200*self.__index,
                            "wires": []
                        }

        self.check_lang = {
                            "id": f"9b15f2bf.568{self.__index}",
                            "type": "function",
                            "z": "8389bbf5.5d9f78",
                            "name": "check_lang",
                            "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                            "outputs": 1,
                            "noerr": 0,
                            "x": 650,
                            "y": 240 + 200*self.__index,
                            "wires": []
                        }

        self.delay =  {
                            "id": f"d72833b6.4ec{self.__index}",
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
                            "y": 240 + 200*self.__index,
                            "wires": []
                        }

        self.mp3_win = {
                            "id": f"5f841428.146{self.__index}",
                            "type": "python-function",
                            "z": "8389bbf5.5d9f78",
                            "name": "mp3_win",
                            "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name 1.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(self._name_hint_1)),
                            "outputs": 1,
                            "x": 1040,
                            "y": 240 + 200*self.__index,
                            "wires": []
                        }

        # вторая строка
        self.hint_btn_ = {
                        "id": f"8ea9804f.cb0{self.__index}",
                        "type": "ui_button",
                        "z": "8389bbf5.5d9f78",
                        "name": f"h2_{self._name_hint_2}",
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
                        "y": 280 + 200*self.__index,
                        "wires": []
                    }

        self.link_out_ = {
                        "id": f"e3072c77.851{self.__index}",
                        "type": "link out",
                        "z": "8389bbf5.5d9f78",
                        "name": "",
                        "links": [
                            "1f1f3cbf.8a3e93"
                        ],
                        "x": 495,
                        "y": 340 + 200*self.__index,
                        "wires": []
                    }

        self.check_lang_ = {
                        "id": f"dd1b90ab.92c{self.__index}",
                        "type": "function",
                        "z": "8389bbf5.5d9f78",
                        "name": "check_lang",
                        "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                        "outputs": 1,
                        "noerr": 0,
                        "x": 650,
                        "y": 280 + 200*self.__index,
                        "wires": [
                            [
                                f"dacd4ab0.ca513{self.__index}"
                            ]
                        ]
                    }

        self.delay_ = {
                    "id": f"dacd4ab0.ca5{self.__index}",
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
                    "y": 280 + 200*self.__index,
                    "wires": []
                }

        self.mp3_win_ = {
                        "id": f"92853d2b.154{self.__index}",
                        "type": "python-function",
                        "z": "8389bbf5.5d9f78",
                        "name": "mp3_win",
                        "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name 2.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(self._name_hint_2)),
                        "outputs": 1,
                        "x": 1040,
                        "y": 280 + 200*self.__index,
                        "wires": [
                            []
                        ]
                    }

        # остальные ноды
        self.kill_python3 = {
                            "id": "f68cbe37b16123a",
                            "type": "exec",
                            "z": "27aa475694f99417",
                            "command": "python3 /media/pi/MP3/kill_talk.py",
                            "addpay": True,
                            "append": "",
                            "useSpawn": "false",
                            "timer": "",
                            "oldrc": False,
                            "name": "",
                            "x": 860,
                            "y": 60,
                            "wires": [
                                [],
                                [],
                                []
                            ]
                        }
        
        self.in_kill_python3 = {
                            "id": "ce55df736a4913ab",
                            "type": "link in",
                            "z": "27aa475694f99417",
                            "name": "kill_omx_hint",
                            "links": [],
                            "x": 635,
                            "y": 60,
                            "wires": []
                        }


class Nodes(NodeTemplate):
    def __init__(self, name: str, config) -> None:
        super().__init__(name, config.HINTS_1, config.HINTS_2)
        # self.config = config
        self._btn = None
        self._hints = None
        self._in_kill_python3 = None
        self._kill_python3 = None

        self.nodes_id_in_python_kill = []


    @property
    def btn(self):
        if self._btn == None:
            self.set_btn_text['wires'].append([self.main_logo['id']])
            self._btn = [
                self.set_btn_text,
                self.main_logo,
                ]
        return self._btn

    @property
    def hints(self):
        if self._hints == None:
            first_raw = self._get_first_row_hints_json()
            second_raw = self._get_second_row_hints_json()
        return [*first_raw, *second_raw]

    def _get_first_row_hints_json(self):
        self.hint_btn['wires'].append([self.link_out['id'], self.check_lang['id']])
        self.check_lang['wires'].append([self.delay['id']])
        self.delay['wires'].append([self.mp3_win['id']])

        self.nodes_id_in_python_kill.append(self.link_out['id'])

        return [
            self.hint_btn,
            self.link_out,
            self.check_lang,
            self.delay,
            self.mp3_win,
        ]

    def _get_second_row_hints_json(self):
        self.hint_btn_['wires'].append([self.link_out_['id'], self.check_lang_['id']])
        self.check_lang_['wires'].append([self.delay_['id']])
        self.delay_['wires'].append([self.mp3_win_['id']])

        self.nodes_id_in_python_kill.append(self.link_out_['id'])

        return [
            self.hint_btn_,
            self.link_out_,
            self.check_lang_,
            self.delay_,
            self.mp3_win_,
        ]

    @property
    def input_python_kill(self):
        if self._in_kill_python3 == None:
            self.in_kill_python3['wires'].append([self.kill_python3['id']])
            self._in_kill_python3 = self.in_kill_python3
        return self._in_kill_python3

    @property
    def kill_talk(self):
        if self._kill_python3 == None:
            self._kill_python3 = self.kill_python3
        return self._kill_python3


class ConfigNodes():
    "Конфигурационный объект"
    def __init__(self, config) -> None:
        self._project = None
        self._group = None

        # json для групп и таблиц dashboard
        self._dashboard_tab = {
                "id": f"7fcf911a.2dae34",
                "type": "ui_tab",
                "name": config.DASHBOARD_PROJECT_NAME,
                "icon": "fa-bars",
                "order": 1,
                "disabled": False,
                "hidden": False
            }

        self._dashboard_group = {
                    "id": f"bf9559aa.2dae34",
                    "type": "ui_group",
                    "name": config.DASHBOARD_GROUP_NAME,
                    "tab": None, # меняем значение в @property def group()
                    "order": 3,
                    "disp": True,
                    "width": 8,
                    "collapse": True
                }

        self._kill_python3 = {
                            "id": f"f68cbe37b16932a",
                            "type": "exec",
                            "z": "27aa475694f99417",
                            "command": "python3 /media/pi/MP3/kill_talk.py",
                            "addpay": True,
                            "append": "",
                            "useSpawn": "false",
                            "timer": "",
                            "oldrc": False,
                            "name": "",
                            "x": 860,
                            "y": 60,
                            "wires": [
                                [],
                                [],
                                []
                            ]
                        }
        
        self._in_kill_python3 = {
                            "id": f"ce55df736a4941eab",
                            "type": "link in",
                            "z": "27aa475694f99417",
                            "name": "kill_omx_hint",
                            "links": [],
                            "x": 635,
                            "y": 60,
                            "wires": [
                                [
                                    "f68cbe37b1646f97"
                                ]
                            ]
                        }

    @property
    def project(self):
        if self._project == None:
            self._project = self._dashboard_tab
        return self._project

    @property
    def group(self):
        if self._group == None:
            self._dashboard_group['tab'] = self._dashboard_tab['id']
            self._group = self._dashboard_group
        return self._group