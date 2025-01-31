# IMPORT THE LIBRARY
import segno

# WEBSITE TO LINK
url = "https://www.google.com"

# CREATE THE QR CODE IMAGE AS A VARIABLE
qr_code = segno.make_qr(url)

# CALL THE METHOD TO SAVE THE QR CODE IMAGE
qr_code.save(
    "Test_QR_Code.png",
    scale=8, # size
    border=2,
    light="#ADD8E6",
    dark = "#2596be",
    quiet_zone="maroon",
    data_dark="green",
    data_light="lightgreen",
)

# TERMINAL FEEDBACK
print("QR Code for", url, "saved successfully!")

# RUN IN TERMINAL
# python single_code.py

# USEFUL RESOURCES: 
# 1. QR COLOR DOCS 
# https://segno.readthedocs.io/en/latest/colorful-qrcodes.html