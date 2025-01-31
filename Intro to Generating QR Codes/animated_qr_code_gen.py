import segno
from urllib.request import urlopen

qr_code = segno.make_qr("https://www.starbucks.co.uk/")
gif_url = urlopen("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnd5NzRhejc0dmQ0MDdtZzhueXk5aHB0b3kwYW0xbmZraHlsdmtseSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lZZwR5gvWDYdFcGNf7/giphy.gif")

qr_code.to_artistic(
    background = gif_url,
    target="animated_morning_qrcode.gif",
    scale = 20,
)

# to create, run in terminal:
# python qr_code_gen.py