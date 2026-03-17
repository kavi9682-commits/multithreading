import threading
import time

def downloads(file_name,duration):
    print("Start download:",file_name)
    time.sleep(duration)
    print("Completed download:",file_name)
    
t1=threading.Thread(target=downloads,args=("file1.pdf",1))
t2=threading.Thread(target=downloads,args=("video.mp4",2))
t3=threading.Thread(target=downloads,args=("audio.mp3",4))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All downloads completed")
