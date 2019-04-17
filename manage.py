#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#Djangoフレームワークを使ったプロジェクトの構造
#manage.py：プロジェクト管理スクリプト（スクリプト：コンパイルを意識せずにすぐに実行できるプログラム）
#setting.py：プロジェクト設定ファイル
#urls.py：ＵＲＬ設定ファイル
#wsgi.py：ＷＳＧＩアプリケーション定義を含むファイル

#os：ファイルの動作、操作、パスの操作等のライブラリ
#sys：Pythonスクリプトに渡されたコマンドライン引数のリスト
import os
import sys


def main():
    #デフォルトのsettings.pyの格納先を指定する。（パスを通す）
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

    #例外処理可能とする(tryは必ず実行)
    try:
        #django.core.managementってライブラリを使用可能にする。
        from django.core.management import execute_from_command_line

        #exceptは例外が発生した場合のみ実行される。
        #ImportError：import文でモジュールをロードしようとして問題が発生した時のエラー
    except ImportError as exc:
        #raiseは故意に例外処理を発生させる
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

        #コマンドライン（コマンドプロンプト）に入力された文字列を引数としてリストに組み込む
        #sys.argvはコマンドライン引数の値を取り込む（０番目はプログラムファイル名、以降の要素にコマンドライン引数の値）
    execute_from_command_line(sys.argv)

#Pythonファイルが「python ファイル名.py というふうに実行されているかどうか」を判定するif文です
#__name__にはpythonファイルのモジュール名が文字列で入っている
#これはインポートされた際にプログラムが動かないようにするため、
if __name__ == '__main__':
    main()

#例外処理にはほかにもある。
#else：例外が発生しなかった場合に行う処理
#finally:例外の有無に関わらず必ず行う処理
#