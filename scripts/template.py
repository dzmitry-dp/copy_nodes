class NodeTemplate:
    def _set_btn_text(self, __index: int, _name_hint_1):
        return {
                    "id": f"2a90beba.57d{__index}",
                    "type": "function",
                    "z": "8389bbf5.5d9f78",
                    "name": "set_btn_text",
                    "func": "var start_flag = global.get('start_flag')||0;\nvar if_lang_code = global.get('if_lang_code')||1;\n\nif (if_lang_code == 1){\n    msg.lang_label = \"set_name\";\n}\nelse{\n    msg.lang_label = \"set_name_FR\";\n}\nreturn msg;".replace('set_name', str(_name_hint_1)),
                    "outputs": 1,
                    "noerr": 0,
                    "x": 150,
                    "y": 380 + 200*__index,
                    "wires": []
                }

    def _main_logo (self, __index, _name_hint_1):
        return {
                    "id": f"1db388a.5ab{__index}",
                    "type": "ui_button",
                    "z": "8389bbf5.5d9f78",
                    "name": f"{_name_hint_1.replace(' 1', '')}",
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
                    "y": 260 + 200*__index,
                    "wires": []
                }

    # первая строка
    def _hint_btn(self, __index, _name_hint_1):
        return {
                        "id": f"cbdcd6f8.4de{__index}",
                        "type": "ui_button",
                        "z": "8389bbf5.5d9f78",
                        "name": f"h1_{_name_hint_1}",
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
                        "y": 240 + 200*__index,
                        "wires": []
                    }

    def _link_out(self, __index):
        return {
                        "id": f"c7ac71ba.89f{__index}",
                        "type": "link out",
                        "z": "8389bbf5.5d9f78",
                        "name": "",
                        "links": [
                            "1f1f3cbf.8a3e93"
                        ],
                        "x": 495,
                        "y": 180 + 200*__index,
                        "wires": []
                    }

    def _check_lang(self, __index):
        return {
                        "id": f"9b15f2bf.568{__index}",
                        "type": "function",
                        "z": "8389bbf5.5d9f78",
                        "name": "check_lang",
                        "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                        "outputs": 1,
                        "noerr": 0,
                        "x": 650,
                        "y": 240 + 200*__index,
                        "wires": []
                    }

    def _delay(self, __index):
        return  {
                        "id": f"d72833b6.4ec{__index}",
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
                        "y": 240 + 200*__index,
                        "wires": []
                    }

    def _mp3_win(self, __index, _name_hint_1):
        return {
                        "id": f"5f841428.146{__index}",
                        "type": "python-function",
                        "z": "8389bbf5.5d9f78",
                        "name": "mp3_win",
                        "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(_name_hint_1)),
                        "outputs": 1,
                        "x": 1040,
                        "y": 240 + 200*__index,
                        "wires": []
                    }

        # вторая строка
    
    def _hint_btn_(self, __index, _name_hint_2):
        return {
                    "id": f"8ea9804f.cb0{__index}",
                    "type": "ui_button",
                    "z": "8389bbf5.5d9f78",
                    "name": f"h2_{_name_hint_2}",
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
                    "y": 280 + 200*__index,
                    "wires": []
                }

    def _link_out_(self, __index):
        return {
                    "id": f"e3072c77.851{__index}",
                    "type": "link out",
                    "z": "8389bbf5.5d9f78",
                    "name": "",
                    "links": [
                        "1f1f3cbf.8a3e93"
                    ],
                    "x": 495,
                    "y": 340 + 200*__index,
                    "wires": []
                }

    def _check_lang_(self, __index):
        return {
                    "id": f"dd1b90ab.92c{__index}",
                    "type": "function",
                    "z": "8389bbf5.5d9f78",
                    "name": "check_lang",
                    "func": "var lang_code = global.get('lang_code');\nmsg.lang_code = lang_code;\nreturn msg;",
                    "outputs": 1,
                    "noerr": 0,
                    "x": 650,
                    "y": 280 + 200*__index,
                    "wires": []
                }

    def _delay_(self, __index):
        return {
                "id": f"dacd4ab0.ca5{__index}",
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
                "y": 280 + 200*__index,
                "wires": []
            }

    def _mp3_win_(self, __index, _name_hint_2):
        return {
                "id": f"92853d2b.154{__index}",
                "type": "python-function",
                "z": "8389bbf5.5d9f78",
                "name": "mp3_win",
                "func": "import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/FR/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(_name_hint_2)),
                "outputs": 1,
                "x": 1040,
                "y": 280 + 200*__index,
                "wires": [
                    []
                ]
            }

        # остальные ноды
    
    def _kill_python3_(self):
        return {
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
        
    def _in_kill_python3_(self):
        return {
                "id": "ce55df736a4913ab",
                "type": "link in",
                "z": "27aa475694f99417",
                "name": "kill_omx_hint",
                "links": [],
                "x": 635,
                "y": 60,
                "wires": []
            }

    #debug console
    
    def _inject(self):
        return {
                    "id": "9c687140.2d607",
                    "type": "inject",
                    "z": "f7c5b52b.d0b038",
                    "name": "",
                    "repeat": "5",
                    "crontab": "",
                    "once": True,
                    "onceDelay": "3.5",
                    "topic": "",
                    "payload": "30",
                    "payloadType": "str",
                    "x": 350,
                    "y": 1120,
                    "wires": [
                        [
                            "56c91654.ef91c8"
                        ]
                    ]
                }

    def _random_delay(self):
        return {
                    "id": "56c91654.ef91c8",
                    "type": "delay",
                    "z": "f7c5b52b.d0b038",
                    "name": "",
                    "pauseType": "random",
                    "timeout": "300",
                    "timeoutUnits": "milliseconds",
                    "rate": "1",
                    "nbRateUnits": "1",
                    "rateUnits": "second",
                    "randomFirst": "300",
                    "randomLast": "700",
                    "randomUnits": "milliseconds",
                    "drop": False,
                    "outputs": 1,
                    "x": 600,
                    "y": 1120,
                    "wires": [
                        [
                            "cd6524b7.f117a8",
                            "3b978cd5.fa4c44"
                        ]
                    ]
                }

    def _mqtt_out(self):
        return {
                    "id": "cd6524b7.f117a8",
                    "type": "mqtt out",
                    "z": "f7c5b52b.d0b038",
                    "name": "",
                    "topic": "/main_sub",
                    "qos": "0",
                    "retain": "false",
                    "broker": "d8344fb8.abc2d",
                    "x": 910,
                    "y": 1120,
                    "wires": []
                }

    def _mqtt_in(self):
        return {
                "id": "95eb414.1442ec",
                "type": "mqtt in",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "topic": "/main_pub",
                "qos": "0",
                "datatype": "auto",
                "broker": "d8344fb8.abc2d",
                "inputs": 0,
                "x": 340,
                "y": 1220,
                "wires": [
                    [
                        "d164a84f.5b9208"
                    ]
                ]
            }

    def _delay_300ms(self):
        return {
                "id": "d164a84f.5b9208",
                "type": "delay",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "pauseType": "delay",
                "timeout": "300",
                "timeoutUnits": "milliseconds",
                "rate": "1",
                "nbRateUnits": "1",
                "rateUnits": "second",
                "randomFirst": "1",
                "randomLast": "5",
                "randomUnits": "seconds",
                "drop": False,
                "outputs": 1,
                "x": 690,
                "y": 1220,
                "wires": [
                    [
                        "3b978cd5.fa4c44"
                    ]
                ]
            }

    def _check_link(self):
        return {
                "id": "3b978cd5.fa4c44",
                "type": "function",
                "z": "f7c5b52b.d0b038",
                "name": "check_link_m",
                "func": "var link_counter_m = flow.get('link_counter_m') || 0;\n\nif(msg.payload == \"30\")\n{\n    link_counter_m = (link_counter_m < 2) ? link_counter_m + 1 : 2;\n}\n\nif(msg.payload == \"31\")\n{\n    link_counter_m = 0;\n}\n\nflow.set('link_counter_m', link_counter_m);\nmsg.link = link_counter_m;\n\nif(link_counter_m <= 1)\n{\n    msg.payload = true;\n    msg.text = \"on-line\";\n    return msg;\n}\nelse\n{\n    msg.payload = false;\n    msg.text = \"off-line\";\n    return msg;\n}\nreturn msg;",
                "outputs": 1,
                "noerr": 0,
                "x": 920,
                "y": 1220,
                "wires": [
                    [
                        "ad2209c.aa751f8",
                        "4e867014.108b2",
                        "ce8f75e1.1addc8"
                    ]
                ]
            }

    def _link_state(self):
        return {
                "id": "ad2209c.aa751f8",
                "type": "ui_text",
                "z": "f7c5b52b.d0b038",
                "group": "e6f2d0f6.b5846",
                "order": 2,
                "width": 7,
                "height": 1,
                "name": "link state main",
                "label": "main: ",
                "format": "msg.text",
                "layout": "row-right",
                "x": 1140,
                "y": 1200,
                "wires": []
            }

    def _swith(self):
        return {
                "id": "4e867014.108b2",
                "type": "ui_switch",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "label": "link m",
                "tooltip": "",
                "group": "e6f2d0f6.b5846",
                "order": 3,
                "width": 1,
                "height": 1,
                "passthru": False,
                "decouple": "true",
                "topic": "",
                "style": "",
                "onvalue": "true",
                "onvalueType": "bool",
                "onicon": "fa-link fa-2x",
                "oncolor": "olivedrab",
                "offvalue": "false",
                "offvalueType": "bool",
                "officon": "fa-unlink fa-2x",
                "offcolor": "orangered",
                "x": 1110,
                "y": 1240,
                "wires": [
                    []
                ]
            }
 

class ConfigNodes:
    "Конфигурационный объект"
        # json для групп и таблиц dashboard
    def _dashboard_tab(self):
        return {
            "id": f"7fcf911a.2dae34",
            "type": "ui_tab",
            "name": '',
            "icon": "fa-bars",
            "order": 1,
            "disabled": False,
            "hidden": False
        }

    def _dashboard_group(self):
        return {
                "id": f"bf9559aa.2dae34",
                "type": "ui_group",
                "name": '',
                "tab": None, # меняем значение в @property def group()
                "order": 3,
                "disp": True,
                "width": 8,
                "collapse": True
            }

    def _mqtt_global(self):
        return {
                "id": "d8344fb8.abc2d",
                "type": "mqtt-broker",
                "name": "",
                "broker": "192.168.0.70",
                "port": "1883",
                "clientid": "web_ui_butcher",
                "usetls": False,
                "compatmode": False,
                "keepalive": "60",
                "cleansession": True,
                "birthTopic": "",
                "birthQos": "0",
                "birthPayload": "",
                "closeTopic": "",
                "closeQos": "0",
                "closePayload": "",
                "willTopic": "",
                "willQos": "0",
                "willPayload": ""
            }