# Project informations
Name: U$/R$ Update <br />
Start date: 01/25/2022 <br />
Version: 001 <br />
Author's name: Rodrigo Wanderley <br />
E-mail: <boaventurarodrigo@yahoo.com.br> <br />
Git hub profile: <https://github.com/Rodrigowb> <br />
Linkedin profile: <https://www.linkedin.com/in/rodrigowanderleyboaventura> <br />
# About the project
This project aims to send me updates twice a day in a personal Telegram group informing the current quotation of the currency pair US Dolar/Brazilian Real. It solves a personal problem that I had, look everytime in financial websites to know the pair price and take decisions for when to buy US Dolar. Now I receive notifications in my phone and don't need to worry about. <br />
The project runs twice a day in the AWS EC2 remote service. Furthermore, I choose to config a cronjob task, as it is a high latency project that does not demand asyncronous execution, demanding less server capability.
# Files description
## mando_bot.py
Provides the resources to get the current USD/BRL using the Yahoo Finance API and check if the current date is a holiday or not in Brazil. If everything goes well with the request, It sends a message with the current quotation to the Telegram group. Otherwise, It sends me an alert message.
## main.py
Runs the execution of the mando_bot.py.
# Technologies used
1. Command Line
2. Git
3. Anaconda
4. Python
5. Yahoo Finance API
6. Telegram API
7. AWS EC2
