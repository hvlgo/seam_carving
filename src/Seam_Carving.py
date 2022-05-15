import numpy as np
from PIL import Image
import time
def parseargs():
    import argparse
    parser = argparse.ArgumentParser(description='Seam_Carving',
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input-file',dest='input_path', default = "", required = True,
                        help = "path to input picture")
    parser.add_argument('-o', '--output-file',dest='output_path', default = "./output.png",
                        help = "path to output picture")
    parser.add_argument('-r', '--ratio', dest='ratio', default=0.5,
                        help="the rate of input and output")
    args = parser.parse_args()
    return args


def damage_graph(image):
    image = image.copy()
    gray = np.dot(image[..., :3], [0.229, 0.587, 0.114])
    grad = np.gradient(gray)
    damage = np.abs(grad[0]) + np.abs(grad[1])
    return damage


def search_seam(img, axis = 1):
    print(img.shape)
    img = img.copy()
    damage = damage_graph(img)
    if axis == 0:
        damage = np.transpose(damage)
        img = np.transpose(img, (1, 0, 2))
    h, w = img.shape[0], img.shape[1]
    cost = np.zeros((h, w))
    path = np.zeros((h, w))
    cost[0, :] = damage[0, :].copy()
    for i in range(1, h):
        if cost[i - 1, 0] > cost[i - 1, 1]:
            cost[i, 0] = damage[i, 0] + cost[i - 1, 1]
            path[i, 0] = 1
        else:
            cost[i, 0] = damage[i, 0] + cost[i - 1, 0]
            path[i, 0] = 0
        if cost[i - 1, w - 2] > cost[i - 1, w - 1]:
            cost[i, w - 1] = damage[i, w - 1] + cost[i - 1, w - 1]
            path[i, w - 1] = 0
        else:
            cost[i, w - 1] = damage[i, w - 1] + cost[i - 1, w - 2]
            path[i, w - 1] = -1
        for j in range(1, w - 1):
            ls = np.array([cost[i - 1, j - 1], cost[i - 1, j], cost[i - 1, j + 1]])
            index = np.argmin(ls)
            cost[i, j] = damage[i, j] + ls[index]
            path[i, j] = index - 1
        
    minval = 0xffff_ffff
    minindex = 0
    for i in range(0, w):
        if cost[h - 1, i] < minval:
            minval = cost[h - 1, i]
            minindex = i
    ls = []
    ls.append(minindex)
    for i in range(h - 1, -1, -1):
        ls.append(int(ls[-1] + path[i, ls[-1]]))
    ls.reverse()
    img_new = np.zeros((h, w - 1, 3))
    for i in range(0, h):
        for j in range(0, w - 1):
            for c in range(0, 3):
                if j < ls[i]:
                    img_new[i, j, c] = img[i, j, c]
                elif j == ls[i]:
                    continue
                else:
                    img_new[i, j - 1, c] = img[i, j, c]
    if axis == 0:
        img_new = np.transpose(img_new, (1, 0, 2))
    img_new = img_new.astype(np.uint8)
    return img_new

def seamCarving(img, path, rate):
    rate = eval(rate)
    img = img.copy()
    h, w = img.shape[0], img.shape[1]
    dh, dw = int(h * (1 - rate)), int(w * (1 - rate))
    for i in range(0, dh):
        img = search_seam(img, 0)
    for j in range(0, dw):
        img = search_seam(img, 1)
    pil_img = Image.fromarray(img)
    pil_img.save(path)
    #cv2.imwrite(path, img)



def main():
    args = parseargs()
    img = np.array(Image.open(args.input_path))
    # cv2.imread(args.input_path)
    starttime = time.time()
    seamCarving(img, args.output_path, args.ratio)
    t = time.time() - starttime
    print(t)

if __name__ == '__main__':
    main()