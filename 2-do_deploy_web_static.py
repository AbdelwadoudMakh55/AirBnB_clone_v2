#!/usr/bin/python3
"""
This module distribute the static content (html, css, images) to the servers
"""


from fabric.api import put, run, env, task
import os


env.hosts = ['52.91.182.154', '34.202.164.102']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ This is the function for deploying the static content """
    if os.path.exists(archive_path) is False:
        return False
    try:
        path = archive_path.split('/')
        filename = path[1]
        no_ext = filename.split('.')[0]
        put(f"./{archive_path}", f"/tmp/{filename}", use_sudo=True)
        run(f"mkdir -p /data/web_static/releases/{no_ext}/")
        run(f"tar -xzf /tmp/{filename} -C /data/web_static/releases/{no_ext}/")
        run(f"mv /data/web_static/releases/{no_ext}/web_static/*"
            + " /data/web_static/releases/{no_ext}/")
        run(f"rm -rf /tmp/{filename}")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{no_ext}/"
            + " /data/web_static/current")
        return True
    except Exception:
        return False
