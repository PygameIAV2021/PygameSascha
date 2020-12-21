# Projekt PyGame im Fach Skriptprogrammierung von Sascha Chladek IAV3/4

# Einbinden der Bibliotheken aus default mit Konstanten
from defaults import *
from game_classes import *

# initialisieren von pygame
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Worms for you")
clock = pygame.time.Clock()

# Background Image
background = pygame.image.load("background.jpg")
imagesize = background.get_rect()
background_scaled = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player Image
player = spritesheet("worms_sprite_sheet.png", 13, 13)
CENTER_HANDLE = 1

animation_index = 0

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")

    # Spiellogik hier integrieren





    # Spielfeld löschen
    screen.fill(WHITE)

    # Spielfeld/figuren zeichnen
    # screen.blit(background_scaled, (0, 0))
    player.draw(screen, animation_index % player.totalCellCount, HSW, HSH, CENTER_HANDLE)
    animation_index += 1

    # Player

    # Grundlinnie zeichnen
    # pygame.draw.line(screen, RED, [0, 430], [640, 430], 5)

    # pygame.draw.circle(screen, WHITE, (HSW, HSH), 6, 7)

    # Fenster aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()


