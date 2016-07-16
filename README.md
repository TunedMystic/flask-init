
# Flask-init

---

A quickstart Flask project template with Docker and Docker Compose.

---

### Installing

You'll need to install the following to set up and run the project:
- [Docker](http://www.docker.com/) - Build, Ship and Run your application as containers
- [Docker Compose](https://docs.docker.com/compose/) - A tool for defining and running multi-container Docker applications

Follow the instructions to [install Docker on your OS](https://www.docker.com/products/overview#/install_the_platform).

---

### Containers

This project defines and configures the following docker containers:

##### app
The flask application. Runs on port _8001_.

##### nginx
The web server, which automatically links the **app** container. Runs on port _80_.

---

### Commands

`docker-compose up` - Builds, (re)creates, starts, and attaches to containers.
- Pass the `-d` flag to run in _detached_ mode.

`docker-compose ps` - Check the status of containers.

`docker-compose logs` - View combined logs.
- Pass the `-f` flag to follow output.

`docker-compose logs <service>` - View the logs of one service.

`docker-compose stop` - Stop running containers.
- Pass the `-t` flag to specify a shutdown time in seconds.

`docker-compose rm` - Remove stopped containers.
- Pass the `-f` flag to force removal.
- Pass the `-v` flag to remove volumes attached to containers.

`docker-compose run <service> <command>` - Run a one-off command on a container.
- Pass the `--rm` flag to remove the container after run.



---

### Logging

Flask, Gunicorn, and Nginx logs can be located at `/app/logs`.
The logs persist to the host directory `./logs`, to avoid losing data across deploys.

---

### Testing

To test, run `docker-compose run --rm app python -m unittest -v`
