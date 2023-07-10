#!/usr/bin/python3
"""
Module generates .tgz archive
from contents of web_static dir.
"""
from fabric.api import local
from datetime import date
from time import strftime


def do_pack():
    """
    Function generates .tgz archive.
    """
    time = strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}"
              ".tgz web_static/".format(time))
        archive_path = "versions/web_static_{}.tgz".format(time)

        return archive_path

    except Exception as e:
        return None
