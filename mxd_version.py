# Find all the MXD files in a folder and print out their ArcGIS Desktop version
# 
# The primary function (getMXDVersion) was stolen verbatim from https://gis.stackexchange.com/a/142689/335
# 
# Beware: the answer on that post that is marked as correct does not work from ArcGIS 10.4 on.  This one
# has been tested through 10.5.1.
#
# This has been tested in Python 2.7 and 3.5, so it should work whether or not you have ArcGIS Pro/Python 3.x
# Installed and messing up your Python environment.
#
import os, sys
# olefile is required: pip install olefile
from olefile import olefile

def getMXDVersion(filename):
    ofile = olefile.OleFileIO(filename)
    stream = ofile.openstream('Version')
    data = stream.read().decode('utf-16')
    version = data.split('\x00')[1]
    return version

# The first argument is the root directory to search for MXDs
if len(sys.argv) == 2:
    top = sys.argv[1]
else:
    top = '.\\'

# Get a list of all the MXD files in the directory tree
mxdfiles = []
for (root, dirs, files) in os.walk(top):
    for fname in files:
        if fname.endswith(".mxd"):
            mxdfiles.append(root + "\\" + fname)

for mxdfile in mxdfiles:
    fileName = os.path.basename(mxdfile)
    version = getMXDVersion(mxdfile)
    print (version + ' ' +  mxdfile)


exit(0)
