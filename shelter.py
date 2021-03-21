import os.path
import pickle
import utils
import sys
import random
from config import system_folder, transformation

# for test
# dir_test = "C:\\Users\\cooky\\Downloads\tests2"
# os.chdir(dir_test)

kind = sys.argv[1]
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

if kind == 'on' and os.path.isfile('temp'):
    print("Your file are currently protected. you can turn off..")
    sys.exit()
elif kind == 'off' and os.path.isfile('temp') is False:
    print("hurry up cover your ")
    sys.exit()

file_transform = dict()
try:
    f = open('temp', 'r+b')
    file_transform = pickle.load(f)
except (KeyError, IOError) as err:
    f = open('temp', 'wb')
    file_transform['dir'] = {}
    file_transform['file'] = {}
    file_transform['kind'] = {'hidden': False}

if kind == 'on':

    count = 0
    for dirpath, dirnames, filenames in sorted(os.walk('.'), reverse=True):

        for filename in filenames:
            extension = os.path.splitext(filename)[1][1:]
            filepath = os.path.join(dirpath, filename)
            base = os.path.basename(filepath)  # No need to store in var
            base_without_ext = os.path.splitext(base)[0]

            if extension in transformation:
                new_name = os.path.join(dirpath, base_without_ext) + '.' + utils.transform(extension)
                if transformation[extension]['change_name']:
                    new_name = os.path.join(dirpath, utils.get_random_name()) + '.' + utils.transform(extension)

                # First save data for future unhiding
                try:
                    file_transform['file'][new_name] = filepath
                    os.rename(filepath, new_name)
                except Exception as err:
                    print(f"changing file error: {err}")

        for dir_name in dirnames:
            origin = os.path.join(dirpath, dir_name)
            if len(origin.split("\\")) == 2 and count < 3:
                count = count + 1
                random_name = system_folder[random.randrange(len(system_folder))] % utils.get_random_name()
            else:
                random_name = utils.get_random_name()
            new = os.path.join(dirpath, random_name)
            try:
                file_transform['dir'][new] = origin
                os.rename(origin, new)
            except Exception as err:
                print(f"changing directory error: {err}")

    pickle.dump(file_transform, f, pickle.HIGHEST_PROTOCOL)
    f.close()

else:
    f = open('temp', 'rb')
    file_transform = pickle.load(f)
    for key in sorted(file_transform['dir'], key=lambda x: (len(x.split('\\')))):
        try:
            os.rename(key, file_transform['dir'][key])
            # print(f"{key}: {file_transform['dir'][key]}")
        except Exception as err:
            print(f"Recovery directory error: {err}")

    for key in sorted(file_transform['file']):
        try:
            os.rename(key, file_transform['file'][key])
            # print(f"{key}: {file_transform['file'][key]}")
        except Exception as err:
            print(f"Recovery file error: {err}")
    f.close()
    os.remove('./temp')