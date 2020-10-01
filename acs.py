import os
import sys
from azure.communication.administration import CommunicationIdentityClient
import argparse

def create_user_grant_access(scope):
	# Create a new user
	try:
		connection_string = os.environ['COMMUNICATION_SERVICES_CONNECTION_STRING']
		client = CommunicationIdentityClient.from_connection_string(connection_string)
		user = client.create_user()
		print("\nCreated a user with ID: " + user.identifier + ":")

		# Issue an access token with the "voip" scope for a new user
		token_result = client.issue_token(user, [scope])
		expires_on = token_result.expires_on.strftime('%d/%m/%y %I:%M %S %p')
		print("\nIssued a token with '" + scope +"' scope that expires at " + expires_on + ":")
		print("\n" + token_result.token)

		# Revoke user access tokens
		# client.revoke_tokens(user)
		# print("\nSuccessfully revoked all tokens for user with ID: " + user.identifier)

		# Delete user
		# client.delete_user(user)
		# print("\nDeleted the user with ID: " + user.identifier)

	except Exception as ex:
		print('Exception:')
		print(ex)


def run():
    # Parse arguments from command line
    parser = argparse.ArgumentParser(description='Azure Communication Services - access token manager - v1.0')
    parser.add_argument('-u','--user', help='User index', type=int)
    parser.add_argument('-s','--scope',help='Requested scope for the access token',choices=['voip', 'chat', 'pstn'], default='chat')
    parser.add_argument('-c','--command',help='Command to execute',choices=['create', 'delete', 'grant', 'revoke', 'list', 'delete_all', 'create_grant', 'revoke_delete'])

    if len(sys.argv)==1:
    	parser.print_help(sys.stderr)
    	sys.exit(1)

    args = parser.parse_args()
    
    # Print parsed arguments 
    print ("Command: %s" % args.command )
    if args.user != None:
    	print ("User index: %d" % args.user )

    if args.command == 'create_grant':
    	create_user_grant_access(args.scope)
    elif args.command == 'list':
    	list_users()
    elif args.command == 'delete_all':
    	delete_all()
    else:
    	print("\nCommand %s not implemented yet" % args.command)			


run()
