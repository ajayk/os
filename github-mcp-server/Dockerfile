FROM golang:1.21-alpine AS builder

WORKDIR /app

# Clone the repository
RUN apk add --no-cache git && \
    git clone https://github.com/github/github-mcp-server.git .

# Build the application
WORKDIR /app/cmd/github-mcp-server
RUN go build -o github-mcp-server

# Create a minimal runtime image
FROM alpine:3.19

# Install ca-certificates for HTTPS connections
RUN apk add --no-cache ca-certificates

# Copy the binary from the builder stage
COPY --from=builder /app/cmd/github-mcp-server/github-mcp-server /usr/local/bin/github-mcp-server

# Create a directory for the config file
RUN mkdir -p /etc/github-mcp-server

# Create an example config file
RUN echo '{\n  "TOOL_ADD_ISSUE_COMMENT_DESCRIPTION": "Add a comment to an existing issue",\n  "TOOL_CREATE_BRANCH_DESCRIPTION": "Create a new branch in a GitHub repository"\n}' > /etc/github-mcp-server/config.json.example

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/github-mcp-server"]

# Default command
CMD ["stdio"]
