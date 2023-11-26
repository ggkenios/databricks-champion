# Databricks Champion

## CI/CD
| | |
| --- | --- |
| Backend | [![CI - Test](https://github.com/ggkenios/databricks-champion/actions/workflows/cicd.yml/badge.svg)](https://github.com/ggkenios/databricks-champion/actions/workflows/backend.yml) |
<br>

## Table of Contents
- [What it does](#what-it-does)
- [Requirements](#requirements)
<br>

## What it does
A simple implementation of a CI/CD pipeline for Databricks using GitHub Actions. The pipeline is triggered when a new commit is pushed to selected branches. The pipeline consists of the following steps:
* **Push** - Pushes the code to the Databricks workspace and runs unit and integration tests.
* **Release** - If the tests pass on the staging environment, the code is released to the production environment.
<br>

## Requirements
* Databricks workspace
* Link Databricks workspace to GitHub account
* GitHub secrets for:
    * Databricks workspace URL
    * Databricks token
