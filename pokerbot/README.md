# PokerBot Group Project (Weeks 4-8)

This repository contains the skeleton code for the PokerBot project agent (server client). In this group project you will develop an agent that plays a simplified version of poker (Kuhn poker) against fellow students. We first explain the setup and then the assignment.


## Setup

_Clone the Client and Server Repositories_

Accept the assignment invitation in GitHub Classroom. This creates a new personal remote with the skeleton code for the PokerBot project. Start VSCode, and in a terminal window, navigate to the root directory where you want to download the assignment repository. Then clone the repository, `git clone git@github.com:tue-5ARA0-<YYYY-QQ>/poker-server-client-<YOUR GITHUB HANDLE>.git poker-server-client`, where you insert the correct year, quartile and your own GitHub handle.

In order to play games with your agent on your own computer, you'll need to install the poker server as well. Type `git clone git@github.com:tue-5ARA0/poker-server-backend.git poker-server-backend`. This will clone the server repository. In order to get the server up and running locally, please consult the readme in the `poker-server-backend` repository.


_Setup the Virtual Environment_

Open a new terminal in VSCode and create a new virtual environment by typing `conda env create -f environment.yml` (unix-based systems users should use `environment_linux.yml` file). This command will create a new `pokerbot39` virtual environment and install required packages. Activate the newly created environment by `conda activate pokerbot39`.


_Install TensorFlow_

TensorFlow must be installed using pip. With the `pokerbot39` environment active, install TensorFlow using
```bash
pip install -r requirements.txt
```
If you are on an unix-based system, use the `requirements_linux.txt` file instead.

_Generate the Game Protocol_

Generate the game protocol by typing `python init.py`. This will setup protocols for the agent to interact with a (local) game server.

_Start a Local Game_

Follow the intructions in the `poker-server-backend` [readme](https://github.com/tue-5ARA0/poker-server-backend) to start a local server. In the terminal that runs your local server you will see test player tokens. These tokens represent the agent ids that the server expects to connect with. You will need to connect an agent to each token. An agent can be connected to the local server by opening a _new_ terminal and running

```bash
python main.py --token "<token UUID here>" --play "random"
``` 

You'll need to repeat this procedure to connect a second agent using the second token in the second terminal. The game will start automatically once both agents are connected. The server waits only a limited amount of time for both agents to connect.

You can also play a local game against a bot (with this setting you need only one terminal):

```bash
python main.py --token "<token UUID here>" --play "bot"
```

_Start an Online Game_

We also have a public (cloud) server running for you to play online games against bots or agents of fellow students. At the start of the project you will receive a unique secret token that identifies your agent to the server (keep this token secret, otherwise internet hackers will steal all of your virtual money and you won't be able to play public games).

In order to play an online game you need to specify a `--global` flag for the script and wait for your opponent to connect as well:

```bash
python main.py --token "<token UUID here>" --global --play "random" # or --play "bot"
```

You may also omit the `--token` argument if you store your secret token in a `token_key.txt` file in the same 
folder as the `main.py` script. 

In case if you want to play against a specific team, you can create a private game with the `--create` argument:

```bash
python main.py --token "<host agent token UUID here>" --global --create
```

The server will then respond with a private game coordinator token that you can share with your opponent, e.g.

```bash
id: "de2c20f1-c6b9-4536-8cb0-c5c5ac816634"
```

Your opponent can use this token to connect to your private game, e.g. (on the opponent's side):

```bash
> python main.py --token "<opponent agent token UUID here>" --play "de2c20f1-c6b9-4536-8cb0-c5c5ac816634"
```


_Name Your Agent_

Think of a fierce name for your agent and specify it with the `--rename` flag:

```bash
> python main.py --rename "<fierce name here>" --global 
```

Don't forget `--global` flag - you want the whole world to thrill before your strenght, right?
After this command the updated name will then appear in the leaderboard once you start playing online games.

_Build and Train Image Recognition Model_

For easy image recognition model testing `main.py` provides two extra arguments for building and training your image recogntiion model. 

Use `--build-model` flag to build image recognition model and exit:
```
> python main.py --build-model
```

Use `--train-model 'n_validation'` command to train image recognition model with the specified `n_validation` and exit:
```
> python main.py --train-model 100
```

Note: in order for this commands to work properly, first, you need to implement `build_model()` and `train_model()` functions from the `model.py` file.

_Full List of Available Options_

For a full list of available options/arguments, use

```bash
python main.py --help
```

## Assignment

You'll need to implement an agent strategy and a card image classifier that recognizes cards dealt as images. The project will be graded on four aspects: _Code_, _Tests_, _AI Engineering_ and _Team Collaboration_. In the first place we care about clean, correct, well-tested and well-motivated code; the performance of your agent is secondary.

Details on the grading criteria can be found in the Rubric that is available on Canvas, together with a list of critical questions that verify whether your group is on the right track.


_Assignment Details_

The current mockup agent plays a random game, and does not yet recognize dealt cards. Your assignment is to equip the poker agent with two main features:

1. A card image classifier - the `on_image()` method;
2. A betting strategy - the `make_action()` method.

For this, you'll need to implement:

- Data set handling (`data_sets.py`);
- An image classifier (`model.py`);
- An betting strategy (`agent.py`);
- Tests for your data set handling, classifier, agent and custom functionality (`test\`);
- Tests for the game and round states (`test\test_client_game_round_state.py`, `test\test_client_game_state.py`).
- A comprehensive and self-contained documentation that includes
  - Explanation of your image recognition model and playing strategy
  - How to build and train your model
  - How to run and play games with your bot


Some guidance is provided, but you'll need to be creative and implement any additional classes/functionality yourself. You can choose your own machine learning toolbox (we suggest TensorFlow with Keras) and are free to modify/create files as you see fit. Make sure to motivate and document your process and implementation.

While it is not forbidden to inspect server communication code, we highly recommend that you don't modify `main.py`, `client\events.py` and `client\controller.py` in order to prevent connection errors. When playing with the online server, a stable internet connection is required (you lose immediately if the connection is severed).
