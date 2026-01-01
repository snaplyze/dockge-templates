# System Stats OLED display

A quick way to display system stats on a 128x64 I2C OLED display.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.the-diy-life.com/Official Docker Documentation: https://github.com/mklements/OLED_Stats_DockerRun this command first to enable is2 communication! \nsudo raspi-config nonint do_i2c 0\nsudo /DietPi/dietpi/func/dietpi-set_hardware i2c enable || sudo /boot/dietpi/func/dietpi-set_hardware i2c enable\n

## Quick Start

```bash
cd /opt/stacks/oled_stats
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `start`: start displaying screen
- `end`: end displaying screen

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/timezone` in container
- `./data/*`: Mapped to `/etc/localtime` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Monitor, Other

---

*Converted from Portainer template to Dockge format*