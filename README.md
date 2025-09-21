# ezpygame

V1.1

**ezpygame** is a lightweight wrapper around `pygame` that simplifies window setup, shape creation, font management, and event handling. Designed for rapid prototyping and creative experimentation, it reduces boilerplate while keeping full control in your hands.

Created by Zyreth.

## Features

- One-line window initialization with customizable flags
- Shape system for rectangles, images, textboxes, and text
- Named font registration and management
- Simplified event loop with mouse and keyboard tracking
- Drawing utilities for text, rectangles, and I-beam cursors
- Image loader with auto-scaling
- Custom exceptions for clarity and debugging

## Quickstart

from ezpygame import EZPYGAME

ez = EZPYGAME()
ez.setup.winit(800, 600, "My Game Window")
ez.add_font("arial", 32, "mainfont")
ez.shapes.create(name="myrect", type="rect", pos=[100, 100], size=[200, 50], color=[255, 0, 0])

while True:
    ez.tick(clear=True, color=(0, 0, 0))
    ez.draw_text("Hello World!", font="mainfont", pos=(120, 120))

## Core Components

### Setup
- winit(width, height, title, flags=[]): Initializes the window. Flags include "fullscreen", "resizable", "noframe", etc.

### Font Management
- add_font(path_or_name, size, name): Registers a font with a name.
- get_font(name): Retrieves a font object.

### Shape System
- create(...): Adds a shape with type "rect", "image", "textbox", or "text".
- get(name): Retrieves a shape object.
- delete(name): Removes a shape.

### Drawing
- draw_text(text, font, pos, color=(255,255,255))
- draw_rect(rect, color)
- draw_ibeam(x, y, height, color)

### Event Loop
- events = tick(clear=False, color=(0,0,0)): Advances the frame and handles events automatically. Plus, it returns the events if you want custom ones
- mouse: Tracks mouse position and clicks.
- keys: Tracks key presses.

### Image Loading
- load_image(path, name): Loads an image with name. Plus, you can draw that image using shape.create(e1=`image name`)

