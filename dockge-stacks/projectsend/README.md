# ProjectSend

ProjectSend is a self-hosted application that lets you upload files and assign them to specific clients that you create yourself! Secure, private and easy. No more depending on external services or e-mail to send those files.

## Quick Start

```bash
cd /opt/stacks/projectsend
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Productivity, Tools

---

*Converted from Portainer template to Dockge format*