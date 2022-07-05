import csv
import os
import queue

RESULT_FILE = 'result.dat'


# ルートディレクトリから再帰的にファイル検索
def crawl_dir(root_dir) -> None:

    # 探索対象のディレクトリ
    dir_queue = queue.Queue()
    dir_queue.put(root_dir)

    # ディレクトリを幅優先探索
    while(dir_queue.qsize()):
        current_dir = dir_queue.get()
        files = os.listdir(current_dir)

        for file in files:
            if os.path.isfile(current_dir + '/' + file):
                if not is_valid_filename(file):
                    output_invalid_file(current_dir, file)

            if os.path.isdir(current_dir + '/' + file):
                dir_queue.put(current_dir + '/' + file)


# 適切なファイル名の場合はTrueを返却
def is_valid_filename(file) -> bool:

    # ファイル名の先頭につける言葉のリスト
    confidential_words = ['conf', 'file']
    for word in confidential_words:
        if file.startswith(word):
            return True

    return False


# NOTE csvじゃなくてパス一覧表示で良い
# 不適切なファイルの出力方法
def output_invalid_file(dir, file):
    with open(RESULT_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([dir, file])


if __name__ == "__main__":

    # ヘッダー行の書き込み（上書き）
    with open(RESULT_FILE, 'w') as f:
        header = ['path', 'file']
        writer = csv.writer(f)
        writer.writerow(header)

    path = "./sample"
    crawl_dir(path)
    
