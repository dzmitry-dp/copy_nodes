import json

import config


if __name__ == "__main__":
    
    with open('generated_flow.json', 'w') as write_file:
        from template import Nodes, ConfigNodes
        
        result_nodes_json_list = []
        id_list = [] # список id нод link out, которые пойдут на ноду "python3 /media/pi/MP3/kill_talk.py"
        for hint in config.HINTS_1:
            nodes = Nodes(name=hint)
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

        # форматируем список списков в просто список
        id_in_python_kill = format_result_list(id_list)

        # специально для потока hints
        nodes.input_python_kill['links'] = id_in_python_kill
        json_data_in_file.append(nodes.input_python_kill)
        json_data_in_file.append(nodes.kill_talk)
        
        # добавляем ноды с настройками проекта
        node_red_configurations_in_json = ConfigNodes()
        json_data_in_file.append(node_red_configurations_in_json.project)
        json_data_in_file.append(node_red_configurations_in_json.group)

        # пишим финальный вариант потока в json файл            
        json.dump(json_data_in_file, write_file)

print("Import generated_flow.json in node-red")