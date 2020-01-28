import pytest

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


# @pytest.fixture(autouse=True)
@pytest.fixture()
def backend(tmpdir):
    tmp_file = tmpdir.join("test.txt")
    tmp_file.write("")
    return tmp_file
  
