[![Build Status](https://travis-ci.org/LouisKnuckles/Zendesk_Ticket_Viewer.svg?branch=master)](https://travis-ci.org/LouisKnuckles/Zendesk_Ticket_Viewer)
# Description
### Using Python -V 3.5.0
A command line tool that prints out Zendesk tickets using the Zendesk API.
You can print out a single ticket or all tickets from your zendesk account

# Project Setup
### A step by step guide to getting the code working on your local

Clone project to your local

Note: remember to create a new [virtualenv]('https://virtualenv.pypa.io/en/stable/userguide/') before proceeding

To create a new virtual enviroment run 

'python virtualenv.py "env-name"'

To activate the new enviroment cd into the directory you just created e.g "env-name" and run
'cd Scripts\activate


### Install dependencies

 Make sure pip is installed 
 `pip install -U pip`
 
Installs dependencies for youLinux/Mac
`pip3 install -r requirements.txt`


### Set Environment Variables

export ZENDESK_ACCESS_TOKEN = 'your_token'
export ZENDESK_EMAIL_ADDRESS = 'your_email_address'
export ZENDESK_SUBDOMAIN = 'your_subdomain'


restart console after setting environment variables

You also want to make sure you are running python 3.0 or higher 
To check your current version

`python -V'

The easyist way to install python for mac is to use [homebrew]('https://brew.sh/')

Then run

'brew install python3'

You should now be able to development this project

# Installation

To install for use in command line

`pip install zendesk_ticket_viewer`

Download the src files from here. 
 
export ZENDESK_ACCESS_TOKEN = 'your_token'
export ZENDESK_EMAIL_ADDRESS = 'your_email_address'
export ZENDESK_SUBDOMAIN = 'your_subdomain'


# Usage Instructions

To start the script run

`python3 zendesk_ticket_viewer/main.py`

Select desired options from the menu.

# Bugs??

Not working? please submit an issue or even better yet feel free to fork and implement a fix ^_^

# Dependency docs

[zdesk](https://github.com/fprimex/zdesk/blob/master/README.md) - API Client used for making calls to Zendesk API

[Zendesk API](https://developer.zendesk.com/rest_api/docs)
