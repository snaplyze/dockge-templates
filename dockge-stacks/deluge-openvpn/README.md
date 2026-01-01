# Deluge openvpn

This container contains OpenVPN and Deluge with a configuration where Deluge is running only when OpenVPN has an active tunnel. It bundles configuration files for many popular VPN providers to make the setup easier.

## Quick Start

```bash
cd /opt/stacks/deluge-openvpn
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PUID`: PGID
- `OPENVPN_PROVIDER`: OPENVPN_PROVIDER
- `OPENVPN_USERNAME`: OPENVPN_USERNAME
- `OPENVPN_PASSWORD`: OPENVPN_PASSWORD

## Ports

- `8112:8112`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/localtime` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/SelfhostedPro/selfhosted_templates/

## Categories

Other, Vpn, Tools

---

*Converted from Portainer template to Dockge format*