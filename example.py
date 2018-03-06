from pycolorhunt import ColorHunt

c = ColorHunt('popular')
for page in c:
    for pallete in page:
        print(pallete)
