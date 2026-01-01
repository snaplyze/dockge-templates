# Mealie

A self-hosted recipe manager and meal planner

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://hay-kot.github.io/mealie/Official Docker Documentation: https://hay-kot.github.io/mealie/documentation/getting-started/install/Default Credentials: Username: changeme@email.com Password: MyPassword. Documentation is Available here.

## Quick Start

```bash
cd /opt/stacks/mealie
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `WEB_CONCURRENCY`: WEB_CONCURRENCY
- `MAX_WORKERS`: MAX_WORKERS
- `RECIPE_PUBLIC`: RECIPE_PUBLIC
- `RECIPE_SHOW_NUTRITION`: RECIPE_SHOW_NUTRITION
- `RECIPE_SHOW_ASSETS`: RECIPE_SHOW_ASSETS
- `RECIPE_LANDSCAPE_VIEW`: RECIPE_LANDSCAPE_VIEW
- `RECIPE_DISABLE_COMMENTS`: RECIPE_DISABLE_COMMENTS
- `RECIPE_DISABLE_AMOUNT`: RECIPE_DISABLE_AMOUNT

## Ports

- `9925:9000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*