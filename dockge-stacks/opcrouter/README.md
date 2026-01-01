# OPC Router

No-code middleware for industrial applications. The OPC Router connects PLCs, PCS, SCADA, MES, SQL databases and servers, label printers, e-mail servers and erp-systems via OPC UA, MQTT, REST, CSV and many others without any programming effort

## Important Note

More information about the EULA.

## Quick Start

```bash
cd /opt/stacks/opcrouter
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `INITIAL_USERNAME`: Initial Admin User user
- `INITIAL_PASSWORD`: Inital Admin User Password
- `OR_I_ACCEPT_EULA`: Accept EULA

## Ports

- `49429`: Service port
- `8080`: Service port
- `8081`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data/database` in container
- `./data/*`: Mapped to `/inray` in container
- `./data/*`: Mapped to `/var/log/opcrouter` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Edge

---

*Converted from Portainer template to Dockge format*