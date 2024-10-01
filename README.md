# iDraw

## プロジェクト概要
iDrawは、ユーザーが作成したSVGファイルを使用してAxiDrawを制御するプロジェクトです。

## 必要なモジュール
- Raspberry Pi 4B
- Arduino Uno
- AxiDraw

## 環境
- Python 3.11

## セットアップ

**注意: 以下のセットアップを行う前に、仮想環境を作成することをお勧めします。**

```sh
$ python3 -m venv your_venv_name
$ source your_venv_name/bin/activate
```

### Raspberry Piでのセットアップ

1. リポジトリをクローンする:
    ```sh
    $ git clone https://github.com/junseiTanaka/idraw.git
    ```

2. Inkscapeアプリケーションをインストールする:
    ```sh
    $ sudo apt update
    $ sudo apt install snapd
    $ sudo reboot
    $ sudo snap install core
    $ sudo snap install inkscape
    ```
3. AxiDraw_API
   ```sh
   $ python -m pip install https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip
   ```
4. 必要なパッケージをインストールする:
    ```sh
    $ cd idraw
    $ pip install -r requirements.txt
    ```

# 使い方
## ①SVGデータをPATHデータに変換する
### SVGデータがある場合
1. AxiDrawで描いて欲しいSVGデータを用意する。
2. SVGデータを`idraw/src/svg`ディレクトリに移動する。
3. ターミナルから以下を実行し、新しいファイルが`path_svg`ディレクトリ内に保存されていることを確認する:
    ```sh
    $ python3 SVGConverter.py
    ```
    
5. AxiDrawとRaspberry PiをUSB接続する。
6. Arduino UnoとRaspberry PiをUSB接続する。

### SVGデータがないが、書きたい文字がjsonファイルにある場合
1. AxiDrawで描いて欲しい文字が書かれたjsonデータを用意する。
2. jsonデータを`idraw/src/json`ディレクトリに移動する。
3. ターミナルから以下を実行し、新しいファイルが`path_svg`ディレクトリ内に保存されていることを確認する:
    ```sh
    $ python3 SVGConverter.py
    ```
    
5. AxiDrawとRaspberry PiをUSB接続する。
6. Arduino UnoとRaspberry PiをUSB接続する。

~~**注意: USB接続の順番を守ること。AxiDraw → Arduino Unoの順番でRaspberry Piに接続する。**~~
USB接続はどちらからでも大丈夫です。
## ②AxiDrawを実行する
7. ターミナルから以下を実行する:
    ```sh
    $ python3 AxiDrawController.py
    ```
①は毎度実行する必要はありません。一度PATHデータが生成されれば②だけ実行すれば大丈夫です。

```
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
