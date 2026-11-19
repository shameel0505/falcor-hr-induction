# -*- coding: utf-8 -*-
"""
Falcor HR Orientation - Master Broadcast Video Renderer & Concat Pipeline
Generates 1080p broadcast video synchronized to narration audio with high visual fidelity.
"""
import os
import json
import subprocess
import imageio_ffmpeg

def get_base_dir():
    # Detect if run from inside 'hr induction' or from parent workspace
    if os.path.exists('index.html') and os.path.exists('frames'):
        return os.path.abspath('.')
    elif os.path.exists('hr induction'):
        return os.path.abspath('hr induction')
    else:
        return os.path.dirname(os.path.abspath(__file__))

def main():
    hr_dir = get_base_dir()
    frames_dir = os.path.join(hr_dir, 'frames')
    audio_dir = os.path.join(hr_dir, 'audio')
    clips_dir = os.path.join(hr_dir, 'clips')
    os.makedirs(clips_dir, exist_ok=True)
    
    durations_path = os.path.join(hr_dir, 'audio_durations.json')
    with open(durations_path, 'r', encoding='utf-8') as f:
        durations = json.load(f)
        
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"Using FFmpeg: {ffmpeg}")
    print(f"Working Directory: {hr_dir}")
    
    total_slides = 21
    clip_files = []
    
    print("\n=== Rendering 21 Individual Slide Video Clips (1080p High Fidelity) ===")
    for i in range(1, total_slides + 1):
        pad_i = f"{i:02d}"
        frame_file = os.path.join(frames_dir, f"slide_{pad_i}.png")
        audio_file = os.path.join(audio_dir, f"slide_{pad_i}.mp3")
        clip_file = os.path.join(clips_dir, f"clip_{pad_i}.mp4")
        
        if not os.path.exists(frame_file):
            raise FileNotFoundError(f"Missing frame file: {frame_file}")
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Missing audio file: {audio_file}")
            
        dur = durations.get(str(i), 20.0)
        print(f"[{pad_i}/21] Rendering Slide {pad_i} ({dur:.2f}s) -> {clip_file}")
        
        # Scale to 1920:-1 (1080p) to avoid memory exhaustion on high-resolution stills
        cmd = [
            ffmpeg, '-y',
            '-loop', '1', '-i', frame_file,
            '-i', audio_file,
            '-vf', 'scale=1920:-1',
            '-c:v', 'libx264', '-tune', 'stillimage', '-preset', 'fast', '-crf', '17',
            '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
            '-pix_fmt', 'yuv420p',
            '-shortest',
            clip_file
        ]
        
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error rendering clip {pad_i}:", res.stderr)
            raise RuntimeError(f"FFmpeg failed on slide {pad_i}")
            
        clip_files.append(clip_file)
        
    print(f"\nAll {total_slides} clips rendered successfully.")
    
    # Create concat list
    concat_list_file = os.path.join(clips_dir, "concat_list.txt")
    with open(concat_list_file, 'w', encoding='utf-8') as f:
        for c in clip_files:
            norm_path = c.replace('\\', '/')
            f.write(f"file '{norm_path}'\n")
            
    master_video = os.path.join(hr_dir, "Falcor_HR_Orientation_Broadcast_Master.mp4")
    print(f"\n=== Concatenating into Master Broadcast: {master_video} ===")
    
    concat_cmd = [
        ffmpeg, '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', concat_list_file,
        '-c', 'copy',
        master_video
    ]
    
    res = subprocess.run(concat_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error during concatenation:", res.stderr)
        raise RuntimeError("FFmpeg concat failed")
        
    v_size = os.path.getsize(master_video)
    print(f"\n=======================================================")
    print(f"SUCCESS: Falcor HR Orientation Master Broadcast Generated!")
    print(f"Path: {master_video}")
    print(f"Size: {v_size / (1024*1024):.2f} MB ({v_size:,} bytes)")
    print(f"=======================================================\n")

if __name__ == '__main__':
    main()

