import numpy

def f(event):
    return {
        "pinned_version": "1.23.5",
        "actual_version": numpy.__version__,
        'result': int(numpy.array(event).sum()),
        'numpy-version': numpy.__version__
    }
