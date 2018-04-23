import view
import applications
import authorize
import language
import os
def get_static_server_path(file,path):
    return os.getcwd() + os.sep + os.path.dirname(file) + os.sep +path