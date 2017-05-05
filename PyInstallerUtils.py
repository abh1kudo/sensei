import os
import sys


def pyInstallerResourcePath(relativePath):
    basePath = getattr(sys, '_MEIPASS', os.path.abspath('./src'))
    return os.path.join(basePath, relativePath)
