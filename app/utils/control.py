import json

class TupleManager:
    def __init__(self):
        self.tuples = []

    def add_tuple(self, key, value):
        for tuple in self.tuples:
            if tuple[0] == key:
                print("Key already exists!")
                return
        self.tuples.append((key, value))
        self.tuples.sort()

    def remove_tuple(self, key):
        self.tuples = [tuple for tuple in self.tuples if tuple[0] != key]

    def list_tuples(self):
        return self.tuples

    def filter_tuples(self, key=None, value=None):
        return [tuple for tuple in self.tuples if (key is None or tuple[0] == key) and (value is None or tuple[1] == value)]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.tuples, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.tuples = json.load(f)
        except FileNotFoundError:
            print("File not found!")




# # Criação de uma instância da classe TupleManager
# manager = TupleManager()

# # Adicionar tuplas
# manager.add_tuple("key1", "value1")
# manager.add_tuple("key2", "value2")

# # Listar todas as tuplas
# print("All tuples:", manager.list_tuples())

# # Filtrar tuplas por chave
# filtered_by_key = manager.filter_tuples(key="key1")
# print("Filtered by key:", filtered_by_key)

# # Filtrar tuplas por valor
# filtered_by_value = manager.filter_tuples(value="value2")
# print("Filtered by value:", filtered_by_value)

# # Remover tupla por chave
# manager.remove_tuple("key1")
# print("After removal:", manager.list_tuples())

# # Salvar tuplas em um arquivo
# manager.save_to_file("tuples.json")

# # Carregar tuplas de um arquivo
# manager.load_from_file("tuples.json")
# print("Loaded from file:", manager.list_tuples())


