#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
import os

WorkDir = "."
NoStrip = ["/"]
Sandbox = ["HOME", "tmp", "usr/local"]

def setup():
    os.chdir(get.workDIR())
    
    sh_files = shelltools.ls("*.sh")
    if not sh_files:
        raise Exception("Hiç .sh dosyası bulunamadı! Mevcut dosyalar: %s" % shelltools.ls("*"))
    
    shelltools.move(sh_files[0], "studio-3t.sh")
    shelltools.chmod("studio-3t.sh", mode=0755)
 
    shelltools.system("./studio-3t.sh -q -dir %s/studio-3t -overwrite" % get.workDIR())
    
def install():
    os.chdir(get.workDIR())
    
    # İkon
    if os.path.exists("studio-3t/.install4j/Studio-3T.png"):
        pisitools.insinto("/usr/share/pixmaps", "studio-3t/.install4j/Studio-3T.png", "studio-3t.png")
    
    # Program dosyaları
    if os.path.exists("studio-3t"):
        pisitools.insinto("/opt/studio-3t", "studio-3t/*")
    
    # Desktop dosyası
    if os.path.exists("studio-3t.desktop"):
        pisitools.insinto("/usr/share/applications", "studio-3t.desktop")
    
    # Sembolik Link
    if os.path.exists("/opt/studio-3t/Studio-3T"):
        pisitools.dosym("/opt/studio-3t/Studio-3T", "/usr/bin/studio-3t")