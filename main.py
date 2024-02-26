from taipy.gui import Gui

#frontend part
content = ""
img_path = "placeholder_image.png" #gives us images for our project

index = """
<|text-center|
<|{"logo.png"}|image|width=25vw|>

<|{content}|file_selector||extensions=.png> Upload an image to use the classifier!

<|{img_path}|image|>

<|label goes here|indicator|value=0|min=0|max=100|width=25vw|>

>
""" 
#Notes for the frontend part of the implementation:
    #html tags for the web app
    #using """ for multi line selection
    #using <|{img_path}|image|> to create an image on the web app
    #using <|{content}|file_selector|> to upload an image of your own


#python part

def on_change(state, ver_name, var_val):
    if var_name == "content":
        state.img_path = var_val
    #testing file selection with routing: print(var_name, var_val)


app = Gui(page=index) #GUI creation called "app"

if __name__ == "__main__":
    app.run=(use_reloader=True)   #helps during the test phase with the web application (we do not have to rerun the py app)