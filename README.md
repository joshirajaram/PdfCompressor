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
    python -m pip install -r requirements.txt
    ```
    ### for some systems we might need to use python3 explicitly
    ```bash
    python3 -m pip install -r requirements.txt
    ```
4. **Update parent folder path and reduction factor in configs.yaml**

    ```yaml
    SRC_ANSWER_SHEETS_FILE_PATH: '/path/to/src/directory'
    IMAGE_QUALITY_REDUCTION_FACTOR: 10 #default is 10, can change as per requirement
    ```
5. **Generate fresh build if not already present**

    ```bash
    pyinstaller --distpath . --onefile pdf_compressor.py
    ```
6. **Run the executable in the repo**
    
    ```bash
    $ ./pdf_compressor  #for *nix based systems
    > pdf_compressor    #for windows systems
    ```
7. **In case executable is throwing exception, please run using the below command**
    ```bash
    python pdf_compressor.py    #use python3 explicitly if needed
    ```
