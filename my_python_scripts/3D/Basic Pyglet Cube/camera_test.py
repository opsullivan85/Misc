import pyglet
from pyglet.gl import *
import ratcave as rc
from camera import FirstPersonCamera

window = pyglet.window.Window(fullscreen=False)
window.set_exclusive_mouse(False)
camera = FirstPersonCamera(window)
print(camera.__position)
# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Meshes from WavefrontReader
monkey = obj_reader.get_mesh("Monkey", position=(0, 0, -1.5), scale=.6)
torus = obj_reader.get_mesh("Torus", position=(-1, 0, -1.5), scale=.4)

# Create Scenes with Meshes.
scene = rc.Scene([monkey, torus])
#scene.camera = camera

@window.event
def on_draw():
    with rc.default_shader:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        camera.draw()
        #scene.draw()
    
    return pyglet.event.EVENT_HANDLED

def move_camera(dt):
    camera.update(dt)
    with rc.default_shader:
        monkey.draw()
    

if __name__ == '__main__':
    pyglet.clock.schedule(move_camera)
    pyglet.app.run()
