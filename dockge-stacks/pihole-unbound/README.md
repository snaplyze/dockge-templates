# Pi-Hole-Unbound

A Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole. This version has Ubound software installed on it so you don't need to rely on external DNS providers. When the installation is complete, navigate to your.ip.goes.here:1010/admin. Follow the article <a href='https://medium.com/@niktrix/getting-rid-of-systemd-resolved-consuming-port-53-605f0234f32f'>here</a>

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://pi-hole.net/Official Docker Documentation: https://github.com/chriscrowe/docker-pihole-unbound/tree/master/one-containerPi-Hosted dedicated documentation: pi-hole.mdWhen the installation is complete, navigate to your.ip.goes.here:1010/admin. Follow the article here if you run into issues binding to port 53. For extra information on this container visit the mainteiner GitHub Page. You can add ports: 5335 to access Ubound externally; 22 to enable SSH; 67 to use DHCP Server. Add those ports in Show advanced options. if you run into issues binding to port 53. If you like to use Pi-Hole's built in DHCP-Server change the Network type to host and open advance options and scroll to Labels and add: NET_ADMIN with the value True. When you do so, specify a port is no more needed, navigate to your.ip.goes.here/admin.

## Quick Start

```bash
cd /opt/stacks/pihole-unbound
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ServerIP`: ServerIP
- `TZ`: TZ
- `DNSSEC`: DNSSEC
- `DNS1`: DNS1
- `DNS2`: DNS2

## Ports

- `53:53`: Service port
- `53:53`: Service port
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