from worktimer.core import util


class TestGetAppDir:

    def setup_method(self):
        self.app_dir = util.get_app_dir()

    def test_includes_app_name(self):
        assert "worktimer" in self.app_dir.lower()


class TestNow:

    def setup_method(self):
        self.now = util.now()

    def test_no_microseconds(self):
        assert self.now.microsecond == 0
