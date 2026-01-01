# Joomla

Another free and open-source CMS

## Quick Start

```bash
cd /opt/stacks/joomla
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `JOOMLA_DB_HOST`: MySQL database host
- `JOOMLA_DB_PASSWORD`: Database password

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/www/html` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Cms

---

*Converted from Portainer template to Dockge format*