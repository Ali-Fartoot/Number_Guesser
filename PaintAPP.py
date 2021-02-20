import pygame


def init():
    global screen
    pygame.init()
    # set screen size
    screen = pygame.display.set_mode((280, 280))
    # title name
    pygame.display.set_caption("MyPaintApp")
    # background color= 'white'
    screen.fill([255, 255, 255])
    main_loop()


# draw circle from start to the end by given radius (like a line that made by several circles)
def round_line(surface, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.display.update(pygame.draw.circle(surface, color, (x, y), radius))


# let program to draw
draw_on = False
# a value for showing last position that mouse had been moving
last_pos = None
# line color
color = (0, 0, 0)
# thickness of line
radius = 8
# a value that let program to continue (False means that "MyPaintApp" closed without saving
# and True means "MyPaintApp" saved 'new' picture and continue the running
resume = False


# return resume
def return_resume():
    return resume


def main_loop():
    global draw_on, last_pos, color, radius, resume

    # Simple exception handling
    try:
        while True:
            for event in pygame.event.get():
                # if program closed by 'close button'
                if event.type == pygame.QUIT:
                    raise StopIteration
                # if you press keyboard buttons
                if event.type == pygame.KEYDOWN:
                    # and that button is 'Enter' (or return0)
                    if event.key == pygame.K_RETURN:
                        # save image as 'image.png'
                        pygame.image.save(screen, "image.png")
                        # and resume because you save 'new' image
                        resume = True
                        # and exit
                        raise StopIteration
                # if you press mouse button and that button is right click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # restart program (for erase background)
                    init()
                # if you press mouse button and that button is left click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # let program to draw
                    draw_on = True
                    # and draw circle
                    pygame.draw.circle(screen, color, event.pos, radius)
                # if you put your finger off from button (button goes up)
                if event.type == pygame.MOUSEBUTTONUP:
                    # don't let program to draw
                    draw_on = False
                # if mouse move
                if event.type == pygame.MOUSEMOTION:
                    if draw_on:
                        # update screen detail and draw
                        pygame.display.update(pygame.draw.circle(screen, color, event.pos, radius))
                        round_line(screen, color, event.pos, last_pos, radius)
                    # save new last position
                    last_pos = event.pos
                pygame.display.flip()
    except StopIteration:
        # if something raise exit
        pygame.quit()