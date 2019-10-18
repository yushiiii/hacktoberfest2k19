## Official repo for ACM HacktoberFest 2k19, PESUECC

This repo contains multiple folders, under which you will find issues and bugs. You can start working on any of the projects and create PR's for them.

[HacktoberFest '19 by DigitalOcean][hck]
Links to other issues tagged [#hacktoberfest][lk] which you can work on

# Important information

As this repo will be forked by multiple people, make sure to navigate to the "Issues" section and claim the issue/comment on it so that other people do not work on it.

# How to start:
-   Fork this repository by clicking the 'Fork' button.
-   Open your fork, and click on "Clone or Download"
-   Copy the URL that shows up. You can download it as a ZIP, but it could lead to issues if you're not familiar with git.
-   Clone this repository to your local filesystem.

    ```git
    git clone <Enter-your-fork's-url-here>
    ```

- After cloning, navigate to the issue that you resolve and start coding!

# How to create a PR:
-   After saving your code, run the following commands.

    ```git
     git remote add upstream https://github.com/acmpesuecc/hacktoberfest2k19.git
     git fetch upstream
     git checkout master
     git merge upstream/master
     git push  
     ```

-   Now your code has been successfully synced to master, and is ready to be merged.
-   Head over to this repo https://github.com/acmpesuecc/hacktoberfest2k19.git
-   Navigate to the Pull Requests tab, and create your Pull Request.

# Useful Links
- [Pull Requests and how to create them][pr]
- [Git commands and about them][git]

# Additional Issues on existing projects built by the ACM team members
- https://github.com/Irfan-S/GitHub-PR-Counter
- https://github.com/Irfan-S/Posturect

[hck]:https://hacktoberfest.digitalocean.com/
[lk]:https://github.com/search?l=&o=desc&q=label%3Ahacktoberfest+state%3Aopen&s=updated&type=Issues
[git]:http://guides.beanstalkapp.com/version-control/common-git-commands.html
[pr]:https://help.github.com/en/articles/creating-a-pull-request
