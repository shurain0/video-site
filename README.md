# video-site
 
"video-site"は動画をみて研修・学習するようなサイトをイメージして作りました。

簡単に言えばUdemyのようなものです。それをYouTubeの動画でできるようにしました。
 
## デモサイト

デモサイトをデプロイしています。

https://videolabo.net/videos/course

ログインしていないと使えない機能があるので、その際は以下のサンプルユーザーを使ってみてください。

ユーザー名：user1

パスワード：upass1
 
## 必要パッケージ

* python 3.8.*
* Django 3.2.*
* Pillow 9.2.*

 
## パッケージのインストール
 
 Pythonのインストールがまだの人は[こちらの記事](https://magazine.techacademy.jp/magazine/15571)を参考にしてください。
 
 また、下記のパッケージのインストールは仮想環境内で行う方がおすすめです。
```bash
pip install Django==3.2.* Pillow
```
 
## プロジェクトを動かすまでのステップ
 
### 1. プロジェクトのクローン
```bash
git clone https://github.com/shurain0/video-site.git
```
### 2. `manage.py`を編集
>```
> def main():
>    """Run administrative tasks."""
>   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
>```
の`config.settings.production`を`config.settings.local`に変更します。

つまり以下のようになります。
>```
> def main():
>    """Run administrative tasks."""
>   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
>```

### 3. モデルのマイグレーション
プロジェクトファイル直下でコマンドを実行。

```bash
python3 manage.py migrate
```

### 4. システム管理者の作成
管理サイトにログインできるシステム管理者を作成します。
```bash
python3 manage.py createsuperuser
```

```
Username (leave blank to user 'root'): admin
Email address:
Password: admin12345
Password (again): admin12345
Superuser created successfully.
```
 好きなusernameとpasswordを入力してください。
 
 メールアドレスは任意です。
 
 ### 5. 開発用Webサーバを起動
プロジェクトファイル直下でコマンドを実行。

```bash
python3 manage.py runserver
```
 
 ### 6. データの登録
 `http://127.0.0.1:8000/admin/`または`http://localhost:8000/admin/`にアクセスし、ログインします。
 
 すると以下のような画面になるので、Coursesを作成し、その後Videosを作成します。
 ![image](https://user-images.githubusercontent.com/88956247/198084583-5d0a0c52-cef0-47fd-aa75-b20cf23d03ba.png)

#### ＊注意
**YouTube動画のURLを入力する際は、共有ボタンを押した時に出てくるURLを使用してください。**
![image](https://user-images.githubusercontent.com/88956247/198085917-4811bad5-cd8c-457e-a845-79d3bc6fd7b1.png)


### 7. サイトにアクセス
ブラウザから`http://127.0.0.1:8000/videos/course/`あるいは`http://localhost:8000/videos/course/`にアクセスします。
 
 これでいけるはず、、、！

 
