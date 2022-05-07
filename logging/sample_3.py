# 設定ファイルによってログ出力を定義する場合
import logging
# configは初期設定を意味する。
import logging.config
# 設定ファイルの読み込み(logger.confについては、shift-jisにしないとエラーが生じることに注意する。)
logging.config.fileConfig(fname='./logging/conf/logger.conf')

# ロガーの作成(root用)
logger = logging.getLogger(__name__)

logger.debug('デバッグログ')
logger.info('情報ログ')
logger.warning('警告ログ')
logger.error('エラーログ')
logger.critical('重大エラーログ')

# ロガーの作成（カスタマイズ用）
logger = logging.getLogger('samplelogger')

logger.debug('デバッグログ')
logger.info('情報ログ')
logger.warning('警告ログ')
logger.error('エラーログ')
logger.critical('重大エラーログ')
