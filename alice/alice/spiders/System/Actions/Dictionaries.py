@pysnooper.snoop('parsehistory')
def unzip_dict(self, ini_dict):
    keys, values = zip(*ini_dict.items())
    return keys, values
