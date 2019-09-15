from PIL import Image
import os

fibonacci_photos = [(100, 100), (100, 100)]
fibonacci_limit = 4

for i in range(fibonacci_limit):
    fibonacci_photos.append((fibonacci_photos[i][0] + fibonacci_photos[i+1][0], fibonacci_photos[i][0] + fibonacci_photos[i+1][0]))

print(fibonacci_photos)

name = "square.png"
path = "C:\\Users\\Capsimir\\Desktop\\VisualStudio\\PythonProjects\\PIL\\"

image1 = Image.open(path + name)
file_name, ext = os.path.splitext(name)

for i in range(len(fibonacci_photos)):
    image1.resize(fibonacci_photos[i]).save((path + "converted\\" + "{}_" + str(fibonacci_photos[i][0]) + "{}").format(file_name, ext))
    image1 = Image.open(path + name)

#width, height = image1.size
#print(str(width) + " " + str(height))

#for f in os.listdir(path):
#    if f.endswith(".jpg"):
#        i = Image.open(path + f)
#        fn, fext = os.path.splitext(f)
        
#        print(fn)

#image1.show()