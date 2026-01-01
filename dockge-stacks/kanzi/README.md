# Kanzi

[Kanzi](https://lexigr.am/), formerly titled Kodi-Alexa, this custom skill is the ultimate voice remote control for navigating Kodi. It can do anything you can think of (100+ intents). This container also contains lexigram-cli to setup Kanzi with an Amazon Developer Account and automatically deploy it to Amazon.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/kanzi/config

## Quick Start

```bash
cd /opt/stacks/kanzi
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `INVOCATION_NAME`: INVOCATION_NAME
- `URL_ENDPOINT`: URL_ENDPOINT

## Ports

- `8000:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Mediaserver

---

*Converted from Portainer template to Dockge format*