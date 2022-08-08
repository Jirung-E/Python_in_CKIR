import json

class JsonLoader:
    def __init__(self):
        self.file = None
        self.json_string = None
        self.json_object = None

    def load(self, file_name):
        self.file = open(file_name, 'r')
        self.json_string = self.file.read()
        self.json_object = json.loads(self.json_string)
        self.file.close()

        return self.json_object

    def show(self):
        print(self.json_string)