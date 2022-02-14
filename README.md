# Generate QR code using Python

## Requirments
```
pip install pyqrcode
pip install pypng
```

## Python code

```python

# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

  
# String which represents the QR code
s = "Successfully created the qr code"

# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("qrcode.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('qrcode.png', scale = 6)
```
