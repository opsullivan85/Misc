import pyglet
from pyglet.window import mouse
from pyglet.window import key
import pyglet.gl as gl

window = pyglet.window.Window()

label = pyglet.text.Label('Yeetus',
                          #font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

image = pyglet.resource.image('grass_side.png')
sprite = pyglet.sprite.Sprite(image, x=50, y=50, blend_src=770, blend_dest=771)
sprite.scale=17
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

@window.event
def on_draw():
    window.clear()
    #image.blit(0,0)
    sprite.draw()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print(window.push_handlers(pyglet.window.event.WindowEventLogger()))
    return
    print('A key was pressed', symbol, modifiers)


@window.event
def on_mouse_press(x, y, button, modifiers):
    window.push_handlers(pyglet.window.event.WindowEventLogger())
    return
    print(f'\nx: {x}',
          f'\ny: {y}',
          f'\nbutton: {button}',
          f'\nmodifiers: {modifiers}')


pyglet.app.run()
