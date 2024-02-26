import pyglet
from pyglet.window import mouse
import motion_capture

#method that creates a button and a label inside it. 
def create_button(label_text, y_offset, color=(0, 1, 0)):
    button_x = window.width // 2 - button_width // 2
    button_y = window.height // 2 + y_offset
    button = pyglet.shapes.Rectangle(button_x, button_y, button_width, button_height, color=color)
    label = pyglet.text.Label(label_text,
                              font_name='Times New Roman',
                              font_size=24,
                              color=(0, 0, 0, 255),
                              x=button_x + button_width // 2,
                              y=button_y + button_height // 2,
                              anchor_x='center', anchor_y='center')
    return button, label

window = pyglet.window.Window(resizable=True)  #window load
window.set_maximum_size(1920, 1080)            #set maximum size
window.set_minimum_size(960, 560)              #set minimum size


#Title "MIDAS" created 
title_label = pyglet.text.Label('MIDAS',
                                font_name='Times New Roman',
                                font_size=82,
                                x=window.width // 2, y=window.height - 60,
                                anchor_x='center', anchor_y='center')

button_width = 250          #button width in pixels default is 200
button_height = 50          #button height in pixels default is 50
start_button, start_label = create_button('Start', -50, color=(255, 215, 0))    #start_button and start_label created using create_button function
quit_button, quit_label = create_button('Quit', -150, color=(255, 215, 0))      #quit_button and quit_label created using create_button function


#button position update as the window is resized
def update_button_positions():
    title_label.y = window.height - 60
    title_label.x = window.width // 2
    start_button_offset = 0  #Start button absolute position from the middle of the screen
    quit_button_offset = -150  #Quit button absolute position from the middle of the screen
    
    #start button position update
    start_button.x = window.width // 2 - button_width // 2
    start_button.y = window.height // 2 + start_button_offset
    start_label.x = window.width // 2
    start_label.y = start_button.y + button_height // 2
    
    #quit button position update
    quit_button.x = window.width // 2 - button_width // 2
    quit_button.y = window.height // 2 + quit_button_offset
    quit_label.x = window.width // 2
    quit_label.y = quit_button.y + button_height // 2

#window resize event handler
@window.event
def on_resize(width, height):
    update_button_positions()

#window draw
@window.event
def on_draw():
    window.clear()
    title_label.draw()
    start_button.draw()
    start_label.draw()
    quit_button.draw()
    quit_label.draw()

#mouse event handler
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if start_button.x <= x <= start_button.x + button_width and start_button.y <= y <= start_button.y + button_height: #when start button is pressed
            motion_capture.main_beta()     #run the main function
            print("Start button pressed")
        elif quit_button.x <= x <= quit_button.x + button_width and quit_button.y <= y <= quit_button.y + button_height:    #when quit button is pressed
            print("Quit button pressed")
            pyglet.app.exit()   #exit the program

            
#run the main function
pyglet.app.run()