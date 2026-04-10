#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

#NoStrip = ["/opt", "/usr"]
#IgnoreAutodep = True
WorkDir = "."
NoStrip = ["/"]


def install():
    pisitools.insinto("/opt/onlyoffice/", "opt/onlyoffice/*")
    pisitools.insinto("/usr/", "usr/*")