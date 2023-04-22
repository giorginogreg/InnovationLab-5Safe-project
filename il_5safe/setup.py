from setuptools import setup, Extension
from Cython.Build import cythonize

ext_options = {
    language: "c++",
    include_dirs: [torch.utils.cmake_prefix_path + "/include"],
    library_dirs: [torch.utils.cmake_prefix_path + "/lib"],
    libraries: ["torch"],
}
extensions = [
    Extension("models.yolo", ["models/yolo.pyx"], **ext_options),
    Extension(
        "models.faster_rcnn", ["./models/faster_rcnn.pyx"], **ext_options
    ),
    Extension("models.retina_net", ["./models/retina_net.pyx"], **ext_options),
]

setup(
    name="il-5safe",
    ext_modules=cythonize(extensions),
)
