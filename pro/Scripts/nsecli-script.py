#!c:\users\asus\desktop\stock-prediction-master__\pro\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nsepy==0.8','console_scripts','nsecli'
__requires__ = 'nsepy==0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nsepy==0.8', 'console_scripts', 'nsecli')()
    )
