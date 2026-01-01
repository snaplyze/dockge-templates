# Mautic

Open-source marketing automation platform

## Quick Start

```bash
cd /opt/stacks/mautic
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MAUTIC_DB_HOST`: MySQL database host
- `MAUTIC_DB_PASSWORD`: Database password

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/www/html` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Marketing

---

*Converted from Portainer template to Dockge format*