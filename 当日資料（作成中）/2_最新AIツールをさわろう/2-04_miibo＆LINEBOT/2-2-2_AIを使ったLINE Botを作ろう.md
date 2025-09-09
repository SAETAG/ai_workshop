# 2-2-2: AIを使ったLINE Botを作ろう

## 会話型AIのLINE Botを作ろう

このパートでは、いよいよメインである「会話型AIのLINE Bot」を作っていきます。
miiboとLINEが連携することで、会話型AIが組み込まれたLINE Botを作ることができます。

---

## 1. 作るもの

### miiboとLINEが連携した会話型AIのLINE Bot

前のパートで作成したmiiboのエージェントをLINEと連携させ、LINEアプリ上で動作するAIチャットボットを完成させます。

**完成イメージ：**
- LINEで友だち追加するだけで使える
- 24時間365日対応可能
- 自然な会話ができるAIアシスタント

---

## 2. ハンズオン: 会話型AIのLINE Botを作ってみよう

### 2-1. LINEにログインしてチャネルを開こう

#### 手順1：LINE Developersにアクセス

1. [LINE Developers](https://developers.line.biz/)を開く
2. 画面右上の**「コンソールにログイン」**をクリック

<img width="1088" height="407" alt="image" src="https://github.com/user-attachments/assets/1df9fcf4-4dba-4744-8013-86a962eff92d" />


#### 手順2：LINEアカウントでログイン

1.  **「LINEアカウントでログイン」** をクリック
2.  **「ログイン」** をクリック

<img width="389" height="503" alt="image" src="https://github.com/user-attachments/assets/202cd22b-4897-474c-82b2-49703a6ed98e" />

#### 手順3：チャネルを開く

1. 画面左側の **「プロバイダー」** を開く
2. 事前に作成した**プロバイダー**をクリック
3. 事前に作成している**チャネル**をクリック

<img width="708" height="560" alt="image" src="https://github.com/user-attachments/assets/0f800f6d-32f7-4583-b46d-385599b332dd" />

管理画面のようなチャネルのページが開かれていたらOKです。

<img width="1012" height="561" alt="image" src="https://github.com/user-attachments/assets/abb3eace-6df0-4884-97aa-f60a675ebce2" />


### 2-2. miiboにLINEの情報を登録しよう

次にmiiboの管理画面に戻り、事前準備で取得したLINEの情報をmiiboに登録して連携の準備をしていきます。

#### 手順1：外部サービス連携画面を開く

1. miiboの管理画面に戻る
2. 左側のメニューバーから**「外部サービス連携」**をクリック

<img width="1103" height="566" alt="image" src="https://github.com/user-attachments/assets/93522e57-5db5-48c4-b9c2-dff04fea8451" />


#### 手順2：LINE連携を選択

1.  **「LINE上で会話する」** をクリック

<img width="898" height="428" alt="image" src="https://github.com/user-attachments/assets/28108d78-df50-4f5e-8644-f7a076f652f2" />


#### 手順3：認証情報を入力

1. メモ帳やWordに控えておいた以下の情報を貼り付け：
   - **チャネルシークレット**
   - **チャネルアクセストークン**

<img width="898" height="437" alt="image" src="https://github.com/user-attachments/assets/db8f02e3-b784-4501-a8dc-41c28398a355" />

2. 2つの情報が入力できたら、 **「LINEと連携する」** ボタンをクリック

#### 手順4：Webhook URLの確認

連携がうまくいくと、**Webhook URL**というURLが発行されます。
このURLをコピーして、次のステップで使用します。

<img width="896" height="485" alt="image" src="https://github.com/user-attachments/assets/1704ebe5-d480-4ae2-9f22-0cf813c06ce8" />

### 💡 Webhookとは？

Webhookとは、アプリケーション間でリアルタイムにデータを共有するための仕組みのことです。
何かしらのイベントが実行されたときに、外部サービスにリアルタイムで通知をします。

**今回の場合：**
- ユーザーがLINEでメッセージを送信
- LINEがWebhook URLにメッセージを送信
- miiboがメッセージを受け取り、AIが返答を生成
- 返答をLINEに送り返す

### 2-3. LINEにWebhook URLを登録しよう

最後に、miiboで発行されたWebhook URLをLINEに登録して連携していきます。

#### 手順1：Webhook URLをコピー

1. miiboで発行された**「Webhook URL」**をコピー

<img width="895" height="514" alt="image" src="https://github.com/user-attachments/assets/b869b3de-63d7-49ab-901a-7977c74826ad" />


#### 手順2：LINE側でWebhook設定

1. LINEのチャネルページに戻る
2. **「Messaging API設定」**タブをクリック

<img width="797" height="428" alt="image" src="https://github.com/user-attachments/assets/784bb04a-dd70-4d64-ae4a-4d423458c017" />

3. **Webhook設定**の中の **「編集」** をクリック

<img width="401" height="142" alt="image" src="https://github.com/user-attachments/assets/7e7441f8-4943-4695-afe8-a9151c21c744" />

#### 手順3：URLを登録

1. コピーしたWebhook URLを貼り付け
2. **「更新」**をクリック

<img width="902" height="219" alt="image" src="https://github.com/user-attachments/assets/50632491-729a-45bd-b08b-1b56812310df" />


#### 手順4：Webhookを有効化

1.  **「Webhookの利用」** の右側にあるスイッチをクリックしてオンにする

<img width="200" height="77" alt="image" src="https://github.com/user-attachments/assets/f96dd533-fb85-46c9-b7ce-25e6ac4b0638" />


#### 手順5：接続テスト

1. **「検証」**をクリック

 <img width="434" height="212" alt="image" src="https://github.com/user-attachments/assets/748043f9-8768-4446-b97e-2fa9175d451e" />
   
2. **「成功」**の表示が出ることを確認

<img width="264" height="107" alt="image" src="https://github.com/user-attachments/assets/5d5ac3e2-4b20-4c8a-a084-17c418785848" />

3. **「OK」**で閉じる

#### 手順6：応答メッセージをOFFにする（重要！）

デフォルトの自動応答メッセージを無効にして、miiboからの応答だけが返るようにします。

1.  **「LINE公式アカウント機能」** セクションまでスクロール
2.  **「応答メッセージ」** の「編集」をクリック

<img width="934" height="315" alt="image" src="https://github.com/user-attachments/assets/dff3f6fa-6e93-4441-a889-40554c2b9ef0" />

3. LINE Official Account Managerが新しいタブで開きます
4.  **「応答設定」** → **「詳細設定」** をクリック
5.  **「応答メッセージ」** をOFFに変更
6.  **「Webhook」** がONになっていることを確認

<img width="865" height="434" alt="image" src="https://github.com/user-attachments/assets/5faefb2f-f723-400b-b185-011dada73cdd" />

💡 **なぜこの設定が必要？**
> この設定をしないと、「メッセージありがとうございます！申し訳ありませんが...」というLINEのデフォルトメッセージが先に返ってきてしまい、その後にmiiboからの応答が届く二重返信になってしまいます。

🎉 これで連携完了です！

### 2-4. 試してみよう

miiboとLINEが連携され、会話型AIのLINE Botが完成しました！

#### テスト方法

1. 作成したLINE Botを友だち追加
2. 何かメッセージを送信
3. AIからの返答を確認

早速、LINE Botに何かメッセージを送信して会話をしてみましょう。
AIと対話できましたか？

#### 試してみる質問例

- 「こんにちは」
- 「佐賀のおいしいものを教えて」などなど
---

## 3. Tips 💡

### 他のサービスとも連携可能

外部サービス連携には今回使ったLINEだけではなく、様々なチャットサービスと連携できます：

- **Slack**: ビジネスチャット
- **Discord**: コミュニティチャット
- **Teams**: Microsoft製ビジネスチャット
- **Webサイト埋め込み**: 自社サイトに設置

連携方法は各設定の中の**「利用方法を見る」**から確認できます。

### トラブルシューティング

**Q: 返答が来ない場合**
- Webhook URLが正しくコピーされているか確認
- Webhookの利用がONになっているか確認
- チャネルアクセストークンが正しいか確認

**Q: エラーメッセージが返ってくる**
- miiboの会話クレジットが残っているか確認
- エージェントが公開状態になっているか確認

---

## 4. チャレンジ 🎯

### 作成したBotを共有しよう

1. 完成した会話型AIのLINE Botと会話した様子をスクリーンショット
2. 授業連絡用のTeamsに投稿
3. 周りの方と共有し、お互いのLINE Botで会話を試してみる

### 共有方法

**Messaging API設定**タブから自分の**QRコード**を表示して、読み取ってもらいましょう。

### 共有時のポイント

- どんな工夫をしたか説明
- 特徴的な返答例を紹介
- 使い道のアイデアを共有

---

## 5. まとめ

### 今回達成したこと

✅ miiboとLINEの連携方法を習得
✅ Webhook URLの仕組みを理解
✅ 実際に動作するLINE Botの作成
✅ AIを活用したサービスの構築

miiboを使って会話型AIのLINE Botを作ることができました！
現在は簡単なメッセージのやり取りができていますが、より自分だけのオリジナルLINE Botにしていきたいですね。

### 次のステップ

次のパートからは、会話型AIを自分好みにどんどんカスタマイズしていきます。楽しみですね！

**カスタマイズ例：**
- プロンプトを工夫して性格を変更
- 特定の役割（英語教師、料理アドバイザーなど）を設定
- 画像認識や音声対応などの高度な機能追加

---

**おめでとうございます！** あなたは今、AIを活用したLINE Botの開発者です！🎊
