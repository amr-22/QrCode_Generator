
# import needed libraries
import qrcode
from PIL import Image

# generate qrcode from data that pass to it
def generate_qrcode(data):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')


# add our Logo in the middle of qrcode
# problem --> logo added with dots in paste     
def add_logo(qr_img, logo_img):
    # Add image
    img = Image.open(qr_img)

    # Add logo
    logo = Image.open(logo_img)
    logo=logo.resize([100,100])


    if img.mode != 'RGB':
        img = img.convert('RGB')


    img.paste(logo, (img.size[0] // 2 - logo.size[0] // 2, img.size[1] // 2 - logo.size[1] // 2))

    img.save('qrcode_logo.png')







# begin Generation

logo_img = "TackleTimeLogo.png"

cipher_text='Tackle Time App'
generate_qrcode(cipher_text)
print('----> qrcode generation Done')

qr_img ="qrcode.png"
add_logo(qr_img,logo_img)
print("-----> logo adding done")