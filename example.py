from pycolorhunt import ColorHunt

# Possible options for init are 'popular', 'hot' and 'random'
c = ColorHunt('popular')
for page in c:
    for pallete in page:
        print(pallete)
