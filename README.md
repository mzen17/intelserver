# Assignment 4
An intelligence server for IP data.

## Backend
Server uses dnspython to do A and AAAA record matching. To start it, run
`python3 server.py` and hit Ctrl+C to quite.

To set up the environment, use either python venvs and the requirement.txt, or install it systemwide.
Server needs netcat to work with the server.

## Clients

Clients must send a JSON to the server on port 5555, or whatever the port was changed to, including the two following data:

- domain: the site that should be targetted
- command: the command that should be ran.

An example JSON is included in the referenceclient.py file. This file should be removed at the end.

## Credits, and third parties
All on the credits.md
