from flask import Blueprint, jsonify

base64_router = Blueprint('base64', __name__)

@base64_router.route('/read_base64', methods=['GET'])
def read_base64_data():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT base64_data FROM sua_tabela WHERE id = 1")
    data_from_database = cursor.fetchone()[0]

    pdf_data = base64.b64decode(data_from_database)

    resource_folder = os.path.join(current_app.root_path, 'resources')

    if not os.path exists(resource_folder):
        os.makedirs(resource_folder)

    pdf_file_path = os.path.join(resource_folder, 'output.pdf')

    with open(pdf_file_path, 'wb') as pdf_file:
        pdf_file.write(pdf_data)

    conn.close()

    return jsonify({"message": "PDF salvo em resources", "pdf_file_path": pdf_file_path})
