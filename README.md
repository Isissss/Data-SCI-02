# Data science for IOT 
Data Science IOT - Keuzevak HR periode 2, 2022

### The idea 
Originally, I wanted to make a diary bot that takes pictures and logs your emotions while you are telling the bot a story about your day to get more insight on your mental health. After doing some research online, I sadly came to the conclusion that this was too complicated with my level of experience and the time we were given for this project. Although I have some IoT experience, I am relatively new to coding and had no experience with the language and device provided to us.

I was inspired by my 11-year-old sister, or actually by her assignment about the air / masks at school during covid. A healthy environment is a must while you are at work or school (or just at home). Not just because of covid, but it's important at any time. The room temperature and humidity play a part in that. A high humidity percentage stimulates the growth of micro-organisms. Tihs can lead to various problems that all negatively affect your overall workflow. Some issues will occur overtime, but concenstration issues can occur right away which is why it's important to pay attention to the humidity.

### Goal of the project
I have set some personal goals for this project, and ofcourse the end-goal of this project.

#### Project
I want to show the status of the humidity and temperature through a simple device so that simple things, such as opening a window, are done before the issues listed earlier occur, but also to spot long-term trends. The information should be tracked and saved. It should then be used on an external website, which provides the last status, a daily, weekly and a monthly report of the avarage temperature and humidity. That way you can spot trends (let's say the humidity is much higer on a certain day, you can increase the ventilation beforehand) but also assure people that the humidity and temperature is healthy to work in. Moreover, the reports could also show a relation between the temperature and the humidity, and show what temperatures are the best to work in to make sure the humidity is good. 

The things I will be using to create this Internet of Things project are:
- Raspberry Pi 3 B+ device
- 4 different LEDs to indicate the status of the humidity level 
- A DHT11 sensor (to measure the humidity and temperature) 

The collected data is the humidity level, the temperature in Celcius (through the DHT11), temperature in Fahrenheid (based on the temperature in C from the DHT11) and the status the status (1 = good 2 = indication of it getting worse 3 = bad)

The data is then sent to ThingSpeak, which saves it so it can be used by the web application through the API for the reports and to show the correlation between the room temperature and humidity.

#### Personal
Prior experiences 
- When I just started my studies (CMGT) I made an IoT device, so I have some knowledge of IoT which I've used in this project. I made a 'vergeet-me-niet' medicine reminder bot for eldery. It was coded in a simplified coding application called 'MakeCode' which uses Javascript as programming language. 
- In the second period of this year, we had to build our own reservation system. I learnt how to make post and get requests, which I could use in this project as well to update the channels and to retrieve information from TeamSpeak.  

I hope to expand my knowledge and get comfortable with the basics of Python so I can start bigger projects like a Discord bot that can help me pick and send predefined replies at my work, as well as counting the amount of tickets I do per day and hour. I work at a Minecraft server's customer service and tickets are done through Discord. Ofcourse a healthy work environment is also important for myself, so I hope to benefit from this device as well. 

## The Project

###Pipeline
I have made a data pipeline for this project. 
<img src="pipeline.jpg"/>


### Sources
During this project I've used several website and sources to create my code. I have gathered information from:
- <a href="https://docs.python-requests.org/en/master/user/quickstart/">Requests Python docs</a>
- <a href="https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/">DHT11 Temperature and Humidity Sensor and the Raspberry Pi</a>
- <a href="https://nl.mathworks.com/help/thingspeak/writedata.html;jsessionid=57ca7fb5ff69ea6dab8a95847248">Mathworks ThingSpeak writedata documentation</a>
- <a href="https://nl.mathworks.com/help/thingspeak/readdata.html;jsessionid=57ca8759e47f248719045080ec55">Mathworks ThingSpeak readdata documentation</a> 
- <a href="https://roboticsbackend.com/raspberry-pi-control-led-python-3/">Control an LED with Raspberry Pi 4 and Python 3</a> 
