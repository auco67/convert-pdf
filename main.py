import sys
from src.lib.convert_pdf_to_text import ConvertPdfToText
from src.lib.convert_pdf_to_csv import ConvertPdfToCsv

def convert_pdf_to_text(pdf_folder, tex_folder):
    convert_pdf = ConvertPdfToText(pdf_folder,tex_folder)
    pdf_file_list = convert_pdf._get_pdf_file_name_list()
    text_file_list = convert_pdf._get_text_file_name_list()

    try:
        if len(pdf_file_list) == len(text_file_list):
            for index, file_path in enumerate(pdf_file_list):
                convert_pdf.convert_pdf_to_text(pdf_path=pdf_file_list[index], text_path=text_file_list[index])
    
    except Exception as e:
        print(e)

def convert_pdf_to_csv(pdf_folder, output_folder):
    convert_pdf_to_csv = ConvertPdfToCsv(pdf_folder=pdf_folder, csv_folder=output_folder)
    pdf_file_list = convert_pdf_to_csv._get_pdf_file_name_list()
    csv_file_list = convert_pdf_to_csv._get_csv_file_name_list()

    try:
        if len(pdf_file_list) == len(csv_file_list):
            for index, file_path in enumerate(pdf_file_list):
                convert_pdf_to_csv.convert_pdf_to_csv(pdf_path=pdf_file_list[index],
                                                      csv_path=csv_file_list[index])

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # pdf_folder = "./pdf_folder"
    # output_folder = "./csv_folder"
    # convert_pdf_to_csv(pdf_folder=pdf_folder, output_folder=output_folder)
    convert_pdf_to_csv(sys.argv[1], sys.argv[2])