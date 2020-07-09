ffmpeg -i input.mp3 -f segment -segment_time 9 -c copy out%03d.mp3

