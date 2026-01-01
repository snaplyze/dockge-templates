# Stash

Helps you organize your *Ahem* ...more MATURE Media material....

## Important Note

## Keep configs, scrapers, and plugins here.  - /portainer/Files/AppData/Config/stash:/root/.stash  ## Point this at your collection.  - ./data:/data  ## This is where your stash's metadata lives  - /portainer/Files/AppData/Config/stashmeta:/metadata  ## Any other cache content.  - /portainer/Files/AppData/Config/stashcache:/cache  ## Where to store generated content (screenshots,previews,transcodes,sprites)  - /portainer/Files/AppData/Config/stashgenerated:/generated

## Quick Start

```bash
cd /opt/stacks/stash
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PORT`: PORT

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Mediaserver

---

*Converted from Portainer template to Dockge format*