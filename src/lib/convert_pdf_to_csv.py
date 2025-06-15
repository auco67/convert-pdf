import os
import csv
from pathlib import Path

import pandas as pd
import pdfplumber

class ConvertPdfToCsv:
    def __init__(self, pdf_folder, csv_folder):
        self._pdf_folder = pdf_folder
        self._csv_folder = csv_folder

    def _get_pdf_file_name_list(self) -> list[str]:
        """PDFファイル名リストを返す

        Returns:
            file_name(list): PDFファイル名リスト
        """
        file_name_list = []
        pdf_folder = Path(self._pdf_folder)

        if not os.path.exists(pdf_folder):
            print(f"エラー：指定されたパス{pdf_folder}は存在しません。")
        
        if not os.path.isdir(pdf_folder):
            print(f"エラー：指定されたパス{pdf_folder}はディレクトリではありません")

        try:
            for item in os.listdir(pdf_folder):
                item_path = pdf_folder / item

                if os.path.isfile(item_path):
                    if item_path.suffix.lower() == ".pdf":
                        file_name_list.append(item_path)

            return file_name_list
        except Exception as e:
            print(f"PDFファイルリスト取得時にエラーが発生しました: {e}")

    def _get_csv_file_name_list(self) -> list[str]:
        """CSVファイルリストを返す

        Returns:
            file_name_list(list): CSVファイル名リスト
        """
        file_name_list = []
        csv_folder = Path(self._csv_folder)
        pdf_folder = Path(self._pdf_folder)

        try:
            for item in os.listdir(pdf_folder):
                item_path = csv_folder/ item.replace(".pdf", ".csv")
                file_name_list.append(item_path)

            return file_name_list

        except Exception as e:
             print(f"CSVファイルリスト作成時にエラーが発生しました: {e}")

    def convert_pdf_to_csv(self, pdf_path:str, csv_path:str) -> None:
        """
        PDFファイルをCSVファイルに変換します。

        Args:
            pdf_path (str): 入力PDFファイルのパス。
            csv_path (str): 出力CSVファイルのパス。
            """
        all_extracted_data = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    # ページからテーブルを抽出
                    # extract_tables() は、検出されたテーブルのリストを返す
                    # 各テーブルは行のリストで、各行はセルのリストで、各セルは文字列
                    tables = page.extract_tables()

                    for table in tables:
                        # 各テーブルをPandas DataFrameに変換
                        # header=None を指定しないと、最初の行をヘッダーとして解釈しようとします
                        df = pd.DataFrame(table)
                        all_extracted_data.append(df)

            if not all_extracted_data:
                print(f"'{pdf_path}' から表が見つかりませんでした。")
                return

            # 抽出されたすべてのデータフレームを結合
            combined_df = pd.concat(all_extracted_data, ignore_index=True)

            # CSVファイルとして保存 (UTF-8 with BOMでExcelでの文字化けを防ぐ)
            combined_df.to_csv(csv_path, index=False, encoding='utf-8-sig')

            print(f"'{pdf_path}' から抽出された表を '{csv_path}' に変換しました。")

        except Exception as e:
            print(f"PDFからテキストへの変換中にエラーが発生しました: {e}")