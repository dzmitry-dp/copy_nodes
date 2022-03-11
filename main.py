import json

def format_result_list(list_in_list) -> list:
    result_list = []
    for _list in list_in_list:
        for item in _list:
            result_list.append(item)
    return result_list

def get_hints_json_data(config):
    # print('Hints_1:\n', config.HINTS_1)
    # print('Hints_2:\n', config.HINTS_2)
    # print('MQTT_NAME:\n', config.MQTT_NAME)
    # print('MQTT_CLIENTS:\n', config.MQTT_CLIENTS)
    # print('COMMANDS:\n', config.COMMANDS)

    "В результате работы этой функции получаю json, который  могу импортировать в node-red"

    from scripts.hints import Hints
        
    result_nodes_json_list = []
    id_list_in_python3_kill_talk = [] # список id нод link out, которые пойдут на ноду "python3 /media/pi/MP3/kill_talk.py"
    id_list_in_set_btn_text = []

    for hint in config.HINTS_1:
        nodes = Hints(name=hint, config=config)
        # print(nodes.input_to_set_btn_text)
        _json_list = [
            *nodes.btn,
            *nodes.hints,
        ]
        # повторяемые объекты потока добавляем в общий список
        result_nodes_json_list.append(_json_list)
        # добавляем id в общий список тех кто ссылается на вход input ноды
        id_list_in_python3_kill_talk.append(nodes.nodes_id_in_python_kill)
        id_list_in_set_btn_text.append(nodes.nodes_id_set_btn_text)

    # подготавливаем данные для записи в файл. Распаковываем списки
    json_data_in_file = format_result_list(result_nodes_json_list)

    # специально для потока hints ноды кототые не повторяются
    id_in_python_kill = format_result_list(id_list_in_python3_kill_talk)
    nodes.input_python_kill['links'] = id_in_python_kill # записываю все id нод, которые ссылаются на input ноду, которая стартует код python3 
    id_in_set_btn_text = format_result_list(id_list_in_set_btn_text)
    nodes.inpt_node['wires'] = [id_in_set_btn_text]
    json_data_in_file.append(nodes.inpt_node)
    json_data_in_file.append(nodes.input_python_kill)
    json_data_in_file.append(nodes.kill_talk)

    return json_data_in_file

def get_debug_json_data(config):
    from scripts.debug import LinkState, Lock
    
    i = 0 # для уникальных id
    result_nodes_json_list = []
    for client in config.MQTT_CLIENTS:
        client_name = client
        client_lable = config.MQTT_CLIENTS[client]

        client_link_state = LinkState(i, client_name, client_lable)
        result_nodes_json_list.append(client_link_state.json_nodes)
        i += 1

    lock_swith = Lock(config.COMMANDS)
    result_nodes_json_list.append(lock_swith.json_nodes)

    # подготавливаем данные для записи в файл. Распаковываем списки
    json_data_in_file = format_result_list(result_nodes_json_list)
    return json_data_in_file

def get_data_from_config_txt():
    from scripts.config_data import Command

    with open('config.txt', 'r') as file:
        cmd_obj = Command(file)
        return cmd_obj

# формируем точку входа
if __name__ == "__main__":
    import scripts.cnf as cnf

    
    cmd_obj = get_data_from_config_txt()

    cnf.LANGUAGE = cmd_obj.language
    cnf.HINTS_1 = cmd_obj.hints_1
    cnf.HINTS_2 = cmd_obj.hints_2
    cnf.MQTT_NAME = cmd_obj.mqtt_name
    cnf.MQTT_CLIENTS = cmd_obj.mqtt_clients
    cnf.COMMANDS = cmd_obj.comands
    
    hints_nodes = get_hints_json_data(config=cnf)
    with open('hints_flow.json', 'w') as write_file:
        # пишим финальный вариант потока в json файл            
        json.dump(hints_nodes, write_file)

    debug_nodes = get_debug_json_data(config=cnf)
    with open('debug_flow.json', 'w') as write_file:
        # пишим финальный вариант потока в json файл            
        json.dump(debug_nodes, write_file)

print("Import generated_flow.json in node-red")
