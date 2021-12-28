# Time_Tracking
An hardware time tracking project to record my daily activities and gather data on how I spend my time.
The goal is to use an hardware an limited device to gather that time in order to avoid phone based solutions that could be unproductive and uneficient.

In my case, I chose to use a raspberry pi zero W with a simple rotary encoder i also use as a button and an a tiny ic2 adafruit display.

### HOW IT WORKS ? 
When the device is powered, it will run the python *main.py* script. The script is an infinite loop. 
If the device hasn't been manipulated and clicked today, the program will enter **Question mode**, if 'Question mode' has been terminated today, it will skip to **Time mode**. 
  - **Question mode** : A few custom questions appear on the display and you get to anwser with the rotary encoder ( rotate to change the anwser option, click to select ), the questions and their anwsers can be changed in the main.py file. It will record the anwser for each questio in a csv file. You need to anwser those questions for the day before this one because as the day may just have started when you anwser, you can't know how it went.
  - **Time mode** : It is the main mode of the device, it waits for a rotation of the rotary encoder to quit the **Idle mode** ( see below ), and then, when rotaded, will ask the user to enter the activity he was doing before rotating. It is better to preceed like this :  
  *Do your activity* -> *End you activity* -> *Select that activity on the device to record it* -> *Do another actiity* -> ... and so on  
  To add or change the activities, you can change the *activities* list and the *Activity* object in the *main.py* file.


## TODO


- ### MAIN FEATURES
    - Add full support for question asking and anwsering from the device
    - Clean the code and the data sending part to avoid potential issues
    - Handle fonts and in particular font size to ensure all the text is displayed on the tiny screen
    - Order the categories and activities in a way that makes more sense

- ### OPTIONNAL FEATURES

    - Send data without interracting with the device -> require asynch code 
    - Multi line display and rolling menu with few options
    - Add a way to revert a button clic with a long press for exemple 
