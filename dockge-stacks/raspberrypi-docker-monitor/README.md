# Raspberry Pi Docker Monitor

Monitor your Raspberry Pi and Dockers using Grafana developed by oijkn. Please download grafana configs from his git https://github.com/oijkn/Docker-Raspberry-PI-Monitoring

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/pi-hosted/pi-hosted/blob/master/docs/rpi_docker_monitor.mdOfficial Docker Documentation: https://github.com/pi-hosted/pi-hosted/blob/master/docs/rpi_docker_monitor.mdPi-Hosted dedicated documentation: rpi_docker_monitor.mdPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/rpi_docker_monitor.sh | bashYoutube Video: Novaspirit Tech - Raspberry Pi Docker Monitoring

## Quick Start

```bash
cd /opt/stacks/raspberrypi-docker-monitor
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PROMETHEUS_RETENTION`: PROMETHEUS_RETENTION

## Ports

- `3000:3000`: Service port

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Monitor, Tools

---

*Converted from Portainer template to Dockge format*