"""Constants used across modules."""

import os


ONLINE_MAXSCRIPT_HELP_URL = {
    "2014": r"http://docs.autodesk.com/3DSMAX/16/ENU/MAXScript-Help/index.html",  # noqa
    "2015": r"http://help.autodesk.com/view/3DSMAX/2015/ENU/index.html",
    "2016": r"http://help.autodesk.com/view/3DSMAX/2016/ENU/index.html",
    "2017": r"http://help.autodesk.com/view/3DSMAX/2017/ENU/index.html",
    "2018": r"http://help.autodesk.com/view/3DSMAX/2018/ENU/index.html",
    "2018": r"http://help.autodesk.com/view/3DSMAX/2019/ENU/index.html",
}

APIPATH = os.path.dirname(os.path.realpath(__file__)) + "\maxscript.api"

# Create the tempfile in "Installed Packages".
TEMPFILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "send_to_3ds_max_temp.ms")

TITLE_IDENTIFIER = "Autodesk 3ds Max"
PREFIX = "Sublime3dsMax:"
NO_SUPPORTED_FILE = (PREFIX + " File type not supported, must be of: "
                     "*.ms, *.mcr, *.mcr, *.mse, *.py")
NO_TEMP = PREFIX + " Could not write to temp file"
NOT_SAVED = PREFIX + " File must be saved before sending to 3ds Max"
MAX_NOT_FOUND = PREFIX + " Could not find a 3ds max instance."
RECORDER_NOT_FOUND = PREFIX + " Could not find MAXScript Macro Recorder"
