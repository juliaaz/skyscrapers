Skyscrapers

Skyscrapers is a program for a logic game in the placement of houses.
In this game you need to place houses of different heights on the game board so that the number of visible houses from a certain position (the number with the arrow is a hint) was equal to the number in the hint. The arrow in the tooltip indicates the direction in which you want to look.
This program works with the game board which is a square N x N, with hints on the sides.
This program will allow you to check whether there is a winning combination on the board.
--------------------------------------------------------------------------------------------------------------------------------------

Functions of the program

Module includes 7 different functions: 
1. read_input |Function reads game board file from path.
Return list of str.|

2. left_to_right_check |Function checks row-wise visibility from left to right.
Returns True if number of building from the left-most hint is visible looking to the right,
False otherwise.|

3. check_not_finished_board |Function checks if skyscraper board is not finished,
'?' present on the game board.
Returns True if finished, False otherwise.|

4. check_uniqueness_in_rows |Function checks buildings of unique height in each row.
Returns True if buildings in a row have unique length, False otherwise.|

5. check_horizontal_visibility |Function checks row-wise visibility (left-right and vice versa)|

6. check_columns |Function checks column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).| 

7. check_skyscrapers |Main function to check the status of skyscraper game board.
Return True if the board status is compliant with the rules,
False otherwise.|

The last one is a main one and returns a Boolean value depending on compliance with the rules of previous functions. The others are for working with given data.