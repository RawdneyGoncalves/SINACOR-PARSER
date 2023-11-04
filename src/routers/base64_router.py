from flask import Blueprint, jsonify, send_file, current_app, Flask
import base64
import os
import mysql.connector
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import uuid

base64_router = Blueprint('base64', __name__)
app = Flask(__name__)

mysql_config = {
    'host': '108.179.193.84',
    'user': 'unite165_rawdney',
    'password': 'Rawdney@2023',
    'database': 'unite165_irpf_bolsa',
}


def convert_base64_to_pdf(base64_data):
    decoded_data = base64.b64decode(base64_data)
    random_filename = str(uuid.uuid4()) + ".pdf"
    pdf_file_path = os.path.join(current_app.root_path, 'resources', random_filename)
    
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, "Texto do PDF gerado a partir de base64")
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()

    with open(pdf_file_path, 'wb') as pdf_file:
        pdf_file.write(pdf)

    return pdf_file_path


@base64_router.route('/read_base64', methods=['GET'])
def read_base64_data():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute("select * from files f")
        data_from_database = cursor.fetchone()[0]
        conn.close()
        pdf_file_path = convert_base64_to_pdf(data_from_database)
      
        return jsonify({"message": "Base64 convertido para PDF", "pdf_file_path": pdf_file_path})
    except Exception as e:
        return jsonify({"error": str(e)})


@base64_router.route('/get_pdf', methods=['GET'])
def get_pdf():
    pdf_file_path = os.path.join(current_app.root_path, 'resources', 'output.pdf')
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.register_blueprint(base64_router, url_prefix='/base64')
    app.run()
