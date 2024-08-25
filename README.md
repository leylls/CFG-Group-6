<img width="783" alt="Screenshot 2024-08-25 at 14 04 53" src="https://github.com/user-attachments/assets/0f11220d-6c08-4eae-b59f-3ff03676b868">



# TRACKMAZON
Our
app is a
price - tracking
app
for Amazon products, and offers users the ability to receive an email notification when a desired  product falls within their preferred price.



## Table of Contents

- Description
- Why TRACKMAZON
- Getting Started 
- Requirements 
- Project Files 
- Email API
- Helpful Tips 
- Acknowledgements 



## Description

TrackMazon is a price-tracking app for Amazon products that alerts users via email when a tracked product hits their desired price. Our project aims to create an application with a user-friendly interface, web scraping for product info, efficient data storage, and an email notification system for when the price drops.


 ## Why TRACKMAZON

Our goal was to create an app that would provide users with the best possible deals on Amazon products. We aimed to offer a convenient and user-friendly experience where users could track prices and receive email notifications when it was the optimal time to purchase their desired items. This feature was intended to help users save money by informing them of the best deals as soon as they became available, making the shopping experience more efficient and cost-effective.




## Getting Started
1. Clone the repository:
```bash
 git clone https://github.com/leylls/CFG-Group-6.git
```

2.  Install
dependencies/external libraries:
```bash
beautifulsoup4 == 4.12.3
certifi == 2024.7.4
charset-normalizer==3.3.2
idna == 3.8
mailjet-rest==1.3.4
requests == 2.32.3
soupsieve == 2.6
urllib3==2.2.2
time.sleep
os.path 
mailjet_rest 
sqlite3

```
3. Running on Mac: Run main.py and make sure to update the API keys in the file.
   Users using Mac will need to use "Manual Price-Drop Check" for task automation. 

5. Running on Windows: Run (.exe file) for task automation. (Note the following limitations: the path cannot contain whitespaces, the computer must be plugged in, and it needs to be turned on at the scheduled time.)


## Requirements
1. Application is developed in Python 3.12

2. You can install the packages using the requirements.txt file.
 
     
                       ```pip install -r requirements.txt  ```




## Project Files Description
Front End

* ft_end_ascii_prints.py - Functions for ASCII art and stylized text output to enhance interface. 
* ft_end_backend_interactions.py - Interactions between the front end and the back end. 
* ft_end_dialogues_choice_logic.py - Logic for handling user choices/ dialogue flows in interface.
* ft_end_input_utils.py - Provides utility functions for processing and validating user input in the terminal interface.

 Back End
* trackmazon_task.py - Track product prices and send email notifications for price drops. 
* db_interactions.py - Database operations, storing and retrieving product price data and user information.
* init_db.py - Initializes the database by creating tables and setting up the necessary schema and initial data.
* list_common_user_agents.txt - A file listing various user-agent strings to rotate during web scraping and avoid detection.
* Web_Scraping.py - Handles the extraction of product price information from websites using web scraping techniques.
* Email_Api.py - Provides functionality to send email notifications, using an external email API.





## Email API

MailJet API - Please register for an account to access the API.
```
https://dev.mailjet.com/email/guides/
```
## Helpful Tips

To stop using the app and remove the scheduled task on Windows 10, follow these instructions:

* Open Task Scheduler: Press Win + S, type "Task Scheduler," and press Enter.

* Locate the Task: In the Task Scheduler window, navigate to Task Scheduler Library in the left pane to find the scheduled task associated with the app.

* Delete the Task: Right-click the task you want to remove and select Delete from the context menu.

* Confirm Deletion: Confirm the deletion when prompted to ensure the task is removed.


You may get a warning from your computer when running the exe. file, please do not be alarmed! Continue and run the program anyway. 


## Authors

Shaira Jiwany, Ikram Ahmed, Leyla Bush, Violeta Pereda, Eva Perez Chirinos. 


## License
This project is open source.



## Project Status

This app is created as a final project for Summer 2024 Software Engineering CFG Degree.

The development of this project has stopped completely as we have submitted and presented this project.


## Acknowledgements 
Thank you CodeFirstGirls, our instructors and the data/software engineering team. 






