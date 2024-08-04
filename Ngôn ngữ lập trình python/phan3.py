#1
from lop import NhanVien
import pickle
import os
#1



#2
def nhan_vien():
    nv1=NhanVien('Văn Khiêm Chương',18,'20 triệu')
    nv2=NhanVien('Bảo Tín',17,'18 triệu')
    nv3=NhanVien('Trịnh Quốc Dân',18,'17 triệu')
    nv=[nv1,nv2,nv3]
    return nv
#3
def hien_thi_list():
    nv=nhan_vien()
    for i in nv:
        print(i)
#4
def sap_xep():
    def __gt__(self,other):
        return (self.tuoi>other.tuoi)
    def __ge__(self,other):
        return(self.tuoi>=other.tuoi)
    def __lt__(self,other):
         return(self.tuoi<other.tuoi)
    def __le__(self,other):
         return(self.tuoi<=other.tuoi)
    def __eg__(self,other):
        return(self.tuoi==other.tuoi)


#5
def luu_list():
    path='C:\\Users\\HOT_BOY\\PycharmProjects\\pythonProject'
    filename='Nhanvien.txt'
    with open(os.path.join(path,filename),'wb') as f:
        pickle.dump(nhan_vien(),f)
    print('Kết thúc quá trình lưu')


#6
def doc_list():
    path = 'C:\\Users\\HOT_BOY\\PycharmProjects\\pythonProject'
    filename = 'Nhanvien.txt'
    try:
        f = open(os.path.join(path, filename), 'rt')
        content = f.readlines()
        f.close()
        print(content)
    except Exception as e:
        print('Error: ', e)
    print('Kết thúc quá trình đọc')


#7
def main():

    nhan_vien()
    hien_thi_list()
    sap_xep()
    luu_list()
    doc_list()

if __name__=='__main__':
    main()