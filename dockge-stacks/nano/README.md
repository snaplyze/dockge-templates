# Nano

[Nano](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/nano/config

## Quick Start

```bash
cd /opt/stacks/nano
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `PEER_HOST`: PEER_HOST
- `LIVE_GENESIS_PUB`: LIVE_GENESIS_PUB
- `LIVE_GENESIS_ACCOUNT`: LIVE_GENESIS_ACCOUNT
- `LIVE_GENESIS_WORK`: LIVE_GENESIS_WORK
- `LIVE_GENESIS_SIG`: LIVE_GENESIS_SIG
- `CLI_OPTIONS`: CLI_OPTIONS
- `LMDB_BOOTSTRAP_URL`: LMDB_BOOTSTRAP_URL

## Ports

- `8075:8075`: Service port
- `7076:3000`: Service port
- `7077:3001`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*