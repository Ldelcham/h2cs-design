# h2cs-design

## Introduction
Repository for WP3 of H2CS project

Binary files should not be uploaded on this repository but sharepoint repository of the WP [here](https://msclefscrl.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?originalPath=aHR0cHM6Ly9tc2NsZWZzY3JsLnNoYXJlcG9pbnQuY29tLzpmOi9nL0VxREZGYlVJZGVGQnBocm9JMEpFWU1vQkNwaVJCbFNDLUZ3WFFRc1I0VXEweXc%5FcnRpbWU9RHdKb1J1bkkyRWc&viewid=9e8eb8d5%2Dce9f%2D4554%2Da177%2Dea7167642b8d&id=%2FShared%20Documents%2FProjets%20de%20recherche%2FH2%20CoopStorage%20%2D%20MICall19%2F6%2E%20WP%2FWP3%20%2D%20Sizing%20tool)

## Contribution

Contribution

For contributing to the project development, you will need a github account (free or paid)

After create a github acount you can loged in h2cs-design repository using your account.

On the web interface, press Fork to fork the repository to your gittest account.

Clone the repository from your gittest account on your computer or your work station

```
git clone http://gittest.cenaero.be:3000/your-gittest-account/pytpee.git
cd pytpee
# Add a remote upstream so that you can get changes from the master branch
git remote add upstream http://gittest.cenaero.be:3000/WEC-ENR/pytpee.git
```

Make changes (for ex. edit README file with vim vi README.md) and then commit your changes

```
vi README.md
commit -m "Made changes to README.md" README.md
```

Fetch upstream changes, without changing local files, and merge changes from the upstream master (the main repo) with your local files

More detail about forking projects could be found [HERE](https://guides.github.com/activities/forking/)

```
# Fetch all branches of remote upstream
git fetch upstream
git merge upstream/master
```

Push the changes to your repository

```
git push
```

Finally, on the web interface of your account, open a Pull Request so that the changes are merged to the master branch. By using @mention system in your Pull Request message, you can ask for feedback from specific people or teams, whether they're down the hall or ten time zones away. Pull Requests provide a way to notify project maintainers about the changes you'd like them to consider.
