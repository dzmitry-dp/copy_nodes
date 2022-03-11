class NodeTemplate:
    def _link_in(self, __index, x=15, y=380):
        return {
                "id": f"3ca965f.4ce{__index}9a",
                "type": "link in",
                "z": "8389bbf5.5d9f78",
                "name": "",
                "links": [],
                "x": x,
                "y": y + 200*__index,
                "wires": []
            }

    def _set_btn_text(self, __index: int, _name_hint_1):
        return {
                    "id": f"2a90beba.57d{__index}",
                    "type": "function",
                    "z": "8389bbf5.5d9f78",
                    "name": "set_btn_text",
                    "func": "var start_flag = global.get('start_flag')||0;\nvar if_lang_code = global.get('if_lang_code')||1;\n\nif (if_lang_code == 1){\n    msg.lang_label = \"set_name\";\n}\nelse{\n    msg.lang_label = \"set_name_LOC\";\n}\nreturn msg;".replace('set_name', str(' '.join(_name_hint_1.split()[:-1]))),
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

    def _link_out(self, __index, x=495, y=180):
        return {
                        "id": f"c7ac71ba.89f{__index}",
                        "type": "link out",
                        "z": "8389bbf5.5d9f78",
                        "name": "",
                        "links": [],
                        "x": x,
                        "y": y + 200*__index,
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

    def _mp3_win(self, __index, _name_hint_1, language):
        return {
                        "id": f"5f841428.146{__index}",
                        "type": "python-function",
                        "z": "8389bbf5.5d9f78",
                        "name": "mp3_win",
                        "func": f"import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/{language}/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(_name_hint_1)),
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
                    "links": [],
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

    def _mp3_win_(self, __index, _name_hint_2, language):
        return {
                "id": f"92853d2b.154{__index}",
                "type": "python-function",
                "z": "8389bbf5.5d9f78",
                "name": "mp3_win",
                "func": f"import os\nimport sys\nfrom subprocess import Popen\n\ntrack1 = \"/media/pi/MP3/GAME/EN/set_name.mp3\"\ntrack2 = \"/media/pi/MP3/GAME/{language}/set_name.mp3\"\nif msg['lang_code'] == 1:\n    player1 = Popen(['omxplayer', track1])\nif msg['lang_code'] == 2:\n    player1 = Popen(['omxplayer', track2])".replace('set_name', str(_name_hint_2)),
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
    def _inject(self, __index):
        return {
                    "id": f"9c687140.2d{__index}7",
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
                    "y": 820 + 200*__index,
                    "wires": []
                }

    def _random_delay(self, __index):
        return {
                    "id": f"56c91654.ef9{__index}8",
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
                    "y": 820 + 200*__index,
                    "wires": []
                }

    def _mqtt_out(self, __index, client_name):
        return {
                    "id": f"cd6524b7.f117a{__index}",
                    "type": "mqtt out",
                    "z": "f7c5b52b.d0b038",
                    "name": "",
                    "topic": f"/{client_name}_sub",
                    "qos": "0",
                    "retain": "false",
                    "broker": "",
                    "x": 910,
                    "y": 820 + 200*__index,
                    "wires": []
                }

    def _mqtt_in(self, __index, client_name):
        return {
                "id": f"95eb414.1442e{__index}",
                "type": "mqtt in",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "topic": f"/{client_name}_pub",
                "qos": "0",
                "datatype": "auto",
                "broker": "",
                "inputs": 0,
                "x": 340,
                "y": 920 + 200*__index,
                "wires": []
            }

    def _delay_300ms(self, __index):
        return {
                "id": f"d164a84f.5b920{__index}",
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
                "y": 920 + 200*__index,
                "wires": []
            }

    def _check_link(self, __index):
        return {
                "id": f"3b978cd5.fa4c4{__index}",
                "type": "function",
                "z": "f7c5b52b.d0b038",
                "name": "check_link_m",
                "func": "var link_counter_m = flow.get('link_counter_m') || 0;\n\nif(msg.payload == \"30\")\n{\n    link_counter_m = (link_counter_m < 2) ? link_counter_m + 1 : 2;\n}\n\nif(msg.payload == \"31\")\n{\n    link_counter_m = 0;\n}\n\nflow.set('link_counter_m', link_counter_m);\nmsg.link = link_counter_m;\n\nif(link_counter_m <= 1)\n{\n    msg.payload = true;\n    msg.text = \"on-line\";\n    return msg;\n}\nelse\n{\n    msg.payload = false;\n    msg.text = \"off-line\";\n    return msg;\n}\nreturn msg;",
                "outputs": 1,
                "noerr": 0,
                "x": 920,
                "y": 920 + 200*__index,
                "wires": []
            }

    def _link_state(self, __index, client_name, client_lable):
        return {
                "id": f"ad2209c.aa751f{__index}",
                "type": "ui_text",
                "z": "f7c5b52b.d0b038",
                "group": "",
                "order": 2,
                "width": 7,
                "height": 1,
                "name": f"link state: {client_name}({client_lable})",
                "label": "main: ",
                "format": "msg.text",
                "layout": "row-right",
                "x": 1140,
                "y": 900 + 200*__index,
                "wires": []
            }

    def _link_state_swith(self, __index):
        return {
                "id": f"4e867014.108b2{__index}",
                "type": "ui_switch",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "label": "link m",
                "tooltip": "",
                "group": "",
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
                "y": 940 + 200*__index,
                "wires": []
            }

    # lock
    def _main_callback_pub(self):
        return {
                "id": "1fb8c0ec.ce05721",
                "type": "mqtt in",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "topic": "/main_callback_pub",
                "qos": "0",
                "datatype": "auto",
                "broker": "",
                "inputs": 0,
                "x": 350,
                "y": 300,
                "wires": []
            }

    def _lock_swith (self, __index, _label, _on, _off):
        return {
                "id": f"1a60ee47.9453{__index}",
                "type": "ui_switch",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "label": f"{_label.replace('_ON', '').replace('_OFF', '')}",
                "tooltip": "",
                "group": "",
                "order": 4,
                "width": 0,
                "height": 0,
                "passthru": False,
                "decouple": "true",
                "topic": "",
                "style": "",
                "onvalue": f"{_on}",
                "onvalueType": "str",
                "onicon": "fa-lock fa-2x",
                "oncolor": "olivedrab",
                "offvalue": f"{_off}",
                "offvalueType": "str",
                "officon": "fa-unlock fa-2x",
                "offcolor": "orangered",
                "x": 700,
                "y": 60 + 50*__index,
                "wires": []
            }

    def _main_sub(self):
        return {
                "id": "fdb4fb1b.238cc81",
                "type": "mqtt out",
                "z": "f7c5b52b.d0b038",
                "name": "",
                "topic": "/main_sub",
                "qos": "0",
                "retain": "false",
                "broker": "",
                "x": 1200,
                "y": 300,
                "wires": []
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

    def _mqtt_broker(self):
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