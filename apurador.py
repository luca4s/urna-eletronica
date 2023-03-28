import json, math
print("Carregando informações...")
with open('data.json', encoding="utf8") as data:
    f = data.read()
def calc(n, d):
    try:
        return math.floor((n / d) * 100)
    except ZeroDivisionError:
        return 0
data = json.loads(f)
candidatos = data['candidatos']
estudantes = data['estudantes']
html = "<!DOCTYPE html> <html> <head> <style> body { font-family: arial, sans-serif; text-align: center; } table { margin-left: auto; margin-right: auto; border-collapse: collapse; width: 75%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } </style> <title>Resultados</title> </head> <body> <h2>Resultados</h2> <table> <tr> <th>Nome</th> <th>Votou?</th> </tr>"
votos = 0
ausente = 0
ausentes = []
votosvalidos = 0
votosbrancos = candidatos["BRANCO"]["votos"]
votosnulos = candidatos["NULO"]["votos"]
candidatomaisvotado = ""
print("Apurando estudantes...")
for estudante in estudantes:
    if estudantes[estudante]["votou"]:
        votos += 1
        html += f" <tr> <td>{estudantes[estudante]['nome']}</td> <td><input type='checkbox' checked disabled></td> </tr>"
    else:
        html += f" <tr> <td>{estudantes[estudante]['nome']}</td> <td><input type='checkbox' disabled></td> </tr>"
html += f" </table> <br> <table> <tr> <th>Votos</th> <th>Votos Válidos</th> <th>Votos em Branco</th> <th>Votos Nulos</th> </tr> <tr> <td>{votos}</td> <td>{votosvalidos} ({calc(votosvalidos, votos)}% dos votos)</td> <td>{votosbrancos} ({calc(votosbrancos, votos)}% dos votos)</td> <td>{votosnulos} ({calc(votosnulos, votos)}% dos votos)</td> </tr> </table> <br> <table> <tr> <th>Número</th> <th>Votos</th> <th>Estudante</th> <th>Vice</th> <th>Partido</th> </tr>"
print("Apurando votos...")
for candidato in candidatos:
    if candidato != "BRANCO" and candidato != "NULO":
        votosvalidos += candidatos[candidato]["votos"]
        if candidatomaisvotado == "":
            candidatomaisvotado = candidatos[candidato]["numero"]
        elif candidatos[candidato]["votos"] > candidatos[candidatomaisvotado]["votos"]:
            candidatomaisvotado = candidatos[candidato]["numero"]
        html += f"<tr> <td>{candidatos[candidato]['numero']}</td> <td>{candidatos[candidato]['votos']} ({calc(candidatos[candidato]['votos'], votosvalidos)}% dos votos válidos)</td> <td>{estudantes[candidatos[candidato]['estudante']]['nome']}</td> <td>{estudantes[candidatos[candidato]['vice']]['nome']}</td> <td>{candidatos[candidato]['partido']}</td> </tr>"
html += " </table> </body> </html>"
with open('index.html', 'w') as file:
    file.write(html)
    print("Pronto!")
