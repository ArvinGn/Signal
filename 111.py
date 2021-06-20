import opencv2
#6 读取图片并灰度转换，计算直方图，显示
img_gray = cv2.imread(" children.jpg",cv2.COLOR_BGR2GRAY)
#读取并进行灰度转换
img_gray_hist = cv2.calcHist([img.gray],[0],None,[256],[0，256])
#计算直方图
show_image(img_gray , "image gray",1)
show_histogram(img_gray_hist,"image gray histogram",2,"m")
#7创建mask，计算位图，直方图
mask = np.zeros(img_gray.shape[ :2],np.uint8)
mask[130:500,600:1400] = 255#获取mask，并赋予颜色
img_mask_hist = cv2.calcHist([img_gray],[0],mask,[256],[0,256])#计算mask的直方图
#8通过位运算(与预算）计算带有mask的灰度图片
mask_img = cv2.bitwise_and(img_gray, img_gray, mask= mask)
mask_img: None = cv2.bitwise_and(img_gray,img_gray,mask = mask)
show_image(mask_img,"gray image with mask " ,3)
show_histogram(img_mask_hist,"histogram with masked gray image ",4,"m")
plt.show()
