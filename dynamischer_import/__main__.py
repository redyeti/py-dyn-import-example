import sys
import importlib

if __name__ == "__main__":
    importlib.import_module("plugins.{}".format(sys.argv[1])).run()
