# Use the smallest stable base image
FROM alpine:latest

# Install sqlite and clean up cache in one layer to keep it small
RUN apk add --no-cache sqlite

# Create a directory for your data
WORKDIR /data

# Run sqlite3 by default
# This allows you to pass a database filename as an argument
ENTRYPOINT ["sqlite3"]
