import importlib
from types import ModuleType
from typing import List, Union, Callable


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    such_objects = []
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            met = getattr(mod, method_name, None)
            if isinstance(met, Callable):
                such_objects.append(met)

        except ImportError:
            continue

    return such_objects
