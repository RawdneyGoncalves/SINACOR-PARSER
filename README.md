## Project Structure

The project has the following directory structure:

- `src/`: The main source code directory.
  - `__init__.py`
  - `app.py`: The main application file.
  - `controller/`: Contains the controllers for handling business logic.
    - `__init__.py`
    - `main_controller.py`: Main controller for the project.
  - `router/`: Handles routing and API endpoints.
    - `__init__.py`
    - `main_router.py`: Main router for the project.
  - `views/`: Manages user interfaces and templates.
    - `__init__.py`
    - `main_view.py`: Main view for the project.

- `venv/`: The virtual environment folder.
  - This directory contains the Python virtual environment where project dependencies are isolated.

- `requirements.txt`: Lists all project dependencies.

- `run.py`: The script to run the application.


+-------------------------+         +-------------------------+         +-------------------------+
|    Banco de Dados      |         |   Fila de Tarefas       |         |     Processador         |
+-------------------------+         +-------------------------+         +-------------------------+
| - get_base64_data()    |         | - enqueue(pdf_data)     |         | - convert_pdf_to_data() |
| - save_pdf_data(data)  |         | - dequeue()             |         | - send_data_as_json()   |
| - register_callback()  |         |                         |         |                         |
+-------------------------+         +-------------------------+         +-------------------------+
          |                               |                               |
          |                               |                               |
          v                               v                               v
+-------------------------+         +-------------------------+         +-------------------------+
|         src/           |         |         src/           |         |         src/           |
+-------------------------+         +-------------------------+         +-------------------------+
| - __init__.py          |         | - __init__.py          |         | - __init__.py          |
| - app.py:             |         | - app.py:             |         | - app.py:             |
|   The main application |         |   The main application |         |   The main application |
| - controller/         |         | - router/              |         | - controller/         |
|   - __init__.py       |         |   - __init__.py       |         |   - __init__.py       |
|   - main_controller.py|         |   - main_router.py     |         |   - main_controller.py|
|     Main controller    |         |     Main router        |         |     Main controller    |
| - router/             |         | - views/               |         | - router/             |
|   - __init__.py       |         |   - __init__.py       |         |   - __init__.py       |
|   - main_router.py    |         |   - main_view.py       |         |   - main_router.py    |
|     Main router        |         |     Main view          |         |     Main router        |
| - views/              |         | - venv/                |         | - views/              |
|   - __init__.py       |         | - requirements.txt     |         |   - __init__.py       |
|   - main_view.py      |         |                         |         |   - main_view.py      |
|     Main view          |         |                         |         |     Main view          |
+-------------------------+         +-------------------------+         +-------------------------+
