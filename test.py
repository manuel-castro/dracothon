import DracoPy
import numpy as np

def generateRandomMesh():
    randomPoints = np.random.uniform(low=1000.0, high=30000.0, size=(18000,))
    randomFaces = []
    for i in range(11000):
        randomFace = np.random.choice(a=6001, size=3, replace=False)
        randomFaces = np.concatenate((randomFaces, randomFace))
    mesh = {}
    mesh['points'] = randomPoints
    mesh['faces'] = randomFaces
    return mesh

def mesh_to_obj(mesh, progress=False):
  objdata = []

  for vertex in mesh['vertices']:
    objdata.append('v %s %s %s' % (vertex[0], vertex[1], vertex[2]))

  faces = [face + 1 for face in mesh['faces']] # obj counts from 1 not 0 as in python
  for i in range(0, len(faces), 3):
    objdata.append('f %s %s %s' % (faces[i], faces[i+1], faces[i+2]))

  return objdata

# mesh = generateRandomMesh()
# dracoBytes = DracoPy.encode_mesh(mesh['points'], mesh['faces'])
# with open('testCube.obj', 'wb') as g:
#   g.write(data)

# with open('489766459477108749.drc', 'rb') as f:
#     file_content = f.read()
#     mesh_object = ps.decode_buffer(file_content)
#     # print(len(mesh_object['points']))
#     # print(len(mesh_object['faces']))
#     # print(mesh_object['points'][0:6])
#     # print(mesh_object['faces'][0:6])
#     # print(max(mesh_object['faces']))
#     # mesh_object['num_vertices'] = len(mesh_object['points']) // 3
#     # mesh_object['vertices'] = (np.array(mesh_object['points'])).reshape(mesh_object['num_vertices'], 3)
#     # mesh_object['faces'] = np.array(mesh_object['faces'])
#     objdata = mesh_to_obj(mesh_object)
#     objdata = '\n'.join(objdata) + '\n'
#     data = objdata.encode('utf8')
#     with open('testCube.obj', 'wb') as g:
#       g.write(data)

with open('489766459477108749.drc', 'rb') as f:
    file_content = f.read()
    mesh_object = DracoPy.decode_buffer_to_mesh(file_content)
    dracoBytes = DracoPy.encode_mesh_to_buffer(mesh_object.points, mesh_object.faces, 14, 1, 98298, (393216, 196608, 0), True)
    with open('testEnc.drc', 'wb') as g:
      g.write(dracoBytes)

with open('testEnc.drc', 'rb') as h:
    file_content = h.read()
    mesh_object = DracoPy.decode_buffer_with_encoded_options_to_mesh(file_content)
    print(mesh_object.encoding_options.quantization_bits)
    print(mesh_object.encoding_options.quantization_origin)
    print(mesh_object.encoding_options.quantization_range)
    print(len(mesh_object.points))
    print(len(mesh_object.faces))
