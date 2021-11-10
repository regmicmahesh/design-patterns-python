class CodeBuilder:

    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, name, type):
        self.fields.append((name, type))
        return self

    def __str__(self):
        code = 'class {root_name}:\n'.format(root_name=self.root_name)
        if len(self.fields) == 0:
            code += '   pass\n'
            return code

        code += "   def __init__(self):\n"
        for name, type in self.fields:
            code += '    self.{name} = {type}\n'.format(name=name, type=type)
        return code


cb = CodeBuilder('Person')

print(cb)
