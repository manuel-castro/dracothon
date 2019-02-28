import setuptools
import os
from skbuild import setup

setup(
    cmake_source_dir='./draco',
    cmake_install_dir='./draco_build',
    packages=['dracothon'],
    ext_modules=[
        setuptools.Extension(
            'dracothon._testScikit',
            sources=[ os.path.join('./', name) for name in ('src/_testScikit.cpp','src/testScikit.cpp') ],
            depends=[ os.path.join('./', 'src/testScikit.h')],
            language='c++',
            include_dirs=[ os.path.join('./', name) for name in ('src/', 'draco/src/', '_skbuild/linux-x86_64-3.6/cmake-install/draco_build/include/') ],
            # extra_objects=[
            #   os.path.join(third_party_dir, 'draco_build/lib/', name) for name in ('libdracoenc.a', 'libdraco.a', 'libdracodec.a')
            # ],
            extra_compile_args=[
              '-std=c++11','-O3'
            ], #don't use  '-fvisibility=hidden', python can't see init module
            extra_link_args=[
              '-l:./_skbuild/linux-x86_64-3.6/cmake-install/draco_build/lib/libdracoenc.a', '-l:./_skbuild/linux-x86_64-3.6/cmake-install/draco_build/lib/libdraco.a', '-l:./_skbuild/linux-x86_64-3.6/cmake-install/draco_build/lib/libdracodec.a'
            ])
    ]
)

# setuptools.setup(
#     ext_modules=[
#         setuptools.Extension(
#             'dracothon._testScikit',
#             sources=[ os.path.join('./', name) for name in ('src/_testScikit.cpp','src/testScikit.cpp') ],
#             depends=[ os.path.join('./', 'src/testScikit.h')],
#             language='c++',
#             include_dirs=[ os.path.join('./', name) for name in ('src/', 'draco/src/', 'draco_build/') ],
#             # extra_objects=[
#             #   os.path.join(third_party_dir, 'draco_build/lib/', name) for name in ('libdracoenc.a', 'libdraco.a', 'libdracodec.a')
#             # ],
#             extra_compile_args=[
#               '-std=c++11','-O3'
#             ], #don't use  '-fvisibility=hidden', python can't see init module
#             extra_link_args=[
#               '-l:./draco_build/libdracoenc.a', '-l:./draco_build/libdraco.a', '-l:./draco_build/libdracodec.a'
#             ])
#     ]
# )