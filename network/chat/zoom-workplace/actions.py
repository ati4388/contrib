#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True


def setup():
    shelltools.system("ar xf zoom_amd64.deb")
    shelltools.system("tar xf data.tar.xz")


def install():
    pisitools.insinto("/opt/", "opt/*")
    pisitools.insinto("/usr/", "usr/*")