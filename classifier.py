from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np
from tensorflow.keras.datasets import cifar100 


class_names = {
    0: 'repülő',
    1: 'autó',
    2: 'madár',
    3: 'macska',
    4: 'szarvas',
    5: 'kutya',
    6: 'béka',
    7: 'ló',
    8: 'hajó',
    9: 'kamion',
}
# class_names = {
#     0: 'akváriumi hal',
#     1: 'ágy',
#     2: 'bogár',
#     3: 'alma',
#     4: 'méh',
#     5: 'medve',
#     6: 'hód',
#     7: 'beetle',
#     8: 'bicycle',
#     9: 'bicikli',
#     10: 'bowl',
#     11: 'boy',
#     12: 'bridge',
#     13: 'bus',
#     14: 'butterfly',
#     15: 'camel',
#     16: 'can',
#     17: 'castle',
#     18: 'caterpillar',
#     19: 'cattle',
#     20: 'chair',
#     21: 'chimpanzee',
#     22: 'clock',
#     23: 'cloud',
#     24: 'cockroach',
#     25: 'couch',
#     26: 'crab',
#     27: 'crocodile',
#     28: 'cup',
#     29: 'dinosaur',
#     30: 'dolphin',
#     31: 'elephant',
#     32: 'flatfish',
#     33: 'forest',
#     34: 'fox',
#     35: 'girl',
#     36: 'hamster',
#     37: 'house',
#     38: 'kangaroo',
#     39: 'keyboard',
#     40: 'lamp',
#     41: 'lawn_mower',
#     42: 'leopard',
#     43: 'lion',
#     44: 'lizard',
#     45: 'lobster',
#     46: 'man',
#     47: 'maple_tree',
#     48: 'motorcycle',
#     49: 'mountain',
#     50: 'mouse',
#     51: 'mushroom',
#     52: 'oak_tree',
#     53: 'orange',
#     54: 'orchid',
#     55: 'otter',
#     56: 'palm_tree',
#     57: 'pear',
#     58: 'pickup_truck',
#     59: 'pine_tree',
#     60: 'plain',
#     61: 'plate',
#     62: 'poppy',
#     63: 'porcupine',
#     64: 'possum',
#     65: 'rabbit',
#     66: 'raccoon',
#     67: 'ray',
#     68: 'road',
#     69: 'rocket',
#     70: 'rose',
#     71: 'sea',
#     72: 'seal',
#     73: 'shark',
#     74: 'shrew',
#     75: 'skunk',
#     76: 'skyscraper',
#     77: 'snail',
#     78: 'snake',
#     79: 'spider',
#     80: 'squirrel',
#     81: 'streetcar',
#     82: 'sunflower',
#     83: 'sweet_pepper',
#     84: 'table',
#     85: 'tank',
#     86: 'telephone',
#     87: 'television',
#     88: 'tiger',
#     89: 'tractor',
#     90: 'train',
#     91: 'trout',
#     92: 'tulip',
#     93: 'turtle',
#     94: 'wardrobe',
#     95: 'whale',
#     96: 'willow_tree',
#     97: 'wolf',
#     98: 'woman',
#     99: 'worm'
# }

model = models.load_model("base.keras")

def image_pred(model, path_to_img):
    image = Image.open(path_to_img)
    image = image.convert("RGB")
    image = image.resize((32, 32))
    data = np.asarray(image)
    data = data / 255
    tries = model.predict(np.array([data])[:1])

    best_tries = tries.max()
    best_preds = class_names[np.argmax(tries)]
    
    return best_tries, best_preds
    
content = ""
img_path = "placeholder_image.png"
prob = 0
pred = ""

index = """
<|text-center|
<|{"logo.png"}|image|width=25vw|>

<|{content}|file_selector|extensions=.jpg|>
Válassz ki egy képet a könyvtáradból!

<|{pred}|>

<|{img_path}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>
>
"""

def on_change(state, var_name, var_val):
    if var_name == "content":
        best_tries, best_preds = image_pred(model, var_val)
        state.prob = round(best_tries * 100)
        state.pred = "A képen egy " + best_pred + " látható!"
        state.img_path = var_val


app = Gui(page=index)

stylekit = {
  "color_background_dark": "#1F2F44",
  "color_primary": "#57f707",
  "color_secondary": "#57f707",
}
if __name__ == "__main__":
    app.run(use_reloader=True, stylekit=stylekit, title="MI_HW")