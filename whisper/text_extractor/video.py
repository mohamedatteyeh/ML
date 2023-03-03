
from datetime import timedelta
import cv2
import numpy as np
import os

# A way to double the speed or extraction of vids

#https://github.com/bml1g12/benchmarking_video_reading_python/issues/1

#class video():
#    def __init__(self,frames):
#        self.frames = frames

def format_timedelta(td):
    results = str(td)
    try: 
        results,ms = results.split('.')
    except ValueError:
        return(results + ".00")
    
    ms = int(ms)
    ms = round(ms/1e4)

    return f"{results}.{ms:02}".replace(":","-")

def frames(c,fps):
    duration = c.get(cv2.CAP_PROP_FRAME_COUNT)/c.get(cv2.CAP_PROP_FPS)
    a = [i for i in np.arange(0,duration,1/fps)]
    return(a)
        
def fps_data(video,sfps):
    filename, _ = os.path.splitext(video)  
    filename += '-opencv'

    if os.path.isdir != filename:
        os.mkdir(filename)

    c = cv2.VideoCapture(video)

    fps = c.get(cv2.CAP_PROP_FPS)
    
    saving_frames = min(fps,sfps)
    saving_frame_duration =  frames(c=c, fps = saving_frames)

    count = 0

    while True:
        is_read,frame = c.read()

        if not is_read:
            break

        frame_duration = count/fps

        try:
            closest_duration = saving_frame_duration[0]
        
        except IndexError:
            break
        
        if frame_duration >= closest_duration:

            frame_duration_formatted = format_timedelta(timedelta(seconds = frame_duration))
            cv2.imwrite(os.path.join(filename,f"frame{frame_duration_formatted}.jpg"),frame)

            try:
                saving_frame_duration.pop(0)
            except IndexError:
                pass
            
        count +=1


input_vid_shorts  = "extractsubs.mp4"
input_vid_crunchy = "crunchyroll.mp4"
input_vid_shorts = "shorts.mp4"


fps_data(input_vid_shorts,1)



