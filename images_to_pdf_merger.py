import os
import re
from PIL import Image

def merge_images_to_pdf(image_folder, output_pdf_name):
    # 1. Retrieve all files in the folder
    files_in_folder = os.listdir(image_folder)
    
    # 2. Filter files ending with image extensions (.png, .jpg, .jpeg)
    image_files = [f for f in files_in_folder if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("No image files found in the specified folder.")
        return

    # 3. NATURAL SORT
    # Extracts numbers from the filename to sort them logically (1, 2... 10, 11... 198)
    # Avoids alphabetical sorting issues (1, 10, 100, 2...)
    image_files.sort(key=lambda f: int(re.search(r'\d+', f).group()) if re.search(r'\d+', f) else 0)
    
    # Create full paths for each image
    image_paths = [os.path.join(image_folder, f) for f in image_files]
    
    print(f"Found {len(image_paths)} images. Starting conversion...")

    # 4. Convert and merge into PDF
    # PDFs do not support PNG transparency (RGBA), so everything is converted to RGB
    pil_image_list = []
    
    # Open the first image (this will be the first page of the PDF)
    first_image = Image.open(image_paths[0]).convert('RGB')
    
    # Open all remaining images
    for path in image_paths[1:]:
        img = Image.open(path).convert('RGB')
        pil_image_list.append(img)
        
    # Save everything to the final PDF file
    first_image.save(output_pdf_name, save_all=True, append_images=pil_image_list)
    
    print(f"Success! The PDF was saved as: {output_pdf_name}")

# --- CONFIGURATION ---
# Use "." if the script is in the same folder as the images, 
# or insert the absolute path (e.g., "C:/Users/Name/Desktop/Images")
target_folder = "." 
final_pdf = "merged_document.pdf"

merge_images_to_pdf(target_folder, final_pdf)
