import numpy

def f(event):
    return {
        "pinned_version": "1.23.5",
        'result': int(event),
        'numpy-version': numpy.__version__
    }
