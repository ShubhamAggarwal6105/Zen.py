import pygame
from backtracking import *
pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

def _flatten(_cls):
    pass

class Button:
    def __init__(self, surface, text, font, _border, _borderwidth, fore, back,_pos, command):
        self.surface = surface
        self.text = text
        self.__inx, self.__iny = 10, 5
        self.font = font
        self.border = _border
        self._borderwidth = _borderwidth
        self.fg = self.foreground = fore
        self.bg = self.background = back
        self.cmd = self.command = command
        self.pos = self.position = _pos
        self.__initR()

    def __initR(self):
        self.__textsurf = self.font.render(self.text, 1, self.fg)
        self.__tsize = self.__textsurf.get_width(), self.__textsurf.get_height()
        self.width = self.__tsize[0] + self.__inx * 2
        self.height = self.__tsize[1] + self.__iny * 2
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def Draw(self, padx = 0, pady = 0):
        self.__initR()
        _px, _py = padx if padx is not None else 0, pady if pady is not None else 0
        
        pygame.draw.rect(self.surface, self.bg, self.rect)
        pygame.draw.rect(self.surface, self.border, self.rect, self._borderwidth)
        
        self.surface.blit(self.__textsurf, 
            (_px + self.pos[0] + self.width // 2 - self.__tsize[0] // 2, 
            _py + self.pos[1] + self.height // 2 - self.__tsize[1] // 2))

    def handle_events(self, event):
        _p = pygame.mouse.get_pos()
        if (_p[0] > self.pos[0] and _p[0] < self.pos[0] + self.width) and\
            (_p[1] > self.pos[1] and _p[1] < self.pos[1] + self.width):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.command()

class Main:
    def __init__(self):
        self._init_display()
        self._init_runtime_vars()

    def _init_display(self):
        self._flags = 0
        self._display = pygame.display.set_mode((500, 700), self._flags)
        self._clock = pygame.time.Clock()

    def _init_runtime_vars(self):
        self._frames = 1000
        self.grid = [[" " for i in range(9)] for j in range(9)] # (cell_x, cell_y) : _value

        self._started = False
        self._hasalt = False

        self._cwid = 500 / 9
        self._sysfont = pygame.font.SysFont("Consolas", 45)
        self._disfont = pygame.font.SysFont("Consolas", 24)
        self._curcell = None
        self._lkeys = [
            pygame.K_1, pygame.K_2, pygame.K_3, 
            pygame.K_4, pygame.K_5, pygame.K_6,
            pygame.K_7, pygame.K_8, pygame.K_9
            ]

        self._solve = Button(self._display, "Solve", self._disfont, GREEN, 1, WHITE, BLACK, (10, 600), self._on_c_solve)

    def _draw_cell(self, _color, _gpos, _w):
        pygame.draw.rect(self._display, _color,
                    (_gpos[0] * self._cwid, _gpos[1] * self._cwid, self._cwid, self._cwid), _w)

    def _r_high(self, ):
        try:
            pos = pygame.mouse.get_pos()
            _c = [i // self._cwid for i in pos]
            if not (_c[0] > 8 or _c[1] > 8 or _c[0] < 0 or _c[1] < 0):
                self._draw_cell(RED, _c, 5)
        except:
            pass

    def _on_c_solve(self):
        print(self.grid, "\n\n\n\n\n", sep="\n")
        if Solve(self.grid, 0, 0):
            print(self.grid)

        else:
            print("no solution!")

    def _render_board(self):
        if self._curcell is not None:
            self._draw_cell(GREEN, self._curcell, 0)
        
        for x in range(9):
            for y in range(9):
                _fsurf = self._sysfont.render(str(self.grid[x][y]), 1, WHITE)
                _fs = _fsurf.get_width(), _fsurf.get_height()
                self._display.blit(_fsurf,
                    (y * self._cwid + (self._cwid // 2) - _fs[0] // 2, x * self._cwid + (self._cwid // 2) - _fs[1] // 2)) 

        for i in range(4):
            pygame.draw.line(self._display, WHITE, (0, i * 166.7), (500, i * 166.7), 5) # horizontal
            pygame.draw.line(self._display, WHITE, (i * 166.7, 0), (i * 166.7, 500), 5) # vertical

        for j in range(1, 9):
            pygame.draw.line(self._display, WHITE, (0, j * self._cwid), (500, j * self._cwid), 1)
            pygame.draw.line(self._display, WHITE, (j * self._cwid, 0), (j * self._cwid, 500), 1)


    def _r_info(self):
        _frsurf = self._disfont.render("FPS: %d" % self._clock.get_fps(), 1, WHITE)
        self._display.blit(_frsurf, (0, 505))

    def run(self):
        while True:
            self._display.fill((0, 0, 0))

            for event in pygame.event.get():
                self._solve.handle_events(event)

                if event.type == pygame.QUIT:
                    pygame.quit()

                if not self._started:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        m = pygame.mouse.get_pos()
                        c = [int(m[0] // self._cwid), int(m[1] // self._cwid)]

                        if (c[0] >= 0 and c[0] <= 8 and c[1] >= 0 and c[1] <= 8):
                            self._curcell = c
                            print(self._curcell)
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LALT:
                            self._hasalt = True

                        if event.key == pygame.K_RETURN:
                            if self._hasalt:
                                self._solve.command()

                        if self._curcell is not None:
                            if event.key in self._lkeys:
                                self.grid[self._curcell[1]][self._curcell[0]] = event.unicode

                            if event.key == pygame.K_BACKSPACE:
                                self.grid[self._curcell[1]][self._curcell[0]] = " "

                            if event.key == pygame.K_ESCAPE:
                                self._curcell = None

                    if event.type == pygame.KEYUP:
                        if self._hasalt:
                            self._hasalt = False

            self._r_high()
            self._render_board()
            self._r_info()
            self._solve.Draw()
            self._clock.tick(self._frames)
            pygame.display.flip()

Main().run()
