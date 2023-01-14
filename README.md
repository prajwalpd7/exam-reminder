# exam-reminder

Exam Reminder

This is a simple script that uses Python and the Twilio library to send WhatsApp messages reminding the number of days remaining for an exam.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
A Twilio account. You can sign up for a free trial at twilio.com
Python 3.6 or later
A WhatsApp account

Installing
1. Clone the repository to your local machine
2. Install the required libraries by running-

$pip install twilio

$pip install emoji


3. Replace the event_date variable with the date of your exam.

4. Replace the from_ and to variables with your Twilio number and the number you want to send the message to.

5. Run the script with the following command:

python examAlert.py.py


important part - 
Automating the script
You can use a task scheduler such as cron on Linux or Task Scheduler on Windows to schedule the script to run at specific intervals. Alternatively, you can use a cloud-based scheduling service like AWS Lambda or Google Cloud Functions to run the script on a schedule without setting up a task scheduler on your local machine.

Built With
`Twilio - The API used for WhatsApp messaging
`Python - The programming language used

Author
Your Name - https://github.com/prajwalpd7

Acknowledgments-
!I would like to acknowledge the Twilio documentation and community for providing the resources and guidance to interact with the WhatsApp API.
!I would also like to acknowledge the Python community and the developers of the libraries used in this project (Twilio, datetime) for their contributions to open-source software.

