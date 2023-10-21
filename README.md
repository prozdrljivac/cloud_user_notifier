# Cloud User Notifier

## Summary

Extendable script for notifying users on cloud platform. Currently only has AWS implementation and it notifies all users.

## Configuration
This configuration guide requires python version specified in `.python-version` file.
As it only implements AWS in the final step it will show how this command is run for AWS.

### Configure AWS
Follow this [guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) to configure AWS on your local machine.

### Create .venv file
``
python -m venv .venv
``

### Activate venv
On Windows
``
. .venv/Script/activate
``

### Install requirements
``
pip install -r requiremets.txt
``

### Configure .env file
1. Run `cp .env.example .env`
2. Add variables

### Look at the subject and message
Just a heads up! Currently subject and message are not dynamic so you will have to change them in code.

### Run the script
``
python main.py aws
``
