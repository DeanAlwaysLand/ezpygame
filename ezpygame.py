import pygame
import sys

class FontNotFoundError(Exception):
    """Raised when the requested font is not found in the system."""
    pass

class Confusion(Exception):
    """Raised when a Zyreth module has a confusion.
    This happens very rarely."""

class error(Exception):
    """Basic error."""

class EZPYGAME():
    def __init__(self, mode: str = ""):
        if mode == "RamSave":
            self.mode = 1
        else:
            print("EZPYGAME v1.0 --\nCreds: Zyreth")
            self.mode = 0
        

        pygame.init()
        self.clock = pygame.time.Clock()
        self.setup = self.Setup(self)
        self.shapes = self.Shapes(self)
        self.fonts = []
        self.fontsname = []
        if mode != 1:
            self.warns = [False] * 20
        else: self.warns = 0

    def test(self):
        print("Working!")
        print("")
    
    class Setup:
        def __init__(self, main):
            self.main = main
        def winit(self, windowx = 800, windowy = 600, name="EZPygame Window", fps = 60, fullscreen = False, resizable = False, noframe = False, scaled = False):
            global screen, running
            running = True
            flags = 0
            if fullscreen:
                flags |= pygame.FULLSCREEN
            if resizable:
                flags |= pygame.RESIZABLE
            if noframe:
                flags |= pygame.NOFRAME
            if scaled:
                flags |= pygame.SCALED

            screen = pygame.display.set_mode((windowx, windowy), flags)
            pygame.display.set_caption(name)
            self.main.clock.tick(fps)
        
        def set_window(self, window):
            global screen
            screen = window

    def tick(self, clear=False, color=(0, 0, 0)) -> list:
        self.keys = []
        self.events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.keys.append(key_name)
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for shape_name, shape_data in self.shapes.shapes.items():
                    sx, sy = shape_data["pos"]
                    sw, sh = shape_data["size"]

                    # Bounds for click detection
                    left = sx
                    right = sx + sw
                    top = sy
                    bottom = sy + sh

                    if left <= x <= right and top <= y <= bottom:
                        self.shapes.shapes[shape_name]["flag1"] = True
                        if self.shapes.shapes[shape_name]["type"] == "textbox":
                            self.shapes.shapes[shape_name]["extra2"] = not self.shapes.shapes[shape_name]["extra2"]


            self.events.append(event)

        pygame.display.flip()
        if clear:
            screen.fill(color)
        self.shapes.tick()
        return self.events
    

    
    def add_font(self, font = "arial", size = 32, name = "arial", type = 0):
        if name in self.fontsname:
            raise ValueError(f"EZPYGAME: add_font: Font {name} already exists!")
        
        if type == 0:
            self.fonts.append(pygame.font.SysFont(font, size))
        elif type == 1:
            self.fonts.append(pygame.font.Font(font, size))
        else:
            raise error("Unknown type, expected 0 or 1")
        
        self.fontsname.append(name)
            
    def draw_text(self, *text, font="arial", color=(255, 255, 255), pos=(200, 200), name=""):
        if name != "":
            if isinstance(self.warns, int):
                raise
            print(r"Warning: name in draw_text will be removed at ezpygame 1.2, please change to font='arial' ")
            font = name
        
        if font not in self.fontsname:
            raise error(f"FONTS: Font '{font}' not found.")
        flat_text = " ".join(str(item) for sublist in text for item in (sublist if isinstance(sublist, list) else [sublist]))
        surf = self.fonts[self.fontsname.index(font)].render(flat_text, True, color)
        screen.blit(surf, pos)


    def draw_rect(self, color: tuple | int = (255, 255, 255), possize: tuple[int, int, int, int] = (200, 200, 100, 100), width: int = 0) -> None:
        if not isinstance(width, int):
            raise error(f"Expected e1 or width to be integer. Got {type(width)}")
        pygame.draw.rect(screen, color, possize, width)
    
    def draw_ibeam(self, pos: tuple[int, int], color=(255, 255, 255)) -> None:
        x, y = pos
        pygame.draw.line(screen, color, (x, y - 10), (x, y + 10), 2)  # vertical line
        pygame.draw.line(screen, color, (x - 3, y - 10), (x + 3, y - 10), 2)  # top tick
        pygame.draw.line(screen, color, (x - 3, y + 10), (x + 3, y + 10), 2)  # bottom tick

    
    class Shapes:
        def __init__(self, main):
            self.shapes = {}
            self.shapenames = []
            self.main = main
            self.images = {}
        
        def create(self, extra1= None, extra2 = None, extra3 = None , name: str ="Shape", type: str ="rect", pos: list | int =[200, 500], size: list | int = [200, 50], color: list | int = [255, 255, 255]):
            if name in self.shapes:
                raise error(f"SHAPES: Shape {name} already exists!")

            if extra1 is None:
                extra1 = 0
            if extra2 is None:
                extra2 = 0
            if extra3 is None:
                extra3 = 0
            

            self.shapes[name] = {
                "type": type,       # Type (ex. rectangle, button)
                "pos": pos,         # Position (ex. 200, 500)
                "size": size,       # Size
                "color": color,     # Color (RGB)
                "extra1": extra1,   # extra1 (ex. transparency)
                "extra2": extra2,   # extra2
                "extra3": extra3,   # extra3
                "flag1": False      # clicked?
                }
            
            self.shapenames.append(name)

            return name
        
        def delete(self, name="Shape"):
            if name not in self.shapes:
                print(f"EZPYGAME: Delete {name}: {name} not found.")
                return 0

            del self.shapes[name]  # This removes the subdictionary
            if name in self.shapenames:
                self.shapenames.remove(name)
            else: raise Confusion("Shape: Unsynced panic")
            

            return 1

        def modify_shape(self, name, **kwargs):
            if name not in self.shapes:
                print(f"SHAPE: Shape '{name}' does not exist.")
                return

            shape = self.shapes[name]

            # Update only the keys provided
            for key, value in kwargs.items():
                if key in shape:
                    shape[key] = value
                else:
                    print(f"SHAPE: Warning: '{key}' is not a valid property for shape '{name}'.")

            self.shapes[name] = shape

        def tick(self):
            if len(self.shapes) != len(self.shapenames):
                    raise Confusion("Shape: Unsynced panic")

            for shape_name in self.shapenames:
                shape = self.shapes[shape_name]
                temp = self.shapes[shape_name]["type"]
                x, y = self.shapes[shape_name]["pos"]
                width, height = self.shapes[shape_name]["size"]
                r, g, b = self.shapes[shape_name]["color"]
                e1 = self.shapes[shape_name]["extra1"]
                e2 = self.shapes[shape_name]["extra2"]
                e3 = self.shapes[shape_name]["extra3"]
                f1 = self.shapes[shape_name]["flag1"]
                if temp == "rect":
                    self.main.draw_rect((r, g, b), (x, y, width, height), e1)
                elif temp == "image":
                    if e1 in self.images:
                        file = self.images[e1]
                        image = pygame.transform.scale(file, (width, height))
                        screen.blit(image, (x, y))
                    else:
                        print(f"EZPYGAME: Image key '{e1}' not found.")
                elif temp == "textbox":
                    mx, my = pygame.mouse.get_pos()

                    # Bounds for click detection
                    left = x
                    right = x + width
                    top = y
                    bottom = y + height

                    if left <= mx <= right and top <= my <= bottom:
                        pygame.mouse.set_visible(False)
                        self.main.draw_ibeam(mx, my)
                    else:
                        pygame.mouse.set_visible(True)
                    
                    if e2 == True:
                        self.shapes[shape_name]["extra1"] += ''.join(str(item) for item in self.main.keys)
                elif temp == "text":
                    self.main.draw_text(e1, font=e2, pos = [x, y])
                        

        
        def atts(self, shape="Shape"):
            try:
                return self.shapes[shape]
            except KeyError:
                return 0
        
        def load_image(self, name="Image", path=""):
            try:
                image = pygame.image.load(path).convert_alpha()
                self.images[name] = image
            except pygame.error as e:
                raise error(f"EZPYGAME: ERROR: path {path}: {e}")

if __name__ == "__main__":
    ezpygame = EZPYGAME()
    ezpygame.setup.winit(1920, 1080, "Ezpygame Testing Experience")
    ezpygame.add_font()
    ezpygame.shapes.create()
    events = []
    while True:
        if events: last_events = events
        events = ezpygame.tick(clear=True, color=(128, 128, 128))
        pos = [200, 200]
        ezpygame.draw_text("Events: ", name="arial", pos = [200, 150])
        
        if not events:
            for event in last_events:
                ezpygame.draw_text(event, name="arial", pos = pos)
                pos[1] += 50
        else:
            for event in events:
                ezpygame.draw_text(event, name="arial", pos = pos)
                pos[1] += 50
