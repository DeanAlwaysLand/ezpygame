# ezpygame

This documentation is currently at version v1.0
Python pygame but easier access

# How to setup:

copy ezpygame.py into the same directory (folder) as the project you want to use it on.
next, on your project, put this setup code:

from ezpygame import EZPYGAME

screen = EZPYGAME()

replace screen with the identifier you want to use.

# How to use?

If you get a Confusion error, please report it in the issues tab or idk cuz im new to github :(
for this, i'm gonna use screen as the identifier.

SCREEN.SETUP:
  winit(window x, window y, window name, fps, fullscreen, resizable, noframe, scaled) // Initializes a window. scaled makes the window be windowed fullscreen
  set_window(window) // set a window instance

SCREEN.SHAPES:
  Extras explained at the end.
  Shapes always go by name, so if you want to edit a shape, use the name.
  Types:
    rect: Rectangle
    image: Image
  
  create(extra1 extra2 extra3 name type position size color) // create a shape.
  # WIP
  
  
