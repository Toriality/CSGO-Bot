import console
import random
import pyperclip

async def joke():
    jokes = [
        "Se você fosse um mapa do CS, você seria o de_licia",
        "Quantos pratas se precisa pra trocar uma lampada? Nenhum, eles nem sabem subir uma escada!",
        "O que o Freddie Mercury diz quando faz uma kill? Another one bites de_dust",
        "Como o padre bateu o carro? Dando uma rezinha.",
        "O que o pato falou para a pata? Vem quá.",
        "Sabe a piada do ponei? Po nei eu XDXDXDXDXDXDXDXDD",
        "Por que os dinossauros não batem palmas? Porque estão todos mortos.",
        "Como o padre se energiza quando esta com sono? Café.",
        "O que a mulher do Goku foi fazer no shopping? Comprar uma super saia jeans :D",
        "Qual a formula quimica da agua benta? H DEUS O",
        "Por que o pirata so assistiu metade do filme? Porque ele estava usando tapa-olhos",
        "Qual cidade é dividida em 4? FOURtaleza",
        "Por que não se deve partir o coração de uma regua? Por que ela tem centimentros",
    ]
    await console.write("say {}".format(random.choice(jokes)))

async def trivia():
    trivs = [
        "O CSGO possui um total de 18 patentes.",
        "Realizado em 2013, a DreamHack Winter foi o primeiro major de CSGO. A premiação foi U$250 mil e a Fnatic foi campeã.",
        "De acordo com a HLTV, o mapa Mirage é o mais jogado de toda a história do CSGO, em seguida Inferno e Dust2.",
        "Apos 9-10 minutos de espera para partida, o jogo ira procurar pessoas com patentes mais baixas ou mais altas que a sua para aumentar as chances de achar uma partida.",
        "Os seus inimigos nao conseguem ouvir voce trocando as armas, granadas ou faca.",
        "Olhar em direção a bomba não reduz o dano causado por ela.",
        "Quick-reloading não é mais rapido que recarregar normalmente.",
        "Voce consegue tacar granadas enquanto defusa se clicar com o botao do mouse direito, podendo alternar para o botao esquerdo posteriormente.",
        "Voce consegue usar o scope enquanto defusa, isso pode enganar os oponentes.",
        "Se voce pressionar o botao direito do mouse enquanto recarrega uma shotgun, a animação ira congelar.",
        "Apertar espaço + cntrl faz você pular mais alto, apertar cntrl + espaço faz pular mais alto ainda.",
        "A maneira mais rapida de subir escadas é pressionando W juntamente com A ou D dependendo da sua posição.",
        "Galinhas conseguem viver debaixo da agua, no CSGO.",
        "O computador do mapa Agency tem um simbolo de banana, uma refeencia a Apple",
        "O som da C4 do CSGO foi editado usando um editor de som pirateado, que feio Valve...",
        "Na radio do mapa Office, voce pode ouvir a voz do fundador da Valve.",
        "Todos os overwatchs duram 8 rounds.",
        "Ha codigos no jogo sobre oculos de visão noturna, mas não foram implementados.",
        "Na versão alpha do CSGO, a scout usava o mesmo som da AWP.",
        "No modo mata-mata você ganha 1 ponto cada vez que mata uma galinha",
        "Corpos mortos são client-side, ou seja, a maneira que estao posicionados para você pode nao ser a messma para outros jogadores.",
        "Voce pode abrir as frestas da ventoinha do Nuke apertando E.",
        "Você consegue destruir uma porta usando a Zeus",
        "O codigo da C4 é 7355608.",
        "CSGO foi lançado dia 21 de Agosto de 2012, 444 dias após o lançamento da primeira versão do Counter Strike",
        "Counter Strike foi primeiramente uma modificação para o jogo Half Life.",
        ]
    await console.write("say {}".format(random.choice(trivs)))

async def allah():
    await console.write("say  ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ ﷽﷽﷽ �")

async def paste():
    await console.write("say {}".format(pyperclip.paste()))

