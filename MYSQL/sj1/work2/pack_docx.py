import zipfile
import os

def pack_docx(unpacked_dir, output_file):
    """Pack unpacked directory back to docx"""
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(unpacked_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate archive path relative to unpacked_dir
                arc_path = os.path.relpath(file_path, unpacked_dir)
                zf.write(file_path, arc_path)

    print(f"Packed to: {output_file}")
    print(f"Size: {os.path.getsize(output_file)} bytes")

pack_docx('../unpacked', '../output/实验一报告_v2.docx')