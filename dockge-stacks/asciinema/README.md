# Asciinema {shmolf}

Self-hosted terminal recording and playback

## Important Note

Application documentation 🗗For the application secret key, you can use the terminal command tr -dc A-Za-z0-9 &lt;/dev/urandom | head -c 64; echo

## Quick Start

```bash
cd /opt/stacks/asciinema
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `HOST_NAME`: Hostname
- `HOST_PORT`: Host Port
- `SECRET_KEY`: Secret Application Key

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*