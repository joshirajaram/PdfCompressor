# PdfCompressor

Script to compress PDF answer scripts in given folder 

## Running a Python Script

To run the Python script, follow these steps:

1. **Navigate to the Script Directory:**

    ```bash
    cd path/to/script/directory
    ```
2. **Install requirements**

    ```bash
    python3 -m pip install -r requirements.txt
    ```
3. **Update parent folder path in configs.yaml**

    ```yaml
    SRC_ANSWER_SHEETS_FILE_PATH: '/path/to/src/directory'
    ```
4. **Generate fresh build if not already present**

    ```bash
    pyinstaller --onefile pdf_compressor.py
    ```
5. **Run the executable in the dist repo**
    ```bash
    ./dist/pdf_compressor
    ```
