import console
import random

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