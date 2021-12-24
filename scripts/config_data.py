class Command:
    def __init__(self, txt_file) -> None:
        self.lines = txt_file.readlines() # список линий текста в config.txt
        # список индексов из списка, где элемент равен '###\n'
        self.index_list = self._return_index_from_list()

        # self.project = None
        # self.group = None
        self.hints_1 = []
        self.hints_2 = []
        self.mqtt_name = None
        self.mqtt_clients = {}
        self.comands = {}

        for i in self.index_list:
            if i > 0: # не смотрим первую строку конфига.txt
                command_line = self.lines[self.index_list[self.index_list.index(i)-1]:i]

                # if 'Project name\n' in command_line:
                #     self.project = self._clear(self.lines[self.i:self.index_list[self.index_list.index(self.i)+1]])[0].replace('\n', '')

                # if 'Group\n' in command_line:
                #     self.group = self._clear(self.lines[i:self.index_list[self.index_list.index(i)+1]])[0].replace('\n', '')
                
                if 'Hints\n' in command_line:
                    hints_list = self._clear(self.lines[i:self.index_list[self.index_list.index(i)+1]])
                    for item in hints_list[::2]:
                        self.hints_1.append(item.replace('\n', ''))

                    for item in hints_list[1::2]:
                        self.hints_2.append(item.replace('\n', ''))

                if 'MQTT_NAME\n' in command_line:
                    mqtt_name = self._clear(self.lines[i:self.index_list[self.index_list.index(i)+1]])
                    self.mqtt_name = mqtt_name[0].replace('\n', '')

                if 'MQTT_CLIENT\n' in command_line:
                    clients_list = self._clear(self.lines[i:self.index_list[self.index_list.index(i)+1]])
                    for client in clients_list:
                        r = client.replace('\n', '').split(';')
                        self.mqtt_clients[r[0]] = r[1]

                if 'COMMANDS\n' in command_line:
                    commands_list = self._clear(self.lines[i:self.index_list[self.index_list.index(i)+1]])
                    for command in commands_list:
                        if command != '\n':
                            r = command.replace('#define ', '').replace(' ', '').replace('\t', '').replace('\n', '')

                            name = r[:-3].replace('_ON', '').replace('_OFF', '')
                            if self.comands.get(name, 'new') == 'new':
                                self.comands[name] = {}

                            if r[:-3][-3:] == '_ON':
                                self.comands[name.replace('_ON', '')]['ON'] = r[-3:]

                            if r[:-3][-3:] == 'OFF':
                                self.comands[name.replace('_OFF', '')]['OFF'] = r[-3:]
                                
                        
    def _return_index_from_list(self):
        "Возвращаю список индексов где строки равны '###\\n' из списка lines"
        idx = []
        for i, line in enumerate(self.lines):
            if line == '###\n':
                idx.append(i)
        return idx

    def _clear(self, line: list):
        if '###\n' in line:
            line.remove('###\n')

        if '\n' in line:
            line.remove('\n')

        return line
