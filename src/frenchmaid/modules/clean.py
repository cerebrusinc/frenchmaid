import os, shutil, sys

platf: str = sys.platform

def delDir(dir_select: str) -> bool:
    try:
        shutil.rmtree(dir_select)
        return True
    except:
        return False

def loopDirsOne(main_dir: str, dir_arr: list[str], num_pycache: int, dir_arr_used: list[str], dir_to_delete: str) -> list[str]:
    iterats: int = num_pycache
    arr: list[str] = dir_arr_used
    arr2: list[str] = dir_arr_used

    if "pyvenv.cfg" not in dir_arr:
        for dir in dir_arr:
            if (dir in dir_arr_used) == False:
                if str(dir) == dir_to_delete:

                    if platf == "win32":
                        arr.append(f"{main_dir}\\{dir}")
                    else:
                        arr2.append(f"{main_dir}/{dir}")

                    iterats += 1
                elif str(dir) != dir_to_delete:

                    other_dir: str = ''

                    if platf == "win32":
                        other_dir = f"{main_dir}\\{dir}"
                    else:
                        other_dir = f"{main_dir}/{dir}"

                    try:
                        other_dirs: list[str] = os.listdir(other_dir)

                        if platf == "win32":
                            iterats_two = loopDirsOne(other_dir, other_dirs, iterats, arr, dir_to_delete)
                        else:
                            iterats_two = loopDirsOne(other_dir, other_dirs, iterats, arr2, dir_to_delete)

                        iterats = iterats + len(iterats_two)
                    except:
                        iterats = iterats


    if platf == "win32":
        return arr
    else:
        return arr2

def loopDirsAll(main_dir: str, dir_arr: list[str], num_pycache: int, dir_arr_used: list[str]) -> list[str]:
    iterats: int = num_pycache
    arr: list[str] = dir_arr_used
    arr2: list[str] = dir_arr_used

    if "pyvenv.cfg" not in dir_arr:
        for dir in dir_arr:
            if (dir in dir_arr_used) == False:
                if str(dir) == "__pycache__" or str(dir) == '.mypy_cache':

                    if platf == "win32":
                        arr.append(f"{main_dir}\\{dir}")
                    else:
                        arr2.append(f"{main_dir}/{dir}")

                    iterats += 1
                elif str(dir) != "__pycache__" or str(dir) != '.mypy_cache':

                    other_dir: str = ''

                    if platf == "win32":
                        other_dir = f"{main_dir}\\{dir}"
                    else:
                        other_dir = f"{main_dir}/{dir}"

                    try:
                        other_dirs: list[str] = os.listdir(other_dir)

                        if platf == "win32":
                            iterats_two = loopDirsAll(other_dir, other_dirs, iterats, arr)
                        else:
                            iterats_two = loopDirsAll(other_dir, other_dirs, iterats, arr2)

                        iterats = iterats + len(iterats_two)
                    except:
                        iterats = iterats

    if platf == "win32":
        return arr
    else:
        return arr2

def clean(dir_main: str, folder: str) -> None:
    try:
        dir_name: str = ''
        
        if platf == "win32":
            dir_name = dir_main[str(dir_main).rfind("\\")+1:len(dir_main)]
        else:
            dir_name = dir_main[str(dir_main).rfind("/")+1:len(dir_main)]
            
        dirs: list[str] = os.listdir(dir_main)
        num_dirs: int = len(dirs)
        arr: list[str] = []
        array_thing: list[str] = []

        if folder == 'all':
            array_thing = loopDirsAll(dir_main, dirs, 0, arr)
        else:
           array_thing = loopDirsOne(dir_main, dirs, 0, arr, folder)

        res: int = len(array_thing)
        
        for official_dir in array_thing:
            delDir(official_dir)

        if res == 0:
            print(f'''\nThere are no pests in your "{dir_name}" directory!''')
        else:
            print(f'\nSuccesfully found {res} pest(s) in {num_dirs} directories and/or files contained within your "{dir_name}" directory. They have been eradicated!\n')

        return

    except Exception as e:
        print('\nflail')
        print(e)
        print('\n')
        return