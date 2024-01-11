#!/usr/bin/python3
"""
This is the full deployment module
"""


from fabric.api import *
from datetime import datetime
import os
env.hosts = ['52.91.182.154', '34.202.164.102']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """ Compressing the web_static files into .tgz """
    current_date = datetime.now()
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    hour = str(current_date.hour)
    min = str(current_date.minute)
    sec = str(current_date.second)
    file_name = "web_static_" + year + month + day + hour + min + sec + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf versions/" + file_name + " web_static")
    path = "versions/" + file_name
    return path


def do_deploy(archive_path):
    """ This is the function for deploying the static content """
    if os.path.exists(archive_path) is False:
        return False
    path = archive_path.split('/')
    file_name = path[1]
    no_ext = file_name.split('.')[0]
    put("./" + archive_path, "/tmp/" + file_name, use_sudo=True)
    run("mkdir -p /data/web_static/releases/" + no_ext + "/")
    run("tar -xzf /tmp/" + file_name + " -C /data/web_static/releases/"
        + no_ext + "/")
    run("mv /data/web_static/releases/" + no_ext + "/web_static/*"
        + " /data/web_static/releases/" + no_ext + "/")
    run("rm -rf /tmp/" + file_name)
    run("rm -rf /data/web_static/current")
    run("ln -sf /data/web_static/releases/" + no_ext + "/ "
        + "/data/web_static/current")
    return True


@task
def deploy():
    """ Full deployment """
    path = execute(do_pack)
    for host in env.hosts:
        with settings(host_string=host):
            do_deploy(path[host])