import json


def get_json_data(config):
    # print('Project:', config.DASHBOARD_PROJECT_NAME)
    # print('Group:', config.DASHBOARD_GROUP_NAME)
    # print('Hints_1', config.HINTS_1)
    # print('Hints_2', config.HINTS_2)

    "В результате работы этой функции получаю json, который  могу импортировать в node-red"

    from template import Nodes#, ConfigNodes
        
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
        # добавляем id в общий список
        id_list.append(nodes.nodes_id_in_python_kill)

    def format_result_list(list_in_list) -> list:
        result_list = []
        for _list in list_in_list:
            for item in _list:
                result_list.append(item)
        return result_list

    # подготавливаем данные для записи в файл
    json_data_in_file = format_result_list(result_nodes_json_list)

    # форматируем список списков
    id_in_python_kill = format_result_list(id_list)

    # специально для потока hints
    nodes.input_python_kill['links'] = id_in_python_kill # записываю все id нод, которые ссылаются на input ноду, которая стартует код  
    json_data_in_file.append(nodes.input_python_kill)
    json_data_in_file.append(nodes.kill_talk)
    
    # добавляем ноды с настройками проекта
    # node_red_configurations_in_json = ConfigNodes(config=config)
    # json_data_in_file.append(node_red_configurations_in_json.project)
    # json_data_in_file.append(node_red_configurations_in_json.group)

    return json_data_in_file

def get_data_from_config_txt():
    with open('config.txt', 'r') as file:
        lines = file.readlines()

        def return_index_from_list():
            "Возвращаю список индексов где строки равны '###\\n' из списка lines"
            idx = []
            for i, line in enumerate(lines):
                if line == '###\n':
                    idx.append(i)
            return idx

        index_list = return_index_from_list() # список индексов из списка, где элемент равен '###\n'
        
        def _clear(line: list):
            if '###\n' in line:
                line.remove('###\n')

            if '\n' in line:
                line.remove('\n')

            return line

        for i in index_list:
            if i > 0:
                comand_line = lines[index_list[index_list.index(i)-1]:i]

                # if 'Project name\n' in comand_line:
                #     project = _clear(lines[i:index_list[index_list.index(i)+1]])[0].replace('\n', '')
                #     continue
                # if 'Group\n' in comand_line:
                #     group = _clear(lines[i:index_list[index_list.index(i)+1]])[0].replace('\n', '')
                #     continue
                if 'Hints\n' in comand_line:
                    hints_1 = []
                    for item in _clear(lines[i:index_list[index_list.index(i)+1]])[::2]:
                        hints_1.append(item.replace('\n', ''))

                    hints_2 = []
                    for item in _clear(lines[i:index_list[index_list.index(i)+1]])[1::2]:
                        hints_2.append(item.replace('\n', ''))
                        
                    return hints_1, hints_2

# формируем точку входа
if __name__ == "__main__":
    import cnf

    with open('generated_flow.json', 'w') as write_file:
        if cnf.HINTS_1 != []:
            json_data_in_file = get_json_data(config=cnf)
            # пишим финальный вариант потока в json файл            
            json.dump(json_data_in_file, write_file)

        else:
            hints_1, hints_2 = get_data_from_config_txt()
            # cnf.DASHBOARD_PROJECT_NAME = project
            # cnf.DASHBOARD_GROUP_NAME = group
            cnf.HINTS_1 = hints_1
            cnf.HINTS_2 = hints_2
            json_data_in_file = get_json_data(config=cnf)
            json.dump(json_data_in_file, write_file)

print("Import generated_flow.json in node-red")
