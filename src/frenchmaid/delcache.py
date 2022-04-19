import os, shutil

current_dir = os.getcwd()

def openDirs(dir_loop):
    try:
        return os.getcwd(dir_loop)
    except:
        return False

def delDir(dir_select):
    try:
        shutil.rmtree(dir_select)
        return True
    except:
        return False

def loopDirs(main_dir, dir_arr, num_pycache, dir_arr_used):
    iterats = num_pycache
    arr = dir_arr_used

    for dir in dir_arr:
        if (dir in dir_arr_used) == False:
            if str(dir) == "__pycache__":
                arr.append(f"{main_dir}\\{dir}")
                iterats += 1
            elif str(dir) != "__pycache__":
                other_dir = f"{main_dir}\\{dir}"
                try:
                    other_dirs = os.listdir(other_dir)
                    iterats_two = loopDirs(other_dir, other_dirs, iterats, arr)
                    iterats = iterats + iterats_two
                except:
                    iterats = iterats

    return arr

def pyCacheOnly(dir_main):
    try:
        dir_name = str(dir_main)[str(dir_main).rfind("\\")+1:len(dir_main)]
        dirs = os.listdir(dir_main)
        num_dirs = len(dirs)
        arr = []

        array_thing = loopDirs(dir_main, dirs, 0, arr)
        res = len(array_thing)
        
        for official_dir in array_thing:
            delDir(official_dir)

        if res == 0:
            print(f'''\nThere are no pests in your "{dir_name}" directory!''')
            return False
        else:
            print(f'\nSuccesfully found {res} pest(s) in {num_dirs} directories contained within your "{dir_name}" directory. They have been eradicated!\n')

    except Exception as e:
        print('\nflail')
        print(e)
        print('\n')
        return False