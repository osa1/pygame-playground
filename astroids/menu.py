import pygame

import game_state

class FadingText:
    def __init__(self, text, font, color, ticks, fading=True):
        self.start_color = color
        self.text = text
        self.font = font
        self.color_backup = color
        self.color = color
        # ticks indicate in how many ticks will text disappear
        self.ticks = ticks
        self.range = color
        self.fading = fading
        # fade speed
        self.step = float(self.range) / self.ticks

    def render(self, ticks):
        if self.fading:
            self.color -= self.step * ticks
        else:
            self.color += self.step * ticks

        if self.color < 0 or self.color > self.range:
            self.fading = not self.fading
            self.color = self.range if self.color > self.range else 0

        return self.font.render(self.text, True, (self.color,)*3)

    def reset_color(self):
        self.color = self.backup_color

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("Monospace", 40)

        self.create_menu()
        self.selected = 0

    def create_menu(self):
        self.start_game = FadingText("New Game", self.font, 0xFF, 500)
        self.about = FadingText("About", self.font, 0xFF, 500)
        self.exit = FadingText("Exit", self.font, 0xFF, 500)
        self.cont = FadingText("Continue", self.font, 0xFF, 500)

        self.options = [self.start_game,
                self.about,
                self.exit]

    def draw(self, surface, maxx, maxy):
        total_height = 0
        surfaces = []
        for i in xrange(len(self.options)):
            if i == self.selected:
                surfaces.append(self.options[i].render(game_state.ticks))
            else:
                surfaces.append(self.options[i].render(0))

        for s in surfaces:
            total_height += s.get_height()

        spacer = 10
        start = maxy/2 - total_height/2 - spacer

        for s in surfaces:
            surface.blit(s, (maxx/2-s.get_width()/2, start+spacer))
            start += s.get_height()

    def key_pressed(self, pressed):
        if pressed[pygame.K_UP]:
            self.create_menu()
            self.selected -= 1
            if self.selected < 0:
                self.selected += len(self.options)
        elif pressed[pygame.K_DOWN]:
            self.create_menu()
            self.selected = (self.selected+1) % len(self.options)
        
        if pressed[pygame.K_RETURN]:
            if self.options[self.selected] == self.start_game:
                game_state.menu_visible = False
                game_state.start_game()
                print "ok"
