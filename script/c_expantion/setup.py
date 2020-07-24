from distutils.core import setup, Extension
setup(name='test_c',
        version='1.0',
        ext_modules=[Extension('test_c', ['test_c.c'])],
)