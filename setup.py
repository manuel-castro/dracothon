import setuptools
import os
from skbuild import setup
from skbuild.constants import CMAKE_INSTALL_DIR

src_dir = './src'
lib_dir = os.path.join(CMAKE_INSTALL_DIR, 'lib/')

# cython --cplus -I./_skbuild/linux-x86_64-3.6/cmake-install/include/draco/ ./src/_testScikit.pyx

setup(
    name='dracothon',
    cmake_source_dir='./draco',
    packages=['dracothon'],
    ext_modules=[
        setuptools.Extension(
            'dracothon._testScikit',
            sources=[ os.path.join(src_dir, name) for name in ('_testScikit.cpp', 'testScikit.cpp') ],
            depends=[ os.path.join(src_dir, 'testScikit.h') ],
            language='c++',
            include_dirs = [ os.path.join(CMAKE_INSTALL_DIR, 'include/')],
            extra_compile_args=[
              '-std=c++11','-O3'
            ],
            extra_link_args=[
                '-l:{0}'.format(os.path.join(lib_dir, lib)) for lib in ('libdracoenc.a', 'libdraco.a', 'libdracodec.a')
            ])
    ]
)
