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
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    name_of_archive = (f"web_static_{time}.tgz")
    path_of_archive = (f"versions/{name_of_archive}")
    local("mkdir -p versions")
    output = local(f"tar -czvf {path_of_archive} web_static",
            capture=True)

    if output.failed:
        return None
    else:
        return path_of_archive
