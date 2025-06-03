# PDF変換

## 使用方法（Windowsの場合）

1. githubからリポジトリをgit cloneする
    ```
    git clone https://github.com/auco67/convert-pdf.git
    ```

2. pdfファイルを格納するフォルダ`pdf_folder`を用意し、PDFファイルを格納する
    ```
    convert-pdf
     └─pdf_folder
        ├─pdf_file_01.pdf
        ├─pdf_file_02.pdf
        ├─...
    ```

3. csvファイルを格納するフォルダ`csv_folder`を用意する
    ```
    convert-pdf
     └─csv_folder
    ```

4. main.batを実行する

    main.batの中身
    ```
    cd dist
    main.exe "../pdf_folder" "../csv_folder"
    pause
    ```

    実行後、`csv_folder`にCSVファイルが格納される

    ```
    convert-pdf
     └─csv_folder
        ├─pdf_file_01.csv
        ├─pdf_file_02.csv
        ├─...
    ```