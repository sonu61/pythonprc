import qrcode

def generate_qrcode(text):
    
    #adding data to qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color ="pink", back_color ="red")
    img.save("qrSonu1102.png")

url = input("enter your url\n")
generate_qrcode(url)