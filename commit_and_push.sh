#!/bin/bash

# Define your GitHub username and repository name
USERNAME="surajvast1"
REPOSITORY="App-code"

# Add all changes to the staging area
git add .

# Check if there are any changes to commit
if [ -n "$(git status --porcelain)" ]; then
    # Commit the changes
    git commit -s -m "Update $(date +%Y-%m-%d)"

    # Push changes to the GitHub repository
    git push origin master
    echo "Changes committed and pushed to GitHub."
else
    echo "No changes to commit."
fi
    