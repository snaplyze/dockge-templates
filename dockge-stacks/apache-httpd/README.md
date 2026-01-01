# Apache Httpd

The Apache HTTP Server is a free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://httpd.apache.org/Official Docker Documentation: https://hub.docker.com/_/httpd

## Quick Start

```bash
cd /opt/stacks/apache-httpd
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080:80`: Service port
- `8443:443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/usr/local/apache2/htdocs/` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Web, Proxy

---

*Converted from Portainer template to Dockge format*