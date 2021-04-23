import importlib
from types import ModuleType
from typing import List, Union, Callable, Optional


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    such_objects = []
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
                if isinstance(mod.method_name, Callable):
                    such_objects.append(mod.method_name)
            elif isinstance(module, str):
                mod = importlib.import_module(module)
                if isinstance(mod.method_name, Callable):
                    such_objects.append(mod.method_name)
            else:
                raise TypeError('Must be list of strings or ModuleType')

            met = getattr(mod, method, None)

            if met:
                return met

        except ImportError:
            continue

    return such_objects
