# Clamav

ClamAV® is an open source antivirus engine for detecting trojans, viruses, malware & other malicious threats.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://docs.clamav.net/Official Docker Documentation: https://hub.docker.com/r/mkodockx/docker-clamavPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_clamav.sh | bash

## Quick Start

```bash
cd /opt/stacks/clamav
docker compose up -d
```

## Ports

- `3310:3310`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/timezone` in container
- `./data/*`: Mapped to `/etc/localtime` in container
- `./data/*`: Mapped to `/etc/clamav` in container
- `./data/*`: Mapped to `/var/lib/clamav` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Anitvirus

---

*Converted from Portainer template to Dockge format*