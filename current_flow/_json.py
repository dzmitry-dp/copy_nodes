#!/bin/python

import os
import json

cur_dir = os.environ.get('PWD')

class JsonFile:
    def __init__(self, directory):
        self.directory = directory
        self.file_name = self.get_file_name()
        self.file_data = None

    def get_file_name(self):
        name_list = [x for x in os.listdir(self.directory) if ".json" in x]
        if len(name_list) == 0:
            return None
        elif len(name_list) == 1:
            return name_list[0]
        else:
            return self.select_json_files(name_list)

    def select_json_files(self, name_list):
        print('Выбери файл: \n')
        for i, f in enumerate(name_list):
            print(str(i+1) + '.', f)
        file_index = int(input('\n'))
        return name_list[file_index-1]

    def get_data(self):
        with open(self.directory + '/' + self.file_name, 'rb') as file:
            self.file_data = json.load(file)

    def write_new_json(self):
        with open(self.directory + '/_' + self.file_name, 'w') as file:
            json.dump(self.file_data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
#   try:
    file_obj = JsonFile(cur_dir)
    if file_obj.file_name == None:
        print('Нет .json файлов в этой папке')
    else:
        file_obj.get_data()
        file_obj.write_new_json()
#   except ValueError:
#       print('\nError!!! Вводи цифры!')
#   except KeyboardInterrupt:
#       print('\nОк. Досвидули!')
#       exit()
