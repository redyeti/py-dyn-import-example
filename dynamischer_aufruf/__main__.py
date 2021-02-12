#!/usr/bin/env python3

import sys
import plugins

if __name__ == "__main__":
    plugins.__dict__[sys.argv[1]].run()

    # oder etwas ordentlicher
    getattr(plugins, sys.argv[1]).run()
