import pygame
pygame.font.init()

import menu
import astroid
import game_state

def detect_collisions():
    if game_state.ship and game_state.running:
        for a in game_state.astroids[:]:
            for p in game_state.ship.point_list():
                if a.inside_polygon(p):
                    return True
    return False

def clean_astroids():
    for a in game_state.astroids[:]:
        if a.posx - 2*a.radius_range > game_state.screenx or \
                a.posx + 2*a.radius_range < 0 or \
                a.posy - 2*a.radius_range > game_state.screeny or \
                a.posy + 2*a.radius_range < 0:
                    game_state.astroids.remove(a)

def run():
    # TODO more maintainable game loop
    game_menu = menu.Menu()
    game_state.key_listeners.append(game_menu.key_pressed)

    score = 0
    score_font = pygame.font.SysFont("Consolas", 13, (255, 255, 255))

    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.KEYUP:
                for listener in game_state.key_listeners:
                    listener(pressed)
        
        for listener in game_state.repeat_key_listeners:
            listener(pressed)

        game_state.screen.fill((0, 0, 0))

        if game_state.create_ship:
            game_state.ship = astroid.Ship()
            game_state.repeat_key_listeners.append(game_state.ship.key_pressed)
            game_state.create_ship = False

        if game_state.menu_visible:
            game_menu.draw(game_state.screen, game_state.screenx, game_state.screeny)

        if game_state.running:
            for ast in game_state.astroids:
                ast.update()
                ast.draw(game_state.screen)
            if game_state.ship:
                score += float(game_state.ticks) / 1000
                score_text = score_font.render(str(score), 1, (255, 255, 255))
                game_state.screen.blit(score_text, (10, 10))

                game_state.ship.update()
                game_state.ship.draw(game_state.screen)

        if detect_collisions():
            game_state.running = False
            game_state.menu_visible = True
            score = 0

        clean_astroids()

        while len(game_state.astroids) < score / 2:
            game_state.astroids.append(astroid.generate_random_astroid())

        pygame.display.flip()
        game_state.ticks = game_state.clock.tick(30)

run()
