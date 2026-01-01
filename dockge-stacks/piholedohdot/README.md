# Pi-Hole DoH/DoT

A Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole with both DoH (DNS over HTTPS) and DoT (DNS over TLS) clients.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://pi-hole.net/Official Docker Documentation: https://hub.docker.com/r/oijkn/pihole-doh-dotPi-Hosted dedicated documentation: pi-hole.mdWhen the installation is complete, navigate to your.ip.goes.here:1010/admin. Follow the article here if you run into issues binding to port 53. If you like to use Pi-Hole's built in DHCP-Server change the Network type to host and open advance options and scroll to Labels and add: NET_ADMIN with the value True. When you do so, specify a port is no more needed, navigate to your.ip.goes.here/admin.

## Quick Start

```bash
cd /opt/stacks/piholedohdot
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

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*