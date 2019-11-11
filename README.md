# 2D Tetris game and an auto-player
A reenvisioned version of Alexey Pajitnov's orignal Tetris game with a built-in autoplayer. 
Tetris has been released for virtually every computer and electronic gaming system, and it is often revered as a classic. Though numerous sequels have been spawned, Tetris games almost always have the same play mechanics: differently shaped blocks drop at varying speeds, and, as the blocks descend, the player must rotate and arrange them to create an uninterrupted horizontal row on the screen. When the player forms one or more solid rows, the completed rows disappear. The goal of the game is to prevent the blocks from stacking up to the top of the screen for as long as possible. This version of the game essentially uses the same mechanics, but comes with an auto-player that has, on average, a score of 2,000,000.

![demo](/demo.gif)

The auto-player algorithm is a very simple genetic algorithm. It does the following:
<ol>
  <li>Look at the current block and the next block and simulate ALL possible combinations (positions and rotations) of the two blocks.</li>
  <li>Calculate a score for each of the positions.</li>
  <li>Move the block to the position with the highest score and repeat.</li>
</ol>

To calculate the score, the auto-player uses parameters such as, height of the grid (the distance from the highest tile in each column to the bottom of the grid), complete lines (the number of complete lines in a grid), number of holes in the grid, etc. Naturally, each paramter is assigned a different weight, which is calculated using experience playing Tetris, researching different human-player strategies, and hit-and-trial.

## Setup ##
All of the code was only tested using Python 3.7.0 so I'd recommend using it as well. Before starting, setup a virtual environment and within that environment, install the dependencies. All dependancies are included in requirements.txt (created using pipreqs) <br />
```
pip install requirements.txt
```

## Usage ##
Run the game by running tetris.py
```
python tetris.py
```
<br />To DISABLE the autoplayer, go to `te_settings.py`and set the boolean variable `DEFAULT_AUTOPLAY` to `false`
<br />Controls:
<br />`a`- Move Left
<br />`s`- Move Right
<br />`k`- Rotate Left
<br />`l`- Rotate Right
<br />`space`- Hard drop
<br /><strong>Compatibility: python version 3.7.0 or later</strong>
