#!/usr/bin/env

import random
from config import adjs, nouns, RAND_RANGE, transformation, system_folder
import hashlib
import os.path


def get_random_name(adjs=adjs, nouns=nouns):
    num = random.randint(0, RAND_RANGE)
    adj = adjs[random.randrange(len(adjs))]
    noun = nouns[random.randrange(len(nouns))]
    return adj + '_' + noun + '_' + str(num)


def transform(extension, transformation=transformation):
    return transformation[extension]['to']


def get_system_name(current_dir):
    os.chdir(current_dir + "\\..")
    path = os.getcwd()
    system_folder_name = system_folder[2]

    os.rename(dir_test, new_chdir)


def md5_for_file(f, block_size=2 ** 20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


