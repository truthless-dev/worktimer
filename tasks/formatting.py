from invoke import task


@task
def check(c):
    """Check all formatting, but do not modify files"""
    c.run("flake8 .", echo=True)
    c.run("isort --check .", echo=True)
    c.run("black --check .", echo=True)


@task(default=True)
def format(c):
    """Format all files"""
    c.run("isort .", echo=True)
    c.run("black .", echo=True)
