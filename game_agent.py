"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Heuristic One
    """
    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    next_moves = float(my_moves - opp_moves)
    return next_moves
    """
    # Heuristic Two
    next_next_moves = 0
    for move in game.get_legal_moves(player):
        next_ply = game.forecast_move(move)
        my_moves = len(next_ply.get_legal_moves(player))
        opp_moves = len(next_ply.get_legal_moves(game.get_opponent(player)))
        next_next_moves = float(max(next_next_moves, my_moves - opp_moves))

    # Heuristic Three
    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    p1x, p1y = game.get_player_location(player)
    p2x, p2y = game.width / 2, game.height / 2
    mahattan_centre_score = float((abs(p1x - p2x) + abs(p1y - p2y)))
    #print("my_moves: {} opp_moves: {} mahattan score: {}".format(my_moves, opp_moves, mahattan_centre_score))
    return (float(my_moves - opp_moves) * next_next_moves / mahattan_centre_score)
    """
    #print("Board Hash Value: ", game.hash())
    #print("Heuristics for the current board:")
    # print(game.to_string())
    # print("player a: ", game.get_legal_moves(player), "player b: ",
    #      game.get_legal_moves(game.get_opponent(player)))
    # if game.get_legal_moves(player) in game.get_legal_moves(game.get_opponent(player)):
    #    return float(my_moves + opp_moves)
    # else:
    # return float(my_moves - opp_moves)
    elif game.move_count > 15:
        return float(my_moves - opp_moves)
    else:
        return float(my_moves - 2 * opp_moves)
    """


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """
            Eucledian Distance 
    """
    p1x, p1y = game.get_player_location(player)
    p2x, p2y = game.width / 2, game.height / 2
    D = 1
    dx = abs(p1x - p2x)
    dy = abs(p1y - p2y)
    return (float(D * math.sqrt(dx * dx + dy * dy)))


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """
            Mahattan Distance
    """
    p1x, p1y = game.get_player_location(player)
    p2x, p2y = game.get_player_location(game.get_opponent(player))
    return float((abs(p1x - p2x) + abs(p1y - p2y)))


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score, timeout=20.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            # Handle any actions required after timeout as needed
            pass

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        def game_in_terminal_state(game, player):
            """ Check if game is in terminal state """
            if game.is_winner(player):
                return True
            elif game.is_loser(player):
                return True
            else:
                return False

        """ minimax routine """
        if game_in_terminal_state(game, self) or depth <= 0:
            return game.get_player_location(game.active_player)
        else:
            def minimizer(game, depth):
                """minimizer routine"""
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()

                if game_in_terminal_state(game, self) or depth <= 0:
                    best_move, score = game.get_player_location(
                        game.active_player), self.score(game, self)
                else:
                    value = float("+inf")
                    for move in game.get_legal_moves(game.active_player):
                        next_ply = game.forecast_move(move)
                        score = maximizer(next_ply, depth - 1)[1]
                        if min(value, score) == score:
                            best_move = move
                            value = score
                return (best_move, score)

            def maximizer(game, depth):
                """ maximizer routine """
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()

                if game_in_terminal_state(game, self) or depth <= 0:
                    best_move, score = game.get_player_location(
                        game.active_player), self.score(game, self)
                else:
                    value = float("-inf")
                    for move in game.get_legal_moves(game.active_player):
                        next_ply = game.forecast_move(move)
                        score = minimizer(next_ply, depth - 1)[1]
                        if max(value, score) == score:
                            best_move = move
                            value = score
                return (best_move, score)

            value = float("-inf")
            #print("Legal Moves: ", game.get_legal_moves(game.active_player))
            for move in game.get_legal_moves(game.active_player):
                next_ply = game.forecast_move(move)
                score = minimizer(next_ply, depth - 1)[1]
                if max(value, score) == score:
                    best_move = move
                    value = score
        return best_move


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """
    move_recorder = dict()

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        # Check if centre of the board if free to occupy
        if (game.move_count < 2):
            idx = game.width / 2
            idy = game.height / 2
            if (idx, idy) in game.get_blank_spaces():
                print(self.game.to_string())
                return (idx, idy)
        else:
            best_move = (-1, -1)

        # TODO: implement order-books to look-up moves.
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            # Implementing the interative deeping. assuming we only need
            # to search 9 levels deep for each move.
            self.search_depth = 1
            while True:
                best_move = self.alphabeta(game, self.search_depth)
                self.search_depth += 1

        except SearchTimeout:
            # Handle any actions required after timeout as needed
            # If Search Timeout is raised then player forfeits the game.
            # Nothing to do.
            pass

        # Return the best move from the last completed search iteration
        #print("TimeOut: Returning Best Move So Far: ", best_move)
        #print("Move Recorder: ", self.move_recorder)
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        best_move = (-1, -1)

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        def best_move_so_far(game, player):
            return (game.get_player_location(player), self.score(game, player))

        def game_in_terminal_state(game, player):
            """ Check if game is in terminal state """
            if game.is_winner(player):
                return True
            elif game.is_loser(player):
                return True
            else:
                return False

        if game_in_terminal_state(game, self):
            return game.get_player_location(self)
        else:
            def minimizer(game, depth, alpha, beta):
                # print("Min receives: Depth: {} Alpha: {} and Beta: {} value".format(
                    # depth, alpha, beta))
                """minimizer routine"""
                best_move = (-1, -1)
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()

                if depth <= 0:
                    best_move, best_value = best_move_so_far(game, self)
                    return (best_move, best_value)
                if game_in_terminal_state(game, self):
                    best_move, score = best_move_so_far(game, self)
                    #print("Terminal State: move: {} score: {}".format(best_move, score))
                    return (best_move, score)
                else:
                    best_value = float("+inf")
                    for move in game.get_legal_moves(game.active_player):
                        next_ply = game.forecast_move(move)
                        _, value = maximizer(next_ply, depth - 1, alpha, beta)
                        if value < best_value:
                            best_value = value
                            best_move = move

                        if value <= alpha:
                            # print("Alpha Cutoff !!! value: {} alpha: {}".format(
                            #    value, alpha))
                            break
                        else:
                            beta = min(beta, value)

                # print("Min returns: Best Move: {} Score: {} Alpha: {} Beta: {}".format(
                #    best_move, value, alpha, beta))
                return (best_move, best_value)

            def maximizer(game, depth, alpha, beta):
                # print("Max receives: Depth: {} Alpha: {} and Beta: {} value".format(
                #    depth, alpha, beta))
                """ maximizer routine """
                best_move = (-1, -1)
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()

                if game_in_terminal_state(game, self) or depth <= 0:
                    best_move, score = best_move_so_far(game, self)
                    #print("Terminal State: move: {} score: {}".format(best_move, score))
                    return (best_move, score)
                else:
                    for move in game.get_legal_moves(game.active_player):
                        best_value = float("-inf")
                        next_ply = game.forecast_move(move)
                        _, value = minimizer(next_ply, depth - 1, alpha, beta)
                        if value > best_value:
                            best_value = value
                            best_move = move

                        if value >= beta:
                            # print("Beta Cutoff !!! value: {} beta: {}".format(
                            #    value, beta))
                            break
                        else:
                            alpha = max(alpha, value)

                # print("Max returns: Best Move: {} Score: {} Alpha: {} Beta: {}".format(
                #    best_move, best_value, alpha, beta))
                return (best_move, best_value)

            #print("\n\nRoot: Going to spout some branches")
            best_move, best_value = maximizer(game, depth, alpha, beta)
            """
            if self.move_recorder[abs(game.hash())]:
                if_exist = self.move_recorder[abs(game.hash())]
                if if_exist[3] < depth:
                    self.move_recorder[abs(game.hash())] = (best_move, best_value, depth, alpha, beta)
            else:
                self.move_recorder[abs(game.hash())] = (best_move, best_value, depth, alpha, beta)
            """
            return best_move
