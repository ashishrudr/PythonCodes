import requests as req

tex = req.get("https://www.hdfcsec.com/")

print(tex.status_code)
