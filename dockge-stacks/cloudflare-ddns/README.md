# Cloudflare DDNS

A robust Cloudflare DDNS updater with a small footprint. The program will detect your machine's public IP addresses and update DNS records using the Cloudflare API.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.cloudflare.com/en-gb/learning/dns/glossary/dynamic-dns/Official Docker Documentation: https://github.com/favonia/cloudflare-ddns/

## Quick Start

```bash
cd /opt/stacks/cloudflare-ddns
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `CLOUDFLARE_API_TOKEN`: CLOUDFLARE_API_TOKEN
- `DOMAINS`: DOMAINS (Comma Separated List)
- `PROXIED`: PROXIED

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Dns, Tools

---

*Converted from Portainer template to Dockge format*