#include<vector>
#include<cstddef>

struct MeshObject {
  std::vector<float> points;
  std::vector<float> normals;
  std::vector<unsigned int> faces;
};

class TestScikit {

 public:
  TestScikit();
  ~TestScikit();
//   void get_draco_encoded_mesh(const std::vector<float> &points, const std::vector<unsigned int> &faces);
  int get_draco_encoded_meshCV(const std::vector<float> &points, const std::vector<unsigned int> &faces, const char **bytes_ptr, std::size_t *bytes_len);
  MeshObject decode_buffer(const char *buffer, std::size_t buffer_len);
  void encode_mesh(const std::vector<float> &points, const std::vector<unsigned int> &faces, const char **bytes_ptr, size_t *bytes_len, int quantization_bits, int compression_level, float quantization_range, const float *quantization_origin);
  // void decodeDracoBufferToBuffer(const char *draco_buffer, std::size_t draco_buffer_len, const char **decoded_output, std::size_t *decoded_len);
  // get_draco_mesh_buffer
};