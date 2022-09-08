ffmpeg -headers "referer: https://www.romaniatv.net/" -i "https://livestream.romaniatv.net/clients/romaniatv/playlist.m3u8" -vf fps=1/5 -t 00:05:00 screens/output%08d.jpg
pip install opencv-python pytesseract wand
