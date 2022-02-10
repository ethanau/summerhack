# IELTS Frequency Words Study Engine
## Description
This program is an IELTS Frequency Words Study Engine that runs on a personal computer and is designed for people preparing for the IELTS exam, but can also be used to prepare for other language exams by customizing the vocabulary database. IELTS and other language exams have been a necessary process for students and some working professionals during their school career, and vocabulary is the foundation. This IELTS Frequency Words Study Engine solves the problem of inefficient memorization and the inability to customize vocabulary databases by studying for 15 minutes at a time and separating mastered and unmastered vocabulary for efficient memorization, and allowing the user to customize the vocabulary database.<br>

## Installation
- **python** <br>
If you are on mac, it includes python, no additional python installation required. 
If you are on windows, you can download and install python through this [link](https://www.python.org/downloads/).<br><br>
- **pandas & requests**<br>
In addition to python, you need to install the pandas and requests libraries.<br>
$ pip install pandas<br>
$ pip install requests

## User Guide
After installation, run **$ python main.py** <br>
The UI of the project is as below.<br>
<img src="/images/UI.png" width="600"><br>
<img src="/images/UI2.png" width="600"><br>
- Click **start** button to start studying <br>
- Click **thumb** button if you have mastered the word, then this word will not appear again until you reset <br>
- Click **cross** button if you are not familiar with the word, than this word will appear again later for your review <br>
- Click **save** button if you are ready to finish the study and the software will save your mastered words and unmastered words to the database, so you can continue learning by process next time <br>
- Click **reset** button if you want to start over with the entire word database, or if you have updated the word database <br>
- If you want to customize the word database, just put your words in 'ielts_words_list.csv' file, and make sure one word occupies one line, than run **$ python word_Interpreter.py** to translate words to form the final word database <br>
## Futher prospects
Due to the short development time, this project is currently only running on personal computers and the program functions are simple, later more functions will be added according to user needs. Moreover, a web application will also be developed based on user demand and deployed on the cloud platform, and also a mobile application.

## Technical challenges
**User interface design** <br>
As an it engineer I do better on back-end development and lack of front-end design experience, so it is challenging for me to design a UI that satisfies the users, I browsed a lot of UI interfaces of other projects during the development process, and let many of my friends put forward a lot of valuable opinions when designing the first draft of UI.

**Word translation API** <br>
This project supports custom word database, but the translation of words requires a suitable and free API, so a lot of time was spent on finding the appropriate API.
