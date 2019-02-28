#include <vector>
#include <fstream>
#include "draco/mesh/triangle_soup_mesh_builder.h"
#include "draco/compression/encode.h"
#include "draco/core/encoder_buffer.h"
#include "draco/core/vector_d.h"
#include "testScikit.h"

TestScikit::TestScikit() {}

TestScikit::~TestScikit() {}

int TestScikit::get_draco_encoded_meshCV(const std::vector<float> &points, const std::vector<unsigned int> &faces, const char **bytes_ptr, std::size_t *bytes_len)
{

  draco::TriangleSoupMeshBuilder mb;
  mb.Start(faces.size());
  const int pos_att_idLOL =
    mb.AddAttribute(draco::GeometryAttribute::POSITION, 3, draco::DataType::DT_FLOAT32);

  for (std::size_t i = 0; i < faces.size(); i += 3) {
    // zi::vl::vec<unsigned, 3> cur_face = faces[i];
    auto point1Index = faces[i]*3;
    auto point2Index = faces[i+1]*3;
    auto point3Index = faces[i+2]*3;
    // mb.SetAttributeValuesForFace(pos_att_id, draco::FaceIndex(i), static_cast<void *>(&point1), static_cast<void *>(&point2), static_cast<void*>(&point3));
    mb.SetAttributeValuesForFace(pos_att_idLOL, draco::FaceIndex(i), draco::Vector3f(points[point1Index], points[point1Index+1], points[point1Index+2]).data(), draco::Vector3f(points[point2Index], points[point2Index+1], points[point2Index+2]).data(), draco::Vector3f(points[point3Index], points[point3Index+1], points[point3Index+2]).data());  
  }

  // printf("after faces\n");
  std::unique_ptr<draco::Mesh> ptr_mesh = mb.Finalize();
  draco::Mesh *mesh = ptr_mesh.get();
  draco::Encoder encoder;
  encoder.SetAttributeQuantization(draco::GeometryAttribute::POSITION, 14);
  encoder.SetSpeedOptions(8, 8);
  draco::EncoderBuffer buffer;
  const draco::Status status = encoder.EncodeMeshToBuffer(*mesh, &buffer);
  printf("after encoder setup\n");
//   const std::string &file = "meshTest" + std::to_string(remapped_id) + ".drc";
  std::ofstream out_file("dracoTestScikit.drc", std::ios::binary);
  out_file.write(buffer.data(), buffer.size());
  printf("after writing\n");
  // std::vector<char> dummy{'t'};
  // return dummy;
  // return *(buffer.buffer());
  *bytes_ptr = buffer.data();
  *bytes_len = buffer.size();
  return 0;
}