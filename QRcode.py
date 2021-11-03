import qrcode
import image
img = qrcode.make('https://www.youtube.com/watch?v=aBt8fN7mJNg&list=RDMMaBt8fN7mJNg&start_radio=1')
img.save('myQRcode.png')
img.show()
