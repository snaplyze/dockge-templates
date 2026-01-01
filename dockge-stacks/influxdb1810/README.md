# Influxdb 1.8.10

InfluxDB is an open source time series database for recording metrics, events, and analytics.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.influxdata.com/Official Docker Documentation: https://docs.influxdata.com/influxdb/v2.0/install/?t=DockerYou will need to add /portainer/Files/AppData/Config/Influxdb/config/influxdb.conf

## Quick Start

```bash
cd /opt/stacks/influxdb1810
docker compose up -d
```

## Ports

- `8086:8086`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/influxdb` in container
- `./data/*`: Mapped to `/etc/influxdb` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*