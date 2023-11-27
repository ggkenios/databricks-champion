<p align="center">
  <a href="https://devoteam.com"><img src="https://media.licdn.com/dms/image/C560BAQEloqEBLHUukg/company-logo_200_200/0/1630631081923/devoteam_logo?e=1709164800&v=beta&t=amHRy8uUVDG-4Kk0ah38IONJIF5uELeVTdj0_7f_nIU" alt="Devoteam"></a>
</p>

## CI/CD
| | |
| --- | --- |
| Tests | [![CI - Test](https://github.com/ggkenios/databricks-champion/actions/workflows/cicd.yml/badge.svg)](https://github.com/ggkenios/databricks-champion/actions/workflows/backend.yml) |
<br>

## Table of Contents
- [What it does](#what-it-does)
- [Requirements](#requirements)
<br>

## What it does
A simple implementation of a CI/CD pipeline for Databricks using **`GitHub Actions`** & **`Databricks Workflows`**. <br>
The pipeline is triggered when a new commit is pushed to selected branches. <br>
<br>
The pipeline consists of the following steps:
* **Push** <br>
    Pushes the code to the Databricks workspace and runs unit and integration tests.

* **Release** <br>
    If the tests pass on the staging environment, the code is released to the production environment.
<br>

## Requirements
* **__Databricks__** workspace
* Link between **__Databricks__** workspace and **__GitHub__** account
* **__GitHub secrets__** for:
    * Databricks URL
    * Databricks token
