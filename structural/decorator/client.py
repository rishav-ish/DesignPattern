from __future__ import annotations

from datasource import FileDataSource
from decorator import DataSourceDecorator, EncryptionDecorator, CompressionDecorator

def main() -> None:
    file_datasource = FileDataSource('data.txt')
    encrypted_datasource = EncryptionDecorator(file_datasource)
    
    compressed_datasource = CompressionDecorator(file_datasource)
    
    file_datasource.read()
    file_datasource.write('data')
    
    compressed_datasource.read()
    compressed_datasource.write('data')
    
    encrypted_datasource.read()
    encrypted_datasource.write('data')
    
    
if __name__ == "__main__":
    main()
    
        
        