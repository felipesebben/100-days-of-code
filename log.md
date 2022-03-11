# 100 Days Of Code - Log

### Day 1: March 2, 2022 

**Today's Progress**: Built a simple band name generator program on Python. The user is asked to provide the name of the city in which he or she grew up and the name of his or her pet. The program will store these values and provide a suggestion based on these two inputs.

**Thoughts:** It was nice to review the basics of strings, variables, and logic. These are essential if I want to incorporate a real programming mindset. Logic is still an odd field to me. At the end, though, I managed to build the program in a few minutes with no need to resort to any external support.

**Link to Work:** [Band Name Generator](https://github.com/felipesebben/100-days-of-code/blob/master/001_band_name_generator/band_name_generator.py)
* * *
### Day 2: March 3, 2022

**Today's Progress**: Built a simple yet challenging tip generator. The user provides three inputs: the total value of the bill, the tip percentage the user would like to give, and the number of people. The program will then provide the amount each person should pay, including the tip. 
    
I also added a hover feature to a data visualization with plotly concerning recurring earthquakes during 30 days. 

**Thoughts:** It was really challenging to do the tip calculator, as you are asked to think in programming ways. But it was satisfying to see it running and calculating tips left and right!

**Link to Work:** 
- [Tip Calculator](https://github.com/felipesebben/100-days-of-code/blob/master/002_tip_calculator/tip_calculator.py)
- [Earthquake Mapping](https://github.com/felipesebben/py_crash_course_exercises/blob/master/project_2-data_visualization/16_downloading_data/eq_world_map.py)
* * *
### Day 3: March 4, 2022

**Today's Progress**: Built a fun yet challenging tresure hunt game which tested my skills with conditional elements. Basically, the user is asked to make choices along a storyline. Each question leads you to another question or the game is over in case you make the wrong choice. 

**Thoughts**: It was nice to challenge myself by applying logical skills to create the game. It might seem like a simple project, yet you need to plan well ahead your conditionals if you want it to work properly!

**Link to Work**:
- [Treasure Hunt Game](https://github.com/felipesebben/100-days-of-code/blob/master/003_treasure_hunt/treasure_island.py)
* * *
### Day 4: March 5, 2022

**Today's Progress**: Built a series of programs aiming at understanding lists, random numbers and conditionalities. Apart from a treasure map and a coin toss game, built a rock paper scissors game, in which the user plays it with the computer. The user provides a number between 0 and 2, which is stored as either as rock, scissor, or paper. The computer generates a random number between this same range, which must be then stored as the computer's choice between the three possible choices. Then, the two choices are compared, and using conditional elements, the outcome is provided either as a loss, a win or a draw. 

**Thoughts**: It was really nice to build this game. I felt that I was getting the logic of Python while I was building it, and as the days go on, it seems that you get more into this rationale! 

**Link to Work**:
- [Rock, Paper, or Scissors](https://github.com/felipesebben/100-days-of-code/blob/master/004_rock_paper_scissors/rock_paper_scissors.py)
* * *
### Day 5: March 6, 2022

**Today's Progress**: Built a password generator using for loop features. The user is asked to provide a given number of symbols, letters, and numbers, with which the program is supposed to provide a unique password. The program then stores the range of choices in three different variables, which will be used to provide a random group of characters using the `choice()` function in the module `random`. Then, given all the user's choices, the program must shuffle the three groups of characters to provide a harder password.

**Thoughts**: I really like these iteration exercises. They are quite logical and you can use these tools in many ways. One can easily think about using `for` loops as a way to automate similar calculations. The exercises were also very interesting, and worked very well as a complementary way to reinforce learning.

**Link to Work**:
- [Password Generator](https://github.com/felipesebben/100-days-of-code/blob/master/005_password_generator/password_generator.py)
* * *
### Day 6: March 7, 2022

**Today's Progress**: Solved an escape the maze challenge, in which I was asked to provide an exit strategy for  a robot. Basically, through functions, `while` loops and conditionalities, you needed to guide the robot's oves according to eventual walls and clear paths. 

**Thoughts**: It was a really nice way to learn more about `while` loops. You can see their usefulness when you need to loop through a bunch of commands without a pre-determined list or range of numbers, for instance. 

**Link to Work**:
- [Maze Challenge](https://github.com/felipesebben/100-days-of-code/blob/master/006_escaping_the_maze/escape_the_maze.py)
    - PS: the inbuilt functions are not avaliable. You can find the challenge [here](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).
* * *
### Day 7: March 8, 2022
**Today's Progress**: I've managed to build a hangman game in python! It was a 5-step process, in which I had to plan a workflow to be able to implement it. 
- I also advanced on my Tableau course, though I find myself stuck in a particular calculation regarding conditionalities.
- I have also done some SQL queries on a videogames dataset. I have so far managed to learn more about number of releases per year according to each console. I am trying to get unique releases for each console, but it is not as easy as I thought!

**Thoughts**: Seven days have passed by so fast! I must say it is challenging to keep up with the volume of work. But I'm confident that this hardwork will benefit me in the long run. I must sleep more, though.

**Link to Work**:
- [Hangman Game](https://github.com/felipesebben/100-days-of-code/blob/master/007_hangman/hangman_final.py)
- [SQL Videogame Queries](https://github.com/felipesebben/DA_videogames/blob/master/3_SQL_DEA.sql)
* * *
### Day 8: March 9, 2022
**Today's Progress**: So far, I've built a caesar cipher. Basically, the user chooses whether he/she wants to encode or decode a given word or sentence that must be provided as an input. Then, a number of shifts in the alphabet must be also given, i.e. if shift equals 2, the encoded message will be provided with an alphabet that is moved two characters write, which means that a would be encrypted as c. The user can encode the message and, if he wants, he can also decode it: he/she must only provide the encrypted message and the number of shifts used in the original encoding.

**Thoughts**: That was a challenging task. It feels sometimes that I will eventually get stuck in one of these projects. I feel compelled to move forward no matter what, a feeling that may not lead to positive outcomes everytime. Well, at, least we are reaching 10% of the course and I can tell that the learning curve is still not that steep! 

**Link to Work**:
[Caesar Cipher](https://github.com/felipesebben/100-days-of-code/blob/master/008_caesar_cipher/caesar_cipher.py)
* * *
### Day 9: March 10, 2022
**Today's Progress**:
- Built a silent auction program in python, in which the user could store as many bids made per individual. The project emphasized the use of dictionaries to store the user's input. After all bidders and their respective bids were stored, the program prints the name of the winner, together with his or her bid, which was the highest among the group.
- Also built a series of visualizations based on data obtained from GitHub's API. I've learned how to access API's, store values into empty lists, and then plot a bar chart using plotly.
- I have also using PgAdmin on a daily basis to explore a dataset on games and their respective scores. My idea is to see which consoles have had better scores. I intend to join this table with another with game ratings such as whether or not the game displays nudity and violence scenes etc. 
- I studied Tableau calculations, including field calculations, table calculations, and quick calculations.
- I also move forward with my 2018 Brazil election dataviz project in Tableau.

**Thoughts**: Man, what a day! Lots of things covered. I liked building this silent auction program, as you must deal with pretty interesting python features. The rest was cool too, it was fun playing around plotly's methods, which are endless by the way! I just wish that I could build some nice visualizations faster.

**Link to Work**: 
- [Silent Auction](https://github.com/felipesebben/100-days-of-code/blob/master/009_silent_auction/blind_auction.py)
* * *
### Day 10: March 11, 2022
**Today's Progress"":
- Built a calculator in python. The user is asked to provide a number, the type of operation he or she wants (add, subtract, multiply, or divide), and another number. The program will print the result of the operation, asking whether the user wants to do other operations on the answer. If so, the user can provide another number and operation. If not, the program restarts, asking the user to provide new numbers for a new calculation.

**Thoughts**:
- It was interesting to work with functions while building this program. You can do many things with less lines of code, which makes your coding more elegant and efficient. 

**Link to Work**:
- [Calculator](https://github.com/felipesebben/100-days-of-code/blob/master/010_calculator/calculator.py)
 
