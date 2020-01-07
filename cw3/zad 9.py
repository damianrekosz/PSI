from cw3.file_manager import FileManager

fn = FileManager('data')
print(fn.read_file())
print()
print("----------------------------------------")
data = "dodałem sobie wincyj teksta"
fn.update_file(data)
print(fn.read_file())