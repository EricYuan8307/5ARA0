import agent
import client.state
from PIL import Image
from model import *


class TestPokerAgent:
    # <ASSIGNMENT: Test agent initialization and the make_action() function. Also test logging and error handling if you
    # chose to use them.>
    
    def test_agent_initialization(self, agent):
        """ Test whether the agent is initialized correctly.

        Args:
            agent (PokerAgent): Poker agent object. 
        """       
        assert agent.pic is None and agent.model is not None
        # Test whether the model is loaded correctly.
        assert type(agent.model) == tf.keras.Sequential
    
    
    
   
    def test_agent_make_action(self, agent, gamestate, gameroundstate):
        """ Test whether the agent makes the correct action.

        Args:
            agent (PokerAgent): Poker agent object.
            gamestate (ClientGameState): ClientGameState object to keep track of one game.
            gameroundstate (ClientGameRoundState): ClientGameRoundState object to keep track of one round.
        """        

        
        gameroundstate.set_moves_history(['CHECK', 'BET'])
        gameroundstate.set_turn_order(1)
        gameroundstate.set_available_actions(['CALL', 'FOLD'])
        agent.pic = 'J'
        possible_action = ['FOLD']
        assert agent.make_action(round=gameroundstate, state=gamestate) in possible_action

        # situation2: Player first-hand. Player get card J and check. If robot choose to BET, the player1 should fold.
        gameroundstate.set_moves_history(['CHECK', 'BET'])
        gameroundstate.set_turn_order(1)
        gameroundstate.set_available_actions(['CALL', 'FOLD'])
        agent.pic = 'K'
        possible_action = ['CALL']
        assert agent.make_action(round=gameroundstate, state=gamestate) in possible_action

        # situation3: Player back-hand and get card Queen. If the bot choose to check, Player should check.
        gameroundstate.set_moves_history(['CHECK'])
        gameroundstate.set_turn_order(2)
        gameroundstate.set_available_actions(['CHECK', 'BET'])
        agent.pic = 'Q'
        possible_action = ['CHECK']
        assert agent.make_action(round=gameroundstate, state=gamestate) in possible_action

        # situation4: Player back-hand and get card Jack. If the robot choose to bet, player should fold.
        gameroundstate.set_moves_history(['BET'])
        gameroundstate.set_turn_order(2)
        gameroundstate.set_available_actions(['CALL', 'FOLD'])
        agent.pic = 'J'
        possible_action = ['FOLD']
        assert agent.make_action(round=gameroundstate, state=gamestate) in possible_action

        # situation5: Player back-hand and get card King. If the robot choose to bet, player should fold.
        gameroundstate.set_moves_history(['CHECK'])
        gameroundstate.set_turn_order(2)
        gameroundstate.set_available_actions(['CHECK', 'BET'])
        agent.pic = 'K'
        possible_action = ['BET']
        assert agent.make_action(round=gameroundstate, state=gamestate) in possible_action
        


    def test_agent_logging(self, agent, gamestate):
        """ Test whether the agent logs the correct information.

        Args:
            agent (PokerAgent): Poker agent object.
            gamestate (ClientGameState): ClientGameState object to keep track of one game.
        """        
        # check if the agent does not crash and stdout is not empty
        agent.on_game_start()
        agent.on_game_end(gamestate, 'WIN')
        agent.on_new_round_request(gamestate)
    