#!/usr/bin/python3
"""
This is the 2-do_deploy_web_static.py module.
This module distribute the static content (html, css, images) to the servers
"""

from fabric.api import put, run, env, task
import os
env.hosts = ['52.91.182.154', '34.202.164.102']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """This is the function for deploying the static content"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        path = archive_path.split('/')
        file_name = path[1]
        no_ext = file_name.split('.')[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/" + no_ext + "/")
        run("tar -xzf /tmp/" + file_name + " -C /data/web_static/releases/"
            + no_ext + "/")
        run("mv /data/web_static/releases/" + no_ext + "/web_static/*"
            + " /data/web_static/releases/" + no_ext + "/")
        run("rm -rf /tmp/" + file_name)
        run("rm -rf /data/web_static/releases/" + no_ext + "/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/" + no_ext + "/ "
            + "/data/web_static/current")
        return True
    except Exception:
        return False
