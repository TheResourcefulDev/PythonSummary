import os
from dotenv import load_dotenv
from github import Github

# Load environment variables from .env file
load_dotenv()

# Retrieve the GitHub API token from the environment variables
api_token = os.getenv("GITHUB_API_TOKEN")

# Create a GitHub instance
g = Github(api_token)

def print_repositories():
    user = g.get_user()
    repositories = user.get_repos()
    for repo in repositories:
        print(repo.name)

def upload_to_github(repo_name):
    user = g.get_user()
    repositories = user.get_repos()
    selected_repo = None

    # Check if the repo_name matches any existing repository
    for repo in repositories:
        if repo.name == repo_name:
            selected_repo = repo
            break

    # If repo_name is not found, create a new repository
    if not selected_repo:
        create_new = input("Repository not found. Do you want to create a new repository with the name '{}'? (y/n): ".format(repo_name))
        if create_new.lower() != 'y':
            print("Aborted.")
            return
        else:
            selected_repo = user.create_repo(repo_name)
            print("New repository '{}' created.".format(repo_name))

    # Upload files to the selected repository
    print("Uploading files to repository '{}'...".format(selected_repo.name))
    for root, dirs, files in os.walk("."):
        for file in files:
            if file != "upload_script.py":
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as content_file:
                    file_content = content_file.read()
                    selected_repo.create_file(file_path, "Upload file: {}".format(file), file_content)
                    print("Uploaded:", file_path)
    print("Upload complete.")

# Print available repositories for selection
print("Available repositories:")
print_repositories()

# Ask for the repository name
repo_name = input("Enter the repository name: ")
if not repo_name:
    repositories = g.get_user().get_repos()
    if repositories.totalCount == 1:
        repo_name = repositories[0].name
    else:
        print("No repository name entered.")
        exit(0)

# Confirm repository selection
print("Selected repository:", repo_name)
confirmation = input("Proceed with uploading to this repository? (y/n): ")
if confirmation.lower() != 'y':
    print("Aborted.")
    exit(0)

# Upload files to the selected repository
upload_to_github(repo_name)
