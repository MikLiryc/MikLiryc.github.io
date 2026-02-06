#!/bin/bash
echo "Building site..."
bundle exec jekyll build

if [ $? -ne 0 ]; then
    echo "❌ Build failed. Press any key to exit."
    read
    exit 1
fi

echo "Starting local server..."
bundle exec jekyll serve

if [ $? -ne 0 ]; then
    echo "❌ Server failed to start. Press any key to exit."
    read
    exit 1
fi

read -p "Press any key to exit..."
