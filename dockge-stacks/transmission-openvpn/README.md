# Transmission OpenVPN v3

This container contains OpenVPN and Transmission with a configuration
where Transmission is running only when OpenVPN has an active tunnel.
It bundles configuration files for many popular VPN providers to make the setup easier.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://transmissionbt.com/Official Docker Documentation: https://haugene.github.io/docker-transmission-openvpn/run-container/Youtube Video: Novaspirit Tech - Torrent with Docker and OPENVPN with Transmission and PIAList of supported providers available here.

## Quick Start

```bash
cd /opt/stacks/transmission-openvpn
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `OPENVPN_PROVIDER`: OPENVPN_PROVIDER
- `OPENVPN_CONFIG`: OPENVPN_CONFIG
- `OPENVPN_USERNAME`: OPENVPN_USERNAME
- `OPENVPN_PASSWORD`: OPENVPN_PASSWORD
- `LOCAL_NETWORK`: LOCAL_NETWORK
- `TRANSMISSION_WATCH_DIR_ENABLED`: watch-dir-enabled

## Ports

- `9091:9091`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container
- `./data/*`: Mapped to `/etc/localtime` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Vpn, Tools

---

*Converted from Portainer template to Dockge format*