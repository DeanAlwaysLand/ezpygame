# ezpygame
Version: v1.0

# Setup
To get started, copy ezpygame.py into the same folder as your project. Then, in your main Python file, import and initialize it like this:

from ezpygame import EZPYGAME

screen = EZPYGAME()
You can replace screen with any variable name you prefer.

# Usage Guide
If you encounter a Confusion error, please report it in the Issues tab. I'm still learning GitHub, so bear with me.

In the examples below, screen will be used as the identifier.

# screen.setup
To initialize the game window, use:

screen.setup.winit(windowx=800, windowy=600, name="My Game", fps=60, fullscreen=False, resizable=True, noframe=False, scaled=False)
This creates a window with the specified width and height, sets the title, and configures options like fullscreen, resizable, borderless, and scaled (which makes the window behave like windowed fullscreen). The fps parameter sets the frame rate.

You can also manually set a window instance using:

screen.setup.set_window(my_window)
# screen.shapes
This module lets you create and manage shapes.

To create a shape, use:

screen.shapes.create(extra1, extra2, extra3, name, type, position, size, color)
The type can be either "rect" for rectangles or "image" for images. name is a unique identifier for the shape. position is a list like [x, y]. size is [width, height]. color is [r, g, b]. extra1 is used for things like border width (for rectangles) or image key (for images). extra2 and extra3 are placeholders for future features or custom data.

To delete a shape:

screen.shapes.delete("shape_name")
To update and draw all shapes, call:

screen.shapes.tick()
To get the attributes of a shape as a dictionary:

data = screen.shapes.atts("shape_name")
To load an image for use in a shape:

screen.shapes.load_image("image_key", "path/to/image.png")
Once loaded, you can use "image_key" as extra1 when creating an image-type shape.

This function handles events and updates the display. Call it once per frame in your game loop:

events = screen.tick(clear=True, color=(0, 0, 0))
If clear is set to True, the screen will be filled with the specified background color. It returns a list of pygame events, which you can use for input handling.

# Fonts and Text
To add a font:

screen.add_font(font="arial", size=32, name="myfont", type=0)
type should be 0 for system fonts or 1 for custom font files.

To draw text on the screen:
 
screen.draw_text("Hello!", name="myfont", color=(255, 255, 255), pos=(100, 100))
Make sure the font name matches one you've added earlier.

Extras and Notes
Shapes have a built-in click detection system. When the mouse is pressed, the shape's flag1 will be set to True if the click was inside its bounds.

This project is still a work in progress. More features are planned, and suggestions are welcome. If something breaks, it's probably the rectangles' fault.
