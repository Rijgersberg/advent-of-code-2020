from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("d15.pyx",
                            compiler_directives={'language_level' : "3"},
                            annotate=True,)
)