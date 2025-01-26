# Github-Actions

Read Docs: https://docs.github.com/en/actions/about-github-actions/understanding-github-actions

## Overview
* GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

* GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.

* GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

## Workflow

* A workflow is a configurable automated process which runs one or more jobs.
* Workflows are defined by a YAML file checked in to your repository.
* In your repository workflows should be located in following directory: .github/workflows
* Name of the workflow can be defined by using "name" property.
  * name: Sample workflow example

### Workflow triggers are events that cause a workflow to run:
* Events that occur in your workflow's repository
* Events that occur outside of Github and trigger a repository_dispatch event on github
* Scheduled times
* manual

# JAVA with Maven project

https://github.com/Veeravarapu-SaiKiran/Java-Maven
