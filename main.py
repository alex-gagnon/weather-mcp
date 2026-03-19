import subprocess
import sys
import os

def main():
    client_path = os.path.join(os.path.dirname(__file__), "src", "clients", "client.py")
    server_path = os.path.join(os.path.dirname(__file__), "src", "server", "weather.py")

    subprocess.run([sys.executable, client_path, server_path])

if __name__ == "__main__":
    main()
