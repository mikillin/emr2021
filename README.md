# EMR2021 - Speech Recognition
Mitglieder:
- Marcel Heinen
- Sergey Rogachevsky
- Yosua Kurniawan

**Packages & Library:**

Speech Recognition:
- $ pip install SpeechRecognition

PyAudio:

**FOR WINDOWS USER NEED TO ADD:**
- $ pip install pipwin
- $ pipwin install pyaudio

**FOR UBUNTU USER NEED TO ADD:**
- $ sudo apt-get install portaudio19-dev python3-pyaudio
- $ pip install PyAudio

rospy:

- $ sudo apt install python-rospy

pyaudio:

- $ sudo apt install python3-pyaudio+

pocketsphinx:
- $ sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
- $ sudo apt-get install swig3.0 **or** $ sudo apt-get install swig (only god knows)

- $ sudo pip install pocketsphinx

**Changelog**

8.8.2021
- add virtual enviroment for visual studio user
- add basic test code for mic input

9.8.2021
- source code for ibm watson voice recognition
- update test-code

10.8.2021
- add se_turtle.py & se_turtle_thread.py

13.8.2021
- add our first turtlesim demo

14.8.2021
- fixed known bug se_turtle_demo1.py : phrasing_audio_distance()
- add se_youbot-gazebo_demo1.py (WIP)

15.8.2021
- fixed typo
- add se_youbot-gazebo_demo2.py

18.8.2021
- add se_youbot-real.py (WIP)
- thread (WIP)

26.8.2021
- add separate node for speech recognition and drive
