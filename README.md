# PdfCompressor

Script to compress PDF answer scripts in given folder 

## Running a Python Script

To run the Python script, follow these steps:

1. **Navigate to the Script Directory:**

    ```bash
    cd path/to/script/directory
    ```
2. **Install Python3 if not present**
    - For Windows: https://www.python.org/downloads/
    - For macOS: https://www.python.org/downloads/macos/
    - For Linux: sudo apt install python3.10
3. **Install requirements**

    ```bash
    python3 -m pip install -r requirements.txt
    ```
4. **Update parent folder path in configs.yaml**

    ```yaml
    SRC_ANSWER_SHEETS_FILE_PATH: '/path/to/src/directory'
    ```
5. **Generate fresh build if not already present**

    ```bash
    pyinstaller --distpath . --onefile pdf_compressor.py
    ```
6. **Run the executable in the repo**
    
    ```bash
    ./pdf_compressor
    ```
