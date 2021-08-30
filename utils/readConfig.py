import pytest
import yaml
import os

@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               "test",
                               "config.yml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")
