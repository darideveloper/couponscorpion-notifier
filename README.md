<div><a href='https://github.com/darideveloper/couponscorpion-notifier/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/couponscorpion-notifier.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/couponscorpion-notifier/raw/master/imgs/logo.png' alt='Couponscorpion Notifier' height='80px'/>

# Couponscorpion Notifier

Check the new courses from the page couponscorpion.com/courses and send a notification by email when new courses are available.

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a><a href='https://www.crummy.com/software/BeautifulSoup/' target='_blank'> <img src='https://github.com/darideveloper/darideveloper/blob/main/imgs/logo%20bs4.png?raw=true' alt='BeautifulSoup4' title='BeautifulSoup4' height='50px'/> </a></div>

# Media

![sample email](https://github.com/darideveloper/couponscorpion-notifier/raw/master/imgs/email.png)

# Details

The project extract check the new courses from the page couponscorpion.com/courses and send a notification by email when new courses are available. You can setup the script to check the new courses in a specific time interval (in minutes); set the email address to send the notification; and set the email address to receive the notification.

# Install

## Prerequisites

* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/couponscorpion_notifier.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```

# Settings

All settings are in the `.env` file. Create it in the root folder with the following content: 

``sh
	WAIT_TIME = 15 # wait time in minutes between checks
	FROM_EMAIL = darideveloper@gmail.com # email address to send the notification
	FROM_EMAIL_PASSWORD = 12345678 # password of the email address to send the notification
	TO_EMAIL = darideveloper@gmail.com # email address to receive the notification
 ```
 
Note: the most of emails dont allow you to send emails from a script with your real password, so you need to create an application password and use it. Here a tutorial for [Gmail](https://support.google.com/accounts/answer/185833?hl=en) and [Outlook](https://support.microsoft.com/en-us/office/create-an-app-password-for-outlook-365-or-outlook-com-9c56a35d-3f3d-4eca-a288-47fa2c772e2a).

# Run

1. Run the project folder with python: 
    ```sh
    python .
    ```
2. Wait for the first check, and check your email address to receive the notification.

# Roadmap

- [x] Get the current courses in the page
- [x] History file to save the courses already checked
- [x] Submit email notification

