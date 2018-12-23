# Git Command Line

## Configurations
```
git config --global user.name "Leon Lei"
git config --global user.email "leonlei35t@gmail.com"
git config --list
git config --local
```

## Help
```
git help config
git config --help
```

## Add to staging
```
git add .
git add sample.txt
```

## Commit
```
git commit -m "initial commit"

# Shortcut to add and commit
# Note that newly created files need to be manually added
git commit -am "second commit"
```

## Cloning an existing repo
```
git clone https://github.com/leon-lei/learning-materials.git
```

## Branching
```
git branch    # shows all current branches
git branch <branch_name>    # creates a new branch
git branch -d <branch_name>    # deletes a branch
```

## Stashing
```
git add <new_file>
git stash
git checkout <another_branch>
....
git checkout <branch_with_stash>
git stash apply    # Grabs the new file stashed away before
```

## Checkout
```
git checkout <branch_name>
git checkout -b <branch_name>     # Creates and then switch over to new branch
```

## Merge
```
git merge tests    # possible to have merge conflicts, which you need to resolve
```

## Merge conflicts
```
a = 1
<<<<<<< HEAD
b = 2
=======
b = 5
>>>>>>> git hash 549842163168165161
```

* Simply edit the code between the <<<< and >>>>> 
* Then commit and push back into the repo to resolve

## Remote
```
git remote -v
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

## Push and Pull
```
git push origin master
git pull origin master

git push origin --delete <branch_name>    # delete a branch on the remote repo
```

## Reset
```
git reset --hard <SHA>
git reset --hard origin/master   # reverts back to remote repo version
```

## Renaming and moving files
```
git rm first.txt
git mv third.txt pudding.txt
git mv third.txt lovenotes/puddingpie.txt
```

## Useful alias with bash
```
alias graph="git log --all --decorate --oneline --graph"
```

## Set up SSH Key on Github
```
# Generate an SSH Key
# When prompted, save to default location and then enter passphrase
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Add SSH Key to computer's SSH Agent
eval "$(ssh-agent -s)"    # enable the SSH agent

ssh-add ~/.ssh/id_rsa    # set the agent to use the key just generated

# Copy the SSH key and paste into Github
# Command below for Linux
xclip -sel clip < ~/.ssh/id_rsa.pub
```