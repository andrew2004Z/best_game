def lvl1(self):
    Window.fill_Window(self, (0, 100, 240))
    sp_wall, sp_exit = Window.draw_l1(self)
    self.size_p = 20
    self.pos_x, self.pos_y = 530, 355
    sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(100, 10, 100))


def lvl2(self):
    Window.fill_Window(self, (0, 100, 240))
    sp_wall, sp_exit = Window.draw_l2(self)
    self.size_p = 5
    self.pos_x, self.pos_y = 695, 258
    sp_pl = Window.rectangle1(self, self.pos_x, self.pos_y, self.size_p, self.size_p, color=(0, 0, 0))


