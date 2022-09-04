# install all the libraries needed
# create a function that collections a text and converts it to a QR Code
# save the code as an image
# run the function
import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fillcolor="black", back_color="white")
    img.save("qrimg001.png")
    
    
url = input("Enter your url: ")
generate_qrcode(url)
