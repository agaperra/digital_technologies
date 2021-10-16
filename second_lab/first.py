from PIL import Image

filename = r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.png"
image = Image.open(filename)
w, h = image.size
im = image.tobytes()

output = im
im_out = Image.frombytes(image.mode, (w, h), output)
im_out.save(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\other.png", 'png')
