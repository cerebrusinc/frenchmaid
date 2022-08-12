import os, sys

from ..modules import ignore

platf = sys.platform
directory_path: str = os.getcwd()
directory: str = ''

if platf == "win32":
    directory = directory_path[str(directory_path).rfind("\\")+1:len(directory_path)]
else:
    directory = directory_path[str(directory_path).rfind("/")+1:len(directory_path)]

class IgnoreSwitch():
    def indirect(self, platform: str):
        switch = getattr(self, platform, lambda: print(f'''\nThis platform isn't supported... yet. You can request for "{platform}" support at https://github.com/lewisjr/frenchmaid/issues"'''))
        return switch()

    def git(self) -> None:
        ignore.git(directory)
        return

    def docker(self) -> None:
        ignore.docker(directory)
        return
