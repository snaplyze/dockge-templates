# Chrony NTP

chrony is a versatile implementation of the Network Time Protocol (NTP). It can synchronise the system clock with NTP servers, reference clocks (e.g. GPS receiver), and manual input using wristwatch and keyboard. It can also operate as an NTPv4 (RFC 5905) server and peer to provide a time service to other computers in the network.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/cturra/docker-ntpOfficial Docker Documentation: https://github.com/cturra/docker-ntp/blob/main/README.md

## Quick Start

```bash
cd /opt/stacks/chrony-ntp
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `LOG_LEVEL`: LOG_LEVEL
- `NTP_SERVERS`: NTP_SERVERS

## Ports

- `123:123`: Service port

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*