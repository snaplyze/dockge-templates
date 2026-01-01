# Portainer to Dockge Template Converter

Автоматический конвертер шаблонов Portainer в формат Docker Compose для Dockge.

**Источник шаблонов:** [Lissy93/portainer-templates](https://github.com/Lissy93/portainer-templates)

**📋 [Список всех доступных сервисов](docs/services.md)** (476 сервисов, 142 категории)

## Возможности

- ✅ **Type 1 & Type 3 поддержка** - конвертация простых контейнеров и compose стеков
- ✅ **Автоматическое скачивание** - загрузка удалённых compose файлов для type 3
- ✅ **Batch конвертация** - массовое преобразование всех шаблонов в отдельные стеки
- ✅ **Single file режим** - создание одного большого compose файла
- ✅ **Интеллектуальное маппирование путей** - автоматическое преобразование `/portainer/...` → `/opt/stacks/...`
- ✅ **Обработка портов** - корректная конвертация формата `:80/tcp` → `"80:80"`
- ✅ **Генерация .env файлов** - автоматическое создание файлов окружения
- ✅ **Создание README** - документация для каждого стека
- ✅ **Фильтры** - по категориям и платформам
- ✅ **Кастомизация** - гибкая настройка через config.json

## Требования

- Python 3.6+
- Нет внешних зависимостей (используется только стандартная библиотека)

## Получение шаблонов

Скачайте актуальные шаблоны от Lissy93:

```bash
curl -o portainer-templates.json https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json
```

## Установка

```bash
# Клонируйте репозиторий или скопируйте файл
chmod +x portainer_to_dockge.py
```

## Быстрый старт

### 1. Batch конвертация (рекомендуется)

Конвертация всех шаблонов в отдельные стеки для Dockge (автоматически скачивает актуальные шаблоны):

```bash
python3 portainer_to_dockge.py -o ./dockge-stacks --mode batch
```

Или с локальным файлом:

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./dockge-stacks \
  --mode batch
```

**Результат:**
```
dockge-stacks/
├── vaultwarden/
│   ├── compose.yaml
│   ├── .env
│   └── README.md
├── nginx/
│   ├── compose.yaml
│   └── README.md
└── mysql/
    ├── compose.yaml
    ├── .env
    └── README.md
```

### 2. Single file режим

Создание одного compose файла со всеми сервисами:

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o docker-compose.yml \
  --mode single
```

### 3. Фильтрация по категориям

Конвертация только определённой категории:

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./database-stacks \
  --category Database
```

### 4. С пользовательской конфигурацией

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./dockge-stacks \
  --config config.json
```

## Использование

### Опции командной строки

```
usage: portainer_to_dockge.py [-h] -i INPUT -o OUTPUT [--mode {batch,single}]
                              [--category CATEGORY] [--platform PLATFORM]
                              [--config CONFIG] [--no-readme] [--no-env]

Опции:
  -i, --input          Входной JSON файл с шаблонами Portainer (обязательно)
  -o, --output         Выходная директория (batch) или файл (single) (обязательно)
  --mode              Режим конвертации: batch или single (по умолчанию: batch)
  --category          Фильтр по категории (например: Database, Tools)
  --platform          Фильтр по платформе (например: linux, windows)
  --config            Файл конфигурации JSON
  --no-readme         Не создавать README файлы
  --no-env            Не создавать .env файлы
```

### Конфигурационный файл

Создайте `config.json` для кастомизации поведения:

```json
{
  "base_path": "/opt/stacks",
  "create_readme": true,
  "create_env": true,
  "skip_types": [2, 3],
  "custom_mappings": {
    "vaultwarden": {
      "/config": "/data"
    },
    "mysql": {
      "/var/lib/mysql": "/data/mysql"
    }
  }
}
```

**Параметры:**
- `base_path` - базовый путь для стеков (по умолчанию: `/opt/stacks`)
- `create_readme` - создавать README.md для каждого стека
- `create_env` - создавать .env файлы
- `skip_types` - пропускать определённые типы шаблонов (1=контейнер, 2=stack, 3=compose)
- `custom_mappings` - пользовательское маппирование путей для конкретных сервисов

## Примеры конвертации

### Пример 1: Vaultwarden

**Portainer template:**
```json
{
  "title": "Vaultwarden",
  "image": "vaultwarden/server:latest",
  "ports": [":80/tcp"],
  "volumes": [{
    "bind": "/portainer/Files/AppData/Config/Vaultwarden",
    "container": "/config"
  }],
  "restart_policy": "unless-stopped"
}
```

**Dockge compose.yaml:**
```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    volumes:
      - /opt/stacks/vaultwarden/data:/config
    ports:
      - "80:80"
    restart: unless-stopped
```

### Пример 2: MySQL с environment

**Portainer template:**
```json
{
  "title": "MySQL",
  "image": "mysql:latest",
  "ports": ["3306/tcp"],
  "env": [
    {
      "name": "MYSQL_ROOT_PASSWORD",
      "label": "Root password"
    },
    {
      "name": "MYSQL_ROOT_HOST",
      "default": "%",
      "preset": true
    }
  ],
  "volumes": [{
    "container": "/var/lib/mysql"
  }]
}
```

**Dockge compose.yaml:**
```yaml
services:
  mysql:
    image: mysql:latest
    container_name: mysql
    ports:
      - "3306:3306"
    volumes:
      - /opt/stacks/mysql/data/var_lib_mysql:/var/lib/mysql
    environment:
      - MYSQL_ROOT_HOST=%
    restart: unless-stopped
```

**.env файл:**
```env
# Environment Variables
# Edit this file to customize your deployment

# Root password (REQUIRED)
MYSQL_ROOT_PASSWORD=CHANGE_ME
```

### Пример 3: Aria2 Pro (Type 3 Stack)

**Portainer template:**
```json
{
  "type": 3,
  "title": "Aria2 Pro",
  "repository": {
    "url": "https://github.com/xneo1/portainer_templates",
    "stackfile": "Template/Stack/aria2pro.yml"
  }
}
```

**Оригинальный compose (скачанный):**
```yaml
services:
  Aria2-Pro:
    image: p3terx/aria2-pro
    volumes:
      - /portainer/Files/AppData/Config/aria2-pro:/config
      - /portainer/Downloads:/downloads
```

**Dockge compose.yaml (конвертированный):**
```yaml
services:
  Aria2-Pro:
    image: p3terx/aria2-pro
    volumes:
      - /opt/stacks/aria2-pro/data:/config
      - /opt/stacks/aria2-pro/downloads:/downloads
    restart: always
```

## Маппирование путей

Конвертер автоматически преобразует пути Portainer в формат Dockge:

| Portainer | Dockge | Примечание |
|-----------|--------|------------|
| `/portainer/Files/AppData/Config/<service>` | `/opt/stacks/<service>/data` | Основные данные |
| `/var/lib/<path>` | `/opt/stacks/<service>/data/lib/<path>` | Системные данные |
| Не указан (только container path) | `/opt/stacks/<service>/data/<path>` | Автоматическое создание |

## Интеграция с Dockge

После конвертации:

1. **Скопируйте стеки на сервер:**
   ```bash
   scp -r dockge-stacks/* user@server:/opt/stacks/
   ```

2. **В Dockge:**
   - Откройте веб-интерфейс Dockge
   - Каждая папка в `/opt/stacks/` автоматически определяется как стек
   - Настройте `.env` файлы при необходимости
   - Запускайте стеки через UI

3. **Или через CLI:**
   ```bash
   cd /opt/stacks/vaultwarden
   docker compose up -d
   ```

## Особенности конвертации

### Порты

- `:80/tcp` конвертируется в `"80:80"` (автоматический маппинг)
- `8080:80/tcp` конвертируется в `"8080:80"` (явный маппинг)
- Поддержка TCP и UDP портов

### Volumes

- Автоматическое создание структуры директорий
- Сохранение readonly флагов
- Интеллектуальное определение назначения данных

### Environment Variables

- Preset переменные добавляются в compose file
- Переменные с default значениями идут в .env файл
- Обязательные переменные помечаются как `CHANGE_ME`

### Специальные параметры

- `privileged: true` - сохраняется
- `interactive: true` - конвертируется в `stdin_open` и `tty`
- `command` - сохраняется
- `network` - сохраняется как `network_mode`

## Troubleshooting

### Проблема: Скрипт не запускается

**Решение:**
```bash
chmod +x portainer_to_dockge.py
python3 portainer_to_dockge.py --help
```

### Проблема: Ошибка при чтении JSON

**Решение:** Убедитесь, что входной файл - валидный JSON:
```bash
python3 -m json.tool portainer-templates.json > /dev/null
```

### Проблема: Неправильное маппирование путей

**Решение:** Используйте custom_mappings в config.json:
```json
{
  "custom_mappings": {
    "service_name": {
      "/container/path": "/custom/host/path"
    }
  }
}
```

## Расширенные примеры

### Конвертация только Linux сервисов

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./linux-stacks \
  --platform linux
```

### Конвертация баз данных без README

```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./db-stacks \
  --category Database \
  --no-readme
```

### Использование с другим base path

Создайте `config.json`:
```json
{
  "base_path": "/home/user/docker-data"
}
```

Запустите:
```bash
python3 portainer_to_dockge.py \
  -i portainer-templates.json \
  -o ./stacks \
  --config config.json
```

## Структура проекта

```
dockge-templates/
├── portainer_to_dockge.py    # Основной скрипт
├── config.example.json        # Пример конфигурации
├── portainer-templates.json   # Входные данные
├── README.md                  # Эта документация
└── dockge-stacks/            # Сгенерированные стеки (создаётся автоматически)
    ├── vaultwarden/
    ├── nginx/
    └── ...
```

## Лицензия

MIT License

## Автор

Snaplyze

## Поддержка

Если вы нашли баг или хотите предложить улучшение, создайте issue в репозитории.

---

**Happy dockering! 🐳**
