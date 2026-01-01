# Stirling PDF {shmolf}

Your locally hosted one-stop-shop for all your PDF needs.

## Important Note

To support multiple languages for OCR, per the Official documentation 🗗, download your Tess Data from from another repo 🗗. Then, place said 'traineddata' files into /portainer/Files/AppData/Libraries/StirlingPDF/tessdata For more information about login, read the official documentation 🗗.

## Quick Start

```bash
cd /opt/stacks/stirling-pdf
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `DOCKER_ENABLE_SECURITY`: Enable Login

## Ports

- `5417:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/configs` in container
- `./data/*`: Mapped to `/usr/share/tesseract-ocr/5/tessdata` in container

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Tools, Pdf

---

*Converted from Portainer template to Dockge format*