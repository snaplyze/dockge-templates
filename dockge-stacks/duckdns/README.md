# Duck DNS

Duck DNS is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice. The service is completely free, and doesn't require reactivation or forum posts to maintain its existence.

## Important Note

ConfigurationFirst, go to duckdns site, register your subdomain and retrieve your tokenThen run the docker create command above with your subdomain(s) and tokenIt will update your IP with the DuckDNS service every 5 minutes

## Quick Start

```bash
cd /opt/stacks/duckdns
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `SUBDOMAINS`: SUBDOMAINS
- `TOKEN`: TOKEN
- `PUID`: PUID
- `PGID`: PGID

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Dns, Tools

---

*Converted from Portainer template to Dockge format*