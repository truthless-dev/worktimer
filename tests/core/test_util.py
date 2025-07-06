import pytest

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


@pytest.mark.parametrize(
    "input,expected",
    [
        (-1, "N/A"),
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
        (7, "N/A"),
    ],
)
class TestWeekdayName:

    def test_full_name(self, input, expected):
        result = util.weekday_name(input)
        assert result == expected

    def test_abbreviation(self, input, expected):
        result = util.weekday_name(input, True)
        assert result == expected[:3]
