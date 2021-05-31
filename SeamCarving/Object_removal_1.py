import cv2
import numpy as np
import scipy.ndimage
import copy
import sys 
import math

#Cách 1: không thay đổi toạ độ mark_point, thu hẹp khung cần xoá bằng cách chia đôi toạ độ x (hàng ngang),
#sau mỗi lần loại đường seam ta sẽ cho những điểm mark_point[i] nằm ở bên phải lùi về 1 đơn vị (chỉ trừ x, giữ nguyên y)
# Chỉ thay đổi cho ma trận năng lượng E, giữ nguyên ma trận gốc I
#điều kiện dừng: lặp bằng độ rộng của vùng cần xoá (do chỉ thu hẹp theo chiều ngang)

#nhược điểm: lặp lại vùng đã xoá nếu đường bao có độ dốc cao (đường bao dạng đầu/đuôi nhỏ, thân to)

def calculateEnergy(I):
    #tính năng lượng theo công thức: https://www.cs.princeton.edu/courses/archive/spr13/cos226/assignments/seamCarving.html
    #giá trị biên = giá trị bên cạnh nó - giá trị cuối cùng
    Dx = np.roll(I,1,1) - np.roll(I,-1,1)
    Dy = np.roll(I,1,0) - np.roll(I,-1,0)
    Dxx = Dx[:,:,0]**2 + Dx[:,:,1]**2 + Dx[:,:,2]**2 #quy về mảng 2 chiều bằng cách cộng bình phương 3 phần tử lại: [a^2 + b^2 + c^2]
    Dyy = Dy[:,:,0]**2 + Dy[:,:,1]**2 + Dy[:,:,2]**2
    E = np.sqrt(Dxx + Dyy)
    #E = Dxx + Dyy
    return E

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        mark_point.append([x,y])
        s = "."
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(Img, s, (x,y), font, 1, (255,255,255), 1, 4)
        cv2.imshow('Anh goc', Img)
        
def input_data():
    print('Nhap ten anh (kem duong dan): ')
    img_name = str(input())
    print('Nhap duong dan luu anh: ')
    img_path_save = str(input())    

    global Img, mark_point
    mark_point = []
    Img = cv2.imread(img_name, 1) #thứ tự BGR
    cv2.imshow('Anh goc', Img)
    print('Kich thuoc ban dau cua Img: ', Img.shape)
    print('Nhan chuot vao cac diem bao quanh vat the ban muon xoa (theo chieu kim dong ho). Nhan enter de ket thuc.')

    cache = copy.deepcopy(Img) #luu lai trang thai cua anh truoc khi danh dau
    while 1:
        cv2.setMouseCallback("Anh goc", click_event)
        if cv2.waitKey(1) == 13: #neu nhan phim enter thi ket thuc danh dau
                break
    Img = copy.deepcopy(cache) #loai bo toa do sau khi danh dau xong bang cach khoi phuc trang thai cu
    #ve cac duong bao cho hinh
    for i in range(len(mark_point)-1):
        start_point = tuple(mark_point[i])
        end_point = tuple(mark_point[i+1])
        cv2.line(Img, start_point, end_point, (0,0,255), 1)
    cv2.line(Img, tuple(mark_point[0]), tuple(mark_point[i+1]), (0,0,255), 1)
    cv2.imshow('Anh goc', Img)
    Img = copy.deepcopy(cache)
    

def calculate_valueM(left, center, right, value): #tinh gia tri nho nhat tai M[i,j]
    #huong di tu duoi len: left = -1, center = 0, right = 1
    minVal = min(left, right, center)
    if (center == minVal):
        return (center + value, 0)
    elif (left == minVal):
        return (left + value, -1)
    else:
        return (right + value, 1)

def min_Matrix(E):
     M = np.empty(E.shape, dtype = object) #mang 2 chieu luu gia tri nho nhat va huong di
     for j in range(E.shape[1]):
         M[0,j] = (E[0,j], -2)
     for i in range(1, M.shape[0]):
         for j in range(0, M.shape[1]):
             if j == 0: #neu gap bien trai thi gia tri ngoai ria = inf
                left = math.inf
             else:
                left = M[i-1, j-1][0]

             if j == M.shape[1]-1: #neu gap bien phai
                 right = math.inf
             else:
                 right = M[i-1,j+1][0]
             
            #tinh gia tri cho M
             M[i,j] = calculate_valueM(left, M[i-1,j][0], right, E[i,j])
     return M


def remove_Seam(I, path):
     global mark_point
     maxX = max(mark_point, key = lambda tup: tup[0])
     minX = min(mark_point, key = lambda tup: tup[0])
     midX = (maxX[0] + minX[0])/2

     tempI = I.tolist() #chuyển về kdl list để có thể xoá 1 phần tử [a,b,c]
     for i in path:
         tempI[i[0]][i[1]] = [0,0,255] 
    
     #show ảnh đường seam
     I = np.array(tempI) #chuyển lại về kdl array để show ảnh   
     Img = I.astype(np.uint8)
     cv2.imshow('Anh cap nhat', Img)
     k = cv2.waitKey(1)
     if k == 27:
        cv2.destroyAllWindows()
        sys.exit()
     
     #"chặt" đường seam
     for i in path:
         tempI[i[0]].pop(i[1]) #xoá trong I
         for j in range(len(mark_point)): #nếu xoá phần tử là đỉnh trong khung
             if i == mark_point[j]:
                 if mark_point[j][0] >= midX:
                     mark_point[j][1] = mark_point[j][1] - 1
                 else:
                     mark_point[j][1] = mark_point[j][1] + 1         
     I = np.array(tempI) #chuyển lại về kdl array
     return I

def main():
    # Buoc 1: Đọc ảnh màu
    global Img, mark_point
    input_data()
     
    # Buoc 2: Tính ảnh năng lượng E    
    I = Img.astype(float)
    E = calculateEnergy(I)
    cv2.imshow('Anh nang luong', E.astype(np.uint8))
   
    #Buoc 3: danh dau phan can loai bo
    E = np.array(E)
    cv2.fillConvexPoly(E, np.array(mark_point), -10000)
   
    minX = min(mark_point, key = lambda tup: tup[0]) #tim kich thuoc cua noi can xoa
    maxX = max(mark_point, key = lambda tup: tup[0])

    count = maxX[0] - minX[0] + 1
    #Buoc 4:  Tìm đường seam nhỏ nhất trên E theo chiều từ trên xuống dưới
    while (count>0):       
        # Dùng pp quy hoạch động
        M = min_Matrix(E)
    
    #truy vết đường đi
        path = []
        i = M.shape[0]-1
        #tim vi tri phan tu nho nhat
        
        minM = M[i,0][0]
        idCol = 0
        for j in range(M.shape[1]):            
            if (M[i,j][0] < minM):
                minM = M[i,j][0]
                idCol = j

        path.append([i,idCol]) #thêm toạ độ của phần tử nhỏ nhất ở dòng cuối cùng
        pos = M[i,idCol][1] #hướng đi của vị trí tiếp theo (từ dưới lên)      
        
        while (pos != -2):
            if pos == -1: #nếu đi sang trái
                idCol = idCol - 1    
            elif pos == 1: #nếu đi sang phải
                idCol = idCol + 1
            i = i-1
            path.append([i,idCol])
            pos = M[i,idCol][1]
    
        # Buoc 4: "chặt" đường seam trên ảnh gốc Img
        I = remove_Seam(I, path)
      
        #show ảnh sau khi "chặt"
        if count == 1:
            print("Done!")            
            Img = I.astype(np.uint8)
            print('Kich thuoc sau khi loai bo: ', Img.shape)
            cv2.imshow('Anh cap nhat', Img)  
            cv2.imwrite(img_path_save, Img)
            cv2.waitKey(0)            
            break
    
        # Buoc 5: cập nhật lại ảnh năng lượng E
        E = calculateEnergy(I)

        #cập nhật lại khung đánh dấu để cho vào E
        maxX = max(mark_point, key = lambda tup: tup[0])
        minX = min(mark_point, key = lambda tup: tup[0])
        midX = (maxX[0] + minX[0])/2
        for i in mark_point: #cập nhật lại những điểm bên phải của khung đánh dấu
            if i[0] >= midX:
                i[0] = i[0] - 1 #khi i thay doi mark_point cũng thay đổi
        
        cv2.fillConvexPoly(E, np.array(mark_point), -10000)
        #cv2.imshow('Anh nang luong', E.astype(np.uint8))

        # Bước 6: nếu chưa muốn dừng thì quay lại bước 3 để tìm đường seam nhỏ nhất tiếp theo
        count = count - 1
    
    cv2.destroyAllWindows()
    
main()
