# mxd-version
DESCRIPTION: Find all the MXD files in a folder and print out their ArcGIS Desktop version.

YOU NEED TO: Add a path on line 26 directing to the folder were your mxd('s) files are located.

REFERENCES: The primary function (getMXDVersion) was copied verbatim from https://gis.stackexchange.com/a/142689/335.  

**Beware:** The answer on that post that is marked as correct does not work from ArcGIS 10.4 on.  This one has been tested through 10.7.1.

This has been tested in Python 2.7 and 3.5, so it should work whether or not you have ArcGIS Pro/Python 3.x Installed and messing up your Python environment.

## olefile
The script requires [olefile](https://pypi.python.org/pypi/olefile).

```bash
pip install olefile
```
