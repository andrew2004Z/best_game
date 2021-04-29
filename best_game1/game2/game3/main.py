import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from PIL import Image
import pygame as pg
import time
import data
import os


class Window:
    def __init__(self, size, name, x, y, x1, y1):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(self.name, size=self.size)
        self.pos_x = x
        self.pos_y = y
        self.pos_x1 = x1
        self.pos_y1 = y1
        self.size_p = 20

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE

    def line_vert(self, x, y, l, color=(0, 0, 0)):
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y - 1,
                                self.window.get_surface(), color)
                sp.append([x - 1, y - 1])
                y = y - 1
        else:
            for i in range(l):
                Window.d1_point(
                    self, x, y + 1, self.window.get_surface(), color)
                sp.append([x, y + 1])
                y = y + 1
        return sp

    def line_vert2(self, x, y, l):
        sp = [[x, y]]
        if l < 0:
            for i in range(l * -1):
                sp.append([x - 1, y - 1])
                y = y - 1
        else:
            for i in range(l):
                sp.append([x, y + 1])
                y = y + 1
        return sp

    def line_goriz(self, x, y, l, color=(0, 0, 0)):
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y, self.window.get_surface(), color)
                x = x - 1
                sp.append([x - 1, y])
        else:
            for i in range(l):
                Window.d1_point(self, x, y, self.window.get_surface(), color)
                x = x + 1
                sp.append([x, y])
        return sp

    def line_goriz2(self, x, y, l):
        sp = [[x, y]]
        if l < 0:
            for i in range(l * -1):
                x = x - 1
                sp.append([x - 1, y])
        else:
            for i in range(l):
                x = x + 1
                sp.append([x, y])
        return sp

    def line_goriz1(self, x, y, l, r, color=(0, 0, 0)):
        for i in range(r + 1):
            Window.line_goriz(self, x, y + i, l, color)

    def line_vert1(self, x, y, l, r, color=(0, 0, 0)):
        for i in range(r + 1):
            Window.line_vert(self, x + i, y, l, color)

    def rectangle(self, x, y, w, h, color=(0, 0, 0)):
        xyw = [x + w, y]
        xyh = [x, y + h]
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        sp.append(Window.line_goriz(self, x, y, w, color))
        sp.append(Window.line_vert(self, x, y, h, color))
        sp.append(Window.line_goriz(self, xyh[0], xyh[1], w, color))
        sp.append(Window.line_vert(self, xyw[0], xyw[1], h, color))

    def rectangle2(self, x, y, w, h):
        xyw = [x + w, y]
        xyh = [x, y + h]
        sp = [[x, y]]
        sp += Window.line_goriz2(self, x, y, w)
        sp += Window.line_vert2(self, x, y, h)
        sp += Window.line_goriz2(self, xyh[0], xyh[1], w)
        sp += Window.line_vert2(self, xyw[0], xyw[1], h)
        # print(sp)
        return sp

    def rectangle1(self, x, y, w, h, color=(0, 0, 0)):
        sp = []
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        for i in range(x, x + w + 1):
            for j in range(y, y + h + 1):
                Window.d1_point(self, i, j, self.window.get_surface(), color)
                sp.append([i, j])
        return sp

    def rec_pos_plaer(self, x, y, w, h):
        sp = []
        for i in range(x, x + w + 1):
            for j in range(y, y + h + 1):
                try:
                    if pix[i - 1, y] != (0, 0, 0) or pix[i - 1, j - 1] != (0, 0, 0) or pix[i, j - 1] != (0, 0, 0) or \
                            pix[i + 1, j] != (0, 0, 0) or pix[i, j + 1] != (0, 0, 0) or pix[i + 1, j + 1] != (
                    0, 0, 0) or pix[i - 1, j + 1] != (0, 0, 0) or pix[i + 1, j - 1] != (0, 0, 0):
                        sp.append([i, j])
                except:
                    pass
        return sp

    def draw_0(self, x1, y1):
        sp = []
        image = Image.open('data/0.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x + x1, y + y1, self.window_timer.get_surface(), pix[x, y])

    def draw_1(self, x1, y1):
        sp = []
        image = Image.open('data/1.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x + x1, y + y1, self.window_timer.get_surface(), pix[x, y])

    def drawDDA(self, x1, y1, x2, y2, color=(0, 0, 0)):
        x, y = x1, y1
        length = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else (y2 - y1))
        dx = (x2 - x1) / float(length)
        dy = (y2 - y1) / float(length)
        Window.d1_point(self, round(x), round(
            y), self.window.get_surface(), color)
        for i in range(int(length)):
            x += dx
            y += dy
            Window.d1_point(self, round(x), round(
                y), self.window.get_surface(), color)

    def draw_l1(self):
        sp = []
        sp1 = []
        image = Image.open('data/1.1.png')
        size = image.size
        pix = image.load()
        for i in range(515, 579):
            sp1.append([i, 712])
            Window.d1_point(self, i, 712, self.window.get_surface(), (255, 0, 0))
        for i in range(515, 579):
            sp1.append([i, 713])
            Window.d1_point(self, i, 713, self.window.get_surface(), (255, 0, 0))
        for i in range(515, 579):
            sp1.append([i, 714])
            Window.d1_point(self, i, 714, self.window.get_surface(), (255, 0, 0))
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] == (0, 0, 0):
                    # print(pix[x - 1, y])
                    try:
                        if pix[x - 1, y] != (0, 0, 0) or pix[x - 1, y - 1] != (0, 0, 0) or pix[x, y - 1] != (0, 0, 0) or \
                                pix[x + 1, y] != (0, 0, 0) or pix[x, y + 1] != (0, 0, 0) or pix[x + 1, y + 1] != (
                        0, 0, 0) or pix[x - 1, y + 1] != (0, 0, 0) or pix[x + 1, y - 1] != (0, 0, 0):
                            sp.append([x, y])
                    except:
                        pass
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))
        return sp, sp1

    def draw_menu(self):
        Window.fill_Window(self, (0, 100, 240))
        sp = []
        image = Image.open('data/Menu.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))

    def draw_pravila(self):
        Window.fill_Window(self, (0, 100, 240))
        image = Image.open('data/pravila.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))

    def draw_you_win(self):
        global level
        image = Image.open('data/YOU WIN.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))
        level = 0

    def draw_game_over(self):
        global level
        image = Image.open('data/game_over.jpg')
        size = image.size
        pix = image.load()
        Window.fill_Window(self, (0, 0, 0))
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (0, 0, 0):
                    Window.d1_point(self, x, y, self.window.get_surface(), pix[x, y])
        level = 0

    def draw_l2(self):
        sp = []
        sp1 = []
        image = Image.open('data/2.1.png')
        size = image.size
        pix = image.load()
        for i in range(9, 45):
            sp1.append([0, i])
            Window.d1_point(self, 0, i, self.window.get_surface(), (255, 0, 0))
        for i in range(9, 45):
            sp1.append([1, i])
            Window.d1_point(self, 1, i, self.window.get_surface(), (255, 0, 0))
        for i in range(9, 45):
            sp1.append([2, i])
            Window.d1_point(self, 2, i, self.window.get_surface(), (255, 0, 0))
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] == (0, 0, 0):
                    try:
                        if pix[x - 1, y] != (0, 0, 0) or pix[x - 1, y - 1] != (0, 0, 0) or pix[x, y - 1] != (0, 0, 0) or \
                                pix[x + 1, y] != (0, 0, 0) or pix[x, y + 1] != (0, 0, 0) or pix[x + 1, y + 1] != (
                        0, 0, 0) or pix[x - 1, y + 1] != (0, 0, 0) or pix[x + 1, y - 1] != (0, 0, 0):
                            sp.append([x, y])
                    except:
                        pass
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))
        return sp, sp1

    def down(self, sp_wall, sp_exit):
        global level
        if not Window.check_collision(self, Window.rectangle2(self, self.pos_x + self.size_p, self.pos_y, self.size_p,
                                                              self.size_p), sp_exit):
            Window.fill_Window(self, (0, 100, 240))
            Window.draw_you_win(self)
            level = 0
            return 0
        elif Window.check_collision(self, Window.rectangle2(self, self.pos_x, self.pos_y + self.size_p, self.size_p,
                                                            self.size_p), sp_wall):
            try:
                Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(self, self.pos_x, self.pos_y + self.size_p, self.size_p, self.size_p)
                self.pos_y = self.pos_y + self.size_p
            except:
                Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p)

    def check_collision(self, sp1, sp2):
        for i in sp1:
            if i in sp2:
                return False
        return True

    def lvl1(self):
        Window.fill_Window(self, (0, 100, 240))
        sp_wall, sp_exit = Window.draw_l1(self)
        self.size_p = 20
        self.pos_x, self.pos_y = 530, 355
        sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
        return sp_wall, sp_exit, sp_pl

    def lvl2(self):
        Window.fill_Window(self, (0, 100, 240))
        sp_wall, sp_exit = Window.draw_l2(self)
        self.size_p = 5
        self.pos_x, self.pos_y = 695, 258
        sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(0, 0, 0))
        return sp_wall, sp_exit, sp_pl

    def up1(self, sp_exit, sp_wall):
        global level
        if not Window.check_collision(self, Window.rectangle2(self, self.pos_x + self.size_p, self.pos_y, self.size_p,
                                                              self.size_p), sp_exit):
            Window.fill_Window(self, (0, 100, 240))
            Window.draw_you_win(self)
            level = 0
            return 0
        elif Window.check_collision(self, Window.rectangle2(self, self.pos_x, self.pos_y - self.size_p, self.size_p,
                                                            self.size_p), sp_wall):
            try:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x, self.pos_y - self.size_p, self.size_p, self.size_p)
                self.pos_y = self.pos_y - self.size_p
            except:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p)

    def left(self, sp_exit, sp_wall):
        global level
        if not Window.check_collision(self, Window.rectangle2(self, self.pos_x + self.size_p, self.pos_y, self.size_p,
                                                              self.size_p), sp_exit):
            Window.fill_Window(self, (0, 100, 240))
            Window.draw_you_win(self)
            level = 0
            return 0
        elif Window.check_collision(self, Window.rectangle2(self, self.pos_x - self.size_p, self.pos_y, self.size_p,
                                                            self.size_p), sp_wall):
            try:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x - self.size_p, self.pos_y, self.size_p, self.size_p)
                self.pos_x = self.pos_x - self.size_p
            except:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p)

    def right(self, sp_exit, sp_wall):
        global level
        if not Window.check_collision(self, Window.rectangle2(self, self.pos_x + self.size_p, self.pos_y, self.size_p,
                                                              self.size_p), sp_exit):
            Window.fill_Window(self, (0, 100, 240))
            Window.draw_you_win(self)
            level = 0
            return 0
        elif Window.check_collision(self, Window.rectangle2(self, self.pos_x + self.size_p, self.pos_y, self.size_p,
                                                            self.size_p), sp_wall):
            try:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x + self.size_p, self.pos_y, self.size_p, self.size_p)
                self.pos_x = self.pos_x + self.size_p
            except:
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                Window.rectangle1(
                    self, self.pos_x, self.pos_y, self.size_p, self.size_p)

    def nado(self):
        sdl2.ext.init()
        self.window.show()
        running = True
        Window.draw_menu(self)
        return running

    def run(self):
        running = Window.nado(self)
        level = 0
        p = 10000000
        times = {
            0: 'error',
            1: 100,
            2: 500}
        while running:
            if level != 0 and time.time() - timing > times[level]:
                Window.draw_game_over(self)
            elif level != 0 and p != str(round(times[level] + (timing - time.time()))):
                os.system('cls')
                p = str(round(times[level] + (timing - time.time())))
                data.print_C(p)
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        Window.draw_menu(self)
                        level = 0
                    elif event.key.keysym.sym == sdl2.SDLK_1:
                        if level == 0:
                            level = 1
                            sp_wall, sp_exit, sp_pl = Window.lvl1(self)
                            timing = time.time()
                    elif event.key.keysym.sym == sdl2.SDLK_2:
                        if level == 0:
                            level = 2
                            sp_wall, sp_exit, sp_pl = Window.lvl2(self)
                            timing = time.time()
                    elif event.key.keysym.sym == sdl2.SDLK_g:
                        if level == 0:
                            Window.draw_pravila(self)
                    elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        r = Window.right(self, sp_exit, sp_wall)
                        if r == 0:
                            level = 0
                    elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                        l = Window.left(self, sp_exit, sp_wall)
                        if l == 0:
                            level = 0
                    elif event.key.keysym.sym == sdl2.SDLK_UP:
                        u = Window.up1(self, sp_exit, sp_wall)
                        if u == 0:
                            level = 0
                    elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                        d = Window.down(self, sp_wall, sp_exit)
                        if d == 0:
                            level = 0
            self.window.refresh()
        return 0


def main():
    window = Window((1082, 722), "PENT", 0, 700, 10, 0)
    pg.init()
    pg.mixer.music.load('data/music3.mp3')
    pg.mixer.music.play()
    window.run()
    os.system('cls')

if __name__ == "__main__":
    sys.exit(main())
