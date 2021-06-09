import pytest

@pytest.fixture()
def global_fixture():
    return 'database connected!'