# Zus.am

Zusam is a free and open-source way to self-host private forums for groups of friends.

## Quick Start

```bash
cd /opt/stacks/zusam
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `INIT_USER`: INIT_USER
- `INIT_PASSWORD`: INIT_PASSWORD

## Ports

- `4180:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/zusam/data` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Social, Forum

---

*Converted from Portainer template to Dockge format*