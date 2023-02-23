import os

# Get the value of the secret named "message"
message = os.environ.get('message')

# Display the message
print('Hello ' + message)
