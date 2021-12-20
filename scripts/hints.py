from scripts.template import NodeTemplate


class Hints(NodeTemplate):
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
