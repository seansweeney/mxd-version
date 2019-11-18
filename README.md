# mxd-version

### Description:
Find all the MXD files in a folder and print out their ArcGIS Desktop version.

### How to:
Add the path to the folder containing your mxd's on line 26 of the mxd_version.py file.

## References:

The primary function (getMXDVersion) was copied verbatim from https://gis.stackexchange.com/a/142689/335.  

**Beware:** The answer on that post that is marked as correct does not work from ArcGIS 10.4 on.  This one has been tested through 10.7.1.

This has been tested in Python 2.7 and 3.5, so it should work whether or not you have ArcGIS Pro/Python 3.x Installed and messing up your Python environment.

## olefile
The script requires [olefile](https://pypi.python.org/pypi/olefile).

```bash
pip install olefile
```
