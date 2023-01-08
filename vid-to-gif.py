import ffmpeg
import random

# Set the input video file
input_video = 'input.mp4'

# Set the output GIF file prefix
output_gif_prefix = 'gif'

# Set the duration of each GIF in seconds
gif_duration = 5

# Set the number of GIFs to generate
num_gifs = 6

# Create a list to store the start times of the GIFs
gif_start_times = []

# Generate random start times for the GIFs
for i in range(num_gifs):
    gif_start_times.append(random.randint(0, 60 - gif_duration))

# Sort the start times
gif_start_times.sort()

# Create the GIFs
for i, start_time in enumerate(gif_start_times):
    # Set the output GIF file path
    output_gif = '{}_{}.gif'.format(output_gif_prefix, i)

    # Use ffmpeg to cut and convert the video to GIF
    (
        ffmpeg
        .input(input_video)
        .filter('trim', start=start_time, duration=gif_duration)
        .output(output_gif, vframes=100, loop=0)
        .run()
    )

print('GIF creation complete!')
