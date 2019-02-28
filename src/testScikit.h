#include<vector>
#include<cstddef>

class TestScikit {

 public:
  TestScikit();
  ~TestScikit();
//   void get_draco_encoded_mesh(const std::vector<float> &points, const std::vector<unsigned int> &faces);
  int get_draco_encoded_meshCV(const std::vector<float> &points, const std::vector<unsigned int> &faces, const char **bytes_ptr, std::size_t *bytes_len);
  // get_draco_mesh_buffer
};