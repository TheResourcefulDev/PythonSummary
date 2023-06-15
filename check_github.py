import os
from dotenv import load_dotenv
from github import Github

# Load environment variables from .env file
load_dotenv()

def check_github_api_token():
    # Retrieve the GitHub API token from the environment variables
    api_token = os.getenv("GITHUB_API_TOKEN")
    print(api_token)

    if api_token:
        try:
            # Create a GitHub instance with the API token
            g = Github(api_token)

            # Check if the token is valid by getting the authenticated user
            user = g.get_user()
            print("Authentication successful! Connected to GitHub user:", user.login)
        except Exception as e:
            print("Authentication failed:", str(e))
    else:
        print("GitHub API token not found in environment variables.")

# Call the function to check the GitHub API token
check_github_api_token()
