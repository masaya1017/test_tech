import logging
# 出力情報を出力先を定義して実行する。
logging.basicConfig(
    level=logging.WARNING, filename='./logging/sample.log',
    filemode='w', format='%(asctime)s-%(process)s-%(levelname)s-%(message)s'
)
# errorの程度によって出力情報を記述
# デバッグ情報
logging.debug('debug.log')
# 情報
logging.info('info.log')
# 警告
logging.warning('warning.log')
# エラー
logging.error('error.log')
# 重大エラー
logging.critical('critical.log')

# 出力内容を文章として定義
user = "SATO"
logging.error(f'user={user} raised error')

# 例外処理の出力(0では割り切れない)
a = 10
b = 0
try:
    c = a/b
except Exception as e:
    # exc-infoを用いることで、エラーがどのファイルのどの位置にあるのかがわかる。
    logging.error(e, exc_info=True)
