"Library to Parse/Modify/Create PDF files"
__version__ = "0.0.1"

from ak_pdf.logger import Log
from icecream import ic

from ak_pdf.reader import Reader

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
    else:
        ic.disable()
    
debug(status=False)