# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

  


# String which represents the QR code
s = " Happy Valentine's Day"

# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
# url.svg("qrcode.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
# Scale - it secify the size of image
url.png('qrcode.jpg', scale = 45)
