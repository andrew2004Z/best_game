from PIL import Image, ImageDraw





def draw_menu(path):
    image = Image.open(path)
    size = image.size
    pix = image.load()
    sp = []
    for i in range(size[0]):
        for j in range(size[1]):
            sp.append([[i, j], pix[i, j]])
    return sp


def draw_rec_f(w_f, h_f, x, y, w, h, char):
    #mas = [['' for x in range(w_f)]for y in range(h_f)]
    mas = []
    for y1 in range(h + y):
        for x1 in range(w + x):
            if h + y >= y1 >= y and w + x >= x1 >= x:
                mas.append([y1, x1, char])
    return mas


#f = open("demofile2.txt", "w")
#f.write(str(draw_rec_f(1080, 720, 362, 283, 386, 90, '00416A')))
# f.close()

def draw_111(path, color=(255, 255, 255, 255)):
    sp = []
    image = Image.open(path)
    size = image.size
    pix = image.load()
    for i in range(size[0]):
        for j in range(size[1]):
            if pix[i, j] == color:
                sp.append([i, j])
    return sp
# rint(draw_menu('menu.png'))

"""
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
    """
    pass

def draw_1(path, color, new_image):
    sp = []
    image = Image.open(path)
    size = image.size
    pix = image.load()
    draw = ImageDraw.Draw(new_image)
    for i in range(size[0]):
        for j in range(size[1]):
            print(pix[i, j])
            if pix[i, j] == color:
                sp.append([i*5, round(j*3.5)])
                #pix[i, j] = (255, 255, 255)
                draw.point((i, j), pix[i, j])
    return sp

#with open('data/1.txt', 'w') as f:
#    f.write(str(draw_111('data/1.png', (0,0,0, 255))))
#print(draw_111('data/1.png', (0,0,0, 255)))
for i in range(0, 10):
    new_image = Image.open(f'data/{i}.jpg')
    draw_1(f'data/{i}.jpg', (255, 255, 255), new_image)
    new_image.save(f'data/{i}.png', 'PNG')
