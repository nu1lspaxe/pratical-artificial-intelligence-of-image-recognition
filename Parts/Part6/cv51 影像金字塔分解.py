'''cv51: 影像金字塔分解'''
import cv2

def main():
    print("""
    Zoom In-Out demo
    ------------------
    * [i] -> Zoom [i]n
    * [o] -> Zoom [o]ut
    * [ESC] -> Close program
    """)
    
    filename = 'data/s.jpg'
    src = cv2.imread(filename)
    # Check if image is loaded fine
    if src is None:
        print ('無法讀取影像!')
        return -1
    
    while 1:
        rows, cols = src.shape[:2] #讀取影像高/寬        
        cv2.imshow('Pyramids Demo', src)
        
        k = cv2.waitKey(0)
        if k == 27: #按 Esc 離開
            break
            
        elif chr(k) == 'i': #上(放大)取樣
            src = cv2.pyrUp(src, dstsize=(2 * cols, 2 * rows))
            print ('** Zoom In: Image x 2')
            
        elif chr(k) == 'o': #下(縮小)取樣
            src = cv2.pyrDown(src, dstsize=(cols // 2, rows // 2))
            print ('** Zoom Out: Image / 2')
            
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()