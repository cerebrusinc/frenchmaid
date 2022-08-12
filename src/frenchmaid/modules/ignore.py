
def git(directory: str) -> None:
    try:
        f = open(".gitignore", "x")
        f.write("__pycache__/*\n.mypy_cache/")
        f.close()
        print(f'\nSuccessfully created a ".gitignore" in your "{directory}" folder. It now ignores all pycache and mypy cache folders!')
        return
    except:
        f_read = open(".gitignore", "r")
        f_write = open(".gitignore", "a")
        f_data = f_read.read()
        array: list[str] = []

        if "__pycache__/*" not in f_data:
            f_write.write("\n__pycache__/*")
            array.append('pycache')

        if ".mypy_cache/" not in f_data:
            f_write.write("\n.mypy_cache/")
            array.append('mypy')

        f_read.close()
        f_write.close()

        if len(array) == 0:
            print(f"""\nLooks like the ".gitignore" file in your "{directory}" directory already ignores all pycache and mypy cache folders!""")
        elif len(array) == 1 and array[0] == "pycache":
            print(f"""\nSuccessfully added all pycache folders to the ".gitignore" file in your "{directory}" directory!""")
        elif len(array) == 1 and array[0] == "mypy":
            print(f"""\nSuccessfully added all mypy cache folders to the ".gitignore" file in your "{directory}" directory!""")
        else:
            print(f"""\nSuccessfully added all pycache and mypy cache folders to the ".gitignore" file in your "{directory}" directory!""")

        return

def docker(directory: str) -> None:
    try:
        f = open(".dockerignore", "x")
        f.write("*__pycache__*\n.mypy_cache")
        f.close()
        print(f'\nSuccessfully created a ".dockerignore" in your "{directory}" folder. It now ignores all pycache and mypy cache folders!')
        return
    except:
        f_read = open(".dockerignore", "r")
        f_write = open(".dockerignore", "a")
        f_data = f_read.read()
        array: list[str] = []

        if "*__pycache__*" not in f_data:
            f_write.write("\n*__pycache__*")
            array.append('pycache')

        if ".mypy_cache" not in f_data:
            f_write.write("\n.mypy_cache")
            array.append('mypy')

        f_read.close()
        f_write.close()

        if len(array) == 0:
            print(f"""\nLooks like the ".dockerignore" file in your "{directory}" directory already ignores all pycache and mypy cache folders!""")
        elif len(array) == 1 and array[0] == "pycache":
            print(f"""\nSuccessfully added all pycache folders to the ".dockerignore" file in your "{directory}" directory!""")
        elif len(array) == 1 and array[0] == "mypy":
            print(f"""\nSuccessfully added all mypy cache folders to the ".dockerignore" file in your "{directory}" directory!""")
        else:
            print(f"""\nSuccessfully added all pycache and mypy cache folders to the ".dockerignore" file in your "{directory}" directory!""")

        return