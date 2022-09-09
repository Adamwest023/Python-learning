# install pillow and import 
# open image using python
# Print current size and specify the size to change 
# save the new resized image

from PIL import Image

def resize_image(size1,size2):

    image = Image.open("assets/img_visible/Headshot.jpg")

    print(f"Current Size: {image.size}")

    resized_image = image.resize((size1,size2))

    resized_image.save('headshot-medium-' + str(size1)  + '.jpeg')
    
size1 = int(input("Enter width: "))
size2 = int(input("Enter height: ")  )

resize_image(size1,size2)

  