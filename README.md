# PdfCompressor

Script to compress PDF answer scripts in given folder 

## Running a Python Script

To run the Python script, follow these steps:

1. **Navigate to the Script Directory:**

    ```bash
    cd path/to/script/directory
    ```
2. **Update parent folder path in configs.yaml**

    ```yaml
    SRC_ANSWER_SHEETS_FILE_PATH: '/path/to/src/directory'
    ```
3. **Generate fresh build if not already present**

    ```bash
    pyinstaller --onefile pdf_compressor.py
    ```
4. **Run the executable in the dist repo**
    ```bash
    ./dist/pdf_compressor
    ```
