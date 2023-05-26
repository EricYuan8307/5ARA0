from model import load_model, identify
from client.state import ClientGameRoundState, ClientGameState
import random


class PokerAgent(object):

    def __init__(self):
        self.model = load_model()
        self.pic = None

    def make_action(self, state: ClientGameState, round: ClientGameRoundState) -> str:
        """
        Next action, used to choose a new action depending on the current state of the game. This method implements your
        unique PokerBot strategy. Use the state and round arguments to decide your next best move.

        Parameters
        ----------
        state : ClientGameState
            State object of the current game (a game has multiple rounds)
        round : ClientGameRoundState
            State object of the current round (from deal to showdown)

        Returns
        -------
        str in ['BET', 'CALL', 'CHECK', 'FOLD'] (and in round.get_available_actions())
            A string representation of the next action an agent wants to do next, should be from a list of available actions
        """
        # get pictures
        round.set_card(self.pic)

        # get the available choice
        action_choice = round.get_available_actions()

        # get the order
        order = round.get_turn_order()

        # random probability
        beta = random.random()/3
        chance = random.random()

        #receive the previous action
        history = round.get_moves_history()


        if order == 1:

            if len(history) == 0:
                if self.pic == "J":
                    if chance <= beta:
                        if "BET" in action_choice:
                            return "BET"
                    else:
                        if "CHECK" in action_choice:
                            return "CHECK"

                if self.pic == "K":
                    if chance <= beta * 3:
                        if "BET" in action_choice:
                            return "BET"
                    else:
                        if "CHECK" in action_choice:
                            return "CHECK"

                if self.pic == "Q":
                    if "CHECK" in action_choice:
                        return "CHECK"
            else:
                if history[-1] == "BET":
                    if self.pic == "J":
                        if "FOLD" in action_choice:
                            return "FOLD"

                    if self.pic == "K":
                        if "CALL" in action_choice:
                            return "CALL"

                    if self.pic == "Q":
                        if chance <= (beta + 1/3):
                            if "CALL" in action_choice:
                                return "CALL"
                        else:
                            if "FOLD" in action_choice:
                                return "FOLD"
        else:
            if self.pic == "K":
                if "BET" in action_choice:
                    return "BET"
                elif "CALL" in action_choice:
                    return "CALL"

            if self.pic == "Q":
                if "CHECK" in action_choice:
                    return "CHECK"
                elif chance <= 1/3:
                    if "CALL" in action_choice:
                        return "CALL"
                else:
                    if "FOLD" in action_choice:
                        return "FOLD"
            if self.pic == "J":
                if "FOLD" in action_choice:
                    return "FOLD"
                elif chance <= 1/3:
                    if "BET" in action_choice:
                        return "BET"
                else:
                    if "CHECK" in action_choice:
                        return "CHECK"



    def on_image(self, image):
        """
        This method is called every time when card image changes. Use this method for image recongition procedure.

        Parameters
        ----------
        image : Image
            Image object
        """
        pic = identify(image,self.model)
        self.pic = pic
        

    def on_error(self, error):
        """
        This methods will be called in case of error either from server backend or from client itself. You can
        optionally use this function for error handling.

        Parameters
        ----------
        error : str
            string representation of the error
        """
        print(error)

    def on_game_start(self):
        """
        This method will be called once at the beginning of the game when server confirms both players have connected.
        """
        print("start")

    def on_new_round_request(self, state: ClientGameState):
        """
        This method is called every time before a new round is started. A new round is started automatically.
        You can optionally use this method for logging purposes.

        Parameters
        ----------
        state : ClientGameState
            State object of the current game
        """
        print("New round. Bank:", state.get_player_bank())

    def on_round_end(self, state: ClientGameState, round: ClientGameRoundState):
        """
        This method is called every time a round has ended. A round ends automatically. You can optionally use this
        method for logging purposes.

        Parameters
        ----------
        state : ClientGameState
            State object of the current game
        round : ClientGameRoundState
            State object of the current round
        """
        print(f'----- Round {round.get_round_id()} results ----- ')
        print(f'  Your card       : {round.get_card()}')
        print(f'  Your turn order : {round.get_turn_order()}')
        print(f'  Moves history   : {round.get_moves_history()}')
        print(f'  Your outcome    : {round.get_outcome()}')
        print(f'  Current bank    : {state.get_player_bank()}')
        print(f'  Show-down       : {round.get_cards()}')

    def on_game_end(self, state: ClientGameState, result: str):
        """
        This method is called once after the game has ended. A game ends automatically. You can optionally use this
        method for logging purposes.

        Parameters
        ----------
        state : ClientGameState
            State object of the current game
        result : str in ['WIN', 'DEFEAT']
            End result of the game
        """
        print(f'----- Game results ----- ')
        print(f'  Outcome:    {result}')
        print(f'  Final bank: {state.get_player_bank()}')
