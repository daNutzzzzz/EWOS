from flask import Flask, request, jsonify
import csv
import paramiko

app = Flask(__name__)

REMOTE_HOST = 'remote_host_address'
SSH_PORT = 22
USERNAME = 'your_username'
PASSWORD = 'your_password'
REMOTE_FILE_PATH = '/path/to/remote/file.csv'

def fetch_remote_file():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(REMOTE_HOST, port=SSH_PORT, username=USERNAME, password=PASSWORD)
        ftp_client = ssh_client.open_sftp()
        remote_file = ftp_client.file(REMOTE_FILE_PATH, 'r')
        file_content = remote_file.read().decode('utf-8')
        ftp_client.close()
        ssh_client.close()
        return file_content
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/parse', methods=['POST'])
def parse_file():
    file_content = fetch_remote_file()
    if not file_content:
        return jsonify({'error': 'Failed to fetch remote file'}), 500

    try:
        data = []
        # Assume CSV format for simplicity
        csv_reader = csv.reader(file_content.splitlines())
        for row in csv_reader:
            data.append(row)
        return jsonify({'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
