# Slack IS Notification Bot

This bot is designed to automate the process of notifying IS when the status of a task in a Slack list is updated to "completed". Instead of having ISs manually check statuses, the bot sends a direct message to the assigned IS as soon as the task is completed.

## How It Works
- The bot listens for task updates in the GIX Attorney review list.
- Whenever a task's status changes to "completed", the bot sends a direct message to the IS responsible for that task.
- The direct message contains the task name and a request for the IS to move the case forward it.

## Prerequisites
To run this bot, you’ll need:
- **Python 3.x** installed on your machine.
- **Slack SDK for Python**: This library allows the bot to interact with Slack.
- And also have created the bot in SlackAPI

To install the required dependencies:
```bash
pip install slack-sdk