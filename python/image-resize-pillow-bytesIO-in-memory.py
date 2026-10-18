import PIL.Image as p
from io import BytesIO

fa = open("a.jpg","rb").read()
bfa = BytesIO(fa)

img = p.open(bfa)
img = img.resize((400,400))

# img.save("a2.jpg")
pqrs = BytesIO()
img.save(pqrs, format="jpeg")

open("a2.jpg","wb").write(pqrs.getbuffer())
