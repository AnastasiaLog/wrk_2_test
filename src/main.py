import argparse
import sys
from config_loader import load_config
from validators import ConfigError


def main():
    parser = argparse.ArgumentParser(description="Анализатор зависимостей (Этап 1)")
    parser.add_argument("-c", "--config", default="config.json", help="Путь к JSON-конфигу")
    args = parser.parse_args()

    try:
        cfg = load_config(args.config)
        print("Параметры конфигурации:")
        for key, val in cfg.items():
            print(f"  {key.ljust(15)} : {val}")
        return 0
    except ConfigError as e:
        print(f"Ошибка конфигурации: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())