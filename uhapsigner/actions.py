#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf uhapsigner_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")

def build():
    pass

def install():
    pisitools.insinto("/usr", "usr/*")
