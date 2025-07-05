"""
Application utility functions.
"""

from datetime import datetime, timedelta


def get_app_dir() -> str:
    r"""Returns the config folder for the application.  The default behavior
    is to return whatever is most appropriate for the operating system.

    To give you an idea, for an app called ``"Foo Bar"``, something like
    the following folders could be returned:

    Mac OS X:
      ``~/Library/Application Support/Foo Bar``
    Mac OS X (POSIX):
      ``~/.foo-bar``
    Unix:
      ``~/.config/foo-bar``
    Unix (POSIX):
      ``~/.foo-bar``
    Windows (roaming):
      ``C:\Users\<user>\AppData\Roaming\Foo Bar``
    Windows (not roaming):
      ``C:\Users\<user>\AppData\Local\Foo Bar``
    """
    from click import get_app_dir

    return get_app_dir("WorkTimer", True, False)


def now() -> datetime:
    """
    Get the current date and time

    The resulting `datetime` object is the same as returned by
    :func:`datetime.now`, except that its microseconds are set to 0. This
    slightly abbreviated form, and timedeltas resulting from it, can
    be printed in a more visually pleasant way with less formatting
    consideration in cases where microseconds are not so important.

    :return: The date and time at the moment the function is called.
    :rtype: :class:`datetime`
    """
    dt = datetime.now()
    # Remove the microseconds.
    dt -= timedelta(microseconds=dt.microsecond)
    return dt
