# Simple ASCII graphics renderer
Its a Python based graphic renderer.

# API
API is pretty standart for graphic rendering. 
- You have a Sprite class and a TextRenderer class which is drawing Sprite classes
- TextRenderer class have 3 methods: draw_sprite, show and clear
- If following standard graphic APIs workflow, you need to clear() canvas, then draw_sprite() on it, then show. Repeat.
- Example of how to define sprites and use renderer is test.py

# Pros
It is really simple and I tried to make it well-commented, so you can modify code and not get stuck with thinking how's everything done. It can handle pretty much of sprites on a screen and still is pretty fast

# Cons
It is really simple so it has no error exceptions or fancy stuff. Also, I made while I was sick, so maybe code is suboptimal :)
