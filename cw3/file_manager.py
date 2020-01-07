class FileManager():
    def __init__(self, file_name):
        print("spawned manager with parameter " + file_name)
        self.fn = file_name

    def read_file(self):
        handle = open(self.fn, encoding='utf-8')
        content = handle.read()
        handle.close()
        return content

    def update_file(self, text_data):
        handle = open(self.fn, 'a+', encoding='utf-8')
        handle.write('\n')
        handle.write(text_data)
        handle.close()