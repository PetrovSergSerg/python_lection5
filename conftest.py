import pytest
from fixture.application import Application
from data.user import User


fixture = None


@pytest.fixture
def app():
    global fixture

    if fixture is None:
        fixture = Application()
    elif not fixture.is_valid():
        fixture = Application()

    fixture.session.ensure_login(User.ADMIN)

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture

    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
    return fixture

