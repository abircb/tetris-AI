# 2D Tetris game and an auto-player
A reenvisioned version of Alexey Pajitnov's orignal Tetris game with a built-in autoplayer. 
Tetris has been released for virtually every computer and electronic gaming system, and it is often revered as a classic. Though numerous sequels have been spawned, Tetris games almost always have the same play mechanics: differently shaped blocks drop at varying speeds, and, as the blocks descend, the player must rotate and arrange them to create an uninterrupted horizontal row on the screen. When the player forms one or more solid rows, the completed rows disappear. The goal of the game is to prevent the blocks from stacking up to the top of the screen for as long as possible. This version of the game essentially uses the same mechanics, but comes with an auto-player that has, on average, a score of 5,000,000.

Essentially, the auto-player uses parameters- such as, height of the grid (the distance from the highest tile in each column to the bottom of the grid), complete lines (the number of complete lines in a grid), number of holes in the grid, etc.- to calculate a score for each possible position of a falling Tetris block. Naturally, each paramter is assigned a different weight, which is calculated using experience playing Tetris, researching different human-player strategies, and hit-and-trial.

## Usage ##
<br />First, install all required dependancies. All dependancies are included in requirements.txt (created using pipreqs) Next, run the game by running tetris.py
<br />To DISABLE the autoplayer, go to te_settings.py and set the boolean variable DEFAULT_AUTOPLAY to False
<br />Controls:
<br />a- Move Left
<br />s- Move Right
<br />k- Rotate Left
<br />l- Rotate Right
<br />space- Hard drop
<br /><strong>Compatibility: python version 3.7.0 or later</strong>
