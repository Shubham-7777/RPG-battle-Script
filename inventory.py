
class Item:
    def __init__(self, name, types, description, prop):
        self.name = name
        self.types = types
        self.description = description
        self.prop = prop

    def name(self):
        return self.name

    def types(self):
        return self.types

    def description(self):
        return self.description

    def prop(self):
        return self.prop
