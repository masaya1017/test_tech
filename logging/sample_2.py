import logging
# __name__によってファイルを参照して出力される。
logger = logging.getLogger(__name__)
# loggerの閾値(DEBUG以上のerrorを取得可能となる。)
logger.setLevel(logging.DEBUG)
# handlerの定義

# ターミナル上にエラーを出力
s_handler = logging.StreamHandler()
# ファイル上にエラーを出力(文字化け予防のため、utf-8を指定)
f_handler = logging.FileHandler('./logging/sample_2.log', encoding='utf-8')

# handlerのログレベル定義
s_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

# Formatter(出力形式を定義)
s_formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
f_formatter = logging.Formatter(
    '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
)
# handlerにformatterを設定
s_handler.setFormatter(s_formatter)
f_handler.setFormatter(f_formatter)

# loggerにhandlerをセット(loggerはログの管理者みたいなもの)
logger.addHandler(s_handler)
logger.addHandler(f_handler)


logger.debug('デバッグログ')
logger.info('情報ログ')
logger.warning('警告ログ')
logger.error('エラーログ')
logger.critical('重大エラーログ')

# 例外処理の出力(0では割り切れない)
a = 10
b = 0
try:
    c = a/b
except Exception as e:
    # exc-infoを用いることで、エラーがどのファイルのどの位置にあるのかがわかる。
    logger.error(e, exc_info=True)
