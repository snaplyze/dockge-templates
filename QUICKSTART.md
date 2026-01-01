# Портainer → Dockge: Быстрый старт

## Что это?

Скрипт для автоматической конвертации шаблонов Portainer в формат Docker Compose для Dockge.

**Источник шаблонов:** [Lissy93/portainer-templates](https://github.com/Lissy93/portainer-templates)

## Скачать актуальные шаблоны

```bash
curl -o portainer-templates.json https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json
```

## Основное использование

### 1. Конвертировать ВСЕ шаблоны

```bash
python3 portainer_to_dockge.py -i portainer-templates.json -o ./dockge-stacks --mode batch
```

**Результат:** 476 готовых стеков в папке `dockge-stacks/`

### 2. Конвертировать только определённую категорию

```bash
# Только базы данных
python3 portainer_to_dockge.py -i portainer-templates.json -o ./databases --category Database

# Только инструменты
python3 portainer_to_dockge.py -i portainer-templates.json -o ./tools --category Tools

# Загрузчики (Downloaders)
python3 portainer_to_dockge.py -i portainer-templates.json -o ./downloaders --category Download
ers
```

### 3. Один большой compose файл

```bash
python3 portainer_to_dockge.py -i portainer-templates.json -o all-services.yml --mode single
```

## Типы шаблонов

Конвертер поддерживает:
- **Type 1**: Простые контейнеры (генерируется compose из JSON)
- **Type 3**: Compose стеки (скачивается и конвертируется удалённый YAML)

## Примеры конвертации

### Aria2 Pro (Type 3 Stack)

**Было (Portainer template):**
```json
{
  "type": 3,
  "repository": {
    "url": "https://github.com/xneo1/portainer_templates",
    "stackfile": "Template/Stack/aria2pro.yml"
  }
}
```

**Стало (Dockge):**
```yaml
services:
  Aria2-Pro:
    image: p3terx/aria2-pro
    volumes:
      - /opt/stacks/aria2-pro/data:/config
      - /opt/stacks/aria2-pro/downloads:/downloads
    ports:
      - 6800:6800
      - 6888:6888
    restart: always
```

### Vaultwarden (Type 1 Container)

**Было (Portainer):**
```json
{
  "ports": [":80/tcp"],
  "volumes": [{
    "bind": "/portainer/Files/AppData/Config/Vaultwarden",
    "container": "/config"
  }]
}
```

**Стало (Dockge):**
```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    ports:
      - "80:80"
    volumes:
      - /opt/stacks/vaultwarden/data:/config
    restart: unless-stopped
```

## Структура вывода

```
dockge-stacks/
├── aria2-pro/             # Type 3 stack (downloaded)
│   ├── compose.yaml
│   └── README.md
├── vaultwarden/           # Type 1 container (generated)
│   ├── compose.yaml
│   └── README.md
├── mysql/
│   ├── compose.yaml
│   ├── .env               # Переменные окружения для настройки
│   └── README.md
└── ... (476 сервисов)
```

## Использование с Dockge

1. **Конвертируйте:**
   ```bash
   python3 portainer_to_dockge.py -i portainer-templates.json -o /opt/stacks --mode batch
   ```

2. **Откройте Dockge** - все стеки появятся автоматически

3. **Настройте .env файлы** для сервисов, которые требуют конфигурации

4. **Запустите** нужные стеки через веб-интерфейс Dockge

## Что конвертируется?

✅ **Type 1 (Containers):**
- Порты (`:80/tcp` → `"80:80"`)
- Volumes (автоматический маппинг путей)
- Environment variables (с созданием .env файлов)
- Restart policies
- Privileged mode
- Commands & Networks

✅ **Type 3 (Compose Stacks):**
- Скачивание удалённых YAML файлов
- Конвертация путей `/portainer/*` → `/opt/stacks/*`
- Сохранение оригинальной сложной конфигурации
- Multi-container стеки (например, Aria2 Pro + AriaNg)

## Статистика конвертации

- **476** шаблонов в репозитории Lissy93
- Поддержка **Type 1** (containers) и **Type 3** (compose stacks)
- Автоматическое скачивание удалённых compose файлов
- Генерация README с документацией

## Помощь

```bash
python3 portainer_to_dockge.py --help
```

Подробная документация: `CONVERTER_README.md`

## Обновление шаблонов

Чтобы получить последние шаблоны от Lissy93:

```bash
# Скачать актуальные шаблоны
curl -o portainer-templates.json https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json

# Конвертировать
python3 portainer_to_dockge.py -i portainer-templates.json -o ./dockge-stacks --mode batch
```
