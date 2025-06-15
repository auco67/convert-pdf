import sys
from src.lib.convert_pdf_to_csv import ConvertPdfToCsv

# 警告を非表示にする
import warnings
warnings.filterwarnings("ignore", message="CropBox missing from /Page, defaulting to MediaBox")
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API.")

def convert_pdf_to_csv(pdf_folder, output_folder):
    convert_pdf_to_csv = ConvertPdfToCsv(pdf_folder=pdf_folder, csv_folder=output_folder)
    pdf_file_list = convert_pdf_to_csv._get_pdf_file_name_list()

    try:
        for index, file_path in enumerate(pdf_file_list):
            pdf_folder = str(pdf_folder).replace("../","")
            csv_folder = str(output_folder).replace("../","")

            csv_file_path = str(file_path).replace(pdf_folder,csv_folder).replace('.pdf','.csv')
            convert_pdf_to_csv.convert_pdf_to_csv(pdf_path=file_path,
                                                    csv_path=csv_file_path)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # pdf_folder = "./pdf_folder"
    # output_folder = "./csv_folder"
    # convert_pdf_to_csv(pdf_folder=pdf_folder, output_folder=output_folder)
    convert_pdf_to_csv(sys.argv[1], sys.argv[2])