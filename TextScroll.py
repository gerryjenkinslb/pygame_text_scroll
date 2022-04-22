import pygame
import time
import os
import sys


class TextScroll:
    def __init__(self, area, font, fg_color, bk_color, text, ms_per_line=300):
        """object to display lines of text scrolled in with a delay between each line
        in font and fg_color with background o fk_color with in the area rect"""

        super().__init__()
        self.rect = area.copy()
        self.fg_color = fg_color
        self.bk_color = bk_color
        self.size = area.size
        self.surface = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.surface.fill(bk_color)
        self.font = font
        self.lines = text.split('\n')
        self.ms_per_line = ms_per_line
        self.y = 0
        self.y_delta = self.font.size("M")[1]
        self.next_time = None
        self.dirty = False

    def _update_line(self, line):  # render next line if it's time
        if self.y + self.y_delta > self.size[1]:  # line does not fit in remaining space
            self.surface.blit(self.surface, (0, -self.y_delta))  # scroll up
            self.y += -self.y_delta  # backup a line
            pygame.draw.rect(self.surface, self.bk_color,
                             (0, self.y, self.size[0], self.size[1] - self.y))  # erase area

        text = self.font.render(line, True, self.fg_color)
        self.surface.blit(text, (0, self.y))
        self.y += self.y_delta

    # call update from pygame main loop
    def update(self):

        time_now = time.time()
        if (self.next_time is None or self.next_time < time_now) and self.lines:
            self.next_time = time_now + self.ms_per_line / 1000
            line = self.lines.pop(0)
            self._update_line(line)
            self.dirty = True
            self.update()  # do it again to catch more than one event per tick

    # call draw from pygam main loop after update
    def draw(self, screen):
        if self.dirty:
            screen.blit(self.surface, self.rect)
            self.dirty = False


# Test this Class

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

STORY1 = """line one of text
second line of text
third line of text
** last line of text that fits
next line should force scroll up
and here again for
each line the follows"""

def example1():
    # start up pygame
    os.environ['SDL_VIDEO_WINDOW_POS'] = "1560,100"
    pygame.init()
    # print(sorted(pygame.font.get_fonts()))
    screen = pygame.display.set_mode((800, 500))
    screen.fill(WHITE)
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Liberation Sans", 30)
    area = pygame.Rect(50, 50, 700, 142)
    box = area.inflate(12, 12)
    print(area)
    pygame.draw.rect(screen, BLUE, box, 3)
    message = TextScroll(area, font, BLACK, WHITE, STORY1, ms_per_line=700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        else:
            # screen.fill(pygame.color.Color('black'))
            message.update()
            message.draw(screen)
            pygame.display.flip()
            clock.tick(60)

STORY2 = """
Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance or nature’s changing course untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall death brag thou wander’st in his shade,
When in eternal lines to time thou grow’st:
  So long as men can breathe or eyes can see,
  So long lives this, and this gives life to thee.

  --- William Shakespeare"""


def example2():
    # start up pygame
    os.environ['SDL_VIDEO_WINDOW_POS'] = "1560,100"
    pygame.init()
    # print(sorted(pygame.font.get_fonts()))
    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Liberation Sans", 30)
    message = TextScroll(pygame.Rect(50, 50, 700, 400), font, YELLOW, BLACK, STORY2, ms_per_line=300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        else:
            # screen.fill(pygame.color.Color('black'))
            message.update()
            message.draw(screen)
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    example1()
