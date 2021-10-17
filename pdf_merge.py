import os
from glob import glob
from PyPDF2 import PdfFileMerger

folder_path = 'mybook'      # Merge 할 PDF 폴더 경로
save_name = ''              # 저장 할 PDF 이름

merger = PdfFileMerger()

for f in glob(folder_path + '*.pdf'):
    merger.append(f)

if save_name != '':
    merger.write(os.path.join(folder_path, save_name)+ ".pdf")
else:
    merger.write(os.path.basename(folder_path) + ".pdf")
merger.close()