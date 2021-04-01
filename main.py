import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx


class Window:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(self.name, size=self.size)

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        #sdl2.ext.fill(surface, BLACK)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE
        #del pixelview

    def d_point(self, x, y, color):
        r, g, b = color
        renderer = sdl2.ext.Renderer(self.window)
        renderer.draw_point([x, y], sdl2.ext.Color(r, g, b))
        renderer.present()
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.window)

    def run(self):
        sdl2.ext.init()
        #window = sdl2.ext.Window(self.name, size=self.size)
        self.window.show()
        running = True
        while running:
            events = sdl2.ext.get_events()
            Window.fill_Window(self, (0, 100, 240))
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_CONTROLLER_BUTTON_X:
                    Window.d1_point(self, 10, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d1_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d1_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d1_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d1_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                    #Window.d_point(self, 10, 20, (0, 0, 0))
                    #Window.d_point(self, 11, 20, (0, 0, 0))
                    #Window.d_point(self, 12, 20, (0, 0, 0))
                    #Window.d_point(self, 13, 20, (0, 0, 0))
                    #Window.d_point(self, 14, 20, (0, 0, 0))
                    #Window.d_point(self, 15, 20, (0, 0, 0))
            self.window.refresh()
        return 0


    


def main():
    window = Window((1080, 720), "Best Game")
    
    window.run()
    #window.fill_Window((240, 0, 0))
    #fill_Window(window, 240, 0, 0)

if __name__ == "__main__":
    #window = Window((1080, 720), (240, 40, 40), "Best Game")
    sys.exit(main())
