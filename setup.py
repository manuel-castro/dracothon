import setuptools
import os
from skbuild import setup
from skbuild.constants import CMAKE_INSTALL_DIR

src_dir = './src'
lib_dir = os.path.join(CMAKE_INSTALL_DIR, 'lib/')

# cython --cplus -3 -I./_skbuild/linux-x86_64-3.6/cmake-install/include/draco/ ./src/_testScikit.pyx

setup(
    name='DracoPy',
    cmake_source_dir='./draco',
    ext_modules=[
        setuptools.Extension(
            'DracoPy',
            sources=[ os.path.join(src_dir, 'DracoPy.cpp') ],
            depends=[ os.path.join(src_dir, 'DracoPy.h') ],
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
