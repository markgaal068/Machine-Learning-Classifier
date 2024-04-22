from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np


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
img_path = "placeh.jpg"
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
        state.pred = "A képen egy " + best_preds + " látható!"
        state.img_path = var_val


app = Gui(page=index)

stylekit = {
  "color_background_dark": "#1F2F44",
  "color_primary": "#57f707",
  "color_secondary": "#57f707",
}
if __name__ == "__main__":
    app.run(use_reloader=True, stylekit=stylekit, title="K1O2S7 - Classifier")