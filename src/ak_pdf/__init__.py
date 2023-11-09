"Library to Parse/Modify/Create PDF files"
__version__ = "0.0.1"

from ak_pdf.utils.logger import Log
from icecream import ic

from ak_pdf.reader import Reader
log = Log()

def debug(status=False):
    """Import this in a new module and enable debug to use debug
    example:
    ```python
    import template_python.debug
    template_python.debug(True)
    ```
    """
    if status:
        ic.enable()
        log.setLevel(10)
    else:
        ic.disable()
        log.setLevel(20)
    
debug(status=False)