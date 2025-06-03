import os
from pathlib import Path
from PyPDF2 import PdfReader

class ConvertPdfToText:
    def __init__(self, pdf_folder, text_folder):
        self._pdf_folder = pdf_folder
        self._text_folder = text_folder

    def convert_pdf_to_text(self, pdf_path:str, text_path:str) -> None:
        """
        PDFファイルをテキストファイルに変換します。

        Args:
            pdf_path (str): 入力PDFファイルのパス。
            text_path (str): 出力テキストファイルのパス。
            """
        try:
            # PDFファイルを読み込む
            reader = PdfReader(pdf_path)

            # 書き込みモードでテキストファイルを開く
            with open(text_path, 'w', encoding='utf-8') as f:
                
                # PDFの総ページ数ループ
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    # ページからテキストを抽出
                    text = page.extract_text()
                    if text:
                        # テキストが抽出された場合のみ書き込む
                        f.write(text)
                        # 各ページの区切り
                        # f.write('\n--- ページ {} の終わり ---\n\n'.format(page_num + 1)) 

            print(f"'{pdf_path}' がテキストファイル '{text_path}' に正常に変換されました。")

        except Exception as e:
            print(f"PDFからテキストへの変換中にエラーが発生しました: {e}")

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

    def _get_text_file_name_list(self) -> list[str]:
        """テキストファイルリストを返す

        Returns:
            file_name_list(list): TEXTファイル名リスト
        """
        file_name_list = []
        text_folder = Path(self._text_folder)
        pdf_folder = Path(self._pdf_folder)

        try:
            for item in os.listdir(pdf_folder):
                item_path = text_folder/ item.replace(".pdf", ".txt")
                file_name_list.append(item_path)

            return file_name_list

        except Exception as e:
             print(f"TEXTファイルリスト作成時にエラーが発生しました: {e}")