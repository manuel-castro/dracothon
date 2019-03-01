# distutils: language = c++
# distutils: sources = ext/third_party/mc/testScikit.cpp

from libc.stdint cimport uint64_t, uint32_t
from libcpp.vector cimport vector
from cpython.mem cimport PyMem_Malloc, PyMem_Free

# c++ interface to cython
cdef extern from "testScikit.h":
    cdef struct MeshObject:
        vector[float] points
        vector[float] normals
        vector[unsigned int] faces

    cdef cppclass TestScikit:
        TestScikit() except +
        #void get_draco_encoded_mesh(vector[float] points, vector[uint32_t] faces)
        int get_draco_encoded_meshCV(vector[float] points, vector[uint32_t] faces, const char **bytes_ptr, size_t *bytes_len) except +
        MeshObject decode_buffer(const char *buffer, size_t buffer_len) except +
        void encode_mesh(vector[float] points, vector[uint32_t] faces, const char **bytes_ptr, size_t *bytes_len, int quantization_bits, int compression_level, float quantization_range, const float *quantization_origin) except +


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
    #def get_draco_encoded_meshCV(self, points, faces):
        #self.thisptr.get_draco_encoded_meshCV(points, faces, &self.c_string, &self.str_len)
        #try:
            #self.py_string = self.c_string[:self.str_len]  # Performs a copy of the data
        #finally:
            #return self.py_string
    def encode_mesh_to_buffer(self, points, faces, quantization_bits=14, compression_level=1, quantization_range=-1, quantization_origin=None):
        cdef float* quant_origin = NULL
        if quantization_origin is not None:
            quant_origin = <float *>PyMem_Malloc(sizeof(float) * 3)
            quant_origin[0] = quantization_origin[0]
            quant_origin[1] = quantization_origin[1]
            quant_origin[2] = quantization_origin[2]
        self.thisptr.encode_mesh(points, faces, &self.c_string, &self.str_len, quantization_bits, compression_level, quantization_range, quant_origin)
        try:
            self.py_string = self.c_string[:self.str_len]  # Performs a copy of the data
        finally:
            if quant_origin != NULL:
                PyMem_Free(quant_origin)
            return self.py_string
    def decode_buffer_to_mesh(self, buffer):
        return self.thisptr.decode_buffer(buffer, len(buffer))
    