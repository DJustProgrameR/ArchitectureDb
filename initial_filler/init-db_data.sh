#!/bin/bash
echo "Started execution"
for file in /src/*.sh; do
    bash $file

    echo "Executed migration $file"
done



