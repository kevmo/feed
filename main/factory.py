from flask import Flask

def create_app(package_name, settings_path, settings_override=None):
  """Returns a :class:`Flask` application instancde configured with common functionality for the Feed platform.

  :param settings_override: a dictionary of settings to override

  """

  app = Flask(package_name)

  app.config.from_object(settings_path)

  app.config.from_object(settings_override)

  return app