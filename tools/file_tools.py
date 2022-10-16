import json


class FileTools:

    @staticmethod
    def read_file(way):
        with open(way) as text:
            data = json.load(text)
        return data

    @staticmethod
    def write_file(data):
        with open('data.json', 'w') as f:
            json.dump(data, f)
