
# Snake client

Snake-game client.

Server: https://github.com/ivan1993spb/snake-server

* Start server: `docker run --rm --net host -d ivan1993spb/snake-server:v3.0.0-rc --log-level debug`
* Create game: `curl -v -X POST -d limit=3 -d width=30 -d height=30 http://localhost:8080/games`
* Start client: `python snake_client.py`
* Optionally you can start async clients to see multiple snakes: `python async_clients.py`

![Screenshot](screenshot.png)
