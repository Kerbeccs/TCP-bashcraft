# manage.py
import os
import sys
from threading import Thread
import signal

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcp_project.settings')
    try:
        from django.core.management import execute_from_command_line
        from tcp_app.tcp_server import TCPServer
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

    # Create TCP server instance
    tcp_server = TCPServer(host='127.0.0.1', port=8080)
    
    def signal_handler(signum, frame):
        """Handle shutdown signals"""
        print("\nShutting down TCP server...")
        tcp_server.stop()
        sys.exit(0)

    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start TCP server in a separate thread
    tcp_thread = Thread(target=tcp_server.start, daemon=True)
    tcp_thread.start()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()