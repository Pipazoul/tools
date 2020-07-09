from PIL import Image

im = Image.open('image.png')

gray = im.convert('L')
bw = gray.point(lambda x: 0 if x<120 else 255, '1')

bw.save('output.png')
bw.show()
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
print(pix_val)