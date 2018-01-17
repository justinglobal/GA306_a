## Git workflow for using Github to work remotely

Github lets us 'pull' or 'clone' an existing repository (your code on github) onto whatever computer we are using.

Open up Terminal.

If you haven't already, install git (All Mac computers have git pre-installed) on your computer. Our computers in class have git pre-installed.

Go to the Desktop (or whatever directory you want to clone into).

In a web browser, find the directory on your Github.com profile that you want to clone (probably `~/ga306`) and locate the green 'clone or download' button on the right near the top. Click it and a box will appear with a link to clone that github repository.

The link should look something like this:

```bash
https://github.com/YOUR-GITHUB-USERNAME-HERE/ga306.git
```

In Terminal, type the following command:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME-HERE/ga306.git
```

Git will copy the ga306 directory into the Desktop.

Use 'cd' to change directories into the new ga306 folder you just created.

Now we need to initialize a new git _locally_ on the computer you are using, with this command:

```bash
git init
```

Make changes as needed, edit files, add new files and directories.

Use git to 'add' and then 'commit' your changes.

```bash
git add -A
git status
```

then

```bash
git commit -m"updates"
git status
```

Now, when you have changes you want to appear on your Github.com profile, it is time to 'push' back to your Github profile. Use the following command:

```bash
git push
```

Git will ask for your github username and password, enter them and continue your workflow as normal.

On our student computers these folders will be erased when a new student logs-on.
