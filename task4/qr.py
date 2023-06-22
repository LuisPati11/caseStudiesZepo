import qrcode
input = "https://zepoapp.com/es"

def createQR(input):
    qr = qrcode.QRCode(version=1,box_size=10,border=4)

    qr.add_data(input)
    qr.make(fit=True)

    # I'm going to use the colours I found on zepo's website, so it's not the typical black and white design
    img = qr.make_image(fill_color='#4425b2',back_color='#6ed3ce')
    img.save('qrZepoV1.jpg')
    img = qr.make_image(fill_color='#000000',back_color='#4425b2')
    img.save('qrZepoV2.jpg')
    img = qr.make_image(fill_color='#6ed3ce',back_color='white')
    img.save('qrZepoV3.jpg')


print("Generating QR Code...")
createQR(input)