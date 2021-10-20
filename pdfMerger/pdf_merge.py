import os
from glob import glob
from PyPDF2 import PdfFileMerger

if __name__=='__main__':

    while(True):
        print("먼저 병합 할 pdf를 한 폴더 안에 모두 넣고, 폴더의 경로를 복사하세요.")
        path = input('폴더 경로 : ')    # Merge 할 PDF 폴더 경로
        
        if not os.path.exists(path):
            path_list = path.split("\\")
            folder_path = os.path.join(*path_list)
            
            if not os.path.exists(folder_path):
                print("경로를 읽을 수 없습니다. 폴더 경로를 다시 확인해주세요.\n")
                continue
            
        else:
            merger = PdfFileMerger()

            files = []
            for f in glob(path + '/*.pdf'):
                files.append(f)
            
            if len(files) <= 1:
                print("병합할 PDF 파일은 1개 이상이여야 합니다.\n")
                continue
            files.sort()

            print("[병합한 PDF 파일 목록]")
            for f in files:
                print(f)
                merger.append(f)

            merger.write(path + ".pdf")
            merger.close()
            print("병합 완료!")
            flag = input("프로그램을 종료하시겠습니까? [y/n] : ")
            if flag == 'y': os.exit()
            else:
                os.system('cls') 
                continue


# pyinstaller --icon=pdfMerger.ico --onefile pdf_merge.py