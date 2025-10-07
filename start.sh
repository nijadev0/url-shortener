#!/bin/bash

# Quick start script for URL Shortener

echo "🚀 Starting URL Shortener..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build and start the containers
echo "📦 Building and starting containers..."
docker compose up --build -d

# Wait for the service to be ready
echo ""
echo "⏳ Waiting for service to be ready..."
sleep 5

echo ""
echo "✅ URL Shortener is running!"
echo ""
echo "📍 Access points:"
echo "   Admin Dashboard: http://localhost:8000/"
echo "   Login: admin / admin"
echo ""
echo "💡 To view logs: docker compose logs -f"
echo "🛑 To stop: docker compose down"
echo ""
