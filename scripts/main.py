#!/usr/bin/env python3
"""
Main application entry point.
"""

import os
import sys
from core_engine.core import Core

def main():
    """
    Initializes the application and starts the main loop.
    """
    if __name__ == "__main__":
        core = Core()
        core.init()
        core.start()

if __name__ == "__main__":
    main()