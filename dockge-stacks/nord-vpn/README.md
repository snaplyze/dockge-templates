# nord-vpn

This is an OpenVPN client docker container that uses recommended NordVPN server. It makes routing containers traffic through OpenVPN easy.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/azinchen/nordvpnOfficial Docker Documentation: https://hub.docker.com/r/azinchen/nordvpn

## Quick Start

```bash
cd /opt/stacks/nord-vpn
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `USER`: NordVPN user
- `PASS`: NordVPN password
- `COUNTRY`: Countries to connect to (see webpage readme)
- `GROUP`: Group name filter to which to connect to
- `RANDOM_TOP`: Range of servers to pick from the top
- `RECREATE_VPN_CRON`: Define when to look again for new defined servers
- `CHECK_CONNECTION_URL`: URL to check internet connection is working to
- `NETWORK`: Subnet to define network access (read Local Network access to services connecting to the internet through the VPN readme to get the right subnet!)
- `OPENVPN_OPTS`: Used to pass extra parameters to openvpn

## Ports

- `8080:80`: Service port

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other

---

*Converted from Portainer template to Dockge format*