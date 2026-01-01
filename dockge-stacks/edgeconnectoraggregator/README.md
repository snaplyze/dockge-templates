# EdgeConnector Aggregator

Offers a powerful OPC UA aggregation service which provides data via OPC UA, as well as MQTT

## Quick Start

```bash
cd /opt/stacks/edgeconnectoraggregator
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TZ`: TZ

## Ports

- `443`: Service port
- `8099`: Service port
- `4897`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/mqtt` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Edge

---

*Converted from Portainer template to Dockge format*