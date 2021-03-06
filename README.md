# Keeping A Local Git Repo in sync with a Remote Repo

_**Note:**_ This is still early development, so not stable for general use at all.

A little side project I'm playing with to see if I can get close to a `Dropbox` like solution, but using `git`.

The idea is that you would have a remote repo, for example on [GitHub](https://github.com/), and then have it cloned on one or more machines. This script will attempt to keep the remote up to date.

The strategy would be to create a branch of each local machine and push this branch to the remote when changes are detected. A pull (or merge) request will be created and assuming you are watching your remote repo, you should get a notification.

If changes are merged to `main` (aka `master`, which is [no longer being used by GitHub](https://github.com/github/renaming)), the `main` branch is feteched and the changes merged to the local machine branch which is again pushed to remote.

It is a lot more work than traditional solutions, but provides more control over changes with full history (nothing ever gets lost) - and yes, this is partly why I am looking at this, as I have some bad experiences before.

This is a Python solution and requires Python 3 on a fairly modern Operating System.

Initially this script will need to run on a schedule (perhaps with something like `cron`), but eventually I hope to create a service. I am also considering a Docker solution as a service solution.

# Installing

## From the GitHub Repo

The following commands assume a *nix type system with `Python3`, `git` and a shell installed and configured to your liking.

The following commands also include the preparation of a Python virtual environment. You can omit the commands on lines 3 and 4 to skip the virtual environment if you like.

```shell
$ git clone git@github.com:nicc777/pygitsync.git
$ cd pygitsync
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ python3 setup.py sdist
(venv) $ pip3 install dist/pygitsync-0.0.1.tar.gz
```

# Preparation before Usage

Create a remote repository, for example on GitHub, and clone it to your local machine.

Note the local path.

For the examples, I'm assuming you have a **private** repository called `documents`. This example assumes the repo is cloned to a local machine on `/home/username/git/documents`.

The local machine hostname in the examples is `test-machine`.


