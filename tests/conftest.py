import pytest
import yaml


def get_path(path):
    with open(path) as stream:
        data = yaml.safe_load(stream)
        return data


@pytest.fixture
def load_fixture_data():
    return get_path
