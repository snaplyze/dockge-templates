# Flame

Flame is self-hosted startpage for your server. Its design is inspired (heavily) by SUI. Flame is very easy to setup and use. With built-in editors, it allows you to setup your very own application hub in no time - no file editing necessary.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/pawelmalak/flameOfficial Docker Documentation: https://github.com/pawelmalak/flame#with-docker-recommended

## Quick Start

```bash
cd /opt/stacks/flame
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PASSWORD`: Flame Password

## Ports

- `5005:5005`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/data` in container
- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*