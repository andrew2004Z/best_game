from PIL import Image

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

print(draw_menu('menu.png'))