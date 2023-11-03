from pypdf import PdfReader, PageObject
from pathlib import Path
from functools import lru_cache

from . import ic
ic.configureOutput(prefix=f'{Path(__file__).name} -> ')

class Reader(PdfReader):
    def __init__(self, filepath: str|Path, password: str|None = None) -> None:
        ic(f'Reader Class Instance started for {filepath}')
        self.filepath: Path = Path(str(filepath))
        assert self.filepath.is_file(), f'{self.filepath} is not a valid file'
        
        super().__init__(stream=self.filepath, strict=False, password=password)
        assert 'pdf' in self.pdf_header.lower(), f'{self.filepath} is not a PDF file'
        
        
    def __str__(self) -> str:
        return f'Reader class instance for {self.filepath}'
    
    def __repr__(self) -> str:
        return f'Reader(filepath={self.filepath})'
    
    @property
    def num_pages(self) -> int:
        return len(self.pages)
    
    @lru_cache(maxsize=None)
    def text(self, page_idx:int) -> str:
        return self.pages[page_idx].extract_text()
    
    def images(self, page_idx: int) -> list:
        return self.pages[page_idx].images # type: ignore
    
    def save_images(self, page_idx: int, folderpath: Path|str) -> list[Path]:
        folderpath = Path(str(folderpath))
        folderpath.mkdir(exist_ok=True, parents=True)
        
        _img_num: int = 1
        files: list[Path] = []
        for img in self.images(page_idx):
            filename: str = f'{_img_num}_{img.name}' # type: ignore
            filepath: Path = folderpath / filename
            ic(f'Saving img: {filename}')
            
            with open(filepath, 'wb') as f:
                f.write(img.data) # type: ignore
                
            files.append(filepath)
            _img_num += 1
            
        ic(f'Saved {_img_num - 1} imgs to {folderpath}')
        return files
    
    
    def page_number(self, page_idx: int|None = None, page: PageObject|None = None) -> str:
        if page_idx is not None and page is not None:
            raise Exception('Only specify either of `page_idx` or `page`')
        if page_idx is None and page is None:
            raise Exception('Must specify either of `page_idx` or `page`')
        
        if page:
            page_idx = self.get_page_number(page)
            
        return self.page_labels[page_idx] # type: ignore
    
    @property
    def encrypted(self) -> bool:
        return self.is_encrypted