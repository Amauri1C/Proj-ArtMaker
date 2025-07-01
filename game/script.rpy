# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("585")


# The game starts here.

label start:

    # Show a background.
    scene bg room

    # Personagens
    show robo

    # These display lines of dialogue.

    e "Somos brabos, ne n, Renata???"
    e "Ja da pra passar de trimestre ja? :D"

    # This ends the game.

    return