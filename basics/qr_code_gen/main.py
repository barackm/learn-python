import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import datetime
import os

data = input("Please enter some data: ").strip()

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(0, 0, 0)
    )
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

directory = "qr_code_gen/images"

if not os.path.exists(directory):
    os.makedirs(directory)
    
try:
    img.save(f"{directory}/code-{timestamp}.png")
    print("QR Code generated successfully")
except Exception as e:
    print(f"Error saving QR Code: {e}")