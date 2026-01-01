# Wireguard

[WireGuard®](https://www.wireguard.com/) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/wireguard/config

## Quick Start

```bash
cd /opt/stacks/wireguard
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `SERVERURL`: SERVERURL
- `SERVERPORT`: SERVERPORT
- `PEERS`: PEERS
- `PEERDNS`: PEERDNS
- `INTERNAL_SUBNET`: INTERNAL_SUBNET
- `ALLOWEDIPS`: ALLOWEDIPS

## Ports

- `51820:51820`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/lib/modules` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Vpnserver

---

*Converted from Portainer template to Dockge format*