from types import ModuleType
from typing import List, Union, Callable


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    print(method_name)
    print(modules)
