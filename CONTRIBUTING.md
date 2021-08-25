# Contributing

For contributing to the project development, you will need a github account (free)

After creating a github acount you can loged in [h2cs-design](https://github.com/cenaero-enb/h2cs-design) repository using your account.

On the web interface, press [Fork](https://github.com/cenaero-enb/h2cs-design) to fork the repository to your gittest account.

Clone the repository from your gittest account on your computer or your work station

```bash
git clone https://github.com/your-github-account/h2cs-design.git
cd h2cs-design
```

Add a remote upstream so that you can get changes from the `main` branch

```bash
git remote add upstream https://github.com/cenaero-enb/h2cs-design.git
```

Make changes (for ex. edit README file with vim vi README.md) and then commit your changes

```bash
vi README.md
commit -m "Made changes to README.md" README.md
```

Fetch upstream changes, without changing local files, and merge changes from the upstream master (the main repo) with your local files

More detail about forking projects could be found [HERE](https://guides.github.com/activities/forking/)

```bash
# Fetch all branches of remote upstream
git fetch upstream
git merge upstream/master
```

Push the changes to your repository

```bash
git push
```

Finally, on the web interface of your account, open a `Pull Request` so that the changes are merged to the `main` or `develop` branch. By using @mention system in your Pull Request message, you can ask for feedback from specific people or teams, whether they're down the hall or ten time zones away. Pull Requests provide a way to notify project maintainers about the changes you'd like them to consider.