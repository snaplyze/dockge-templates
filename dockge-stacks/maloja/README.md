# Maloja

Simple self-hosted music scrobble database to create personal listening statistics. No recommendations, no social network, no nonsense.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/krateng/malojaOfficial Docker Documentation: https://github.com/krateng/maloja/blob/master/README.mdPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_maloja.sh | bash

## Quick Start

```bash
cd /opt/stacks/maloja
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MALOJA_FORCE_PASSWORD`: MALOJA_FORCE_PASSWORD
- `MALOJA_DATA_DIRECTORY`: MALOJA_DATA_DIRECTORY

## Ports

- `42010:42010`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Music

---

*Converted from Portainer template to Dockge format*