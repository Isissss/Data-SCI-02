# Data science for IOT 
Data Science IOT - Keuzevak HR periode 2, 2022

## Idea 
Originally, I wanted to make a diary bot that takes pictures and log your emotions while you are telling the bot a story about your day to get more insight on your mental health. After doing some research online, I sadly came to the conclusion that this was too complicated with my level of experience and the time we were given for this project. Although I have some IoT experience, I am relatively new to coding and had no experience with the language and device provided to us.

I started thinking about what else I could do, and started thinking about school and work. A healthy environment is a must while you are at work or school (or just at home). Not just because of covid, but it's important at any time. The room temperature and humidity play a part in that. A high humidity percentage stimulates the growth of micro-organisms. This can lead to allergic reactions and problems such as tightness of the chest, headaches, coughing and a chronical nose cold, which all has a negative effect on your overall workflow. These are all issues that will only show up after some time, but concenstration issues can occur right away. 

##### Inspiation
I was inspired by my 11-year-old sister, or actually by her assignment about the air / masks at school during covid. 

## Goal of the project
I have set some personal goals for this project, and ofcourse the end-goal of this project.

#### Project
I want to show the status of the humidity and temperature through a simple device so that simple things, such as opening a window, are done before the issues listed earlier occur. The information should be tracked and saved. It should then be used on an external website, which provides the last status, a daily, weekly and a monthly report of the avarage temperature and humidity. That way you can spot trends (let's say the humidity is much higer on a certain day, you can increase the ventilation beforehand) but also assure people that the humidity and temperature is healthy to work in. Moreover, the reports could also show a relation between the temperature and the humidity, and show what temperatures are the best to work in. 

The things I will be using to create this Internet of Things application are a Raspberry Pi 3 B+ device, 4 different LEDs to indicate the status of the humidity level and a DHT11 sensor (humidity and temperature sensor). 

The collected data is the humidity level, the temperature in Celcius (through the DHT11), temperature in Fahrenheid (based on the temperature in C from the DHT11) and the status the status (1 = good 2 = indication of it getting worse 3 = bad)

The data is then sent to ThingSpeak, which saves it so it can be used by the web application through the API for the reports. 

#### Personal
##### Experience
When I just started my studies (CMGT) I made an IoT device, so I have some knowledge of IoT. I made a 'vergeet-me-niet' madicine reminder for eldery coded in a beginner's coding program called 'MakeCode' a simplified application that uses Javascript as programming language. 

In the second period of this year, we had to build our own reservation system. I learnt how to make post and get requests, which I could use in this project as well to update the channels and to retrieve information from TeamSpeak. 

I hope to expand my knowledge and get comfortable with Python and the hardware
