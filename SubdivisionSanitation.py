"""
 SYNOPSIS

     Attributor

 DESCRIPTION

    * Attributes the spatial and facility identifiers for the sewer and stormwater tables
    * Calculates the GXPCity field for sewer gravity mains by finding only gravity mains in that ward polygon
    * Appends new GPS points from the Y: drive and calculates a spatial identifier

 REQUIREMENTS

     Python 3
     arcpy
 """

import arcpy
import logging
import os
import sys
import traceback


def ScriptLogging():
    """Enables console and log file logging; see test script for comments on functionality"""
    current_directory = os.getcwd()
    script_filename = os.path.basename(sys.argv[0])
    log_filename = os.path.splitext(script_filename)[0]
    log_file = os.path.join(current_directory, f"{log_filename}.log")
    if not os.path.exists(log_file):
        with open(log_file, "w"):
            pass
    message_formatting = "%(asctime)s - %(levelname)s - %(message)s"
    date_formatting = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=message_formatting, datefmt=date_formatting)
    logging_output = logging.getLogger(f"{log_filename}")
    logging_output.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logging_output.addHandler(console_handler)
    logging.basicConfig(format=message_formatting, datefmt=date_formatting, filename=log_file, filemode="w", level=logging.INFO)
    return logging_output


def SubdivisionSanitation():
    """Collection of attribution functions"""

    # Logging
    logger = ScriptLogging()
    logger.info("Script Execution Start")

    # Environment settings
    arcpy.env.overwriteOutput = True

    # Subdivision path
    parcel_test = r"F:\Shares\FGDB_NonCityData\SANGIS_Data.gdb"
    subdivision_polygons = os.path.join(parcel_test, "Sub_Poly")

    # Try running the simple function below
    try:
        expression = "!Sub_Name!.replace(\"\'\", \"\")"
        arcpy.CalculateField_management(subdivision_polygons, "Sub_Name", expression, "PYTHON3")
    except (IOError, KeyError, NameError, IndexError, TypeError, UnboundLocalError, ValueError):
        traceback_info = traceback.format_exc()
        try:
            logger.info(traceback_info)
        except NameError:
            print(traceback_info)
    except arcpy.ExecuteError:
        try:
            logger.error(arcpy.GetMessages(2))
        except NameError:
            print(arcpy.GetMessages(2))
    except:
        logger.exception("Picked up an exception!")
    finally:
        try:
            logger.info("Script Execution Complete")
        except NameError:
            pass


def main():
    SubdivisionSanitation()


if __name__ == '__main__':
    main()
