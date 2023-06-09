import os
import pytest
from PIL import Image
from client.state import ClientGameState, ClientGameRoundState
from agent import PokerAgent
from model import *

TEST_DIR = os.path.dirname(os.path.abspath(__file__))  # Mark the test root directory
TRAINING_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "training_images")
TEST_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "test_images")

os.environ['Luminous Marten']="true"



# Context to retain objects passed between steps
class Context:
    coordinator_id = "placeholder_id"
    token = "placeholder_token"
    start_bank = 5
    moves_history = ['CHECK']
    available_actions = ['CHECK', 'BET']
    cards = ['J', 'Q', 'K']
    outcome = '1'
    

@pytest.fixture()
def image(request):
    return Image.open(os.path.join(TEST_IMAGE_TEST_DIR, "J_451.png"))


# Create a ClientGameState object fixture. Scope = module because we only need to create it once.
@pytest.fixture(scope="module")
def gamestate():
    return ClientGameState(Context.coordinator_id, Context.token, Context.start_bank)


# Create a gamestate object fixture. Scope = module because we only need to create it once.
@pytest.fixture(scope="module")
def gameroundstate():
    gameroundstate = ClientGameRoundState(coordinator_id = Context.coordinator_id, round_id = 1)
    gameroundstate.set_cards(Context.cards)
    gameroundstate.set_moves_history(Context.moves_history)
    gameroundstate.set_available_actions(Context.available_actions)
    return gameroundstate

# Create a pokeragent object fixture. 
@pytest.fixture(scope="module")
def agent():
    return PokerAgent()

  


# <ASSIGNMENT: Define your own fixtures for testing here>

# Create a ClientGameState object fixture. Scope = module because we only need to create it once.
@pytest.fixture(scope="module")
def gamestate():
    return ClientGameState(Context.coordinator_id, Context.token, Context.start_bank)


# Create a gamestate object fixture. Scope = module because we only need to create it once.
@pytest.fixture(scope="module")
def gameroundstate():
    gameroundstate = ClientGameRoundState(coordinator_id=Context.coordinator_id, round_id=1)
    gameroundstate.set_cards(Context.cards)
    gameroundstate.set_moves_history(Context.moves_history)
    gameroundstate.set_available_actions(Context.available_actions)
    return gameroundstate


# Create a pokeragent object fixture.
@pytest.fixture(scope="module")
def agent():
    return PokerAgent()
