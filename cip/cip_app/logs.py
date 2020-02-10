import datetime
from cip.settings import DEBUG as d

def logging(trace):
    # This is to control debug mode is on or off.
    # Some variables are finally static and constants.
    # They're controlled in one file. They're stored in
    # settings file in all project.
    debug = d

    # A variable is defined with local datetime that is replaced '.' instead '/'
    file_name = str(datetime.datetime.now().strftime("%x") + ".txt").replace('/', '.')

    # If debug is true, we can create trace files, in other say logs.
    # There are two statements for existing file and non-existing file.
    # Try section is for existing file. Lines in existing log file is read from text,
    # they are written in to new text file with new trace text.
    # Except section is to create new log file.
    # They are finally closed in finally statement for both cases.
    if (debug == True):
        try:
            with open(str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(trace) + " @ " + str(datetime.datetime.now()) + "\n" + str(lines_in_log_file))
        except:
            with open(str(file_name), "a") as log_file:
                log_file.write(str(trace) + " @ " + str(datetime.datetime.now()) + "\n")
        finally:
            log_file.close()
    # Otherwise (if debug is false) logging is impossible to write.
    else:
        print("Logging is impossible to write.")

