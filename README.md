Flimmer mit Pusher
------------------

A very basic chat application using Pusher.


## Setup 

Clone repository.

Run in terminal to create virtual environment.

    python -m venv .venv
    . venv/bin/activate

Run in terminal to install dependencies.

    pip install -r requirements.txt

## Configuration

Copy [env.example](./env.example) to .env

    cp env.example .env

Replace variable values for your Pusher application.


## Running

Run in terminal to serve application with flask dev server.

    python flimmer.py

