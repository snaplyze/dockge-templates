# Passky Server

Passky is a simple, modern, lightweight, open-source and secure password manager.

## Important Note

Do not forget to perform regular backups, especially before each update.

## Quick Start

```bash
cd /opt/stacks/passky-server
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ADMIN_USERNAME`: ADMIN_USERNAME
- `ADMIN_PASSWORD`: ADMIN_PASSWORD

## Ports

- `8080:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/www/html/databases` in container

## Source

Template maintainer:  https://github.com/Qballjos/portainer_templates/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*