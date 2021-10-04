"""
 SYNOPSIS

     Attributor

 DESCRIPTION

    * Sanitizes subdivision names (replaces apostrophes with empty spaces)

 REQUIREMENTS

     Python 3
     arcpy
 """

import arcpy
import os
import traceback
import sys
sys.path.insert(0, "C:/Scripts")
import Logging


def subdivision_sanitation():
    """Sanitize subdivision names"""

    # Environment settings
    arcpy.env.overwriteOutput = True

    # Subdivision path
    parcel_test = r"F:\Shares\FGDB_NonCityData\SANGIS_Data.gdb"
    subdivision_polygons = os.path.join(parcel_test, "Sub_Poly")

    # Replace apostrophes
    expression = "!Sub_Name!.replace(\"\'\", \"\")"
    arcpy.CalculateField_management(subdivision_polygons, "Sub_Name", expression, "PYTHON3")


if __name__ == "__main__":
    traceback_info = traceback.format_exc()
    try:
        Logging.logger.info("Script Execution Started")
        subdivision_sanitation()
        Logging.logger.info("Script Execution Finished")
    except (IOError, NameError, KeyError, IndexError, TypeError, UnboundLocalError, ValueError):
        Logging.logger.info(traceback_info)
    except NameError:
        print(traceback_info)
    except arcpy.ExecuteError:
        Logging.logger.error(arcpy.GetMessages(2))
    except:
        Logging.logger.info("An unspecified exception occurred")
