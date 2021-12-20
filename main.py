import json


def get_json_data(config):
    # print('Project:', config.DASHBOARD_PROJECT_NAME)
    # print('Group:', config.DASHBOARD_GROUP_NAME)
    # print('Hints_1', config.HINTS_1)
    # print('Hints_2', config.HINTS_2)

    "В результате работы этой функции получаю json, который  могу импортировать в node-red"

    from scripts.template import Nodes#, ConfigNodes
        
    result_nodes_json_list = []
    id_list = [] # список id нод link out, которые пойдут на ноду "python3 /media/pi/MP3/kill_talk.py"

    for hint in config.HINTS_1:
        nodes = Nodes(name=hint, config=config)
        _json_list = [
            *nodes.btn,
            *nodes.hints,
        ]
        # повторяемые объекты потока добавляем в общий список
        result_nodes_json_list.append(_json_list)
        # добавляем id в общий список тех кто ссылается на вход input ноды
        id_list.append(nodes.nodes_id_in_python_kill)

    def format_result_list(list_in_list) -> list:
        result_list = []
        for _list in list_in_list:
            for item in _list:
                result_list.append(item)
        return result_list

    # подготавливаем данные для записи в файл. Распаковываем списки
    json_data_in_file = format_result_list(result_nodes_json_list)

    # специально для потока hints
    # форматируем список списков и для списка id
    id_in_python_kill = format_result_list(id_list)
    nodes.input_python_kill['links'] = id_in_python_kill # записываю все id нод, которые ссылаются на input ноду, которая стартует код python3 
    json_data_in_file.append(nodes.input_python_kill)
    json_data_in_file.append(nodes.kill_talk)
    
    # добавляем ноды с настройками проекта
    # node_red_configurations_in_json = ConfigNodes(config=config)
    # json_data_in_file.append(node_red_configurations_in_json.project)
    # json_data_in_file.append(node_red_configurations_in_json.group)

    return json_data_in_file

def get_data_from_config_txt():
    from scripts.comands import Command

    with open('config.txt', 'r') as file:
        cmd_obj = Command(file)
        return cmd_obj

        # lines = file.readlines() # список линий текста в config.txt

        # def return_index_from_list():
        #     "Возвращаю список индексов где строки равны '###\\n' из списка lines"
        #     idx = []
        #     for i, line in enumerate(lines):
        #         if line == '###\n':
        #             idx.append(i)
        #     return idx

        # index_list = return_index_from_list() # список индексов из списка, где элемент равен '###\n'
        
        # for i in index_list:
        #     if i > 0: # не смотрим первую строку конфига.txt
        #         command_line = lines[index_list[index_list.index(i)-1]:i]
        #         comand_obj = Command(i, lines, index_list, command_line)
        #         return comand_obj

# формируем точку входа
if __name__ == "__main__":
    import scripts.cnf as cnf

    with open('generated_flow.json', 'w') as write_file:
        if cnf.HINTS_1 != []:
            json_data_in_file = get_json_data(config=cnf)

        else:
            cmd_obj = get_data_from_config_txt()
            
            cnf.HINTS_1 = cmd_obj.hints_1
            cnf.HINTS_2 = cmd_obj.hints_2
            cnf.MQTT_NAME = cmd_obj.mqtt_name
            cnf.MQTT_CLIENTS = cmd_obj.mqtt_clients
            cnf.COMMANDS = cmd_obj.comands
            json_data_in_file = get_json_data(config=cnf)
        
        # пишим финальный вариант потока в json файл            
        json.dump(json_data_in_file, write_file)

print("Import generated_flow.json in node-red")
