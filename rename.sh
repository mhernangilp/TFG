#!/bin/bash

prefix="enron-2-"
for file in *; do
  mv "$file" "$prefix$file"
done
