from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize Slack WebClient using the bot token - we would need to replace the token below
client = WebClient(token='slack_token')

# Define the Slack channel (or user) to send messages to - most likely user depending on flow
slack_channel = '#your-channel'


# Function to send a message to the assigned paralegal when task status changes
def send_slack_message(paralegal, task, status):
    """
    Sends a direct message to the IS when a task's status is updated to 'completed'.

    Args:
    - paralegal (str): The Slack username or ID of the IS who should be notified.
    - task (str): The task name or description.
    - status (str): The updated status of the task.

    This function uses the Slack WebClient to send a formatted message to the assigned
    paralegal, letting them know the task's status has changed and that they need to take action.
    """
    message = f"Task: {task} is now marked as {status}. Please review this task."

    try:
        # Send a direct message to the paralegal using their Slack ID or username
        response = client.chat_postMessage(channel=f"@{paralegal}", text=message)
        print(f"Message sent to {paralegal}: {message}")  # Confirm message sent in console
    except SlackApiError as e:
        # Handle any potential errors from the Slack API (e.g., invalid token or user ID)
        print(f"Error sending message: {e.response['error']}")


# Simulated function that listens for task updates in a Slack list
def listen_for_task_updates():
    """
    This function simulates listening for task updates in a Slack list.

    In a real-world scenario, this would hook into Slack's Events API or Webhooks to monitor
    updates to task statuses. When the status of a task changes to 'completed', it triggers
    the notification to the paralegal responsible for the task.

    Replace this with actual data handling in production.
    """
    # Simulated task update
    task = "case number" # here we replace with actuall case number
    status = "completed" # this is the status that will trigger the bot
    paralegal = "IS_name"

    # Notify the paralegal if the task is marked as 'completed'
    if status == "completed":
        send_slack_message(paralegal, task, status)


# If this script is executed directly, simulate task updates
if __name__ == "__main__":
    # Trigger the task update listener function (this would be event-driven in reality)
    listen_for_task_updates()
