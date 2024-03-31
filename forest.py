import numpy as np
import time

from text_renderer import TextRenderer, Sprite
import sprites

def main():

    ### GLOBAL VARIABLES ###
    # fps is optional
    fps = 60

    trees_amount = 50

    canvas_width = 200
    canvas_height = 54

    ### GLOBAL VARIABLES END ###

    # define sprites
    tre = Sprite(sprites.tree)
    fox = Sprite(sprites.fox)
    rabbit1 = Sprite(sprites.rabbit)
    rabbit2 = Sprite(sprites.rabbit)

    #define renderer
    render = TextRenderer(canvas_width, canvas_height)

    # coords - are offset from starting point
    coords_rab1 = [0, 0]
    coords_fox = [0, 0]
    coords_rab2 = [0, 0]

    tree_coords = np.dstack((np.random.randint(0, canvas_width, size=trees_amount), np.random.randint(0, canvas_height, size=trees_amount)))

    starting_point = [100, 20]

    # animate with time binding
    start_time = time.time()

    # main loop
    while True:

        # animate via sine and cosine
        estimated_time = time.time() - start_time
        coords_rab1[0] = starting_point[0] + (np.sin(estimated_time)*80).astype(int)
        coords_rab1[1] = starting_point[1] + (np.cos(estimated_time)*20).astype(int)

        coords_fox[0] = starting_point[0] - (np.sin(estimated_time+4)*80).astype(int)
        coords_fox[1] = starting_point[1] - (np.cos(estimated_time*2+4)*20).astype(int)

        coords_rab2[0] = starting_point[0] - (np.sin(estimated_time+5)*80).astype(int)
        coords_rab2[1] = starting_point[1] - (np.cos(estimated_time*2+5)*20).astype(int)

        # Step 1. Draw
        render.draw_sprite(rabbit1, *coords_rab1)
        render.draw_sprite(fox, *coords_fox)
        render.draw_sprite(rabbit2, *coords_rab2)

        for treee in tree_coords[0]:
            render.draw_sprite(tre, *treee)

        # Step 2. Show
        render.show()

        # Step optional. Limit FPS
        time.sleep(1/fps)

        # Step 3. Clear
        render.clear()


if __name__ == '__main__':
    main()