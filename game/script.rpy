# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Define nome de personagem
define e = Character("585")
define i = Character("Glitch")

#Define como narrador (sem nome = não personagem)
define none = Character(" ")

# The game starts here.default menuset = set()
default menuset = set ()

# Label inicial
label inicio:
    $ boolean1 = 0
    $ boolean2 = 0

# Label de primeira resposta
label flowI:
    "idk"
    $ boolean1 += 1
    jump queroqva

#Label de segunda resposta
label flowII:
    "idk part 2"
    $ boolean2 += 1
    jump queroqva

#Label da pergunta
label warever:
    menu slas:
        "funciona??"
        "talvez va":
            jump flowI

        "nao vai":
            jump flowII

#Label de verificacao de terceira resposta
label queroqva:
    if boolean1 > 0:
        if boolean2 > 0:
            jump allTrue
        else:
            jump warever
    else:
        jump warever

#Label de quando tem terceira
label allTrue:
    menu bruh:
        "funciona?"
        "talvez va":
            jump flowI
        "nao vai":
            jump flowII
            
        "foi":
            jump flow
        

label start:
    jump inicio
    jump queroqva
    label flow:
        scene bg fnf
        
    #toca musica
    play music "audios/WantToBeClose.mp3"

    none "Sala de aula..."
    none "Os alunos da 585 debatem sobre o projeto de art maker..."

    # Exibe Personagem
    show robo

    # These display lines of dialogue.
    e "Somos brabos, ne n, Renata???"
    e "Ja da pra passar de trimestre ja? :D"
    show skin943 at right
    i "iai mn..."

    #toca efeito sonoro
    play sound "audios/OHMAGA.mp3"

    e "Tapoha meno...."
    hide robo

    none "é isso :D"

    # This ends the game.
    
    return