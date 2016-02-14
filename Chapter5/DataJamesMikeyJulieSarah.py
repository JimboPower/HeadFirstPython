def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def coach_data(file_name):
    try:       
        with open(filename) as f:
            data = f.readline()
            return(data.strip().split(','))
    except IOError as ioerr:
               print("Files Error!!" + str(ioerr))
               return(None)

coach_data('sarah2.txt')
    
