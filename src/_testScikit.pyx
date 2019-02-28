# distutils: language = c++
# distutils: sources = ext/third_party/mc/testScikit.cpp

from libc.stdint cimport uint64_t, uint32_t
from libcpp.vector cimport vector

# c++ interface to cython
cdef extern from "testScikit.h":
    cdef cppclass TestScikit:
        TestScikit() except +
        #void get_draco_encoded_mesh(vector[float] points, vector[uint32_t] faces)
        int get_draco_encoded_meshCV(vector[float] points, vector[uint32_t] faces, const char **bytes_ptr, size_t *bytes_len)

# creating a cython wrapper class
cdef class PySciKit:
    cdef TestScikit *thisptr
    cdef const char* c_string
    cdef size_t str_len
    cdef bytes py_string
    def __cinit__(self):
        self.thisptr = new TestScikit()
    def __dealloc__(self):
        del self.thisptr
    #def get_draco_encoded_mesh(self, points, faces):
        #self.thisptr.get_draco_encoded_mesh(points, faces)
    def get_draco_encoded_meshCV(self, points, faces):
        self.thisptr.get_draco_encoded_meshCV(points, faces, &self.c_string, &self.str_len)
        try:
            self.py_string = self.c_string[:self.str_len]  # Performs a copy of the data
        finally:
            return self.py_string