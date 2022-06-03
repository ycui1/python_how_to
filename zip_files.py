from pathlib import Path
from zipfile import ZipFile

book_folder = Path()
with ZipFile("zipped_code_ch02_11.zip", "w") as zip_file:
    for code_file in sorted(book_folder.glob("code_ch*")):
        print(f"Adding {code_file} to the zip file")
        zip_file.write(code_file)
