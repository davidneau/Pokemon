import requests # request img from web
import shutil # save img locally

image_folder = r"C:\Users\david\Documents\Programmation\Web\Pokemon\Front\src\assets\images"
url_images = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"

for num in range(1500):
    print(num)
    res = requests.get(url_images + str(num+1) + ".png", stream = True)
    if res.status_code == 200:
        with open(image_folder + "/Pokemon-175px/" + str(num+1) + ".png",'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded')
    else:
        print('Image Couldn\'t be retrieved')