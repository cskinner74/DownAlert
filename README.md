# DownAlert
Python3 script to check status of a URL, triggering a Slack alert if site is unresponsive or down.

## Setup
Requires Python3.7+

Run `pip3 install -r requirements.txt` to install dependencies

Edit `config-sample.ini` with Slack webhook URL for your workspace and rename to `config.ini`.

## Usage
`python3 DownAlert.py [-v] url`

`url` must start with `http://` or `https://`

`-v` option toggles verbose mode on

Can be scneduled as a cronjob to check periodically in background.
