# PdfCompressor

Script to compress PDF answer scripts in given folder 

## Running a Python Script

To run the Python script, follow these steps:

1. **Clone or download and unzip the repo**

    ```bash
    git clone https://github.com/joshirajaram/PdfCompressor.git
    ```
2. **Navigate to the Script Directory:**

    ```bash
    cd path/to/script/directory
    ```
3. **Install Python3 if not present**
    - For Windows: https://www.python.org/downloads/
    - For macOS: https://www.python.org/downloads/macos/
    - For Linux: sudo apt install python3.10
4. **Install requirements**

    ```bash
    python -m pip install -r requirements.txt
    ```
    ### For some systems we might need to use python3 explicitly
    ```bash
    python3 -m pip install -r requirements.txt
    ```
5. **Update parent folder path and reduction factor in configs.yaml**

    ```yaml
    SRC_ANSWER_SHEETS_FILE_PATH: '/path/to/src/directory'
    IMAGE_QUALITY_REDUCTION_FACTOR: 10 #default is 10, can change as per requirement
    ```
6. **Generate fresh build if not already present**

    ```bash
    pyinstaller --distpath . --onefile pdf_compressor.py
    ```
7. **Run the executable in the repo**
    
    ```bash
    $ ./pdf_compressor  #for *nix based systems
    > pdf_compressor    #for Windows systems
    ```
8. **In case the executable is throwing an exception, please run using the below command**
    ```bash
    python pdf_compressor.py    #use python3 explicitly if needed
    ```
