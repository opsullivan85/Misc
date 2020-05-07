import pyglet
import ratcave as rc
from pyglet.window import key

# Create Window
window = pyglet.window.Window()

keys = key.KeyStateHandler()
window.push_handlers(keys)

'''
def update(dt):
    pass
pyglet.clock.schedule(update)
'''

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Meshes from WavefrontReader
monkey = obj_reader.get_mesh("Monkey", position=(0, 0, -1.5), scale=.6)
torus = obj_reader.get_mesh("Torus", position=(-1, 0, -1.5), scale=.4)

# Create Scenes with Meshes.
scene = rc.Scene([monkey, torus])

def rotate_meshes(dt):
    #dt is the time between frames
    monkey.orientation.x += 15 * dt  
    torus.orientation.y += 80 * dt
pyglet.clock.schedule(rotate_meshes)

def move_camera(dt):
    camera_speed = 3
    #print(key.__dict__)
    if keys[key.W]:
        scene.camera.position.z -= camera_speed * dt
    if keys[key.A]:
        scene.camera.position.x -= camera_speed * dt
    if keys[key.S]:
        scene.camera.position.z += camera_speed * dt
    if keys[key.D]:
        scene.camera.position.x += camera_speed * dt
    if keys[key.SPACE]:
        scene.camera.position.y += camera_speed * dt
    if keys[key.LSHIFT]:
        scene.camera.position.y -= camera_speed * dt
pyglet.clock.schedule(move_camera)

def rotate_camera(dx, dy):
    scene.camera.rotation.y -= dx
    scene.camera.rotation.x += dy

@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    rotate_camera(dx, dy)

pyglet.app.run()
