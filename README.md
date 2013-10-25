# site

This project houses the main django website.

## Installation

### Requirements

To install the required python modules using pypi:
    
    $ sudo pip install django boto python-social-auth

If we come across problematic versions of any required projects in the future, a virtualenv configuration will be required.

### Configuration

All settings for development purposes should go in `traded_io/traded_io/local_settings.py` - the most important of which will be database and AWS-related.  Boto will naturally use whatever credentials are in ~/.boto but we should write the code based around the project-specific settings.

The main project settings file `traded_io/traded_io/settings.py` will have empty string defaults and comments about what needs to be set in local_settings.

## Launching

The `manage.py` file is +x, so starting a development instance on your local machine should be as straightforward as

    $ cd traded_io
    $ ./manage.py runserver

## Development

We will follow a branch/commit/merge strategy.  Never push to `master`.  Rarely, if ever, should you push directly to `dev`.  Our process should be to branch from `dev` for new features or bugfixes, merge back together into `dev` our work, and finally merge that into `master`.  `master` should always be the released site, `dev` should be the current working state of the next version of the site.  Generally speaking, the process should basically be as follows (legend: `[branch] $ [command] [parameters]`):

    [no branch]   $ git clone git@github.com:Traded/site.git
    [no branch]   $ cd site
    [master]      $ git checkout dev
    [dev]         $ git branch new-feature
    [dev]         $ git checkout new-feature
    [new-feature] $ git status

At this point, `git status` should tell you that you're on your new feature or bugfix branch.  Alternatively, you can use `git checkout -b new-feature` instead of the branch/checkout 2 step process above.  Checking out `dev` beforehand ensures that these changes should merge cleanly back into `dev` later.

    # On branch new-feature
    ... make some changes ...
    [new-feature] $ git add [files or just .]
    [new-feature] $ git commit -m "Quick commit message"
    [new-feature] $ git push -u origin new-feature:new-feature

Now you've pushed the `new-feature` branch to the `origin` remote (github) and it's ready to be merged into `dev`.  The `-u` is a shortcut for later on.  If you plan to push several times to the same branch, having its upstream on `origin` lets you not think about it. 

    # On branch new-feature
    ... make some changes ...
    [new-feature] $ git add [files or just .]
    [new-feature] $ git commit -m "Another commit message"
    [new-feature] $ git push
    ... make some changes ...
    [new-feature] $ git add [files or just .]
    [new-feature] $ git commit -m "Resolve merge conflict or something"
    [new-feature] $ git push

Each time `git push` is issued the changes are sent to the branch on github.