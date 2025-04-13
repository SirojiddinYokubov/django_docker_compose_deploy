import os

environment = os.getenv("ENVIRONMENT", "local")
print("ENVIRONMENT:", environment)

if environment in ["local", "test"]:
    from .testing import * # noqa
else:
    from .live import * # noqa
