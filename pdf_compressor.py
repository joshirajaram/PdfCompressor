from pypdf import PdfWriter
import os
import time

env_filepath = os.getenv("SRC_ANSWER_SHEETS_FILE_PATH")
print("SRC File path:", env_filepath)
start_time = time.time()
answer_sheets = []
original_sizes = {}
compressed_sizes = {}
for (root, dirs, files) in os.walk(env_filepath):
    answer_sheets = files
    
print("answer sheets: ", answer_sheets)

for file in answer_sheets:
    original_sizes[file] = os.path.getsize(os.path.join(env_filepath, file))
    
os.mkdir(env_filepath + "/compressed_pdfs")
    
for file in answer_sheets:
    writer = PdfWriter(clone_from=os.path.join(env_filepath, file))

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=10)

    with open(env_filepath + "/compressed_pdfs/" + file, "wb") as f:
        writer.write(f)
        
end_time = time.time()

print("Total time elapsed: ", end_time - start_time)

for file in answer_sheets:
    compressed_sizes[file] = os.path.getsize(os.path.join(env_filepath, "compressed_pdfs", file))
    
for file in answer_sheets:
    print("File name: ", file,  "Original size: ", original_sizes[file], 
          "Compressed size: ", compressed_sizes[file], "Percentage reduction: ", (original_sizes[file] - compressed_sizes[file])*100/original_sizes[file]//1)