import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
import os
from PIL import Image, ImageDraw
from sdl2.ext.compat import isiterable


from math import sqrt

def check_click(X1, Y1, X, Y,R):
    if (X - X1)**2 +(Y - Y1)**2 <= R**2:
        return True
    else:
        return False


class Window:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(name, size=size)

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE

    def draw_menu(self, i, j):
        image = Image.open('lvl_1.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                Window.d1_point(self, x + i, y + j, self.window.get_surface(), pix[x, y][:3])

    def draw_you_win(self, i, j, color=None):
        sp = []
        image = Image.open('approachcircle.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if color == None:
                    Window.d1_point(self, x + i, y + j, self.window.get_surface(), pix[x, y][:3])
                else:
                    Window.d1_point(self, x + i, y + j, self.window.get_surface(), (0, 0, 0))


    def run_1(self):
        sdl2.ext.init()
        self.window.show()
        running = True
        sp = []
        flag = True
        Window.fill_Window(self, (0,0,0))
        Window.draw_menu(self, 500, 50)
        time = sdl2.timer.SDL_GetTicks() / 1000
        #if round(time) == 4 and flag is True:
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                if event.key.keysym.sym == sdl2.SDLK_m:
                    motion = event.motion
                    Window.fill_Window(self, (0,0,0))
                    Window.draw_you_win(self, 100, 100, None)
                if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    motion = event.motion
                    print(motion.x, motion.y)
                    #for i in range(1000):
                    #    for j in range(1000):
                    #        if check_click(i, j, 65):
                    #            sp.append([i, j])
                    #for i in sp:
                    #    print(i)
                    #Window.fill_Window(self, (0,0,0))
                    Window.draw_you_win(self, 100, 100, None)
                    print(check_click( 170, 170, motion.x, motion.y, 65))
                    if check_click( 170, 170, motion.x, motion.y, 65):
                        #sp.append(motion.x, motion.y)
                        Window.draw_you_win(self, 100, 100, 0)
                if event.key.keysym.sym == sdl2.SDLK_x:
                    Window.draw_you_win(self, 100, 100, 0)
            
            self.window.refresh()
        return 0


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 0, 0))
        super(SoftwareRenderer, self).render(components)


class song():
    pass


class note_sprite(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=100, posy=100):
        self.sprite = sprite
        self.sprite.position = posx, posy


class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0


class Note(sdl2.ext.Applicator):
    def __init__(self):
        super().__init__()
        print(self.componenttypes)
        self.componenttypes = note_sprite, sdl2.ext.Sprite
        print(self.componenttypes)

    def start_timer(self):
        self.status = True
        self.paused = False
        self.startTicks = sdl2.timer.SDL_GetTicks()

    # def stop(self):
    #     self.status = False
    #     self.paused = False

    def get_ticks(self):
        return sdl2.timer.SDL_GetTicks() - self.startTicks

    def process(self, world, componentsets):
        collitems = [comp for comp in componentsets if self._overlap(comp)]
        #print(collitems)
        for sprite in componentsets:
            print(sprite)
            print("smh")
            sprite.x += 50

class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.ai = False


class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0, ai=False):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        self.playerdata = PlayerData()
        self.playerdata.ai = ai


class game_pr():
    def __init__(self, world, window):
        note = Note()
        world.add_system(note)
        sdl2.ext.init()
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        running = True
        flag = True
        while running:
            events = sdl2.ext.get_events()
            note.start_timer()
            time = sdl2.timer.SDL_GetTicks() / 1000
            events = sdl2.ext.get_events()
            for event in events:
                if event.key.keysym.sym == sdl2.SDLK_w:
                    Window.run_1()
                if event.key.keysym.sym == sdl2.SDLK_z:
                    note.start_timer()
                    print("n")
                if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    motion = event.motion
                    print(motion.x, motion.y)
                    print(sdl2.timer.SDL_GetTicks() / 1000)
                    print(note.get_ticks() / 1000)
                if event.key.keysym.sym == sdl2.SDLK_m:
                    running = False
                    break
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
            world.process()
        return None


def run():
    window = sdl2.ext.Window("The Pong Game", size=(1600, 900))
    menu = sdl2.ext.World()
    world = sdl2.ext.World()


    note = Note()
    spriterenderer = SoftwareRenderer(window)
    menu.add_system(spriterenderer)
    world.add_system(spriterenderer)
    menu.add_system(note)
    world.add_system(note)


    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    lvl_1 = factory.from_image("lvl_1.png")
    note_sp = note_sprite(menu, lvl_1)
    running = True
    state = sdl2.mouse.SDL_GetMouseState(None, None)

    menu_high = Player(menu, lvl_1, 50, 150)
    sdl2.ext.init()
    window.show()

    while running:
        events = sdl2.ext.get_events()

        for event in events:
            if event.key.keysym.sym == sdl2.SDLK_z:
                note.start_timer()
                print("n")
            if event.key.keysym.sym == sdl2.SDLK_q:
                game_pr(world, window)
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                motion = event.motion
                print(motion.x, motion.y)
                if motion.x >= 589 and motion.x <= 1429 and motion.y >= 218 and motion.y <= 423:
                    game_pr.suka(world, window)
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        menu.process()
    return 0


def main():
    window = Window((1980, 1080), ' jdhkjdshngfluwd')
    window.run_1()


if __name__ == "__main__":
    sys.exit(main())