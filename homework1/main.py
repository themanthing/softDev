from homework1 import a
from homework1 import b
from homework1.import_monster.monster import methods_importer

# print(dir())
print(methods_importer("s", [a, b]))
print(methods_importer("a", [a]))
print(methods_importer("foo", [a, b]))
print(methods_importer("Foo", [a]))
