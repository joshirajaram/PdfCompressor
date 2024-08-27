from pypdf import PdfWriter
import os
import time
import yaml
import traceback
import shutil
from datetime import datetime
from contextlib import redirect_stdout, redirect_stderr

def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def optimize_pdfs(config, formatted_time):
    src_filepath = config["SRC_ANSWER_SHEETS_FILE_PATH"]
    print("SRC File path:", src_filepath)
    start_time = time.time()
    answer_sheets = []
    original_sizes = {}
    compressed_sizes = {}
    for (root, dirs, files) in os.walk(src_filepath):
        answer_sheets = files
    
    print("discovered answer sheets:")
    for sheets in answer_sheets:
        print(sheets)

    for file in answer_sheets:
        original_sizes[file] = os.path.getsize(os.path.join(src_filepath, file))
        
    dirname = "compressed_pdfs" + "_" + str(len(answer_sheets)) + "_scripts_" + formatted_time
    os.mkdir(os.path.join(src_filepath, dirname))
        
    for file in answer_sheets:
        print("Optimizing file:", file)
        try:
            writer = PdfWriter(clone_from=os.path.join(src_filepath, file))

            for page in writer.pages:
                for img in page.images:
                    img.replace(img.image, quality=config["IMAGE_QUALITY_REDUCTION_FACTOR"])

            with open(os.path.join(src_filepath, dirname, file), "wb") as f:
                writer.write(f)
            
            print(file, "optimization SUCCESS")
        except:
            print(file, " may be corrupted. Optimization FAIL")

    shutil.make_archive("zipped_"+dirname, 'zip', os.path.join(src_filepath, dirname))
            
    end_time = time.time()

    print("Total time elapsed: ", end_time - start_time)

    for file in answer_sheets:
        try:
            compressed_sizes[file] = os.path.getsize(os.path.join(src_filepath, dirname, file))
        except:
            print("Optimization skipped for file", file)
        
    for file in answer_sheets:
        try:
            print("File name:", file,  "Original size:", original_sizes[file], 
            "Optimized size:", compressed_sizes[file], "Percentage reduction:", (original_sizes[file] - compressed_sizes[file])*100/original_sizes[file]//1)
        except:
            pass

def main():
    now = datetime.now()
    formatted_time = now.strftime('%Y-%m-%d_%H-%M-%S')
    log_files_path = os.getcwd()+'/logs'
    if not os.path.exists(log_files_path):
        os.makedirs(log_files_path)
    log_file_name = "pdf_compressor_log_" + formatted_time + ".txt"
    
    with open(os.path.join(log_files_path, log_file_name), 'w') as fp:
        with redirect_stdout(fp):
            with redirect_stderr(fp):
                config = load_config('./configs.yaml')
                try:
                    optimize_pdfs(config, formatted_time)
                except Exception:
                    print("Exception occurred. Please check stacktrace.")
                    print(traceback.format_exc())
    
    
if __name__ == '__main__':
    main()