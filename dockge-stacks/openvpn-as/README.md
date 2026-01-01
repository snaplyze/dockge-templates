# openvpn-as

OpenVPN Access Server is a full featured secure network tunneling VPN software solution that integrates OpenVPN server capabilities, enterprise management capabilities, simplified OpenVPN Connect UI, and OpenVPN Client software packages that accommodate Windows, MAC, Linux, Android, and iOS environments.

## Quick Start

```bash
cd /opt/stacks/openvpn-as
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `INTERFACE`: INTERFACE
- `PGID`: PGID
- `PUID`: PUID
- `TZ`: TZ

## Ports

- `943`: Service port
- `9443`: Service port
- `1194`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/dnburgess/self-hosted-template/

---

*Converted from Portainer template to Dockge format*