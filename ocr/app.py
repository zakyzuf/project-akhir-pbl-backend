# Import modul yang diperlukan
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Definisikan variabel global
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Buat fungsi untuk memeriksa apakah ekstensi file diperbolehkan
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Buat objek Flask
app = Flask(__name__)

# Set konfigurasi untuk folder upload
app.config['UPLOAD_FOLDER'] = 'D:\Kuliah\project-akhir-pbl-backend\static'

# Buat rute untuk mengunggah media
@app.route('/media/upload', methods=['POST'])
def upload_media():
    # data = request.get_json()
    # token = data['token']

    # if token != '#@<!3c8e_237bc+v)ps;*&er':
    #     return jsonify({'error': 'unauthorized'}), 401
    # Cek apakah ada file yang diunggah
    if 'image' not in request.files:
        return jsonify({'error': 'media not provided'}), 400

    # Ambil file yang diunggah
    file = request.files['image']

    # Cek apakah file kosong
    if file.filename == '':
        return jsonify({'error': 'no file selected'}), 400

    # Cek apakah ekstensi file diperbolehkan
    if file and not allowed_file(file.filename):
        return jsonify({'error': 'file extension not allowed'}), 400

    # Amankan nama file
    filename = secure_filename(file.filename)

    # Simpan file ke folder upload
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Kembalikan respons sukses
    return jsonify({'msg': 'media uploaded successfully'})

# Jalankan server
if __name__ == '__main__':
    app.run(debug=True, port=5006)
