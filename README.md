# Test-Rails-Api
I built a small Python project that talks to the TestRail API using environment variables for security and a simple client for common actions.

## Project Structure 
- main.py — demo of the client
- config.py — loads .env settings
- testrail_client.py — API wrapper
- examples/ — basic usage scripts
- requirements.txt — dependencies


## Features
- Get projects, sections, cases, runs, and users
- Create runs, add case results, and close runs
- Clean config with .env and basic error handling


## Setup
Install dependencies (skip if using Google Colab):
```bash
pip install -r requirements.txt
```

## ENV Setup
The sample env file is titled env-sample.txt you can change the name to ".env" and replace with your credentials. 

## Troubleshooting
- 401/403: check email, API key, and API access in TestRail. Check settings to enable api usage after api key creation
- 404: check IDs (project, run, case, section)
- Network errors: check your URL and internet connection