# Urna Eletrônica (recriado por luca4s)
Uma simulação de urna eletrônica que pode ser ultilizada para fazer eleições.
# Requisitos:
- Python3 (com pip)
- Experiência com Python (caso queira fazer modificações)
# Como utilizar:
- Clone o repositório
```
git clone https://github.com/luca4s/urna-eletronica.git
```
- Baixe os requisitos
```
python3 -m pip install -r requirements.txt
```
- Configure o `data.json` com os eleitores e candidatos (PRECISA incluir branco e nulo)
- Inicie o script
```
./run.sh
```
# Guia
- Para confirmar, aperte `ENTER` no teclado numérico
- Para corrigir, aperte `+` no teclado numérico
- Para votar em branco, aperte `,` no teclado numérico
- Para voltar ao início depois da tela de FIM, digite `217` no teclado numérico (`NumLock` deve estar ligado)
- Para fechar, aperte `ESC`
Após fechar, os votos contados serão automaticamente apurados e inseridos no arquivo `resultados.html`
