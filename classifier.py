from taipy.gui import Gui

content = ""
img_path = "placeholder_image.png"

index = """
<|text-center|
<|{"logo.png"}|image|width=20vw|>

<|{content}|file_selector|extensions=.png|>
Válassza ki a feltölteni kívánt filet!

<|{img_path}|image|>

<|label goes here|indicator|value=0|min=0|max=100|width=15vw|>
"""

def on_change(state, var_name, var_val):
    if var_name == "content":
        state.img_path = var_val    #image update

app = Gui(page=index)

stylekit = {
  "color_background_dark": "#1F2F44",
  "color_primary": "#57f707",
  "color_secondary": "#57f707",
}
if __name__ == "__main__":
    # Override the background color to orange
    app.run(use_reloader=True, dark_mode=True, stylekit=stylekit, title="MI_HW")
