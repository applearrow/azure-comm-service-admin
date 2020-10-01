# azure-comm-service-admin
Python scripts to create a user and grab an access token for Azure Communication Services

1. pip install azure-communication-administration
2. export an env var called COMMUNICATION_SERVICES_CONNECTION_STRING and put there your connection string
COMMUNICATION_SERVICES_CONNECTION_STRING=https://collaboration-android-poc-comm.communication.azure.com/;accesskey=OtG2XpjElj6Rr/78DDN...
3. Create a new user and request an access token for 'voip':
   python acs.py -c create_grant -s voip
4. Copy the printed access token to your iOS/android project. Along with the token you will see the expiration date printed for that token.   
   
