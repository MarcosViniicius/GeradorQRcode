import qrcode
img = qrcode.make('Link do QRcode')
type(img) 
img.save("qrcode.png")