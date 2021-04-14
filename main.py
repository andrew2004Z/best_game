import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from math import sin, cos, sqrt
from PIL import Image
import random


def draw_1(path, color, new_image):
    sp = []
    image = Image.open(path)
    size = image.size
    pix = image.load()
    for i in range(size[0]):
        for j in range(size[1]):
            if pix[i, j] == color:
                sp.append([i*5, round(j*3.5)])
                #pix[i, j] = (255, 255, 255)
    return sp

def draw_menu(path):
    image = Image.open(path)
    size = image.size
    pix = image.load()
    sp = []
    for i in range(size[0]):
        for j in range(size[1]):
            sp.append([[i, j], pix[i, j]])
    return sp


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

    def draw_menu(self):
        matrix = draw_menu('Menu.png')
        for i in matrix:
            Window.d1_point(self, i[0][0], i[0][1],
                            self.window.get_surface(), i[1][:-1])

    def d_point(self, x, y, color):
        r, g, b = color
        renderer = sdl2.ext.Renderer(self.window)
        renderer.draw_point([x, y], sdl2.ext.Color(r, g, b))
        renderer.present()
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.window)

    def line_vert(self, x, y, l, color=(0, 0, 0)):
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y - 1,
                                self.window.get_surface(), color)
                sp.append([x-1, y-1])
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
                sp.append([x-1, y-1])
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
                Window.d1_point(self, x-1, y, self.window.get_surface(), color)
                x = x - 1
                sp.append([x-1, y])
        else:
            for i in range(l):
                Window.d1_point(self, x, y, self.window.get_surface(), color)
                x = x + 1
                sp.append([x, y])
        return sp

    def line_goriz2(self, x, y, l):
        sp = [[x,  y]]
        if l < 0:
            for i in range(l * -1):
                x = x - 1
                sp.append([x-1, y])
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
        #print(sp)
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
                    if pix[i - 1, y] != (0, 0, 0) or pix[i - 1, j - 1] != (0, 0, 0) or pix[i, j - 1] != (0, 0, 0) or pix[i + 1, j] != (0, 0, 0) or pix[i, j + 1] != (0, 0, 0) or pix[i + 1, j + 1] != (0, 0, 0) or pix[i - 1, j + 1] != (0, 0, 0) or pix[i + 1, j - 1] != (0, 0, 0):
                        sp.append([i, j])
                except:
                   pass
        return sp

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
                    #print(pix[x - 1, y])
                    try:
                        if pix[x - 1, y] != (0, 0, 0) or pix[x - 1, y - 1] != (0, 0, 0) or pix[x, y - 1] != (0, 0, 0) or pix[x + 1, y] != (0, 0, 0) or pix[x, y + 1] != (0, 0, 0) or pix[x + 1, y + 1] != (0, 0, 0) or pix[x - 1, y + 1] != (0, 0, 0) or pix[x + 1, y - 1] != (0, 0, 0):
                            sp.append([x, y])
                    except:
                        pass
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))
        return sp, sp1
    

    def draw_menu(self):
        sp = []
        image = Image.open('data/Menu.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))


    def draw_you_win(self):
        sp = []
        image = Image.open('data/YOU WIN.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] != (255, 255, 255):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))

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
                    #print(pix[x - 1, y])
                    try:
                        if pix[x - 1, y] != (0, 0, 0) or pix[x - 1, y - 1] != (0, 0, 0) or pix[x, y - 1] != (0, 0, 0) or pix[x + 1, y] != (0, 0, 0) or pix[x, y + 1] != (0, 0, 0) or pix[x + 1, y + 1] != (0, 0, 0) or pix[x - 1, y + 1] != (0, 0, 0) or pix[x + 1, y - 1] != (0, 0, 0):
                            sp.append([x, y])
                    except:
                        pass
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))
#                    sdl2.SD
        return sp, sp1
        #Window.line_goriz1(self, 1, 1, 1080, 3)
        #Window.line_goriz1(self, 1, 716, 470, 3)
        #Window.line_goriz1(self, 545, 716, 536, 3)
        #Window.line_vert1(self, 1, 1, 716, 3)
        #Window.line_vert1(self, 1076, 1, 716, 3)
        #Window.line_vert1(self, 545, 626, 90, 3)
        #Window.line_goriz1(self, 545, 626, 263, 3)
        #Window.line_goriz1(self, 545, 536, 285, 3)
        #Window.line_vert1(self, 830, 422, 263, 3)
        #Window.line_goriz1(self, 830, 626, 250, 3)
        #Window.line_vert1(self, 465, 500, 126, 3)
        #Window.line_vert1(self, 375, 590, 126, 3)
        #Window.line_vert1(self, 185, 656, 63, 3)
        #Window.line_goriz1(self, 280, 446, 500, 3)
        #Window.rectangle(self, 1, 1, 1077, 717)
        #Window.rectangle(self, 2, 2, 1076, 716)
        #Window.rectangle(self, 3, 3, 1076, 716)
        #Window.rectangle(self, 4, 4, 1076, 716)

    def check_collision(sp1, sp2):
        for i in sp1:
            if i in sp2:
                return False
        return True

    def run(self):
        sdl2.ext.init()
        # window = sdl2.ext.Window(self.name, size=self.size)
        self.window.show()
        running = True
        Window.fill_Window(self, (0, 100, 240))
        Window.draw_menu(self)
        start_game = False
        while running:
            #if start_game and random.randint(1, 10) > 9:
            #    try:
            #        Window.rectangle1(self, self.pos_x1,
            #                          self.pos_y1, 5, 5, color=(100, 10, 100))
            #        Window.rectangle1(self, self.pos_x1,
            #                          self.pos_y1 + 10, 5, 5)
            #        self.pos_y1 = self.pos_y1 + 10
            #    except:
            #        pass
            #if start_game and self.pos_x1 == self.pos_x and self.pos_y1 == self.pos_y:
            #    print('Game over')
            #    sdl2.ext.quit()
            #    return None
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        Window.fill_Window(self, (0, 100, 240))
                        Window.draw_menu(self)
                    elif event.key.keysym.sym == sdl2.SDLK_1:
                        Window.fill_Window(self, (0, 100, 240))
                        sp_wall, sp_exit = Window.draw_l1(self)
                        self.pos_x, self.pos_y = 530, 355
                        sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                    elif event.key.keysym.sym == sdl2.SDLK_2:
                        Window.fill_Window(self, (0, 100, 240))
                        sp_wall, sp_exit = Window.draw_l2(self)
                        self.size_p = 5
                        self.pos_x, self.pos_y = 50, 10
                        sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(0, 0, 0))
                    elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        #print(Window.rec_pos_plaer(self, self.pos_x + 10, self.pos_y, 20, 20))
                        #print()
                        #print(sp_wall)
                        if not Window.check_collision(Window.rectangle2(self, self.pos_x +  self.size_p, self.pos_y, self.size_p, self.size_p), sp_exit):
                            Window.fill_Window(self, (0, 100, 240))
                            Window.draw_you_win(self)
                        elif Window.check_collision(Window.rectangle2(self, self.pos_x +  self.size_p, self.pos_y, self.size_p, self.size_p), sp_wall):
                            try:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p,  self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x +  self.size_p, self.pos_y,  self.size_p, self.size_p)
                                self.pos_x = self.pos_x + self.size_p
                            except:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p, self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p, self.size_p)
                    elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                        if not Window.check_collision(Window.rectangle2(self, self.pos_x +  self.size_p, self.pos_y, self.size_p, self.size_p), sp_exit):
                            Window.fill_Window(self, (0, 100, 240))
                            Window.draw_you_win(self)
                        elif Window.check_collision(Window.rectangle2(self, self.pos_x -  self.size_p, self.pos_y, self.size_p, self.size_p), sp_wall):
                            try:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p,  self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x -  self.size_p, self.pos_y,  self.size_p,  self.size_p)
                                self.pos_x = self.pos_x -  self.size_p
                            except:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p,  self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y, self.size_p,  self.size_p)
                    elif event.key.keysym.sym == sdl2.SDLK_UP:
                        if not Window.check_collision(Window.rectangle2(self, self.pos_x +  self.size_p, self.pos_y, self.size_p, self.size_p), sp_exit):
                            Window.fill_Window(self, (0, 100, 240))
                            Window.draw_you_win(self)
                        elif Window.check_collision(Window.rectangle2(self, self.pos_x, self.pos_y -  self.size_p, self.size_p, self.size_p), sp_wall):
                            try:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y, self.size_p,  self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y -  self.size_p, self.size_p,  self.size_p)
                                self.pos_y = self.pos_y -  self.size_p
                            except:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y, self.size_p,  self.size_p)
                    elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                        if not Window.check_collision(Window.rectangle2(self, self.pos_x +  self.size_p, self.pos_y, self.size_p, self.size_p), sp_exit):
                            Window.fill_Window(self, (0, 100, 240))
                            Window.draw_you_win(self)
                        elif Window.check_collision(Window.rectangle2(self, self.pos_x, self.pos_y +  self.size_p, self.size_p, self.size_p), sp_wall):
                            try:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p,  self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y +  self.size_p, self.size_p, self.size_p)
                                self.pos_y = self.pos_y +  self.size_p
                            except:
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p, self.size_p, color=(100, 10, 100))
                                Window.rectangle1(
                                    self, self.pos_x, self.pos_y,  self.size_p, self.size_p)
                    elif event.key.keysym.sym == sdl2.SDLK_r:
                        Window.fill_Window(self, (100, 90, 7))
                        self.pos_x, self.pos_y = 0, 700
                        # try:
                        #    Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                        #    Window.rectangle1(self, x, y + 10, 20, 20)
                        #    y = y + 10
                        # except:
                        #    Window.rectangle1(self, x, y, 20, 20, color=(100, 10, 100))
                        #    Window.rectangle1(self, x, y, 20, 20)
                        # for i in range(10, 100):
                        #    for j in range(10, 20):
                        #        Window.d1_point(self, i, j, self.window.get_surface(), (100, 100, 100))
                        # Window.d1_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                        # Window.d1_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                elif event.type == sdl2.SDL_CONTROLLER_BUTTON_X:
                    Window.d_point(
                        self, 10, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(
                        self, 11, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(
                        self, 12, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(
                        self, 13, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(
                        self, 14, 20, self.window.get_surface(), (0, 0, 0))
                    # Window.d_point(self, 10, 20, (0, 0, 0))
                    # Window.d_point(self, 11, 20, (0, 0, 0))
                    # Window.d_point(self, 12, 20, (0, 0, 0))
                    # Window.d_point(self, 13, 20, (0, 0, 0))
                    # Window.d_point(self, 14, 20, (0, 0, 0))
                    # Window.d_point(self, 15, 20, (0, 0, 0))
            self.window.refresh()
        return 0


def main():
    window = Window((1082, 722), "Best Game", 0, 700, 10, 0)

    window.run()
    # window.fill_Window((240, 0, 0))
    # fill_Window(window, 240, 0, 0)


if __name__ == "__main__":
    # window = Window((1080, 720), (240, 40, 40), "Best Game")
    sys.exit(main())
