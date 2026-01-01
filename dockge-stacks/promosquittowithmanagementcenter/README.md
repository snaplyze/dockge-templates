# Pro Mosquitto with Management Center

Commercial-grade Mosquitto MQTT broker with Management Center

## Important Note

The Mosquitto broker password must be at least 12 characters.

## Quick Start

```bash
cd /opt/stacks/promosquittowithmanagementcenter
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `CEDALO_LICENSE_KEY`: License key
- `CEDALO_MOSQUITTO_PASSWORD`: Mosquitto password
- `CEDALO_MC_USER`: Management Center username
- `CEDALO_MC_PASSWORD`: Management Center password

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Edge

---

*Converted from Portainer template to Dockge format*