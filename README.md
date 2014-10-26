DeadlyDangerDungeon
===================

Python script to play the Deadly Danger Dungeon Board game from AVGN/Board James


### Game Information

Link to [Episode](http://www.cinemassacre.com/2010/03/26/board-james-deadly-danger-dungeon/)

Link to [Scanned Game Board](http://i157.photobucket.com/albums/t75/MikeMatei/Deadly_Danger_Dungeon_scann.jpg)

Link to [General Information/Rules](http://cinemassacre.com/2010/05/05/deadly-danger-dungeon/)


### Script Information

Only requirement is Python 2.7.x


Running the script will play the game once with one player, the script takes the most direct path to the end goal. A few assumptions regarding the rules have been made that could change the outcome of the game:


+ Reaching the end does not require landing on the last space, any movement past the last space is considered winning.
+ The potion remains availible at either spot and is not used up. The same player can benefit multiple times.


Running the script followed by a number will run the game that many number of times and tally the total.

### Conclusion

Ran the script through 1000000 games resulting in 999732 deaths and 268 wins (0.0268%). 
