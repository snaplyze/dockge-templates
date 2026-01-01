# Adguard

AdGuard Home is a network-wide software for blocking ads & tracking. After you set it up, it’ll cover ALL your home devices, and you don’t need any client-side software for that. With the rise of Internet-Of-Things and connected devices, it becomes more and more important to be able to control your whole network.

## Quick Start

```bash
cd /opt/stacks/adguard
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `CONTEXT_PATH`: CONTEXT_PATH

## Ports

- `53:53`: Service port
- `53:53`: Service port
- `67:67`: Service port
- `68:68`: Service port
- `68:68`: Service port
- `80:80`: Service port
- `443:443`: Service port
- `853:853`: Service port
- `3000:3000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/opt/adguardhome/work` in container
- `./data/*`: Mapped to `/opt/adguardhome/conf` in container

## Source

Template maintainer:  https://github.com/mikestraney/portainer-templates/

## Categories

Other

---

*Converted from Portainer template to Dockge format*