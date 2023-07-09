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
        time = datetime.now().strftime("%Y%m%d%H%M%S")

        tgz_archive = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(tgz_archive))

        return tgz_archive

    except Exception as e:
        return None
