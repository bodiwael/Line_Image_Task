import cv2

import numpy as np

import sys

def main():

    font = cv2.FONT_HERSHEY_SIMPLEX

    frame = cv2.imread("/home/abdelrahman/Line_Follower/Image6.jpeg")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,50,50])

    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    gray = cv2.bitwise_not(gray)

    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    horizontal = np.copy(bw)

    vertical = np.copy(bw)

    cols = horizontal.shape[1]

    horizontal_size = cols / 20

    horizontal_size=int(horizontal_size)

    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))

    horizontal = cv2.erode(horizontal, horizontalStructure)

    horizontal = cv2.dilate(horizontal, horizontalStructure) 

    rows = vertical.shape[0]

    verticalsize = rows / 20

    verticalsize = int(verticalsize)

    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))

    vertical = cv2.erode(vertical, verticalStructure)

    vertical = cv2.dilate(vertical, verticalStructure)

    white_pix = np.sum(horizontal == 255)

    if white_pix > 100 :
        
        print("Horizontal Detected")
        
        blue = "H"

    else:
        
        blue = "V"
        
        print("Vertical Detected")

    img = cv2.imread("/home/abdelrahman/Line_Follower/Image6.jpeg")

    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_canny = cv2.Canny(img, 25 , 255)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_dark_red = np.array([0, 50, 50]).reshape((1,1,3))

    high_dark_red = np.array([255, 255, 255]).reshape((1,1,3))

    sq = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    squ = []

    (h, w) = img.shape[:2]

    centerx, centery = (w // 14), (h // 14)

    sq[0] = img[0 : centery, 0 : centerx]

    sq[1] = img[0 : centery, centerx : centerx*4]

    sq[2] = img[0 : centery, centerx*4 : centerx*7]

    sq[3] = img[0 : centery, centerx*7 : centerx*10]

    sq[4] = img[0 : centery, centerx*10 : centerx*13]

    sq[5] = img[0 : centery, centerx*13 : w]

    sq[6] = img[centery*2 : centery*5, 0 : centerx]

    sq[7] = img[centery*2 : centery*5, centerx : centerx*4]

    sq[8] = img[centery*2 : centery*5, centerx*4 : centerx*7]

    sq[9] = img[centery*2 : centery*5, centerx*7 : centerx*10]

    sq[10] = img[centery*2 : centery*5, centerx*10 : centerx*13]

    sq[11] = img[centery*2 : centery*5, centerx*13 : w]

    sq[12] = img[centery*5 : centery*9, 0 : centerx]

    sq[13] = img[centery*5 : centery*9, centerx : centerx*4]

    sq[14] = img[centery*5 : centery*9, centerx*4 : centerx*7]

    sq[15] = img[centery*5 : centery*9, centerx*7 : centerx*10]

    sq[16] = img[centery*5 : centery*9, centerx*10 : centerx*13]

    sq[17] = img[centery*5 : centery*9, centerx*13 : w]

    sq[18] = img[centery*9 : centery*13, 0 : centerx]

    sq[19] = img[centery*9 : centery*13, centerx : centerx*4]

    sq[20] = img[centery*9 : centery*13, centerx*4 : centerx*7]

    sq[21] = img[centery*9 : centery*13, centerx*7 : centerx*10]

    sq[22] = img[centery*9 : centery*13, centerx*10 : centerx*13]

    sq[23] = img[centery*9 : centery*13, centerx*13 : w]

    sq[24] = img[centery*13 : h, 0 : centerx]

    sq[25] = img[centery*13 : h, centerx : centerx*4]

    sq[26] = img[centery*13 : h, centerx*4 : centerx*7]

    sq[27] = img[centery*13 : h, centerx*7 : centerx*10]

    sq[28] = img[centery*13 : h, centerx*10 : centerx*13]

    sq[29] = img[centery*13 : h, centerx*13 : w]

    i = 0

    while (i < 30):
        
        img_hsv = cv2.cvtColor(sq[i], cv2.COLOR_BGR2HSV)

        red_mask = cv2.inRange(img_hsv, low_dark_red, high_dark_red)
        
        white_pix = np.sum(red_mask == 255)

        if white_pix > 100 :
               
            print("Square " + str(i) +" detected")
            
            squ.append("True")
        
        else:
            
            squ.append("False")
            
            print(str(i) + " Removed")
                    
        i += 1
        
    print(len(squ))

    i = 0

    while (i < 30):
        
        gray = cv2.cvtColor(sq[i], cv2.COLOR_BGR2GRAY)

        gray_blurred = cv2.blur(gray, (3, 3))

        detected_circles = cv2.HoughCircles(gray_blurred,
                                            
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                                            
                    param2 = 30, minRadius = 1, maxRadius = 40)

        if detected_circles is not None:

            detected_circles = np.uint16(np.around(detected_circles))
            
            Final = i
            
            print("Square " + str(i) + " Circle Detected")

            for pt in detected_circles[0, :]:
                
                a, b, r = pt[0], pt[1], pt[2]

                cv2.circle(img, (a, b), r, (0, 255, 0), 2)

                cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
                
                cv2.putText(sq[i],'Square 1',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                
                cv2.imshow("Detected Circle", sq[i])
        
        i += 1
        
    print(Final)

    if (blue == "V"):

        if(squ[Final] == "True"):
            
            if(Final > 17):
                
                if(squ[Final-1] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Final-1])
                    
                    print("First Con")
                
                elif(squ[Final+1] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Final+1])
                    
                    print("Second Con")
                
                elif(squ[Final-6] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Final-6])
                    
                    print("Third Con")
                     
            elif(Final < 17):
                
                if(squ[Final-1] == "True"):
                    
                    cv2.putText(sq[Final-1],'Square 2',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                    cv2.imshow("Square 2" ,sq[Final-1])
                    
                    Final = Final-1
                    
                    print("First Con")
                    
                    if(squ[Final+6] == "True"):
                        
                        cv2.putText(sq[Final+6],'Square 3',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                        cv2.imshow("Square 3" ,sq[Final+6])
                        
                        Final = Final+6
                        
                        print("First Con")
                        
                        if(squ[Final+6] == "True"):
                            
                            cv2.putText(sq[Final+6],'Square 4',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                            cv2.imshow("Square 4" ,sq[Final+6])
                            
                            Final = Final+6
                            
                            print("First Con")
                            
                            if(squ[Final+6] == "True"):
                                
                                cv2.putText(sq[Final+6],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final+6])
                                
                                Final = Final+6
                                
                                print("First Con")
                            
                            elif(squ[Final-1] == "True"):
                                
                                cv2.putText(sq[Final-1],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final-1])
                                
                                Final = Final-1
                                
                                print("Second Con")
                                
                                if(squ[Final-6] == "True"):
                                    
                                    cv2.putText(sq[Final-6],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                    cv2.imshow("Square 6" ,sq[Final-6])
                                    
                                    Final = Final-6
                                    
                                    print("First Con")
                                    
                                    if(squ[Final-6] == "True"):
                                        
                                        cv2.putText(sq[Final-6],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                        cv2.imshow("Square 7" ,sq[Final-6])
                                        
                                        Final = Final-6
                                        
                                        print("First Con")
                                        
                                        if(squ[Final-6] == "True"):
                                            
                                            cv2.putText(sq[Final-6],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                            cv2.imshow("Square 8" ,sq[Final-6])
                                            
                                            Final = Final-6
                                            
                                            print("First Con")
                                        
                                        elif(squ[Final-1] == "True"):
                                            
                                            cv2.putText(sq[Final-1],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                
                                            cv2.imshow("Square 8" ,sq[Final-1])
                                            
                                            Final = Final-1
                                            
                                            print("Second Con")
                                            
                                            if(squ[Final+6] == "True"):
                                                
                                                cv2.putText(sq[Final+6],'Square 9',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                cv2.imshow("Square 9" ,sq[Final+6])
                                                
                                                Final = Final+6
                                                
                                                print("First Con")
                                                
                                                if(squ[Final+6] == "True"):
                                                    
                                                    cv2.putText(sq[Final+6],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                    cv2.imshow("Square 10" ,sq[Final+6])
                                                    
                                                    Final = Final+6
                                                    
                                                    print("First Con")
                                                    
                                                    if(squ[Final+6] == "True"):
                                                        
                                                        cv2.putText(sq[Final+6],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                        cv2.imshow("Square 11" ,sq[Final+6])
                                                        
                                                        Final = Final+6
                                                        
                                                        print("First Con")
                                                    
                                                    elif(squ[Final-1] == "True"):
                                                        
                                                        cv2.putText(sq[Final-1],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-1])
                                                        
                                                        Final = Final-1
                                                        
                                                        print("Second Con")
                                                        
                                                        if(squ[Final-6] == "True"):
                                                            
                                                            cv2.putText(sq[Final-6],'Square 12',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                            cv2.imshow("Square 12" ,sq[Final-6])
                                                            
                                                            Final = Final-6
                                                            
                                                            print("First Con")
                                                            
                                                            if(squ[Final-6] == "True"):
                                                                
                                                                cv2.putText(sq[Final-6],'Square 13',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                                cv2.imshow("Square 13" ,sq[Final-6])
                                                                
                                                                Final = Final-6
                                                                
                                                                print("First Con")
                                                                
                                                                if(squ[Final-6] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-6],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                                    cv2.imshow("Square 14" ,sq[Final-6])
                                                                    
                                                                    Final = Final-6
                                                                    
                                                                    print("First Con")
                                                                
                                                                elif(squ[Final-1] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-1],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                                        
                                                                    cv2.imshow("Square 14" ,sq[Final-1])
                                                                    
                                                                    Final = Final-1
                                                                    
                                                                    print("Second Con")
                                                                    
                                                                elif(squ[Final+1] == "True"):
                                                        
                                                                    cv2.imshow("Square 14" ,sq[Final+1])
                                                                    
                                                                    Final = Final+1
                                                                    
                                                                    print("Third Con")
                                                            
                                                            elif(squ[Final-1] == "True"):
                                                    
                                                                cv2.imshow("Square 13" ,sq[Final-1])
                                                                
                                                                Final = Final-1
                                                                
                                                                print("Second Con")
                                                                
                                                            elif(squ[Final+1] == "True"):
                                                    
                                                                cv2.imshow("Square 13" ,sq[Final+1])
                                                                
                                                                Final = Final+1
                                                                
                                                                print("Third Con")
                                                        
                                                        elif(squ[Final-1] == "True"):
                                                
                                                            cv2.imshow("Square 12" ,sq[Final-1])
                                                            
                                                            Final = Final-1
                                                            
                                                            print("Second Con")
                                                            
                                                        elif(squ[Final+1] == "True"):
                                                
                                                            cv2.imshow("Square 12" ,sq[Final+1])
                                                            
                                                            Final = Final+1
                                                            
                                                            print("Third Con")
                                                        
                                                    elif(squ[Final+1] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final+1])
                                                        
                                                        Final = Final+1
                                                        
                                                        print("Third Con")
                                                
                                                elif(squ[Final-1] == "True"):
                                        
                                                    cv2.imshow("Square 10" ,sq[Final-1])
                                                    
                                                    Final = Final-1
                                                    
                                                    print("Second Con")
                                                    
                                                elif(squ[Final+1] == "True"):
                                        
                                                    cv2.imshow("Square 10" ,sq[Final+1])
                                                    
                                                    Final = Final+1
                                                    
                                                    print("Third Con")
                                            
                                            elif(squ[Final-1] == "True"):
                                    
                                                cv2.imshow("Square 9" ,sq[Final-1])
                                                
                                                Final = Final-1
                                                
                                                print("Second Con")
                                            
                                        elif(squ[Final+1] == "True"):
                                
                                            cv2.imshow("Square 8" ,sq[Final+1])
                                            
                                            Final = Final+1
                                            
                                            print("Third Con")
                                    
                                    elif(squ[Final-1] == "True"):
                            
                                        cv2.imshow("Square 7" ,sq[Final-1])
                                        
                                        Final = Final-1
                                        
                                        print("Second Con")
                                        
                                    elif(squ[Final+1] == "True"):
                            
                                        cv2.imshow("Square 7" ,sq[Final+1])
                                        
                                        Final = Final+1
                                        
                                        print("Third Con")
                                
                                elif(squ[Final-1] == "True"):
                        
                                    cv2.imshow("Square 6" ,sq[Final-1])
                                    
                                    Final = Final-1
                                    
                                    print("Second Con")
                                    
                                
                            elif(squ[Final+1] == "True"):
                    
                                cv2.imshow("Square 5" ,sq[Final+1])
                                
                                Final = Final+1
                                
                                print("Third Con")
                        
                        elif(squ[Final-1] == "True"):
                    
                            cv2.imshow("Square 4" ,sq[Final-1])
                            
                            Final = Final-1
                            
                            print("Second Con")
                            
                        elif(squ[Final+1] == "True"):
                    
                            cv2.imshow("Square 4" ,sq[Final+1])
                            
                            Final = Final+1
                            
                            print("Third Con")
                        
                    elif(squ[Final-1] == "True"):
                    
                        cv2.imshow("Square 3" ,sq[Final-1])
                        
                        Final = Final-1
                        
                        print("Second Con")
                
                elif(squ[Final+1] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Final+1])
                    
                    Final = Final+1
                    
                    print("Second Con")
                
                elif(squ[Final+6] == "True"):
                    
                    cv2.putText(sq[Final+6],'Square 2',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                    cv2.imshow("Square 2" ,sq[Final+6])
                    
                    Final = Final+6
                    
                    print("Third Con")
                    
                    if(squ[Final+6] == "True"):
                        
                        cv2.putText(sq[Final+6],'Square 3',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                        cv2.imshow("Square 3" ,sq[Final+6])
                        
                        Final = Final+6
                        
                        print("First Con")
                        
                        if(squ[Final+6] == "True"):
                            
                            cv2.putText(sq[Final+6],'Square 4',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                            cv2.imshow("Square 4" ,sq[Final+6])
                            
                            Final = Final+6
                            
                            print("First Con")
                            
                            if(squ[Final+6] == "True"):
                                
                                cv2.putText(sq[Final+6],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final+6])
                                
                                Final = Final+6
                                
                                print("First Con")
                            
                            elif(squ[Final-1] == "True"):
                                
                                cv2.putText(sq[Final-1],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final-1])
                                
                                Final = Final-1
                                
                                print("Second Con")
                                
                                if(squ[Final-6] == "True"):
                                    
                                    cv2.putText(sq[Final-6],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                    cv2.imshow("Square 6" ,sq[Final-6])
                                    
                                    Final = Final-6
                                    
                                    print("First Con")
                                    
                                    if(squ[Final-6] == "True"):
                                        
                                        cv2.putText(sq[Final-6],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                        cv2.imshow("Square 7" ,sq[Final-6])
                                        
                                        Final = Final-6
                                        
                                        print("First Con")
                                        
                                        if(squ[Final-6] == "True"):
                                            
                                            cv2.putText(sq[Final-6],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                            cv2.imshow("Square 8" ,sq[Final-6])
                                            
                                            Final = Final-6
                                            
                                            print("First Con")
                                        
                                        elif(squ[Final-1] == "True"):
                                            
                                            cv2.putText(sq[Final-1],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                
                                            cv2.imshow("Square 8" ,sq[Final-1])
                                            
                                            Final = Final-1
                                            
                                            print("Second Con")
                                            
                                            if(squ[Final+6] == "True"):
                                                
                                                cv2.putText(sq[Final+6],'Square 9',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                cv2.imshow("Square 9" ,sq[Final+6])
                                                
                                                Final = Final+6
                                                
                                                print("First Con")
                                                
                                                if(squ[Final+6] == "True"):
                                                    
                                                    cv2.putText(sq[Final+6],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                    cv2.imshow("Square 10" ,sq[Final+6])
                                                    
                                                    Final = Final+6
                                                    
                                                    print("First Con")
                                                    
                                                    if(squ[Final+6] == "True"):
                                                        
                                                        cv2.putText(sq[Final+6],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                        cv2.imshow("Square 11" ,sq[Final+6])
                                                        
                                                        Final = Final+6
                                                        
                                                        print("First Con")
                                                    
                                                    elif(squ[Final-1] == "True"):
                                                        
                                                        cv2.putText(sq[Final-1],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-1])
                                                        
                                                        Final = Final-1
                                                        
                                                        print("Second Con")
                                                        
                                                        if(squ[Final-6] == "True"):
                                                            
                                                            cv2.putText(sq[Final-6],'Square 12',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                            cv2.imshow("Square 12" ,sq[Final-6])
                                                            
                                                            Final = Final-6
                                                            
                                                            print("First Con")
                                                            
                                                            if(squ[Final-6] == "True"):
                                                                
                                                                cv2.putText(sq[Final-6],'Square 13',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                                cv2.imshow("Square 13" ,sq[Final-6])
                                                                
                                                                Final = Final-6
                                                                
                                                                print("First Con")
                                                                
                                                                if(squ[Final-6] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-6],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                                                    cv2.imshow("Square 14" ,sq[Final-6])
                                                                    
                                                                    Final = Final-6
                                                                    
                                                                    print("First Con")
                                                                
                                                                elif(squ[Final-1] == "True"):
                                                        
                                                                    cv2.imshow("Square 14" ,sq[Final-1])
                                                                    
                                                                    Final = Final-1
                                                                    
                                                                    print("Second Con")
                                                                    
                                                                elif(squ[Final+1] == "True"):
                                                        
                                                                    cv2.imshow("Square 14" ,sq[Final+1])
                                                                    
                                                                    Final = Final+1
                                                                    
                                                                    print("Third Con")
                                                            
                                                            elif(squ[Final-1] == "True"):
                                                    
                                                                cv2.imshow("Square 13" ,sq[Final-1])
                                                                
                                                                Final = Final-1
                                                                
                                                                print("Second Con")
                                                                
                                                            elif(squ[Final+1] == "True"):
                                                    
                                                                cv2.imshow("Square 13" ,sq[Final+1])
                                                                
                                                                Final = Final+1
                                                                
                                                                print("Third Con")
                                                        
                                                        elif(squ[Final-1] == "True"):
                                                
                                                            cv2.imshow("Square 12" ,sq[Final-1])
                                                            
                                                            Final = Final-1
                                                            
                                                            print("Second Con")
                                                            
                                                        elif(squ[Final+1] == "True"):
                                                
                                                            cv2.imshow("Square 12" ,sq[Final+1])
                                                            
                                                            Final = Final+1
                                                            
                                                            print("Third Con")
                                                        
                                                    elif(squ[Final+1] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final+1])
                                                        
                                                        Final = Final+1
                                                        
                                                        print("Third Con")
                                                
                                                elif(squ[Final-1] == "True"):
                                        
                                                    cv2.imshow("Square 10" ,sq[Final-1])
                                                    
                                                    Final = Final-1
                                                    
                                                    print("Second Con")
                                                    
                                                elif(squ[Final+1] == "True"):
                                        
                                                    cv2.imshow("Square 10" ,sq[Final+1])
                                                    
                                                    Final = Final+1
                                                    
                                                    print("Third Con")
                                            
                                            elif(squ[Final-1] == "True"):
                                    
                                                cv2.imshow("Square 9" ,sq[Final-1])
                                                
                                                Final = Final-1
                                                
                                                print("Second Con")
                                            
                                        elif(squ[Final+1] == "True"):
                                
                                            cv2.imshow("Square 8" ,sq[Final+1])
                                            
                                            Final = Final+1
                                            
                                            print("Third Con")
                                    
                                    elif(squ[Final-1] == "True"):
                            
                                        cv2.imshow("Square 7" ,sq[Final-1])
                                        
                                        Final = Final-1
                                        
                                        print("Second Con")
                                        
                                    elif(squ[Final+1] == "True"):
                            
                                        cv2.imshow("Square 7" ,sq[Final+1])
                                        
                                        Final = Final+1
                                        
                                        print("Third Con")
                                
                                elif(squ[Final-1] == "True"):
                        
                                    cv2.imshow("Square 6" ,sq[Final-1])
                                    
                                    Final = Final-1
                                    
                                    print("Second Con")
                                    
                                
                            elif(squ[Final+1] == "True"):
                    
                                cv2.imshow("Square 5" ,sq[Final+1])
                                
                                Final = Final+1
                                
                                print("Third Con")
                        
                        elif(squ[Final-1] == "True"):
                    
                            cv2.imshow("Square 4" ,sq[Final-1])
                            
                            Final = Final-1
                            
                            print("Second Con")
                            
                        elif(squ[Final+1] == "True"):
                    
                            cv2.imshow("Square 4" ,sq[Final+1])
                            
                            Final = Final+1
                            
                            print("Third Con")
                        
                    elif(squ[Final-1] == "True"):
                    
                        cv2.imshow("Square 3" ,sq[Final-1])
                        
                        Final = Final-1
                        
                        print("Second Con")
                        
                    elif(squ[Final+1] == "True"):
                    
                        cv2.imshow("Square 3" ,sq[Final+1])
                        
                        Final = Final+1
                        
                        print("Third Con")

    elif (blue == "H"):

        if(squ[Final] == "True"):
            
            if(Final > 17):
                
                if(squ[Final-1] == "True"):
                    
                    cv2.putText(sq[Final-1],'Square 12',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                    cv2.imshow("Square 2" ,sq[Final-1])
                    
                    Final = Final-1
                    
                    print("First Con")
                    
                    if(squ[Final-1] == "True"):
                        
                        cv2.putText(sq[Final-1],'Square 3',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                        cv2.imshow("Square 3" ,sq[Final-1])
                        
                        Final = Final-1
                        
                        print("First Con")
                        
                        if(squ[Final-1] == "True"):
                            
                            cv2.putText(sq[Final-1],'Square 4',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                            
                            cv2.imshow("Square 4" ,sq[Final-1])
                            
                            Final = Final-1
                            
                            print("First Con")
                            
                            if(squ[Final-1] == "True"):
                                
                                cv2.putText(sq[Final-1],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final-1])
                                
                                Final = Final-1
                                
                                print("First Con")
                                
                                if(squ[Final-1] == "True"):
                                    
                                    cv2.putText(sq[Final-1],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                    cv2.imshow("Square 6" ,sq[Final-1])
                                    
                                    Final = Final-1
                                    
                                    print("First Con")
                                
                                elif(squ[Final-6] == "True"):
                                    
                                    cv2.putText(sq[Final-6],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                    
                                    cv2.imshow("Square 6" ,sq[Final-6])
                                    
                                    Final = Final-6
                                    
                                    print("Third Con")
                                    
                                    if(squ[Final-1] == "True"):
                                        
                                        cv2.putText(sq[Final-1],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                        cv2.imshow("Square 7" ,sq[Final-1])
                                        
                                        Final = Final-1
                                        
                                        print("First Con")
                                    
                                    elif(squ[Final+1] == "True"):
                                        
                                        cv2.putText(sq[Final+1],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                        
                                        cv2.imshow("Square 7" ,sq[Final+1])
                                        
                                        Final = Final+1
                                        
                                        print("Second Con")
                                        
                                        if(squ[Final+1] == "True"):
                                            
                                            cv2.putText(sq[Final+1],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                            cv2.imshow("Square 8" ,sq[Final+1])
                                            
                                            Final = Final+1
                                            
                                            print("First Con")
                                            
                                            if(squ[Final+1] == "True"):
                                                
                                                cv2.putText(sq[Final+1],'Square 9',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                cv2.imshow("Square 9" ,sq[Final+1])
                                                
                                                Final = Final+1
                                                
                                                print("First Con")
                                                
                                                if(squ[Final+1] == "True"):
                                                    
                                                    cv2.putText(sq[Final+1],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                    cv2.imshow("Square 10" ,sq[Final+1])
                                                    
                                                    Final = Final+1
                                                    
                                                    print("First Con")
                                                    
                                                elif(squ[Final-6] == "True"):
                                                    
                                                    cv2.putText(sq[Final-6],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                    cv2.imshow("Square 10" ,sq[Final-6])
                                                    
                                                    Final = Final-6
                                                    
                                                    print("Second Con")
                                                    
                                                    if(squ[Final-1] == "True"):
                                                        
                                                        cv2.putText(sq[Final-1],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-1])
                                                        
                                                        Final = Final-1
                                                        
                                                        print("First Con")
                                                        
                                                        if(squ[Final-1] == "True"):
                                                            
                                                            cv2.putText(sq[Final-1],'Square 12',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                            cv2.imshow("Square 12" ,sq[Final-1])
                                                            
                                                            Final = Final-1
                                                            
                                                            print("First Con")
                                                            
                                                            if(squ[Final-1] == "True"):
                                                                
                                                                cv2.putText(sq[Final-1],'Square 13',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                                cv2.imshow("Square 13" ,sq[Final-1])
                                                                
                                                                Final = Final-1
                                                                
                                                                print("First Con")
                                                                
                                                                if(squ[Final-1] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-1],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                                    cv2.imshow("Square 14" ,sq[Final-1])
                                                                    
                                                                    Final = Final-1
                                                                    
                                                                    print("First Con")
                                                                    
                                                                elif(squ[Final-6] == "True"):
                                                    
                                                                    cv2.imshow("Square 14" ,sq[Final-6])
                                                    
                                                                    Final = Final-6
                                                    
                                                                    print("Second Con")
                                                                
                                                            elif(squ[Final-6] == "True"):
                                                
                                                                cv2.imshow("Square 13" ,sq[Final-6])
                                                
                                                                Final = Final-6
                                                
                                                                print("Second Con")
                                                            
                                                        elif(squ[Final-6] == "True"):
                                            
                                                            cv2.imshow("Square 12" ,sq[Final-6])
                                            
                                                            Final = Final-6
                                            
                                                            print("Second Con")
                                                        
                                                    elif(squ[Final+1] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final+1])
                                                        
                                                        Final = Final+1
                                                        
                                                        print("Second Con")
                                                        
                                                    elif(squ[Final-6] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-6])
                                                        
                                                        Final = Final-6
                                                        
                                                        print("Third Con")
                                                
                                            elif(squ[Final-6] == "True"):
                                            
                                                cv2.imshow("Square 9" ,sq[Final-6])
                                                
                                                Final = Final-6
                                                
                                                print("Second Con")
                                        
                                        elif(squ[Final-6] == "True"):
                                            
                                            cv2.imshow("Square 8" ,sq[Final-6])
                                            
                                            Final = Final-6
                                            
                                            print("Second Con")
                                    
                                    elif(squ[Final-6] == "True"):
                                        
                                        cv2.imshow("Square 7" ,sq[Final-6])
                                        
                                        Final = Final-6
                                        
                                        print("Third Con")
                            
                            elif(squ[Final+1] == "True"):
                                
                                cv2.imshow("Square 4" ,sq[Final+1])
                                
                                Final = Final+1
                                
                                print("Second Con")
                            
                            elif(squ[Final-6] == "True"):
                                
                                cv2.imshow("Square 4" ,sq[Final-6])
                                
                                Final = Final-6
                                
                                print("Third Con")
                        
                        elif(squ[Final+1] == "True"):
                            
                            cv2.imshow("Square 3" ,sq[Final+1])
                            
                            Final = Final+1
                            
                            print("Second Con")
                        
                        elif(squ[Final-6] == "True"):
                            
                            cv2.imshow("Square 3" ,sq[Final-6])
                            
                            Final = Final-6
                            
                            print("Third Con")
                    
                    elif(squ[Final+1] == "True"):
                        
                        cv2.imshow("Square 3" ,sq[Final+1])
                        
                        Final = Final+1
                        
                        print("Second Con")
                    
                    elif(squ[Final-1] == "True"):
                        
                        cv2.imshow("Square 3" ,sq[Final-6])
                        
                        Final = Final-1
                        
                        print("Third Con")
                
                elif(squ[Final+1] == "True"):
                    
                    cv2.putText(sq[Final+1],'Square 2',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                    cv2.imshow("Square 2" ,sq[Fianl+1])
                    
                    Final = Final +1
                    
                    print("Second Con")
                
                elif(squ[Final-6] == "True"):
                    
                    cv2.putText(sq[Final-6],'Square 2',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                    cv2.imshow("Square 2" ,sq[Final-6])
                    
                    Final = Final - 6
                    
                    print("Third Con")
                    
                    if(squ[Final-1] == "True"):
                        
                        cv2.putText(sq[Final-1],'Square 3',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                        cv2.imshow("Square 3" ,sq[Final-1])
                        
                        Final = Final-1
                        
                        print("First Con")
                        
                        if(squ[Final-1] == "True"):
                            
                            cv2.putText(sq[Final-1],'Square 4',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                            
                            cv2.imshow("Square 4" ,sq[Final-1])
                            
                            Final = Final-1
                            
                            print("First Con")
                            
                            if(squ[Final-1] == "True"):
                                
                                cv2.putText(sq[Final-1],'Square 5',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                cv2.imshow("Square 5" ,sq[Final-1])
                                
                                Final = Final-1
                                
                                print("First Con")
                                
                                if(squ[Final-1] == "True"):
                                    
                                    cv2.putText(sq[Final-1],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                    cv2.imshow("Square 6" ,sq[Final-1])
                                    
                                    Final = Final-1
                                    
                                    print("First Con")
                                
                                elif(squ[Final-6] == "True"):
                                    
                                    cv2.putText(sq[Final-6],'Square 6',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                    
                                    cv2.imshow("Square 6" ,sq[Final-6])
                                    
                                    Final = Final-6
                                    
                                    print("Third Con")
                                    
                                    if(squ[Final-1] == "True"):
                                        
                                        cv2.putText(sq[Final-1],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                    
                                        cv2.imshow("Square 7" ,sq[Final-1])
                                        
                                        Final = Final-1
                                        
                                        print("First Con")
                                    
                                    elif(squ[Final+1] == "True"):
                                        
                                        cv2.putText(sq[Final+1],'Square 7',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                        
                                        cv2.imshow("Square 7" ,sq[Final+1])
                                        
                                        Final = Final+1
                                        
                                        print("Second Con")
                                        
                                        if(squ[Final+1] == "True"):
                                            
                                            cv2.putText(sq[Final+1],'Square 8',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                            cv2.imshow("Square 8" ,sq[Final+1])
                                            
                                            Final = Final+1
                                            
                                            print("First Con")
                                            
                                            if(squ[Final+1] == "True"):
                                                                                  
                                                cv2.putText(sq[Final+1],'Square 9',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                cv2.imshow("Square 9" ,sq[Final+1])
                                                
                                                Final = Final+1
                                                
                                                print("First Con")
                                                
                                                if(squ[Final+1] == "True"):
                                                    
                                                    cv2.putText(sq[Final+1],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                    cv2.imshow("Square 10" ,sq[Final+1])
                                                    
                                                    Final = Final+1
                                                    
                                                    print("First Con")
                                                    
                                                elif(squ[Final-6] == "True"):
                                                    
                                                    cv2.putText(sq[Final-6],'Square 10',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                    cv2.imshow("Square 10" ,sq[Final-6])
                                                    
                                                    Final = Final-6
                                                    
                                                    print("Second Con")
                                                    
                                                    if(squ[Final-1] == "True"):
                                                        
                                                        cv2.putText(sq[Final-1],'Square 11',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-1])
                                                        
                                                        Final = Final-1
                                                        
                                                        print("First Con")
                                                        
                                                        if(squ[Final-1] == "True"):
                                                            
                                                            cv2.putText(sq[Final-1],'Square 12',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                            cv2.imshow("Square 12" ,sq[Final-1])
                                                            
                                                            Final = Final-1
                                                            
                                                            print("First Con")
                                                            
                                                            if(squ[Final-1] == "True"):
                                                                
                                                                cv2.putText(sq[Final-1],'Square 13',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                                cv2.imshow("Square 13" ,sq[Final-1])
                                                                
                                                                Final = Final-1
                                                                
                                                                print("First Con")
                                                                
                                                                if(squ[Final-1] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-1],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                            
                                                                    cv2.imshow("Square 14" ,sq[Final-1])
                                                                    
                                                                    Final = Final-1
                                                                    
                                                                    print("First Con")
                                                                    
                                                                elif(squ[Final-6] == "True"):
                                                                    
                                                                    cv2.putText(sq[Final-6],'Square 14',(100,180), font, 1, (100,255,155), 2, cv2.LINE_AA)
                                                    
                                                                    cv2.imshow("Square 14" ,sq[Final-6])
                                                    
                                                                    Final = Final-6
                                                    
                                                                    print("Second Con")
                                                                
                                                            elif(squ[Final-6] == "True"):
                                                
                                                                cv2.imshow("Square 13" ,sq[Final-6])
                                                
                                                                Final = Final-6
                                                
                                                                print("Second Con")
                                                            
                                                        elif(squ[Final-6] == "True"):
                                            
                                                            cv2.imshow("Square 12" ,sq[Final-6])
                                            
                                                            Final = Final-6
                                            
                                                            print("Second Con")
                                                        
                                                    elif(squ[Final+1] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final+1])
                                                        
                                                        Final = Final+1
                                                        
                                                        print("Second Con")
                                                        
                                                    elif(squ[Final-6] == "True"):
                                            
                                                        cv2.imshow("Square 11" ,sq[Final-6])
                                                        
                                                        Final = Final-6
                                                        
                                                        print("Third Con")
                                                
                                            elif(squ[Final-6] == "True"):
                                            
                                                cv2.imshow("Square 9" ,sq[Final-6])
                                                
                                                Final = Final-6
                                                
                                                print("Second Con")
                                        
                                        elif(squ[Final-6] == "True"):
                                            
                                            cv2.imshow("Square 8" ,sq[Final-6])
                                            
                                            Final = Final-6
                                            
                                            print("Second Con")
                                    
                                    elif(squ[Final-6] == "True"):
                                        
                                        cv2.imshow("Square 7" ,sq[Final-6])
                                        
                                        Final = Final-6
                                        
                                        print("Third Con")
                            
                            elif(squ[Final+1] == "True"):
                                
                                cv2.imshow("Square 4" ,sq[Final+1])
                                
                                Final = Final+1
                                
                                print("Second Con")
                            
                            elif(squ[Final-6] == "True"):
                                
                                cv2.imshow("Square 4" ,sq[Final-6])
                                
                                Final = Final-6
                                
                                print("Third Con")
                        
                        elif(squ[Final+1] == "True"):
                            
                            cv2.imshow("Square 3" ,sq[Final+1])
                            
                            Final = Final+1
                            
                            print("Second Con")
                        
                        elif(squ[Final-6] == "True"):
                            
                            cv2.imshow("Square 3" ,sq[Final-6])
                            
                            Final = Final-6
                            
                            print("Third Con")
                    
                    elif(squ[Final+1] == "True"):
                        
                        cv2.imshow("Square 3" ,sq[Final+1])
                        
                        Final = Final+1
                        
                        print("Second Con")
                    
                    elif(squ[Final-1] == "True"):
                        
                        cv2.imshow("Square 3" ,sq[Final-6])
                        
                        Final = Final-1
                        
                        print("Third Con")
                     
            elif(Final < 17):
                
                if(squ[Final-1] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Fianl-1])
                    
                    print("First Con")
                
                elif(squ[Final+1] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Fianl+1])
                    
                    print("Second Con")
                
                elif(squ[Final+6] == "True"):
                    
                    cv2.imshow("Square 2" ,sq[Final+6])
                    
                    print("Third Con")
                    
    def concat_vh(list_2d):
        
        return cv2.vconcat([cv2.hconcat(list_h) 
                            for list_h in list_2d])

    img_tile = concat_vh([[sq[0], sq[1], sq[2], sq[3], sq[4], sq[5]],
                          [sq[6], sq[7], sq[8], sq[9], sq[10], sq[11]],
                          [sq[12], sq[13], sq[14], sq[15], sq[16], sq[17]],
                          [sq[18], sq[19], sq[20], sq[21], sq[22], sq[23]],
                          [sq[24], sq[25], sq[26], sq[27], sq[28], sq[29]]])

    cv2.imshow("Final", img_tile)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    main()