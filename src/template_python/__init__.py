"Placeholder module info"
__version__ = "0.0.1"

from template_python.logger import Log
from icecream import ic
from pathlib import Path

log = Log()
log.info('Project Management Module Initialized')

ic.disable()
ic.enable()     # Comment this line out to enable debugger


if ic.enabled:
    log.setLevel(10) #debug
else:
    log.setLevel(20) #info

log.debug(f'Icecream Debugger: {ic.enabled}')