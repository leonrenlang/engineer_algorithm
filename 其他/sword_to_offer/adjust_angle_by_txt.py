# 根据图片内的文字矫正图片（from_haibing)


points = addPointsYEdg(points) #加边
        rect = cv2.minAreaRect(points)  # points是预测出来的mask
        
        (x,y), (w,h), angle = rect
        if angle < -45:
            angle = 90 + angle
        bbox = cv2.boxPoints(rect)
        
        bbox = np.array(bbox, dtype=int)
        
        
        croped = crop_by_poly(img,bbox)     #根据最小外接矩形，将图片裁剪出来，有填充
        croped = rotate_img(croped, angle)  #旋转图片
        croped = de_blank(croped)
        
        #根据文字部分再次做角度矫正
        crop_img,angle = predictAngle(croped)
        cropeds.append(crop_img)
        bbox_list.append([bbox[1], bbox[2], bbox[3], bbox[0]])

    return pred, np.array(bbox_list), cropeds

def addPointsYEdg(points):
    y_list = points[:,1]
    min_y = min(y_list)
    max_y = max(y_list)
    edge_height = (max_y-min_y)*0.1 if (max_y-min_y)*0.2 >1 else 1
    for point in points:
        if  abs(point[1]-min_y) < abs(point[1]-max_y):
            #上边点
            if point[1] > edge_height:
                point[1] = point[1]-edge_height
        else:
            point[1] = point[1] + edge_height
    return points

# 逆时针旋转图像degree角度（原尺寸）
def rotateImage(src, degree):
    # 旋转中心为图像中心
    h, w = src.shape[:2]
    # 计算二维旋转的仿射变换矩阵
    RotateMatrix = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), degree, 1)
    print(RotateMatrix)
    # 仿射变换，背景色填充为白色
    rotate = cv2.warpAffine(src, RotateMatrix, (w, h), borderValue=(255, 255, 255))
    return rotate


def predictAngle(img_cv2):
    gray_img = cv2.cvtColor(img_cv2,cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    #thresh 为那张经过黑白处理的图片.小票部分基本为黑,文字部分基本为白,这样找线反而不合理



    #对于这个二值图像，我们先获取图像中灰度值不为零的所有像素的坐标(x,y)，这些都是表示文本的像素。
    whereid = np.where(thresh > 0)
    # 交换横纵坐标的顺序，否则下面得到的每个像素点为(y,x)
    whereid = whereid[::-1]
    # 将像素点格式转换为(n_coords, 2)，每个点表示为(x,y)
    coords = np.column_stack(whereid)

    (x, y), (w, h), angle = cv2.minAreaRect(coords)
    if angle < -45:
        angle = 90 + angle

    # rotate the image to deskew it
    h, w = img_cv2.shape[:2]
    center = (w // 2, h // 2)
    # center = x, y  # 可以试试中心点设置为文本区域中心会是什么情况
    Mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img_cv2, Mat, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return  rotated,angle