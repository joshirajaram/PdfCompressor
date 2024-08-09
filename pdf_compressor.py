from pypdf import PdfWriter
import os
import time
import yaml
import traceback

def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main(config):
    src_filepath = config["SRC_ANSWER_SHEETS_FILE_PATH"]
    print("SRC File path:", src_filepath)
    start_time = time.time()
    answer_sheets = []
    original_sizes = {}
    compressed_sizes = {}
    for (root, dirs, files) in os.walk(src_filepath):
        answer_sheets = files
        
    print("discovered answer sheets:", answer_sheets)

    for file in answer_sheets:
        original_sizes[file] = os.path.getsize(os.path.join(src_filepath, file))
        
    os.mkdir(os.path.join(src_filepath, "compressed_pdfs"))
        
    for file in answer_sheets:
        print("Compressing file:", file)
        writer = PdfWriter(clone_from=os.path.join(src_filepath, file))

        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality=config["IMAGE_QUALITY_REDUCTION_FACTOR"])

        with open(os.path.join(src_filepath, "compressed_pdfs", file), "wb") as f:
            writer.write(f)
            
    end_time = time.time()

    print("Total time elapsed: ", end_time - start_time)

    for file in answer_sheets:
        compressed_sizes[file] = os.path.getsize(os.path.join(src_filepath, "compressed_pdfs", file))
        
    for file in answer_sheets:
        print("File name:", file,  "Original size:", original_sizes[file], 
            "Compressed size:", compressed_sizes[file], "Percentage reduction:", (original_sizes[file] - compressed_sizes[file])*100/original_sizes[file]//1)
        
if __name__ == '__main__':
    config = load_config('./configs.yaml')
    try:
        main(config)
    except Exception:
        print("Exception occurred. Please check stacktrace.")
        print(traceback.format_exc())
