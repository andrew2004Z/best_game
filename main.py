import sys
import sdl2
import sdl2.ext


class Window:
    def __init__(self, size, color, name):
        self.size = size
        self.color = color
        self.name = name

    def run(self):
        sdl2.ext.init()
        window = sdl2.ext.Window(self.name, size=self.size)
        window.show()
        running = True
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
            window.refresh()
        return 0


def main():
    window = Window((1080, 720), (240, 40, 40), "Best Game")
    window.run()

if __name__ == "__main__":
    window = Window((1080, 720), (240, 40, 40), "Best Game")
    sys.exit(main())
