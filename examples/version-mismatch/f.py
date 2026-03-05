import numpy

def f(event):
    x = numpy.float(3.14)

    return {
        "pinned_version": "1.23.5",
        "actual_version": numpy.__version__,
        "result": x,
    }
