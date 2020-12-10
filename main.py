# Projekt PyGame im Fach Skriptprogrammierung von Sascha Chladek IAV3/4

# Einbinden der Bibliotheken aus default mit Konstanten
from defaults import *

# initialisieren von pygame
pygame.init()

# Background Image
background = pygame.image.load("background.jpg")
imagesize = background.get_rect()

# Fenster öffnen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])

# Titel für Fensterkopf
pygame.display.set_caption("Worms for you")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

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
    background_scaled = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGTH))
    screen.blit(background_scaled, (0,0))

    # Grundlinnie zeichnen
    pygame.draw.line(screen, RED, [0, 430], [640, 430], 5)

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
