# Simple ASCII graphics renderer
Its a Python based graphic renderer.

# API
API is pretty standart for graphic rendering. 
- You have a Sprite class and a TextRenderer class which is drawing Sprite classes
- TextRenderer class have 3 methods: draw_sprite, show and clear
- If following standard graphic APIs workflow, you need to clear() canvas, then draw_sprite() on it, then show. Repeat.
- Example of how to define sprites and use renderer is forest.py (You'll maybe need to adjust field width and height for your console)

# Files
- text_renderer.py - contains API
- sprites.py - contains ASCII art, formatted for creating Sprite object from it
- forest.py - a little demoscene using text_renderer API and sprites from sprites.py 

# Pros
It is really simple and I tried to make it well-commented, so you can modify code and not get stuck with thinking how's everything done. It can handle pretty much of sprites on a screen and still is pretty fast

# Cons
It is really simple so it has no error exceptions or fancy stuff. Also, I made while I was sick, so maybe code is suboptimal :)
