# How to play the Game

After git clone, run  `data_sets.py` to generate dataset; 
Run  `model.py` to train the image classification model;
In order to play an online game you can use 
```bash
python main.py  --global --play "bot" 
```

# Data handling
## Dataset specification

| Input data specification |                   |
|----------------|-----------------------------|
| Labels         | `J`, `Q`, `K`              |
| Image size     |32 x 32 pixels                |
| Rotation angle |0 to 15 degrees              |
| Noise level    |0 to 1 with 0.1 stepsize     |

## Implementation
### Feature extraction
The extracted feature shape is (32*32) which meets the input requirement of the model. The feature values are divided by 255 to normalize the values in the range [0,1].
### Data set generation
The generated data set contains an amount of images, each image has one out of four difference letters from `J`, `Q`, `K`. Each image is ramdomly rotated by 0 to 15 degrees with noise level 0 to 1. The name of image is organized as `label_i.png`, where the 'lable' demonstrates the letter showned in the image and the 'i' represents the generated order of the image.
### Data set load and separation
 - Load the generated data set.
 - Extract features and labels from each image in the data set.
 - Separate the data set into training and validation sets with extracted features and labels.

## DVC
DVC is a tool that helps to version control generated data sets and trained models. It is also very convenient to share the data sets and trained model with team members. Furthermore DVC was chosen because it's easy to setup, has a familiar git-like interface and is free and open-source with great community support. 

For our implementation we have opted to use DVC in combination with SSH remote storage.


## Data versioning
Model and dataset versions can be tracked with DVC. To track the data version, the data is first stored in on the local machine. Then the following commands are used to store the data on the remote storage:

```bash
dvc add dataset  # track dataset version in DVC
git add dataset.dvc # track DVC dataset file in git
git commit -m "Add dataset version 1"
dvc push
```
Now the train/test datasets can be pulled by any team member using the following DVC command:

```bash
dvc pull --remote ssh-storage data_sets\
```

## Generated data set overview
The following table lists the generated data sets.

| Generated dataset |    Nr. of images   |
|----------------|-----------------------------|
| Training set                | 10000 (80/20 train/val split)          |
| Test set                    | 2000                                   |
| Unit test test set          | 4                                      |
| Unit test training set      | 4                                      |


# Model
## How to build, train and evaluate a model?
A model is built by using the `build_model()` in the `model.py` file.  When we have a model, we can train it using the `train_model()` function. We have to give the model we want to train, indicate the amount of validation data and note if we want to save the trained model into a file. After training the model can be evaluated using the `evaluate_model()` function, this return the accuracy on the test set, which contains 2000 images. To simplify training and testing a seperate file `train.py` is created. In this file the model is build, trained and tested. To run it simply use:

```bash
python train.py
```

This will build a model trained with 2000 validation images and the trained model won't be saved, however this function has optional arguments to change if the model should be saved and the amount of validation images:

```bash
usage: train.py [-h] [-v N_VAL] [-s SAVE_MODEL]

Train and evaluate model

optional arguments:
  -h, --help     show this help message and exit
  -v N_VAL       number of validation samples
  -s SAVE_MODEL  decide if model should be saved or not
```

## Our model structure
The model used to classify the card images is a simple Convolutional Neural Network (CNN) called PasaNet. It consist of 3 convolutional layers followed by a ReLU activation layer, a batch normalization layer and a pooling layer. A fully connected layer followed by a ReLU activation layer completes the model. The model is built using the Tensorflow framework. The model only takes a few milliseconds to identify an image, well within the latency requirement. Below, a summary of the model is given.


```bash
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
      flatten (Flatten)           (None, 1024)              0

      dense (Dense)               (None, 128)               131200

      dense_1 (Dense)             (None, 3)                 387
================================================================
Total params: 131,587
Trainable params: 131,587
Non-trainable params: 0
----------------------------------------------------------------
Evaluate on test data
16/16 [] - 0s 2ms/step - loss: 0.1231 - accuracy: 0.9700
test acc: 0.9700000286102295
----------------------------------------------------------------
```


## Final model
Using *Weights & Biases* several combinations of learning rates, batch sizes, amount of epochs and optimizers are evaluated. The model achieves a 97% accuracy on the test set, the model is only not able to identify extremey noise images like the image shown below. 

![training acc](https://github.com/tue-5ARA0-2022-Q1/pokerbot-team-9/blob/main/training_acc.png)
![training loss](https://github.com/tue-5ARA0-2022-Q1/pokerbot-team-9/blob/main/training_loss.png)

In the end the following data and hyperparamets are used for the final model:

### Hyperparametes
- Number of epochs: 10
- Learning rate: 0.0001
- Optimizer: Adam
- Batch size: 50
- Loss: Cross-Entropy

### Results
- Accuracy on test set: 97%

# Strategy
## Kuhn Poker
Kuhn poker is an extremely simplified form of poker developed by Harold W. Kuhn as a simple model zero-sum two-player imperfect-information game, amenable to a complete game-theoretic analysis. In Kuhn poker, the deck includes only three playing cards``[J, Q, K]`` and the actions  ``[Fold, Call, Bet, Check]`` . One card is dealt to each player, which may place bets similarly to a standard poker. If both players bet or both players pass, the player with the higher card wins, otherwise, the betting player wins.

## Game Description
In conventional poker terms, a game of Kuhn poker proceeds as follows:

Each player antes 1.
Each player is dealt one of the three cards, and the third is put aside unseen.
Player one can check or bet 1.
  If player one checks then player two can check or bet 1.
    If player two checks there is a showdown for the pot of 2 (i.e. the higher card wins 1 from the other player).
    If player two bets then player one can fold or call.
      If player one folds then player two takes the pot of 3 (i.e. winning 1 from player 1).
      If player one calls there is a showdown for the pot of 4 (i.e. the higher card wins 2 from the other player).
  If player one bets then player two can fold or call.
    If player two folds then player one takes the pot of 3 (i.e. winning 1 from player 2).
    If player two calls there is a showdown for the pot of 4 (i.e. the higher card wins 2 from the other player).
This can be checked from below picture.
![poker tree](https://github.com/tue-5ARA0-2022-Q1/pokerbot-team-9/blob/agent-test/Kuhnpoker-tree.png)


## Optimal strategy
The game has a mixed-strategy Nash equilibrium; when both players play equilibrium strategies, the first player should expect to lose at a rate of −1/18 per hand (as the game is zero-sum, the second player should expect to win at a rate of +1/18). There is no pure-strategy equilibrium.

Kuhn demonstrated there are infinitely many equilibrium strategies for the first player, forming a continuum governed by a single parameter. In one possible formulation, player one freely chooses the probability {\displaystyle \alpha \in [0,1/3]}{\displaystyle \alpha \in [0,1/3]} with which he will bet when having a Jack (otherwise he checks; if the other player bets, he should always fold). When having a King, he should bet with the probability of {\displaystyle 3\alpha }3\alpha  (otherwise he checks; if the other player bets, he should always call). He should always check when having a Queen, and if the other player bets after this check, he should call with the probability of {\displaystyle \alpha +1/3}{\displaystyle \alpha +1/3}.

The second player has a single equilibrium strategy: Always betting or calling when having a King; when having a Queen, checking if possible, otherwise calling with the probability of 1/3; when having a Jack, never calling and betting with the probability of 1/3.

## Nash equilibrium

### Definition
A strategy is said to be dominant if one of the parties in a game chooses some definite strategy regardless of the strategy choices of the other party. A combination is defined as a Nash equilibrium if the strategy chosen by any one participant is optimal given that the strategies of all other participants are determined.

### Classification
Nash equilibrium can be divided into two categories: "pure-strategy Nash equilibrium" and "mixed-strategy Nash equilibrium".
To explain pure strategy Nash equilibrium and mixed strategy Nash equilibrium, it is necessary to first explain pure strategies and mixed strategies.

A pure strategy is a complete definition of how a player wants to play a game. In particular, pure strategies determine the moves to be made in any given situation. A strategy set is a collection of pure strategies that a player can play. A mixed strategy is a strategy that is formed by assigning a probability to each pure strategy. A mixed strategy allows a player to choose a pure strategy at random. Probability calculations are used in the mixed strategy game equilibrium because each strategy is random and achieves a certain probability when the optimal payoff is achieved. Because the probabilities are continuous, there are infinitely many mixed strategies, even if the set of strategies is finite.

Of course, strictly speaking, each pure strategy is a "degenerate" mixed strategy, where the probability of a particular pure strategy is 1 and the others are 0.

Therefore, a "pure strategy Nash equilibrium" is one in which all players involved use pure strategies, and a corresponding "mixed strategy Nash equilibrium" is one in which at least one player uses a mixed strategy. Not every game has a pure-strategy Nash equilibrium; for example, the "money problem" has only a mixed-strategy Nash equilibrium, but not a pure-strategy Nash equilibrium. However, there are many games that have pure strategy Nash equilibrium (e.g., coordination games, prisoner's dilemma, and deer hunting games). There are even games that have both pure and mixed strategy equilibrium.


### Nash's Existence Theorem
Nash proved that if mixed strategies (where a player chooses probabilities of using various pure strategies) are allowed, then every game with a finite number of players in which each player can choose from finitely many pure strategies has at least one Nash equilibrium, which might be a pure strategy for each player or might be a probability distribution over strategies for each player.

Nash equilibria need not exist if the set of choices is infinite and non-compact. An example is a game where two players simultaneously name a number and the player naming the larger number wins. Another example is where each of two players chooses a real number strictly less than 5 and the winner is whoever has the biggest number; no biggest number strictly less than 5 exists (if the number could equal 5, the Nash equilibrium would have both players choosing 5 and tying the game). However, a Nash equilibrium exists if the set of choices is compact with each player's payoff continuous in the strategies of all the players.


## Evaluation & Improvements

### The number of cards
The implemented strategy supports 3-card game as the dictionary is generated based on ["J","Q","K"], i.e. we can always find any of these four cards in the resulting dictionary no matter how many cards are dealt in the actual game. However, it is beliveved that will perform better in 4-card cases than 3-card, because the utility is calculated based on the relationship between four cards, resulting in an inaccurate estimation for 3-card games sometimes.

### The number of players
If the rules of actions in a round are not changed, the strategy dictionary is robust for running the poker game against any number of players, because the information set of any player only includes the card in hand and the action history in a round, which is always a valid key in the dictionary, but the utility will be inappropriate except for the game with two players. The reason is that the generated Kuhn game tree only considers all the comparisons between two cards and the alternation between two players in a round and that the utility of each action is calculated based on the tree.

### Algorithm Improvement: Counterfactual Regret Minimization(CFR)
We can also use Counterfactual Regret Minimization Algorithm, which is a classical algorithm for solving decisions in information asymmetry games. It is based on regret, or regrets. The algorithm first makes a decision, and then judges the effect of the decision in the game based on the outcome of the game to determine whether it should have been done. It is regret for what was done and regret for what was not done.

CFR is based on depth-first search. When training, it recursively traverses each decision for the information obtained until the end of the game, and regrets each step of the decision based on the game result when it returns. The regret is corresponded to the information one by one.2 When making a decision, the decision is made based on this.

The decision is made based on the information only at the time of decision making, independent of the previous decision history. This can be achieved by adding the decision history to the information in order to make a decision by referring to the decision history at decision time.
