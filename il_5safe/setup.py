from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("yolo", ["./models/yolo.pyx"]),
    Extension("faster_rcnn", ["./models/faster_rcnn.pyx"]),
    Extension("retina_net", ["./models/retina_net.pyx"])
]

setup(
    name='il-5safe',
    ext_modules=cythonize(extensions),
    zip_safe=False,
)