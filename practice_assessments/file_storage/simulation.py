import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

import numpy
import sortedcontainers
"""
Simulates a coding framework operation on a list of lists of strings.

Parameters:
list_of_lists (List[List[str]]): A list of lists containing strings.
"""

def simulate_coding_framework(list_of_lists):

    file_storage = OrderedDict()
    logs = []

    def FILE_UPLOAD(file_name, size):
        if file_name in file_storage:
            return RuntimeError

        file_storage[file_name] = size
        print(f"Uploading {file_name} of size {size}")
        logs.append(f"uploaded {file_name}")

    def FILE_GET(file_name):
        if file_name in file_storage:
            print(f"Getting {file_name}")
            logs.append(f"got {file_name}")
            return file_storage[file_name]

    def FILE_COPY(source, dest):
        if source not in file_storage:
            return RuntimeError
        size = file_storage[source]
        file_storage[dest] = size
        del file_storage[source]

        logs.append(f"copied {source} to {dest}")
    
    for args in list_of_lists:
        method = args[0]
        params = args[1:]
        if method == "FILE_UPLOAD":
            file_name, size = params
            FILE_UPLOAD(file_name, size)
        elif method == "FILE_GET":
            file_name = params[0]
            FILE_GET(file_name)
        elif method == "FILE_COPY":
            source = params[0]
            dest = params[1]
            FILE_COPY(source, dest)

    return logs