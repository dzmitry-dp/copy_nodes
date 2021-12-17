import json


if __name__ == "__main__":
    print("""
    # The "Group" and "Tabs" names are configured in the config.py.
    Now Enter/Paste your list of names. Ctrl-D or Ctrl-Z ( windows ) to save it.

    """)

    name_list = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        name_list.append(line)

    with open('generated_flow.json', 'w') as write_file:
        from template import Node
        
        i = 0 # внешний счетчик количества объектов. Объект - это однотипная еденица, которая состоит из nodes
        obj_list = []
        for line in name_list:
            node = Node(line, i)
            for n in node.hints:
                obj_list.append(n)
            i += 1 # считю в какой раз буду вызывать объект
            
        json.dump(obj_list, write_file)

print("Import generated_flow.json in node-red")