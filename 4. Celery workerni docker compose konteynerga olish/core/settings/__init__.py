import os

environment = os.getenv("ENVIRONMENT", "local")
print("ENVIRONMENT:", environment)

if environment in ["local", "test", "dev"]:
    from .testing import * # noqa
else:
    from .live import * # noqa
