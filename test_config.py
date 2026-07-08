from src.config import ConfigManager

config = ConfigManager()

print(config.get("app", "name"))
print(config.get("app", "theme"))

config.set("app", "theme", value="light")

print(config.get("app", "theme"))