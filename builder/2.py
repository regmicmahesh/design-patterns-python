class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str__(self):
        return self.__str(0)

    def __str(self, indent):
        i = ' ' * (indent * self.indent_size)
        o = f'{i}<{self.name}>\n'
        for e in self.elements:
            o += e.__str(indent + 1)
        if self.text:
            o += f'{i}  {self.text}\n'
        o += f'{i}</{self.name}>\n'
        return o

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        e = HtmlElement(child_name, child_text)
        self.__root.elements.append(e)
        return self

    def __str__(self):
        return str(self.__root)

builder = HtmlBuilder('ul')
builder.add_child_fluent('li', 'hello').add_child('li', 'world')
print(builder)
