import os
from setuptools import setup, find_packages

def get_files_from_directory(directory_path):
    files_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Adding file: {file_path}")  
            files_list.append(file_path)
    return files_list

APP = ['src/run.py']
DATA_FILES = [
    ('src', get_files_from_directory('src')),
    ('test', get_files_from_directory('test'))
]
OPTIONS = {
    'argv_emulation': True,
    'packages': find_packages(),
    'includes': [
        'Cython', 'IPython', 'Image', 'Numeric', 'OpenSSL.crypto', 'PyQt5', 'PyQt6', 'PyQt6.QtGui',
        'PySide2', 'PySide6', 'PySide6.QtGui', 'StringIO', '_dummy_thread', '_manylinux',
        '_pytest', '_registry', '_ufunc', 'array_api_compat', 'array_interface_testing',
        'cPickle', 'ccompiler_opt', 'checks', 'com', 'com.sun.jna', 'com.sun.jna.platform',
        'cryptography', 'cryptography.x509.extensions', 'cupy', 'cupy.cuda', 'cupy_backends',
        'cupyx', 'dask.distributed', 'dask.sizeof', 'dask.utils', 'distributed',
        'distributed.utils', 'dl', 'dummy_thread', 'gi', 'gi.repository', 'google.cloud',
        'grpc_tools', 'grpc_tools.protoc', 'jax', 'keras.optimizers.optimizer_v2', 'kubernetes',
        'mem_policy', 'mod', 'mpi4py', 'numarray', 'numpy.lib.array_utils', 'numpy_distutils',
        'numpy_distutils.command.build_flib', 'numpy_distutils.command.cpuinfo',
        'numpy_distutils.cpuinfo', 'numpy_distutils.fcompiler', 'numpydoc', 'pandas',
        'pandas.api.types', 'pandas.errors', 'pandas.plotting', 'pep517', 'pickle5', 'polars',
        'polars.testing', 'pooch', 'portpicker', 'psutil', 'pyamg', 'pytest', 'pytest_timeout',
        'setuptools_scm', 'shiboken2', 'shiboken6', 'simplejson', 'sip', 'sparse', 'sphinx',
        'tensorflow.compat.v1', 'tensorflow_io', 'tf_keras', 'tf_keras.optimizers.legacy',
        'tf_keras.optimizers.optimizer_v2', 'tflite_runtime', 'theano', 'thread', 'torch',
        'tornado', 'tornado.gen', 'tornado.template', 'uarray', 'unicodedata2', 'viztracer',
        'win32com', 'win32com.shell', 'win32pdh', 'yaml', 'zopfli',
        'tensorflow', 'matplotlib', 'sklearn'  # Common libraries that might be using these modules
    ]
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
