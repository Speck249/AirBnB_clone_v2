#!/usr/bin/python3
"""
Module generates .tgz archive
from contents of web_static dir.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function generates .tgz archive.
    """
    try:
        local("mkdir -p versions")

        time = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_name = "web_static_{}.tgz".format(time)
        local("tar -cvzf versions/{}"
              " web_static".format(archive_name))

        return "versions/{}".format(archive_name)

    except Exception as e:
        return None
