try:
    import requests
    import os
    import time

except ModuleNotFoundError:
    print('\033[1;31mOps!!!, o modulo requests não foi encontrado, por favor instale com o pip3\033[0;0m')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MyBanner():
    print('''
\033[1;33m                           .'clcc;.':;
                    .',,:cllodxxxxxxxdddcllo: .
                ..coodxk0KXNNNNWWWWNNNNXK0OOklo;,.
              ;cooxOKNNWWWWWWWWWWWWWWWWWWWWNNKOxdc,
             odxOXNWWWWWWWX...      ..,WWWWWWWWNXOdoc.
          'clxXNWWWWWWX..                ..,NNNNXXX0xl;:
         ,lx0NWWWWWWK  oooololllllllllllccclxkkkkkkKXKOd.
        cdkNNWWWW,     xxxxxxxxxxxxxxxxxxxxxxxxxxxxOXNNOd:
       'dONWWWWx       xxxxkkkkkkkkkkkkxxxxxxxxxxxxOXNWN0dc
      .d0NWWWW;        .......   .'kkkkkkkxxc.....'0NWWWN0o,
      lkNWWWW:                    .kkkkkkkkk;       KWWWWNOo.
     ;dNNWWWO                     .kkkkkkkkk;       cWWWWWNdl.
    .oONWWWW.                      kkkkkkkkk,        :WWWWN0Od
    ;oKNWWWW.                      xkkkkkkkk'        .WWWWNNxo
    cONNWWWWX                      dkkkkkkkk'        .NWWWNNo;
     kNNWWWW:                      lkkkkkkkk.        .WWWWNNk'
     cXNWWWW0                      xkkkkkkkk.         WWWWNNk ;
     .kNWWWWN,    ;               ;kkkkkkkkk         0WWWWNO;
      ;KNWWWWK.  lxdl:,         .cxkkkkkkkk;        .WWWWNXl
       oNWWWWWo.;xxxxxxxoollllodxkkkkkkkkkl       :cNWWWWNx.
        oNWWWNXkxxxxxxxxxkkkkkkkkkkkkkkkkc       .0WWWWWNk.
         oNNWNXkxxxxxxxxxxxxxkkkkkkkkxxc       .dNWWWWNXx
          cXNNNXK0Okxxxxxxxxxxxxxxxo.        xXNWWWWWNXd,
            ;XNNNNNNXKK0o.,                ;KWWWWWWNXo.
              dNNWWWWWWWNKOd,',.  .:;';cxKNWWWWWWNKl
                .xNNWWWWWWWWWWWNNNWWWWWWWWWWWWNNk
                  .'.0NNNWWWWWWWWWWWWWWWWNNNK0.
                         ..xKKXNNNNXKXN:...\033[0;0m
    ''')
    time.sleep(3)

def main():

    try:
        clear()
        print('''\033[1;92m
\t     ██╗     █████╗     ███████╗
\t     ██║    ██╔══██╗    ██╔════╝
\t     ██║    ███████║    ███████╗
\t██   ██║    ██╔══██║    ╚════██║
\t╚█████╔╝    ██║  ██║    ███████║
\t ╚════╝     ╚═╝  ╚═╝    ╚══════╝
                \033[1;97mJo Animes Search
            \033[1;92m[\033[1;96mi\033[1;92m] \033[1;97mDigite o nome do anime\033[0;0m

              ''')

        #Request
        anime = input('\033[1;94m>>>\033[1;97m ')
        try:
            api = requests.get(f'https://appanimeplus.tk:443/animetvtech-60.php?search={anime}').json()
            anime_id = api[0]['id']
            anime_api = requests.get(f'https://appanimeplus.tk:443/animetvtech-60.php?info={anime_id}').json()

            #Info anime
            nome = anime_api[0]['category_name']
            ds = anime_api[0]['category_description']
            gn = anime_api[0]['category_genres']
            ano = anime_api[0]['ano']

            #Output
            clear()
            print(f'''
\033[1;92m{nome}

\033[1;97m{ds}

\033[1;94m{gn}
\033[1;93m{ano}\033[0;0m
              ''')

        except Exception as erro:
            clear()
            print('\033[1;31mAnime não encontrado\033[0;0m\n')

        opc = input('\033[1;95mDeseja voltar ? (\033[1;92ms\033[1;95m/\033[1;91mn\033[1;95m):\033[1;97m ')
        if opc == 'S' or opc == 's':
            main()

        else:
            clear()
            MyBanner()
            exit()

    except KeyboardInterrupt:
        print('\n\033[1;31mSaindo!\033[0;0m\n')


clear()
MyBanner()
main()
