# Pi-Hole

A Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole.

## Important Note

When the installation is complete, navigate to your.ip.goes.here:1010/admin. Follow the article here if you run into issues binding to port 53.

## Quick Start

```bash
cd /opt/stacks/pihole
docker compose up -d
```

## Ports

- `53:53`: Service port
- `53:53`: Service port
- `67:67`: Service port
- `1010:80`: Service port
- `4443:443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/pihole` in container
- `./data/*`: Mapped to `/etc/dnsmasq.d` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Adblocking

---

*Converted from Portainer template to Dockge format*