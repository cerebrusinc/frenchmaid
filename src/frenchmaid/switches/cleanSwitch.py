import os

from ..modules import clean

directory: str = os.getcwd()

class CleanSwitch():
    def indirect(self, folder: str):
        switch = getattr(self, folder, lambda: print(f'''\nThis folder type isn't supported... yet. You can request for "{folder}" support at https://github.com/lewisjr/frenchmaid/issues"'''))
        return switch()

    def all(self) -> None:
        clean.clean(directory, 'all')
        return

    def pycache(self) -> None:
        clean.clean(directory, '__pycache__')
        return

    def mypy(self) -> None:
        clean.clean(directory, '.mypy_cache')
        return
