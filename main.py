from utils import read_video, save_video
from trackers import Tracker
import os

def main():
    #read video
    video_frames = read_video('C:/Users/Rick/OneDrive/Documenten/HBO-ICT HAN/Jaar 4/Minor DDM/Ind project/Input_video/08fd33_4.mp4')

    #initialize tracker
    tracker = Tracker('models/best.pt  ')

    #get object tracks
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs_tracks.pkl')


    # Draw output
    ## Drar object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    #Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')

if __name__=='__main__':
    main()


