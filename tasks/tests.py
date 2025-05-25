from invoke import task


@task(default=True)
def all(c):
    """Run all tests"""
    c.run("pytest")
