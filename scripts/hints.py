from scripts.template import NodeTemplate


class Hints(NodeTemplate):
    def __init__(self, name: str, config) -> None:
        super().__init__()

        self._name_hint_1 = name # элемент из списка config.HINTS_1
        # Из второго списка берем имя которое соответствует порядковому номеру первого списка
        self.__index = config.HINTS_1.index(self._name_hint_1) # порядковый номер
        self._name_hint_2 = config.HINTS_2[self.__index] # такой же по счету элемент, как и в 1м списке

        self._inpt_node = None
        self._btn = None
        self._hints = None
        self._in_kill_python3 = None
        self._kill_python3 = None

        self.nodes_id_in_python_kill = [] # ноды которые будут ссылаться на input ноду на python скрипт
        self.nodes_id_set_btn_text = [] # id нод на который заходит input

    @property
    def inpt_node(self):
        if self._inpt_node is None:
            _link_in = self._link_in(0) # т.к. нода должна быть одна, то даю произвольный idx=0
            self._inpt_node = _link_in
        return self._inpt_node

    @property
    def btn(self):
        if self._btn == None:
            # _link_in = self._link_in(self.__index)
            set_btn_text = self._set_btn_text(self.__index, self._name_hint_1)
            self.nodes_id_set_btn_text.append(set_btn_text['id'])
            main_logo = self._main_logo(self.__index, self._name_hint_1)
            set_btn_text['wires'].append([main_logo['id']])
            self._btn = [
                # _link_in,
                set_btn_text,
                main_logo,
                ]
        return self._btn

    @property
    def hints(self):
        if self._hints == None:
            first_raw = self._get_first_row_hints_json(self.__index, self._name_hint_1)
            second_raw = self._get_second_row_hints_json(self.__index, self._name_hint_2)
        return [*first_raw, *second_raw]

    def _get_first_row_hints_json(self, __index, hint_name):
        hint_btn = self._hint_btn(__index, hint_name)
        link_out = self._link_out(__index)
        check_lang = self._check_lang(__index)
        delay = self._delay(__index)
        mp3_win = self._mp3_win(__index, hint_name)

        hint_btn['wires'].append([link_out['id'], check_lang['id']])
        check_lang['wires'].append([delay['id']])
        delay['wires'].append([mp3_win['id']])

        self.nodes_id_in_python_kill.append(link_out['id'])

        return [
            hint_btn,
            link_out,
            check_lang,
            delay,
            mp3_win,
        ]

    def _get_second_row_hints_json(self, __index, hint_name):
        hint_btn = self._hint_btn_(__index, hint_name)
        link_out = self._link_out_(__index)
        check_lang = self._check_lang_(__index)
        delay = self._delay_(__index)
        mp3_win = self._mp3_win_(__index, hint_name)

        hint_btn['wires'].append([link_out['id'], check_lang['id']])
        check_lang['wires'].append([delay['id']])
        delay['wires'].append([mp3_win['id']])

        self.nodes_id_in_python_kill.append(link_out['id'])

        return [
            hint_btn,
            link_out,
            check_lang,
            delay,
            mp3_win,
        ]
    
    @property
    def input_python_kill(self):
        if self._in_kill_python3 == None:
            self._in_kill_python3 = self._in_kill_python3_()
            kill_python3 = self._kill_python3_()
            self._in_kill_python3['wires'].append([kill_python3['id']])
        return self._in_kill_python3

    @property
    def kill_talk(self):
        if self._kill_python3 == None:
            self._kill_python3 = self._kill_python3_()
        return self._kill_python3
