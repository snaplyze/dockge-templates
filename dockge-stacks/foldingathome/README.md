# Foldingathome

[Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/foldingathome/config

## Quick Start

```bash
cd /opt/stacks/foldingathome
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `7396:7396`: Service port
- `36330:36330`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*