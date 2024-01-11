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
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        p_n_x = path_ + no_ext + "/"
        put(archive_path, "/tmp/", use_sudo=True)
        run("mkdir -p " + p_n_x)
        run("tar -xzf /tmp/" + filename + " -C " + p_n_x)
        run("rm -rf /tmp/" + filename)
        run("mv " + p_n_x + "web_static/* " + p_n_x)
        run("rm -rf " + p_n_x + "/web_static")
        run("rm -rf " + s_link)
        run("ln -s " + p_n_x + " " + s_link)
        return True
    except Exception:
        return False
