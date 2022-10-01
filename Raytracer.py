from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

# Opacos
green = Material(diffuse=(0, 1, 0), spec=8)
moon = Material(texture=Texture("moon.bmp"))

# Reflectivos
gold = Material(diffuse=(0.7, 0.7, 0), spec=32, matType=REFLECTIVE)
mirror = Material(diffuse=(0.9, 0.9, 0.9), spec=64, matType=REFLECTIVE)

# Transparentes
canica = Material(diffuse=(0.9, 0.2, 0.9), spec=32,
                  ior=1.5, matType=TRANSPARENT)
glass = Material(diffuse=(0.9, 0.9, 0.9), spec=64,
                 ior=1.5, matType=TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("landscape2.bmp")

rtx.lights.append(AmbientLight(intensity=0.1))
rtx.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.8))

rtx.scene.append(Sphere(V3(-3, 2, -10), 1, green))
rtx.scene.append(Sphere(V3(-3, -2, -10), 1, moon))

rtx.scene.append(Sphere(V3(0, 2, -10), 1, gold))
rtx.scene.append(Sphere(V3(0, -2, -10), 1, mirror))

rtx.scene.append(Sphere(V3(3, 2, -10), 1, canica))
rtx.scene.append(Sphere(V3(3, -2, -10), 1, glass))


rtx.glRender()

rtx.glFinish("output.bmp")
