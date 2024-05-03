#!/bin/bash

# Directory containing the input videos
INPUT_DIR="input"
# Directory where the output videos will be saved
OUTPUT_DIR="outputs"

# Create the output directory if it does not exist
mkdir -p "$OUTPUT_DIR"

# Assume all videos have the same dimensions, so we get the dimensions from the first video
FIRST_VIDEO=$(ls $INPUT_DIR | head -n 1)

# Extract video height and width using ffprobe
VID_WIDTH=1080
VID_HEIGHT=1920

# Zoom factor as a percentage (e.g., 100 for no zoom, 50 for zoom in to 200% of original size)
ZOOM=120

# Position of the bottom of the crop area as a percentage (0 for bottom, 100 for top)
BOTTOM=60

# Calculate the size for cropping. Apply the zoom factor.
CROP_SIZE=$(( (VID_WIDTH < VID_HEIGHT ? VID_WIDTH : VID_HEIGHT) * 100 / ZOOM ))

# Calculate the y-offset for cropping based on the bottom parameter
Y_OFFSET=$(( (VID_HEIGHT - CROP_SIZE) * BOTTOM / 100 ))

# Loop through all .mov files in the input directory
for VID_FILE in "$INPUT_DIR"/*.mov; do
    # Extract the filename without the directory
    FILENAME=$(basename "$VID_FILE")
    # Output filename in the output directory
    OUTPUT_VID="$OUTPUT_DIR/$FILENAME"
    
    # Run ffmpeg to crop the video based on calculated size and y-offset, then output a square video
    ffmpeg -i "$VID_FILE" -vf "crop=${CROP_SIZE}:${CROP_SIZE}:0:${Y_OFFSET}" -c:a copy "$OUTPUT_VID"
done

echo "Batch processing complete. Cropped videos are in $OUTPUT_DIR."
