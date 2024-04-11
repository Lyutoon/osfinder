ALLOWED_IMPORTS = {
    "math",
    "time",
    "datetime",
    "pandas",
    "scipy",
    "numpy",
    "matplotlib",
    "plotly",
    "seaborn",
}

import scipy
import math
import time
import datetime
import numpy 
import matplotlib
import plotly
import pandas
import seaborn

module = 'pandas'

def find_import_path(start_obj, target_attr):
    stack = [(start_obj, module)]
    trace = []
    while stack:
        current_obj, import_path = stack.pop()
        if len(import_path.split('.')) > 5:
            continue
        try:
            for attr_name in dir(current_obj):
                attr = getattr(current_obj, attr_name)
                if attr_name == target_attr:
                    print(f"{import_path}.{target_attr}")
                    trace.append(f"{import_path}.{target_attr}")
                elif isinstance(attr, type(current_obj)):
                    module_path = f"{import_path}.{attr_name}"
                    stack.append((attr, module_path))
                if len(trace) > 1000:
                    return trace
        except:
            pass

    return None

target_attr = 'os'
import_path = find_import_path(eval(module), target_attr)