# ブラウザを複数動かすサンプル

複数のブラウザを起動して、ページ遷移しながら各ページの

## 準備
* 使用するブラウザをダウンロードする https://selenium-python.readthedocs.io/installation.html#drive
* どこかにダウンロードしたxxxdriver.exeを置く。今回はこのリポジトリーのルート。

## 内容

### sample_base.py
* https://kamekokamekame.net にアクセス
* ページ内の適当なリンクをクリック
* 表示されたページのタイトルを表示する
* 10回表示したら終わり

## sample_threading.py
* threadingを使った処理
* 3つのブラウザを起動する

## sample_futures.py
* futuresを使った処理
* 3つのブラウザを起動する

