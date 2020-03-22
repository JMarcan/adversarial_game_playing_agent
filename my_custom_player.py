import random

from isolation.isolation import _WIDTH, _HEIGHT
from sample_players import DataPlayer

_CORNERS = [0, 10, 104, 114]
_WALLS = list(range(1, 10)) + list(range(105, 114)) + [i * (_WIDTH + 2) for i in range(1, _HEIGHT - 1)] + [i * (_WIDTH + 2) + (_WIDTH - 1) for i in range(1, _HEIGHT - 1)]
_CENTER = 57

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        

        if state.ply_count == 0:
            # if we do the first move, select the center
            self.queue.put(_CENTER)
        elif state.ply_count == 1:
            # if we do the second move, select wide opening
            opens = [i for i in state.actions() if i not in _CORNERS and i not in _WALLS and i != 57]
            self.queue.put(random.choice(opens))
            
        else:
            # for each other move, select the optimal minimax move at a fixed search depth of 3 plies
                 
            # Debug print final board status
            from isolation import DebugState
            dbstate = DebugState.from_state(state)
            print(dbstate)
            
            self.queue.put(self.minimax(state, depth=3)) 
        
       

    def minimax(self, state, depth):

        def min_value(state, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1))
            return value

        def max_value(state, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1))
            return value

        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1))
    
    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)