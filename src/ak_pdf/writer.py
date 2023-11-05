from pathlib import Path
from pypdf import PdfWriter
from pypdf._reader import PdfReader
from pypdf._utils import StrByteType
from ak_pdf.reader import Reader

class Writer(PdfWriter):
    def __init__(self, fileobj: StrByteType = "", clone_from: StrByteType | PdfReader | Path | None = None) -> None:
        super().__init__(fileobj, clone_from)
        
    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def compress(self, reader: Reader, lossless: bool=True, writer: PdfWriter|None = None) -> PdfWriter:
        if writer is None:
            writer = PdfWriter()
            
        #https://pypdf.readthedocs.io/en/stable/user/file-size.html#removing-duplication
        for page in reader.pages:
            writer.add_page(page)
        
        #https://pypdf.readthedocs.io/en/stable/user/file-size.html#lossless-compression
        for page in writer.pages:
            # ⚠️ This has to be done on the writer, not the reader!
            page.compress_content_streams(level=9)  # This is CPU intensive!
            
        #https://pypdf.readthedocs.io/en/stable/user/file-size.html#reducing-image-quality
        if not lossless:
            for page in writer.pages:
                for img in page.images:
                    img.replace(img.image, quality=80)
        
        writer.add_metadata(reader.metadata) # type: ignore
        
        return writer
    
    def save(self, filepath: Path|str, writer = None) -> None:
        """Save Writer to file

        Args:
            filepath (Path | str): Filepath to pdf
            writer (Writer|None, optional): Can pass a different writer to write to file. Defaults to None.
        """
        filepath = Path(str(filepath))
        if writer is None:
            writer = self
        
        with open(filepath, 'wb') as f:
            writer.write(f)
