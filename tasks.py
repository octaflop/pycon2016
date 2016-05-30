import os

from invoke import ctask as task

REL = os.path.dirname(os.path.realpath(__file__))

@task
def docs(ctx):
    os.chdir("notes")
    ctx.run("make html")
    os.chdir(REL)
    ctx.run("sphinx-autobuild notes notes/_build/html/ -p 8001")
    webbrowser.open("http://127.0.0.1:8001")

