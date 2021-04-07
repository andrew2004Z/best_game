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
#f.close()

#rint(draw_menu('menu.png'))
def draw_1(path, color, new_image):
    image = Image.open(path)
    size = image.size
    pix = image.load()
    draw = ImageDraw.Draw(new_image)
    for i in range(size[0]):
        for j in range(size[1]):
            if pix[i, j] == color:
                #pix[i, j] = (255, 255, 255)
                draw.point((i, j), (255, 255, 255))
new_image = Image.open('1.png')
draw_1('1.png', (255, 147, 171), new_image)
new_image.save('2.png', 'PNG')