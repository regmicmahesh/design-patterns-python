class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(self.entries)


#    def save(self, filename):
#        file = open(filename, "w")
#        file.write(str(self))
#        file.close()
#
#    def load(self, filename):
#        pass
#
#    def load_from_web(self, url):
#        pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        pass

    @staticmethod
    def load_from_file(journal, filename):
        pass

    @staticmethod
    def save_to_web(journal, url):
        pass

    @staticmethod
    def load_from_web(journal, url):
        pass

