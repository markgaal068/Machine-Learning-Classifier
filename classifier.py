from taipy.gui import Gui #import the GUI from taipy.gui


content = ""
img_path = "placeholder_image.png"
#HTML tags for Webpage implementation (Frontend)
#Notes for html:
    #using """ to multiline tasking in python frontend
    #using <|{}|> to image selection / task selection and styling


index = """
<|text-center|
<|{logo.png}|image|>

<|{content}|file_selector|background-color-blue|>
Válassza ki a feltölteni kívánt filet!


<|{img_path|image>
>
"""


app = Gui(page=index) #using "app" named variable to have a Gui instance

if __name__ == "__main__":
    app.run(use_reloader=True) #live app on port 127.0.0.1:5000 port -->using this line to avoid rerun after changes


