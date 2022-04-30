#The loadURDF.py file is an opersource code and it not created by the team. It loads and displays the URDF model in the simulated environment.
#source code: https://github.com/bulletphysics/bullet3/blob/master/docs/pybullet_quickstart_guide/PyBulletQuickstartGuide.md.html
import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)# p.DIRECT for non graphical version 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-10)
placeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("diffDrivecar.xacro",cubeStartPos,cubeStartOrientation)

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240. )
cubePos, cube0rn = p.getBasePositionAndOrientation(boxId)

p.disconnect()


