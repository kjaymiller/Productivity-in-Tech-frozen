from PIL import Image
from sys import argv

def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
 
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)
 
maxsize = (250, 250)

if __name__ == '__main__':
    img = argv[1]
    image = Image.open(img)
    watermark_photo(
            './static/pit-podcast_base.jpg' ,
            image.thumbnail(maxsize, PIL.Image.ANTIALIAS),
            img,
            position=(375,750))
