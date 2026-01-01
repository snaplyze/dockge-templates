# Chevereto

Chevereto is a powerful and fast image hosting script that allows you to create your very own full featured image hosting website in just minutes. Please note that this offers only the free Chevereto version.

## Quick Start

```bash
cd /opt/stacks/chevereto
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `CHEVERETO_DB_HOST`: CHEVERETO_DB_HOST
- `CHEVERETO_DB_USERNAME`: CHEVERETO_DB_USERNAME
- `CHEVERETO_DB_PASSWORD`: CHEVERETO_DB_PASSWORD
- `CHEVERETO_DB_NAME`: CHEVERETO_DB_NAME
- `CHEVERETO_DB_PREFIX`: CHEVERETO_DB_PREFIX

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/www/html/images` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Photos

---

*Converted from Portainer template to Dockge format*