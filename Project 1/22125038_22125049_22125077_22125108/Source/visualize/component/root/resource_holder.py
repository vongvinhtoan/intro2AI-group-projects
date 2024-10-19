class ResourceHolder:
    def __init__(self):
        self.resources = {}
    def add(self, key, value):
        self.resources[key] = value
    def get(self, key):
        return self.resources[key]
    def remove(self, key):
        del self.resources[key]