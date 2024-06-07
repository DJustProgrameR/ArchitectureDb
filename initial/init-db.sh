#!/bin/bash

for file in /migrations/*; do
    filename=$(basename "$file")
    version=${filename:1:14}
    if [[ "$version" -gt $LAST_MIGRATION_VERSION ]]; then
        echo "Stopping migration at version $version"
        break
    fi
    echo "Executing migration $version"
    if [[ $file == *.sql ]]; then
      psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$file"
    else
          bash $file
    fi
done