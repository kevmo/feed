from flask import jsonify

from .. import factory
from ..settings import FrontendBaseConfig


def create_app(settings_path=None, settings_override=None):

  app = factory.create_app(__name__, FrontendBaseConfig, __path__)

  return app