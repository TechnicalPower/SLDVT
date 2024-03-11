import pyglet
from pyglet.window import mouse
import motion_capture


window = pyglet.window.Window( resizable=True, style=pyglet.window.Window.WINDOW_STYLE_DEFAULT)
window.set_minimum_size(960, 560)
window.set_maximum_size(1920, 1080)
label = pyglet.text.Label('MIDAS',
                          font_name='Times New Roman',
                          font_size=90,
                          x=window.width//2, y=window.height-100,
                          anchor_x='center', anchor_y='center')

button_y_offset = 150
button_width = 200
button_height = 50
button_x = window.width // 2 - button_width // 2
button_y = label.y - button_y_offset - button_y_offset

start = pyglet.shapes.Rectangle(button_x, button_y, button_width, button_height, color=(255, 215, 0, 255))
quit  = pyglet.shapes.Rectangle(button_x, button_y, button_width, button_height - 100, color=(255, 215, 0, 255))

start_label = pyglet.text.Label('Start',
                                 font_name='Times New Roman',
                                 font_size=24,
                                 color=(0,0,0,255),
                                 x=window.width // 2,
                                 y=button_y + button_height // 2,
                                 anchor_x='center', anchor_y='center')

quit_label = pyglet.text.Label('Quit',
                                 font_name='Times New Roman',
                                 font_size=24,
                                 color=(0,0,0,255),
                                 x=window.width // 2,
                                 y=button_y + (button_height // 2) - 200,
                                 anchor_x='center', anchor_y='center')

@window.event
def on_resize(width, height):
    label.x = width // 2
    label.y = height - 100
    label.draw()
    start.x = width // 2 - button_width // 2
    start.y = label.y - button_y_offset
    start_label.x = width // 2
    start_label.y = start.y + button_height // 2
    quit.x =  width // 2 - button_width // 2
    quit.y = label.y - button_y_offset - 100
    quit_label.x = width // 2
    quit_label.y = quit.y + button_height // 2 - 50

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1)
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    label.draw()
    start.draw()
    start_label.draw()
    quit.draw()
    quit_label.draw()

@window.event
def on_mouse_press(x, y, quit, modifiers):
    if quit == mouse.LEFT:
        if (button_x <= x <= button_x + button_width and
                button_y <= y <= button_y + button_height):
            pyglet.app.exit()

@window.event
def on_mouse_press(x, y, start, modifiers):
    if start == mouse.LEFT:
        if (button_x <= x <= button_x + button_width and
                button_y <= y <= button_y + button_height):
            motion_capture.main_beta()
    

pyglet.app.run()
