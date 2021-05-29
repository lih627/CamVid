"""
Map CamVid 32 classes to 11 classes
https://github.com/jijnasa/Fully-Convolutional-Neural-Network/blob/master/camvidPixelLabelIDs.m
"""

RGBLabel2LabelName = {
    (128, 128, 128): "Sky",

    (0, 128, 64): "Building",
    (128, 0, 0): "Building",
    (64, 192, 0): "Building",
    (64, 0, 64): "Building",
    (192, 0, 128): "Building",

    (192, 192, 128): "Pole",
    (0, 0, 64): "Pole",

    (128, 64, 128): "Road",
    (128, 0, 192): "Road",
    (192, 0, 64): "Road",

    (0, 0, 192): "Sidewalk",
    (64, 192, 128): "Sidewalk",
    (128, 128, 192): "Sidewalk",

    (128, 128, 0): "Tree",
    (192, 192, 0): "Tree",

    (192, 128, 128): "SignSymbol",
    (128, 128, 64): "SignSymbol",
    (0, 64, 64): "SignSymbol",

    (64, 64, 128): "Fence",

    (64, 0, 128): "Car",
    (64, 128, 192): "Car",
    (192, 128, 192): "Car",
    (192, 64, 128): "Car",
    (128, 64, 64): "Car",

    (64, 64, 0): "Pedestrian",
    (192, 128, 64): "Pedestrian",
    (64, 0, 192): "Pedestrian",
    (64, 128, 64): "Pedestrian",

    (0, 128, 192): "Bicyclist",
    (192, 0, 192): "Bicyclist",

    (0, 0, 0): "Void"
}

palette = [128, 128, 128,
           128, 0, 0,
           192, 192, 128,
           128, 64, 128,
           0, 0, 192,
           128, 128, 0,
           192, 128, 128,
           64, 64, 128,
           64, 0, 128,
           64, 64, 0,
           0, 128, 192]

CAMVID_CLASSES = ['Sky',
                  'Building',
                  'Pole',
                  'Road',
                  'Sidewalk',
                  'Tree',
                  'SignSymbol',
                  'Fence',
                  'Car',
                  'Pedestrian',
                  'Bicyclist',
                  'Void']
Class2LabelId = {}

for i, v in enumerate(CAMVID_CLASSES):
    Class2LabelId[v] = i

Class2LabelId['Void'] = 255

print(Class2LabelId)

CAMVID_CLASS_COLORS = [
    (128, 128, 128),
    (128, 0, 0),
    (192, 192, 128),
    (128, 64, 128),
    (0, 0, 192),
    (128, 128, 0),
    (192, 128, 128),
    (64, 64, 128),
    (64, 0, 128),
    (64, 64, 0),
    (0, 128, 192),
    (0, 0, 0),
]

zero_pad = 256 * 3 - len(palette)
for i in range(zero_pad):
    palette.append(0)


def convert32to11(label_dir, save_dir):
    import os
    import numpy as np
    from PIL import Image
    import glob
    img_paths = glob.glob(os.path.join(label_dir, '*.png'))
    img_paths.sort()
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for idx, img_path in enumerate(img_paths):
        img_name = img_path.split('/')[-1]
        img = Image.open(img_path)
        np_img = np.array(img)
        np_img_ret = 255 * np.ones(np_img.shape[:2], dtype=np.uint8)
        w, h = np_img.shape[:2]
        for x in range(w):
            for y in range(h):
                rgb = np_img[x, y, :]
                rgb = tuple(rgb)
                if rgb in RGBLabel2LabelName:
                    label = RGBLabel2LabelName[rgb]
                else:
                    print("({}, {}) in {}, rgb {}, changed to Void".format(x, y, rgb,
                                                                           img_name))
                    label = 'Void'
                np_img_ret[x, y] = Class2LabelId[label]
        img = Image.fromarray(np_img_ret)

        img.save(os.path.join(save_dir, img_name))
        print(idx, img_name)
    print('Done')


def convertGraytoRGB(gray_dir, save_dir):
    import os
    import glob
    from PIL import Image
    img_paths = glob.glob(os.path.join(gray_dir, '*.png'))
    img_paths.sort()
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for idx, img_path in enumerate(img_paths):
        img_name = img_path.split('/')[-1]
        img = Image.open(img_path).convert('P')
        img.putpalette(palette)
        img.save(os.path.join(save_dir, img_name))
        print(idx, img_name)
    print('Done')


def _write(path, imglabels):
    with open(path, 'w') as f:
        for (img, label) in imglabels:
            print("{} {}".format(img, label), file=f)
    print('Done')

def _get_anno(segnetanno_path):
    img_paths = []
    with open(segnetanno_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            img_name = line.split()[0]
            img_name = img_name.split('/')[-1]
            img_paths.append(img_name)
            print(img_name)
    return img_paths

def generate_img_pairs(root_dir, img_dir, label_dir, save_dir, segnetanno_dir):
    import glob
    import os
    imgs = glob.glob(os.path.join(root_dir, img_dir, '*.png'))
    labels = glob.glob(os.path.join(root_dir, label_dir, '*.png'))
    assert len(imgs) == len(labels), "img {} != label {}".format(len(imgs), len(labels))
    imgs.sort()
    labels.sort()

    imgs = [os.path.join(img_dir, os.path.split(p)[1]) for p in imgs]
    labels = [os.path.join(label_dir, os.path.split(p)[1]) for p in labels]
    img_names = [_.split('/')[-1] for _ in imgs]
    img_label = list(zip(img_names, imgs, labels))

    name2subset = {}
    segnet_file_name = ['train', 'test', 'val']
    for anno_file in segnet_file_name:
        annos = _get_anno(os.path.join(segnetanno_dir, anno_file+'.txt'))
        for _ in annos:
            name2subset[_] = anno_file

    datasets = {'train': [], 'val': [], 'test': []}

    for (name, img, label) in img_label:
        datasets[name2subset[name]].append([img, label])

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    train_file = 'camvid_train.txt'
    val_file = 'camvid_val.txt'
    trainval_file = 'camvid_trainval.txt'
    test_file = 'camvid_test.txt'

    _write(os.path.join(save_dir, train_file), datasets['train'])
    _write(os.path.join(save_dir, val_file), datasets['val'])
    _write(os.path.join(save_dir, trainval_file), datasets['train'] + datasets['val'])
    _write(os.path.join(save_dir, test_file), datasets['test'])

if __name__ == '__main__':
    '''
    Demo to generate gray label, 11 classes rgb color label, subsets for training
    '''
    # 1. Generate Gary labels
    convert32to11(label_dir='path/to/CamVid_RGB',
                  save_dir='path/to/CamVidGray')
    # 2. From Gray labels, generate 11 classes Color labels
    convertGraytoRGB(gray_dir='path/to/CamVidGray',
                     save_dir='path/to/CamVidColor11')
    # 3. Generate training pairs (txt file)
    generate_img_pairs(root_dir='path/to/CamVid',
                       img_dir='CamVid_RGB',
                       label_dir='CamVidGray',
                       save_dir='path/to/CamVid',
                       segnetanno_dir='path/to/CamVid/SegNetanno')
