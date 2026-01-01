# ContentBox

Open-source modular CMS

## Quick Start

```bash
cd /opt/stacks/contentbox
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `express`: express
- `install`: install
- `CFENGINE`: CFENGINE

## Ports

- `8080`: Service port
- `8443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data/contentbox/db` in container
- `./data/*`: Mapped to `/app/includes/shared/media` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Cms

---

*Converted from Portainer template to Dockge format*