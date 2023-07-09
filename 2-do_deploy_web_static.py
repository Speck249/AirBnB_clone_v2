#!/usr/bin/python3
"""
Module deploys archive
to web servers.
"""
from os import path
from fabric.api import put
from fabric.api import run
from fabric.api import env

env.user = 'ubuntu'
env.hosts = ['54.90.42.36', '100.25.34.43']
env.key_filename = ['~/.ssh/web01/school', '~/.ssh/web02/new_school']


def do_deploy(archive_path):
    """
    Deploys archive.
    """

    if not path.exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    archive_name = file_name.split(".")[0]

    try:
        """Upload archive to /tmp/."""
        put(archive_path, "/tmp/{}".format(file_name))

        """Uncompress archive to given dir."""
        run("mkdir -p /data/web_static/releases/{}".format(archive_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases"
            "/{}".format(file_name, archive_name))

        """Delete archive from web server"""
        run("rm /tmp/{}".format(file_name))

        """Move web_static directory contents to parent directory."""
        target_dir = "/data/web_static/releases/{}".format(archive_name)
        run("mv {}/web_static/* {}".format(target_dir, target_dir))

        """Delete web_static directory."""
        run("rm -rf {}/web_static".format(target_dir))

        """Delete symbolic link from web server"""
        run("rm -rf /data/web_static/current")

        """Create a new symbolic link."""
        run("ln -s /data/web_static/releases/{}/ /data/web_static"
            "/current".format(archive_name))

        return True

    except Exception as e:
        return False
