# 2-5-1: MAKEで佐賀の最新ニュースを自動収集しよう 📰

## 🤖 MAKEで何ができる？

### ✨ 主要な機能
- **ワークフロー自動化**: 複数のアプリを連携させて自動処理
- **RSS/API連携**: Webサイトやサービスからデータを自動取得
- **データ整形・加工**: 取得したデータを見やすく整理
- **スケジュール実行**: 決まった時間に自動でタスクを実行
- **ノーコード操作**: プログラミング不要でドラッグ&ドロップ

### 💡 こんなシーンで活用できます
- **情報収集の自動化**: ニュース、SNS、競合情報の定期収集
- **レポート作成**: データを自動でスプレッドシートに整理
- **通知システム**: 重要な情報を即座にSlackやメールで共有
- **業務効率化**: 定型作業を完全自動化
- **データ分析**: 複数ソースからデータを統合して分析

---

## 📚 初心者向け基礎知識

### RSSフィードとは？
RSS（Really Simple Syndication）は、Webサイトの更新情報を配信するための仕組みです。

#### 💡 身近な例で理解しよう
- **普通のWebサイト**: 毎日サイトを訪問して新着記事をチェック（手動）
- **RSSフィード**: 新着記事の情報が自動的に届く（自動）

#### RSSフィードの見つけ方
1. ウェブサイトの下部で「RSS」アイコン（オレンジ色の電波マーク）を探す
2. 「フィード」「Feed」「RSS」というリンクをクリック
3. URLが「.xml」「/feed」「/rss」で終わることが多い

### MAKEの基本用語
- **シナリオ**: 自動化の設計図（レシピのようなもの）
- **モジュール**: 機能の部品（料理の材料や調理器具）
- **トリガー**: 自動化を開始するきっかけ（タイマーやセンサー）
- **フィルター**: データを選別する条件（ふるいや網）

---

## 1. 作るもの

### 🎯 佐賀の最新情報自動収集システム
佐賀県の公式サイトやニュースサイトのRSSから最新情報を自動収集し、整理されたGoogleスプレッドシートを作成します！

### 📝 収集する情報の例

#### 🏛️ 佐賀県公式情報
- 県の重要なお知らせ
- イベント・催し物情報
- 観光・グルメの新着情報
- 行政情報・政策発表

#### 📰 佐賀関連ニュース
- 地域ニュースサイト
- 全国ニュースの佐賀関連記事
- スポーツ・文化情報
- 経済・ビジネス関連ニュース

---

## 2. ハンズオン：佐賀情報収集システムを作ろう

### 2-1. 必要なアカウント準備

#### 必須アカウント（すべて無料）
1. **MAKEアカウント**
   - [make.com](https://www.make.com/)
   - 無料プランで月1,000回の実行が可能

2. **Googleアカウント**
   - Googleスプレッドシート用
   - 既存のアカウントでOK

### 2-2. Googleスプレッドシートの準備

#### 簡単3ステップで準備完了！

1. **新規スプレッドシートを作成**
   - [Googleドライブ](https://drive.google.com/)→「新規」→「Googleスプレッドシート」
   - シート名を「佐賀最新ニュース」に変更

2. **見出し行を作成**（A1〜E1に入力）
   | 日付 | タイトル | 概要 | URL | カテゴリ |
   |-----|---------|------|-----|----------|

3. **完了！**

<img width="812" height="572" alt="image" src="https://github.com/user-attachments/assets/8943d16d-d84a-46d9-a0dd-6d9b1f7fc6c8" />




### 2-3. 佐賀関連RSSフィードの調査

#### 今回使用するRSSフィード

**佐賀新聞 公式RSS**
- URL: `https://www.saga-s.co.jp/list/feed/rss`
- 佐賀県の最新ニュースが自動配信されます

💡 **RSSフィード確認方法**
1. 各サイトで「RSS」「フィード」リンクを探す
2. ブラウザで開いてXML形式であることを確認
3. URLをメモしておく

### 2-4. MAKEでワークフロー作成（最短3ステップ）

#### ステップ1：新規シナリオ作成

1. [MAKE](https://www.make.com/)にログイン → 「+」で新規シナリオ作成

<img width="1104" height="399" alt="image" src="https://github.com/user-attachments/assets/9f341ae7-f34e-4462-adc1-baedc2153ed9" />


2. 「Build from scratch（）」を選択

<img width="659" height="395" alt="image" src="https://github.com/user-attachments/assets/42d3bda5-41da-4af0-9b57-388293816e6b" />


#### ステップ2：RSSフィード取得

1. 画面中央の「+」 → 「RSS」を検索


<img width="650" height="459" alt="image" src="https://github.com/user-attachments/assets/c18b7b07-2307-490c-a12c-2b753c133f32" />


2. 「Watch RSS feed items」を選択


<img width="584" height="435" alt="image" src="https://github.com/user-attachments/assets/9d9ee7ed-958d-4265-b804-989037c3df28" />


3. 設定:
   - **URL**: `https://www.saga-s.co.jp/list/feed/rss`（佐賀新聞RSS）
   - **Maximum number**: `5`（まずは5件でテスト）
   - 「SAVE」で保存

<img width="618" height="432" alt="image" src="https://github.com/user-attachments/assets/c8e42b9c-c12f-4b79-b691-3618bd66d433" />

4. 設定
   - Choose where to start:「All RSS feed items」を選択して「SAVE」
  
<img width="598" height="368" alt="image" src="https://github.com/user-attachments/assets/f9b0c3a5-a41c-4282-b19a-b3d0691cde2b" />


#### ステップ3：Googleスプレッドシートに保存

1. RSSの右の「+」 → 「Google Sheets」を選択

<img width="995" height="447" alt="image" src="https://github.com/user-attachments/assets/e2667946-774b-4f6d-9809-29ab2d57b790" />

2. 「Add a Row」を選択

<img width="992" height="442" alt="image" src="https://github.com/user-attachments/assets/b212f9cf-59d4-40cf-ada9-25cd39c1f8ff" />

3. Googleアカウントを連携（初回のみ）「Create a connection」→「Sign with Google」３回くらい認証が聞かれるので「OK」などを押して進む

<img width="1000" height="404" alt="image" src="https://github.com/user-attachments/assets/0d7b2c8b-5a95-4892-b717-e9df08e2aac8" />

4. 設定:
   - Connectnion: My Google connection のままでOK
   - Search Method: Search by path のままでOK
   - Drive: My Drive ののままでOK
   - Spreadsheet ID: 「Click here to choose file」を押して先ほど作成した「佐賀最新ニュース」を選択
      - 選択すると「Sheet Name」がでてくるので「シート１」を選択し、以下も順に設定
      - Table contains headers: Yes
      - Values(RSSから取ったデータを、スプレッドシートのどの列に入れるかの設定)
          - 日付 (A) → RSSモジュールの Date updated
          - タイトル (B) → RSSモジュールの Title
          - 概要 (C) → RSSモジュールの Summary
          - URL (D) → RSSモジュールの URL
          - カテゴリ (E) → RSSモジュールの Categories
          - すべて選択して「SAVE」
       
   <img width="1048" height="549" alt="image" src="https://github.com/user-attachments/assets/94b97bd0-6cfb-4d40-8389-90ee198008f7" />


#### 完成！テスト実行

1. 「Save」ボタンでシナリオ（ワークフロー）を保存

<img width="719" height="68" alt="image" src="https://github.com/user-attachments/assets/c28766b4-2fd5-4e31-89bc-7cccff10cbcc" />

2. 「Run once」でテスト実行

<img width="713" height="65" alt="image" src="https://github.com/user-attachments/assets/326a9582-c694-4105-b287-fd11d762bfdd" />

   - 成功するとGoogleスプレッドシートにニュースが追加されます！

<img width="751" height="326" alt="image" src="https://github.com/user-attachments/assets/4a32c00b-5c19-4348-9c28-43d642e935e8" />

3. スケジュール設定
  - RSSアイコンの横にある「時計」マークを押すと、RSSからどのくらいの頻度でいつ情報を取得するか選べます
  - 下記画像は、「毎日」の「13時」に取得

<img width="572" height="337" alt="image" src="https://github.com/user-attachments/assets/f55e3be1-8778-4a5e-9901-14d735315021" />

 - ホーム画面→「ALL scenarios」からON/OFFを設定できます

<img width="1104" height="290" alt="image" src="https://github.com/user-attachments/assets/c7ed76f5-1b01-4506-8faa-e876b538a49e" />


### 🎉 これで完成！

シンプルな2ステップで、RSSからニュースを自動収集するシステムができました。
毎日決まった時間にニュースがスプレッドシートに追加されます。

---

## 3. Tips 💡

### ワークフロー最適化のコツ

#### データ品質を向上させる工夫

1. **キーワードベースの重要度判定**
   ```
   重要度 = 高：「緊急」「警報」「重要」
   重要度 = 中：「イベント」「観光」「グルメ」
   重要度 = 低：その他
   ```

2. **カテゴリの自動分類**
   ```
   行政：「県庁」「市役所」「議会」
   観光：「祭り」「イベント」「観光地」
   経済：「企業」「商工会」「雇用」
   災害：「台風」「地震」「警報」
   ```

3. **データクリーニングの強化**
   - 重複タイトルの検知と統合
   - 文字化けの自動修正
   - 不適切なコンテンツのフィルタリング

### 他の活用例

#### 🏢 ビジネス情報収集
```
競合他社のプレスリリース監視
→ Googleスプレッドシートに自動保存
→ 重要な発表をSlack通知
```

#### 📊 市場調査自動化
```
業界ニュースの自動収集
→ AIによる感情分析
→ ダッシュボードで可視化
```

#### 🎯 イベント情報管理
```
地域イベント情報収集
→ カレンダーアプリと連携
→ 事前リマインダー送信
```

---

## 4. チャレンジ 🎯

### 機能拡張のアイデア

1. **複数RSS対応**
   - 複数のフィードを並行処理
   - ソース別の信頼度スコア

2. **AI分析の追加**
   - ChatGPTによる記事要約
   - 感情分析とトレンド検出

3. **視覚化の強化**
   - Googleデータスタジオでダッシュボード作成
   - 時系列グラフで情報トレンド表示

4. **多言語対応**
   - 英語ニュースも収集
   - 自動翻訳機能の追加

---

## 5. まとめ

### 今回学んだこと

✅ RSSフィードからの自動データ取得
✅ データフィルタリングと整形技術  
✅ Googleスプレッドシートとの連携
✅ 重複チェックとデータ品質管理
✅ スケジュール実行による自動化

このシステムで、佐賀の最新情報を見逃すことがなくなり、
効率的な情報収集が可能になります！

### 応用の可能性

- 🏛️ **自治体・官公庁**: 住民向け情報発信の効率化
- 🏢 **企業**: 業界動向の自動監視システム
- 📰 **メディア**: ニュースソースの統合管理
- 🎓 **研究機関**: 専門分野の情報収集自動化

---

### 🎓 初心者向けアドバイス

1. **最初は簡単な設定から**
   - RSS 1つ、1日1回の実行から始める
   - 動作確認後に徐々に機能を追加

2. **エラーが出ても焦らない**
   - エラーメッセージをGoogle翻訳で確認
   - MAKEのコミュニティフォーラムで質問

3. **学習リソース**
   - MAKE公式チュートリアル（日本語字幕あり）
   - YouTubeで「MAKE 自動化」で検索

**次のステップ**: 収集したデータを分析して、佐賀の情報トレンドを発見してみましょう！📈
