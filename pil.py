from PIL import Image

img=Image.open(r"C:\Users\bhara\Downloads\picture.jpeg")
#img.show()
#print(img.size)
#print(img.format)
#print(img.mode)

rotated=img.rotate(180)
#rotated.show()

resized=img.resize((200,200))
#resized.show()

cropped=img.crop((100,100,200,200))    #(left,upper,right,lower)
#cropped.show()

gray=img.convert('L')
#gray.show()
