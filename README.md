# Build an Adversarial Game Playing Agent

![Example game of isolation on a square board](assets/game_isolation.gif)

## Motivation
AI is an important topic for robotics and self-driving cars.
I did this project as part of Udacity, Artificial Intelligence Nanodegree.

#  Project
I've implemented AI Player for  game of isolation in my_custome_player.py, method get_action()  
My AI player is based on minmax search, optimized with  alpha beta pruning, enhanced with heuristics.


# Game rules
In the game Isolation, two players each control their own single token and alternate taking turns moving the token from one cell to another on a rectangular grid. Whenever a token occupies a cell, that cell becomes blocked for the remainder of the game. An open cell available for a token to move into is called a "liberty". The first player with no remaining liberties for their token loses the game, and their opponent is declared the winner.

In knights Isolation, tokens can move to any open cell that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. On a blank board, this means that tokens have at most eight liberties surrounding their current location. Token movement is blocked at the edges of the board (the board does not wrap around the edges), however, tokens can "jump" blocked or occupied spaces (just like a knight in chess).

Finally, agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond. The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move.