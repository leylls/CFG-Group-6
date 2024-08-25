<img width="783" alt="Screenshot 2024-08-25 at 14 04 53" src="https://github.com/user-attachments/assets/0f11220d-6c08-4eae-b59f-3ff03676b868">


<br><br>
The modern world of e-commerce can be challenging for consumers to navigate. It can be volatile - and sometimes manipulative; with continuous misleading promotional offers. 🤑

We all know Amazon and how daunting it can get to get the best deal for your desired product. 

But not to worry, **TrackMazon wants to become your shopping ally**! 🦸‍♀️

In a nutshell, TrackMazon is a price-tracking app for Amazon products that offers users the ability to receive an email notification when a tracked product falls within their set desired price.


## Table of Contents

- How can TRACKMAZON help me with my shopping?
- So, how do I get this app?
  * Windows
  * Mac
- Getting Started
- How to stop TrackMazon's automated task
- Requirements
- Project Files Description


 ## How can TRACKMAZON help me with my shopping?
Imagine this, you're scrolling through Amazon to find your favourite pairs of sneakers and you see the best price is £200. You feel a bit unsure and you leave it for the day. You come back the next day to see they now cost £230. You get a bit upset and you leave it there. You realize perhaps £230 is not that much, so you come back to them just to find out they are on sale for £210. Exhausting, right? 😥

Our app will track these price changes for you and send you an email whenever the sneaker's price falls to an amount that feels right to **YOU**. 

## So, how do I get this app?
First things first, there is a difference if you are using either Windows or Mac, so please read carefully...

### Windows
For Windows users, we have created `TrackMazon.exe`, a plug-and-play program that you can find within `TrackMazon.zip`.

You may get a warning from your computer when running the `TrackMazon.exe` file, please do not be alarmed! Continue and run the program anyway. 

The first time you run this executable, the application will set up in your computer an automatic daily price-drop check.

❗ Please note: 
- You will need to delete this task manually if you ever want to stop using our app (see Section 'How to stop TrackMazon's automated task').
- The  file path where the executable is stored cannot contain whitespaces for the executable to work correctly.


### Mac
For Mac users, there's no plug-and-play executable available. You will need to run the program through the source code, see the next section for a step-by-step.

This app depends on MailJet API to operate email notifications. You will need to manually insert your own API key and API secret key in lines 86 and 87 on file cronjob/trackmazon_task.py. To get this, please follow the below link:
``` https://app.mailjet.com/signup?lang=en_US ```

❗ Please note, that users with Mac systems will need to do a "Manual Price-Drop Check" as automated price tracking has not yet been enabled. You will find this option within option [2] My Tracked Products.


## Getting Started
1. Clone the repository:
```bash
 git clone https://github.com/leylls/CFG-Group-6.git
```

2.  Install dependencies/external libraries:
You can install the packages using the requirements.txt file.
     
```pip install -r requirements.txt  ```

## How to stop TrackMazon's automated task (only for Windows users)

To stop using the app and remove the scheduled task on Windows, follow these instructions:

* Open Task Scheduler: Press Win + S, type "Task Scheduler," and press Enter.

* Locate the Task: In the Task Scheduler window, navigate to Task Scheduler Library in the left pane to find the scheduled task associated with the app.

* Delete the Task: Right-click the task you want to remove and select Delete from the context menu.

* Confirm Deletion: Confirm the deletion when prompted to ensure the task is removed.


## Requirements
Application is developed in Python 3.12


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
* web_scraping.py - Handles the extraction of product price information from websites using web scraping techniques.
* email_api.py - Provides functionality to send email notifications, using an external email API.

  Cron Job
* job.bat & job_wrapper.vbs - These files work together to make the insertion of the command for the creation of the scheduled task.
* trackmazon_task.py - Full logic for the scheduled task.
* task_scheduler.py - Here lies the functions that will interact with Window's built-in Task Scheduler through the Command Prompt (cmd).
* utils.py - Code that interacts with the boundary (i.e. task_scheduler.py) and the cron-job logic (i.e. trackmazon_task.py).


## Authors

Shaira Jiwany, Ikram Ahmed, Leyla Bush, Violeta de Pereda, Eva Perez Chirinos. 


## License
This project is open source.



## Project Status

This app is created as a final project for Summer 2024 Software Engineering CFG Degree.

The development of this project has stopped completely as we have submitted and presented this project.


## Acknowledgements 
Thank you CodeFirstGirls, our instructors and the data/software engineering team. 






