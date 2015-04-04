from flask import jsonify

from .. import factory
from ..settings import APIBaseConfig


def create_app(settings_path=None, settings_override=None):

  app = factory.create_app(__name__, APIBaseConfig)

  return app