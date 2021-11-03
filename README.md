# QRcode-Builder-with-Python
Install required Libraries :==
   pip install qrcode
   pip install image
import libraries
   import qrcode
   import image
img = qrcode.make("Your Link for which you want to make QRcode ")
img.save('qrCode.png')  == Save the image
img.show() == show the image
