import pygame, sys, json
with open('data.json', encoding="utf8") as data:
    f = data.read()
data = json.loads(f)
pygame.init()
confirma = pygame.mixer.Sound("CONFIRMA.wav")
fim = pygame.mixer.Sound("FIM.wav")
screen = pygame.display.set_mode([1366, 768], pygame.FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 56)
mediumfont = pygame.font.SysFont('arial', 32)
smallfont = pygame.font.SysFont('arial', 22)
bigfont = pygame.font.SysFont('arial', 112)
SEC = 1
CC = False
RA = ""
NV = ""
V = ""
info = ""
running = True
sec3lastpressed = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                running = False
            elif event.key == pygame.K_KP_ENTER and CC:
                if SEC == 1:
                    CC = False
                    info = ""
                    SEC = 2
                    confirma.play()
                elif SEC == 2:
                    data["estudantes"][RA]["votou"] = True
                    data["candidatos"][V]["votos"] += 1
                    info = ""
                    RA = ""
                    V = ""
                    NV = ""
                    CC = False
                    SEC = 3
                    fim.play()
                    with open("data.json", "w") as outfile:
                        json.dump(data, outfile)
            elif event.key == pygame.K_KP_PLUS:
                info = ""
                CC = False
                if SEC == 1:
                    RA = ""
                elif SEC == 2:
                    V = ""
                    NV = ""
            elif event.key == 1073741923:
                if SEC == 2:
                    NV = ""
                    CC = True
                    V = "BRANCO"
                    info = "VOTO EM BRANCO"
            else:
                if SEC == 1:
                    if len(RA) < 9:
                        info = ""
                        RA += event.unicode
                    if len(RA) == 9:
                        if data["estudantes"].get(RA) is not None:
                            if not data["estudantes"][RA]["votou"]:
                                info = data["estudantes"][RA]["nome"]
                                CC = True
                            else:
                                info = "JÁ VOTOU"
                        else:
                            info = "RA INVÁLIDO"
                elif SEC == 2:
                    if len(NV) < 2:
                        NV += event.unicode
                    if len(NV) == 2:
                        V = NV
                        if data["candidatos"].get(V) is None:
                            V = "NULO"
                            info = "VOTO NULO"
                        CC = True
                elif SEC == 3:
                    sec3lastpressed += str(event.key)
                    if sec3lastpressed.endswith("107374191410737419131073741919"):
                        sec3lastpressed = ""
                        SEC = 1

    screen.fill((255, 255, 255))
    line = pygame.Rect(0, 700, 1366, 3)
    pygame.draw.rect(screen, (0, 0, 0), line)
    helpstr = ["Aperte VERDE para confirmar.", "Aperte VERMELHO para corrigir.", "Aperte BRANCO para votar em branco."]
    for i, stg in enumerate(helpstr):
        helptext = smallfont.render(stg, True, (0, 0, 0))
        screen.blit(helptext, helptext.get_rect(bottom=728+i*20))
    if SEC == 1:
        xs = [683-220, 683-165, 683-110, 683-55, 683, 683+55, 683+110, 683+165, 683+220]
        for x in xs:
            rect = pygame.Rect(x, 384, 50, 80)
            rect.center = (rect.x, rect.y)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        for i, char in enumerate(RA):
            chartext = font.render(char, True, (0, 0, 0))
            screen.blit(chartext, chartext.get_rect(center=(xs[i], 384)))
        text = font.render("Insira seu RA.", True, (0, 0, 0))
        infotext = font.render(info, True, (0, 0, 0))
        screen.blit(text, text.get_rect(center=(683, 384-100)))
        screen.blit(infotext, infotext.get_rect(center=(683, 384+100)))
    elif SEC == 2:
        seuvotopara = smallfont.render("SEU VOTO PARA", True, (128, 128, 128))
        representantedeturma = font.render("Representante de Turma", True, (0, 0, 0))
        numero = mediumfont.render("Número: ", True, (0, 0, 0))
        xs = [200, 255]
        for x in xs:
            rect = pygame.Rect(x, 261, 50, 80)
            rect.center = (rect.x, rect.y)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        for i, char in enumerate(NV):
            chartext = font.render(char, True, (0, 0, 0))
            screen.blit(chartext, chartext.get_rect(center=(xs[i], 261)))
        if V != "":
            if V == "NULO":
                numeroerrado = font.render("NÚMERO ERRADO", True, (0, 0, 0))
                votonulo = bigfont.render(info, True, (0, 0, 0))
                screen.blit(numeroerrado, (25, 311))
                screen.blit(votonulo, votonulo.get_rect(center=(683, 504)))
            elif V == "BRANCO":
                votobranco = bigfont.render(info, True, (0, 0, 0))
                screen.blit(votobranco, votobranco.get_rect(center=(683, 504)))
            else:
                estudantev = data["candidatos"][V]["estudante"]
                vice = data["candidatos"][V]["vice"]
                partido = data["candidatos"][V]["partido"]
                fotoestudante = pygame.image.load(f"fotos/{estudantev}.png")
                fotovice = pygame.image.load(f"fotos/{vice}.png")
                rectestudante = pygame.Rect(1041, 25, 300, 400)
                rectvice = pygame.Rect(1191, 450, 150, 200)
                pygame.draw.rect(screen, (0, 0, 0), rectestudante, 0)
                pygame.draw.rect(screen, (0, 0, 0), rectvice, 0)
                nome = mediumfont.render(f'Nome: {data["estudantes"][estudantev]["nome"]}', True, (0, 0, 0))
                partido = mediumfont.render(f'Partido: {partido}', True, (0, 0, 0))
                vicerepresentante = mediumfont.render(f'Vice-Representante: {data["estudantes"][vice]["nome"]}', True, (0, 0, 0))
                screen.blit(fotoestudante, rectestudante)
                screen.blit(fotovice, rectvice)
                screen.blit(nome, (25, 311))
                screen.blit(partido, (25, 361))
                screen.blit(vicerepresentante, (25, 411))
        screen.blit(seuvotopara, (25, 10))
        screen.blit(representantedeturma, representantedeturma.get_rect(center=(643, 150)))
        screen.blit(numero, (25, 241))
    elif SEC == 3:
        text = bigfont.render("FIM", True, (0, 0, 0))
        screen.blit(text, text.get_rect(center=(683, 384)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
