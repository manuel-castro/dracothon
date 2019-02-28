from dracothon import PySciKit
import numpy as np

def generateRandomMesh():
    randomPoints = np.random.uniform(low=1000.0, high=2000.0, size=(18000,))
    randomFaces = []
    for i in range(11000):
        randomFace = np.random.choice(a=6001, size=3, replace=False)
        randomFaces = np.concatenate((randomFaces, randomFace))
    mesh = {}
    mesh['points'] = randomPoints
    mesh['faces'] = randomFaces
    return mesh

ps = PySciKit()
mesh = generateRandomMesh()
dracoBytes = ps.get_draco_encoded_meshCV(mesh['points'], mesh['faces'])