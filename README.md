# click-app cookiecutter template

Cookiecutter template for creating new [Click](https://click.palletsprojects.com/) command-line tools.

Use this template on your own machine with cookiecutter, or create a brand new repository based on this template entirely through the GitHub web interface using [click-app-template-repository](https://github.com/simonw/click-app-template-repository).

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:

    pipx install cookiecutter

Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:gurrutia/cookiecutter-minimal-click-app` and then answer the prompts. Here's an example run:

    $ cookiecutter gh:gurrutia/cookiecutter-minimal-click-app
    app_name []: click app template demo
    description []: Demonstrating https://github.com/gurrutia/cookiecutter-minimal-click-app
    hyphenated [click-app-template-demo]: 
    underscored [click_app_template_demo]: 
    github_username [gurrutia]: <your-username>
    author_name [Gerardo Urrutia]: <your-name>

I strongly recommend accepting the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `click-app-template-demo` - the tool name you enter is converted to lowercase and uses hyphens instead of spaces.

## Developing your command-line tool

Having created the new structure from the template, here's how to start working on the tool.

If your tool is called `my-new-tool`, you can start working on it like so:

    cd my-new-tool

    # Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies so you can edit the project:
    pip install -e .[test]

    # Confirm your tool can be run from the command-line
    my-new-tool --version

You should see the following:

    my-new-tool, version 0.0.1

You can run the default test for your tool like so:

    pytest

This will execute the test in `tests/test_my_new_tool.py`.

Now you can open the `my_new_tool/cli.py` file and start adding Click [commands and groups](https://click.palletsprojects.com/en/8.0.x/commands/).

## Creating a Git repository for your tool

You can initialize a Git repository for your tool like this:

    cd my-new-tool
    git init
    git add .
    git commit -m "Initial structure from template"
    # Rename the 'master' branch to 'main':
    git branch -m master main

## Publishing your tool to GitHub

Use https://github.com/new to create a new GitHub repository sharing the same name as your tool, which should be something like `my-new-tool`.

Push your `main` branch to GitHub like this:

    git remote add origin git@github.com:YOURNAME/my-new-tool.git
    git push -u origin main

The template will have created a GitHub Action which runs your tool's test suite against every commit.

## Publishing your tool as a package to PyPI

The template also includes an Action for publishing packages to [PyPI](https://pypi.org/).

To use this action, you need to create a PyPI account and an API token against that account.

Once you have created your account, navigate to https://pypi.org/manage/account/token/ and create an API token. For initial publication of the package you will need to set the scope of the token to "Entire account (all projects)".

Add that token to your repository as a GitHub secret called `PYPI_TOKEN`. You can find this in the "Settings -> Secrets -> New Secret" area of the repository. The token should begin with the string `pypi-`.

Now, any time you create a new "Release" on GitHub the Action will build your package and push it to PyPI. The tag for the new release needs to match the `VERSION` string at the top of your `pyproject.toml` file.

After the first release has gone out you can create a new PyPI API token that is scoped just to that project and use that to replace the `PYPI_TOKEN` secret in your GitHub repository settings.
