# Example Apps

This repository contains files for showing how to interact with our public API.

## Pre-Requisite

1. Make sure to have Python 3.10+ installed.
2. Run `pip install -r requirements.txt`

## public_api.py

This shows how to make requests for creating and getting interview sessions. You will need your API key which you can get from https://admin.techinterviewer.ai.

You can see the full endpoint docs at https://api.techinterviewer.ai/docs.

## webhook_example_server.py

This shows how to create your webhook route. 
1. Go to https://admin.techinterviewer.ai/settings
2. Create and run an ngrok proxy locally with `ngrok http 5000`. 
3. Run the Flask server in `webhook_example_server.py` by doing `python webhook_example_server.py`. 