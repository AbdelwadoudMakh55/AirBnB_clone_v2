#!/usr/bin/python3
"""
This is the 2-do_deploy_web_static.py module.
This module distribute the static content (html, css, images) to the servers
"""

from fabric.api import put, run, env
import os
env.hosts = ['52.91.182.154', '34.202.164.102']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """This is the function for deploying the static content"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        path_ = "/data/web_static/releases/"
        s_link = "/data/releases/current"
        filename = archive_path.split('/')[1]
        no_ext = filename.split('.')[0]
        put(archive_path, "/tmp/")
        run(f"mkdir -p {path_}{no_ext}/")
        run(f"tar -xzf /tmp/{filename} -C {path_}{no_ext}/")
        run(f"rm -rf /tmp/{filename}")
        run(f"mv {path_}{no_ext}/web_static/* {path_}{no_ext}/")
        run(f"rm -rf {path_}{no_ext}/web_static")
        run(f"rm -rf {s_link}")
        run(f"ln -s {path_s}{no_ext}/ {s_link}")
        return True
    except Exception:
        return False
