#!/bin/bash
FILES=input/*
for f in $FILES
do
  filename="$(basename -- $f)"
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  ffmpeg -i $f  -vf fps=1/4  output/image_extract/$filename-%d.jpg
done

