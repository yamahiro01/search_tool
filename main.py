import os

# csv_path
CAT_CSV_PATH = "cat.csv"
DEFAULT_CATS = ["しろねこさん","くろねこさん","くりーむさん"]

# CSVから読み込み
def read_source(csv_path:str):
    # ファイルの新規作成
    if not os.path.exists(csv_path):
        print(f"csv_path:{csv_path}が存在しません。新規作成します。")
        write_source(csv_path, DEFAULT_CATS)
    # ファイルの読み込み
    with open(csv_path, 'r', encoding="utf-8_sig") as f:
        return f.read().splitlines()

def write_source(csv_path:str, source:list):
    # sourceをCSVに書き込み
    with open(csv_path, mode='w', encoding="utf-8_sig") as f:
        f.write("\n".join(source))

### 検索ツール
def search():
    
    #  検索ソース
    source = read_source(CAT_CSV_PATH)
    
    while True:
        # ユーザー入力
        word =input("ねこあつめに登場するねこの名前を入力してください >>> ")
    
        # 検索ロジック
        if word in source:
            print(f"{word}が見つかりました")
        else:
            print(f"{word}は見つかりませんでした")
            # 追加
            is_add = input("追加登録しますか？(n:しない y:する) >>> ")
            if is_add == "y":
                source.append(word)
        
        # sourceをcsvに書き込み
        write_source(CAT_CSV_PATH, source=source)
        
# 検索ツールの実行
if __name__ == "__main__":
    search()