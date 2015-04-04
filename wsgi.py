"""

  wsgi
  ~~~~~~~~~~
  feed wsgi module

"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from main import api, frontend

if __name__ == "__main__":
  app = DispatcherMiddleware(frontend.create_app(),{
      '/api': api.create_app()
    }
  )

  run_simple('0.0.0.0', 6969, app, use_reloader=True, use_debugger=True)
