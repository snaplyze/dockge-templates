# Booksonic-air

[Booksonic-air](http://booksonic.org) is a platform for accessing the audibooks you own wherever you are. At the moment the platform consists of Booksonic Air - A server for streaming your audiobooks, successor to the original Booksonic server and based on Airsonic. Booksonic App - An DSub based Android app for connection to Booksonic-Air servers. .

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/booksonic-air/configmkdir -p /volume1/docker/booksonic-air/audiobooksmkdir -p /volume1/docker/booksonic-air/podcastsmkdir -p /volume1/docker/booksonic-air/othermedia

## Quick Start

```bash
cd /opt/stacks/booksonic-air
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `CONTEXT_PATH`: CONTEXT_PATH

## Ports

- `4040:4040`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/audiobooks` in container
- `./data/*`: Mapped to `/podcasts` in container
- `./data/*`: Mapped to `/othermedia` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Libraryserver

---

*Converted from Portainer template to Dockge format*