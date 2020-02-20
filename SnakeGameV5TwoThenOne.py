import math
import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os, shutil


def ask():
    print("Enter dimensions:")
    print("Example: 4x3")
    dimensions = input("Input:")
    return int(dimensions[:dimensions.find("x")]), int(dimensions[dimensions.find("x")+1:])

def upHelper(i,arr,board,canEven,before,counter):
    arr=oddUp(i,arr,board,canEven)
    board=updateBoard(arr,board)
    if len(arr)>before:
        counter = counter + "a"
        plt.matshow(board)
        plt.savefig('results/plot'+str(counter))
        #plt.show()
        return counter, True
    else:
        return counter, False

def rightHelper(i,arr,board,canEven,before,counter):
    arr=oddRight(i,arr,board,canEven)
    board=updateBoard(arr,board)
    if len(arr)>before:
        counter = counter + "a"
        plt.matshow(board)
        plt.savefig('results/plot'+str(counter))
        #plt.show()
        return counter, True
    else:
        return counter, False
    
def downHelper(i,arr,board,canEven,before,counter):
    arr=oddDown(i,arr,board,canEven)
    board=updateBoard(arr,board)
    if len(arr)>before:
        counter = counter + "a"
        plt.matshow(board)
        plt.savefig('results/plot'+str(counter))
        #plt.show()
        return counter, True
    else:
        return counter, False
    
def leftHelper(i,arr,board,canEven,before,counter):
    arr=oddLeft(i,arr,board,canEven)
    board=updateBoard(arr,board)
    if len(arr)>before:
        counter = counter + "a"
        plt.matshow(board)
        plt.savefig('results/plot'+str(counter))
        #plt.show()
        return counter, True
    else:
        return counter, False
    
def Ham():
    rows,cols = ask()
    dimType = 0
    #evenByEven evenByOdd OddbyEven OddByOdd
    if rows%2==0 and cols%2==0:
        dimType = 0
    if rows%2==0 and cols%2:
        dimType = 1
    elif rows%2 and cols%2==0:
        dimType = 2
    else:
        dimType = 3
        
    probArr = []
    #print('probArr:',probArr)
    board = np.zeros((rows,cols))
    a=rows//2-1
    b=cols//2-1
    arr = [[a,b],[a,b+1],[a+1,b+1],[a+1,b]]
    board=updateBoard(arr,board)
    notFilled = True
    #counter used to name files a, aa, aaa...
    counter = "a"
    dirArr = [0,1,2,3]
    tempDir = dirArr[:]
    plt.matshow(board)
    plt.savefig('results/plot'+str(counter))
    
    canEven = True
    while notFilled:
        before = len(arr)
        #--------
        for i in range(len(arr)):
            if dimType == 2:
                counter,testBreak = upHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                counter, testBreak = rightHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                counter, testBreak = leftHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                if not canEven:
                    counter, testBreak = downHelper(i,arr,board,canEven,before,counter)
                    if testBreak:
                        break
            else:
                counter,testBreak = upHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                counter, testBreak = rightHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                counter, testBreak = downHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
                counter, testBreak = leftHelper(i,arr,board,canEven,before,counter)
                if testBreak:
                    break
            
        if canEven and before==len(arr):
            canEven = False
                
        if 0 not in board:
            notFilled = False
        
        if len(arr)==before:
            choose2 = False
def updateBoard(arr,board):
    for i in range(len(arr)):
        board[arr[i][0]][arr[i][1]]=0.05*(i+1)
    return board
#oddUp attempts to insert up
def oddUp(i,arr,board,canEven):
    #print('---------------------------up')
    first = arr[i]
    if i+1<len(arr): #test at arr[i+1]
        second=arr[i+1]
    else:
        second = arr[0]
    zeroCounter = 0
    while ((first[0]-zeroCounter-1>=0 and board[first[0]-zeroCounter-1][first[1]]==0)and(second[0]-zeroCounter-1>=0 and board[second[0]-zeroCounter-1][second[1]]==0)): #checks spaces in up
        zeroCounter = zeroCounter + 1
    if canEven:
        if zeroCounter>=2:
            arr.insert(i+1,[first[0]-1,first[1]])
            arr.insert(i+2,[first[0]-2,first[1]])
            arr.insert(i+3,[second[0]-2,second[1]])
            arr.insert(i+4,[second[0]-1,second[1]])
            #print('first:',first)
            #print('second:',second)
            #print('up')
    elif zeroCounter>0:
        arr.insert(i+1,[first[0]-1,first[1]])
        arr.insert(i+2,[second[0]-1,second[1]])
        #print('first:',first)
        #print('second:',second)
        #print('up-else')
    #print('---------------------------up')
    return arr
#oddRight attempts to insert right
def oddRight(i,arr,board,canEven):
    #print('---------------------------right')
    #while loop counts open pixels to the right
    first = arr[i]
    if i+1<len(arr): #test at arr[i+1]
        second=arr[i+1]
    else:
        second = arr[0]
    zeroCounter = 0
    while ((first[1]+zeroCounter+1<len(board[0]) and board[first[0]][first[1]+zeroCounter+1]==0)and(second[1]+zeroCounter+1<len(board[0]) and board[second[0]][second[1]+zeroCounter+1]==0)): #checks spaces in right
        zeroCounter = zeroCounter + 1
    if canEven:
        if zeroCounter>=2:
            arr.insert(i+1,[first[0],first[1]+1])
            arr.insert(i+2,[first[0],first[1]+2])
            arr.insert(i+3,[second[0],second[1]+2])
            arr.insert(i+4,[second[0],second[1]+1])
            #print('first:',first)
            #print('second:',second)
            #print('right')
            
    elif zeroCounter>0:
        arr.insert(i+1,[first[0],first[1]+1])
        arr.insert(i+2,[second[0],second[1]+1])
        #print('first:',first)
        #print('second:',second)
        #print('right-else')

    #print('---------------------------right')
    return arr
#oddDown attempts to insert down
def oddDown(i,arr,board,canEven):
    #print('---------------------------down')
    zeroCounter = 0
    first = arr[i]
    if i+1<len(arr): #test at arr[i+1]
        second=arr[i+1]
    else:
        second = arr[0]
    while ((first[0]+zeroCounter+1<len(board) and board[first[0]+zeroCounter+1][first[1]]==0)and(second[0]+zeroCounter+1<len(board) and board[second[0]+zeroCounter+1][second[1]]==0)) : #checks spaces in down
        zeroCounter = zeroCounter + 1
    if canEven:
        if zeroCounter>=2:
            arr.insert(i+1,[first[0]+1,first[1]])
            arr.insert(i+2,[first[0]+2,first[1]])
            arr.insert(i+3,[second[0]+2,second[1]])
            arr.insert(i+4,[second[0]+1,second[1]])
            #print('first:',first)
            #print('second:',second)
            #print('down')
            
    elif zeroCounter>0:
        arr.insert(i+1,[first[0]+1,first[1]])
        arr.insert(i+2,[second[0]+1,second[1]])
        #print('first:',first)
        #print('second:',second)
        #print('down-else')
        
    #print('---------------------------down')
    return arr
#oddLeft attempts to insert left
def oddLeft(i,arr,board,canEven):
    #print('---------------------------left')
    zeroCounter = 0
    first = arr[i]
    if i+1<len(arr): #test at arr[i+1]
        second=arr[i+1]
    else:
        second = arr[0]
    while ((first[1]-zeroCounter-1>=0 and board[first[0]][first[1]-zeroCounter-1]==0)and(second[1]-zeroCounter-1>=0 and board[second[0]][second[1]-zeroCounter-1]==0)): #checks spaces in left
        zeroCounter = zeroCounter + 1
    if canEven:
        if zeroCounter>=2:
            arr.insert(i+1,[first[0],first[1]-1])
            arr.insert(i+2,[first[0],first[1]-2])
            arr.insert(i+3,[second[0],second[1]-2])
            arr.insert(i+4,[second[0],second[1]-1])
            #print('first:',first)
            #print('second:',second)
            #print('left')
            
    elif zeroCounter>0:
        arr.insert(i+1,[first[0],first[1]-1])
        arr.insert(i+2,[second[0],second[1]-1])
        #print('first:',first)
        #print('second:',second)
        #print('left-else')
        
    #print('---------------------------left')
    return arr

def clearFolder():
    folder = 'results'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
def makeVideo():
    image_folder = 'results'
    video_name = 'video.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
clearFolder()
Ham()
makeVideo()
#main()
