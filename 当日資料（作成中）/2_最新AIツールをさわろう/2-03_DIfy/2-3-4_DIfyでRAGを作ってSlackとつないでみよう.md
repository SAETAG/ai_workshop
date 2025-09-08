Difyにナレッジを蓄積して、RAGを作ってSlack上から検索してみよう！

ポイント解説：RAGとは？

１、まずはナレッジをcsv形式で作ろう
　
 ①以下のプロンプトをGeminiになげてみよう

あなたは日本の歴史に詳しい郷土史家です。
佐賀県が輩出した、あるいは佐賀の発展に大きく貢献した歴史上の偉人を調査し、その結果をCSV形式でまとめてください。

# 出力形式
・CSV形式で出力してください。
・1行目はヘッダーとして「名前,説明」とします。
・2行目以降に、各偉人の名前と、その人物の特筆すべき功績や後世への影響について、専門家の視点から150字以内で要約した説明を記述してください。

# 人選の条件
・「佐賀の七賢人」は必ず含めてください。
・上記に加え、古代から近代までの幅広い時代から、重要な人物をバランス良く選んでください。
・合計で15名程度リストアップしてください。

②出力された結果を「メモ帳」にはって「.csv」で保存しよう

出力結果
名前,説明
大隈重信,日本の近代化に大きく貢献した政治家。早稲田大学の創設者であり、外交面でも活躍し、不平等条約の改正に尽力した。
大木喬任,司法制度の確立に尽力し、日本近代の法治国家の基盤を築いた。教育分野でも活躍し、東京大学の前身となる大学の設立にも関わった。
佐野常民,日本赤十字社の創設者。世界に先駆けて戦争負傷者の救護活動に尽力し、国際的な人道支援の先駆者として知られる。
副島種臣,新政府の外交を担い、特に清との交渉では琉球の帰属問題を解決するなど、近代日本の外交基盤を築いた。書家としても優れていた。
江藤新平,司法卿として司法制度の整備を推進し、日本初の近代的司法制度の基礎を築いた。後に佐賀の乱を起こすが、その改革精神は評価されている。
島義勇,開拓使主席判官として、札幌の都市計画を立案・実行し、北海道の近代的な開拓の礎を築いた。佐賀の乱で江藤新平と共に処刑された。
鍋島直正,幕末の佐賀藩主。いち早く西洋の科学技術を導入し、反射炉やアームストロング砲を製造するなど、佐賀藩の近代化を強力に推進した。
高取清,日本の製薬産業の先駆者。日本で初めてチフス予防薬の製造に成功し、公衆衛生の向上に大きく貢献した。
枝吉神陽,佐賀藩の尊王攘夷派のリーダー。佐賀の七賢人の一人である枝吉神陽は、鍋島直正の政治顧問として、藩政改革に影響を与えた。
田代孫三郎,江戸時代後期の佐賀藩士。医学を学び、西洋医学を佐賀に広めた。彼の功績は、佐賀藩の近代化に大きく貢献した。
神埼宗清,戦国時代の武将。龍造寺氏に仕え、多くの戦功を挙げた。龍造寺四天王の一人として知られ、鍋島氏の台頭を支えた。
神代勝利,戦国時代の武将。肥前神代氏の当主であり、龍造寺氏に抵抗したが、最終的には臣従し、龍造寺氏の佐賀統一に貢献した。
神代長良,江戸時代前期の学者。佐賀藩の藩校弘道館で儒学を教え、藩士の教育に尽力した。多くの門下生を輩出し、佐賀の文化発展に貢献した。
中野武営,ジャーナリスト。日本経済新聞社の創業者の一人。実業界にも進出し、東京商工会議所の会頭を務めるなど、日本の近代経済の発展に貢献した。
岩村通俊,政治家。日本の近代国家建設に尽力し、北海道開拓使長官、沖縄県知事などを歴任した。

保存するときはファイル名の末尾を「.csv」にしてcsv形式で保存しよう！
<img width="761" height="128" alt="image" src="https://github.com/user-attachments/assets/b71c7eb0-01ad-443a-b4ac-c654e034cc1f" />

ポイント解説：csvとは？
・・・・・

２、Difyにナレッジベースを作ろう！

①トップ画面にいき、上にある「ナレッジ」ボタンを押す

<img width="797" height="339" alt="image" src="https://github.com/user-attachments/assets/308099e1-683e-4a13-aeff-bd24d8dc7f97" />

②ナレッジベースを作成を押す

<img width="803" height="272" alt="image" src="https://github.com/user-attachments/assets/48d59207-a779-4347-bc6f-4c125272532a" />

③テキストファイルをアップロードの「参照」をおすとファイルが選択できるので、１で作成したcsvファイル「佐賀出身の偉人.csv」を選択する。

<img width="599" height="429" alt="image" src="https://github.com/user-attachments/assets/63596608-a66b-4bf5-86bb-bb290b1450f2" />

④「次へ」を押す

<img width="657" height="390" alt="image" src="https://github.com/user-attachments/assets/b0ddd624-47e7-4d15-a101-6ce156195737" />

⑤「チャンク設定」の「チャンクのオーバーラップ」の値を０にする

<img width="498" height="251" alt="image" src="https://github.com/user-attachments/assets/a3bd5a2f-aa4b-4718-9a45-9941d0d6969e" />

⑥「チャンクをプレビュー」を押すと、右側にチャンクプレビューが表示される

<img width="534" height="470" alt="image" src="https://github.com/user-attachments/assets/1cab0e94-ddb5-46b0-9e5c-be301c148ab0" />

ポイント解説：チャンクとは？
・・・・・

⑦左側の画面を一番下までスクロールし、「保存して処理」を押す

<img width="1097" height="590" alt="image" src="https://github.com/user-attachments/assets/f947e88b-2048-4365-b613-3237ce0ca380" />

⑧ナレッジベース作成完了！「ドキュメントに移動」

<img width="552" height="427" alt="image" src="https://github.com/user-attachments/assets/be61c40c-681e-4ae8-9547-630e58ef475e" />

⑩画面左のバーにある「検索テスト」を押す

<img width="1125" height="299" alt="image" src="https://github.com/user-attachments/assets/9380c949-8a29-48b4-a3bd-cae34610984c" />

⑪ソーステキストに任意の文字、例えば「総理大臣」を入れて「テスト」をおすと右側に検索結果が表示される。

<img width="1112" height="425" alt="image" src="https://github.com/user-attachments/assets/defcc019-d004-4039-96a4-cf7c5479c1da" />

ポイント解説：セマンティック検索
検索結果には「総理大臣」という文字が含まれていないにもかかわらず、検索結果として表示されています。

これは、DifyのようなRAG（Retrieval-Augmented Generation）ツールが、キーワードの完全一致だけでなく、**意味的な類似性（セマンティック検索）**に基づいて関連性の高い情報を取得しているためです。

この画面に表示されている結果は以下の内容を示唆しています。

検索クエリとチャンクの関連性: 検索キーワード「総理大臣」と、検索結果として表示された3つのチャンクの間に、意味的な関連性があるとDifyが判断したということです。

Chunk-07: 「大隈重信」に関する記述です。「大隈重信」は内閣総理大臣を務めており、「総理大臣」という言葉と意味的に関連性が高いと判断されたと考えられます。

Chunk-04: 「副島種臣」に関する記述です。「外交」や「近代日本の外交基盤」といったキーワードが、内閣総理大臣の職務と関連性が高いと判断された可能性があります。

Chunk-09: 「枝吉神陽」に関する記述です。「藩政改革」という言葉が、近代国家の礎を築いた「総理大臣」という役割と意味的に関連があると判断された可能性があります。

スコアと関連性の高さ: 各チャンクには「SCORE」が表示されており、これは検索クエリとの関連性の高さを示しています。このスコアが高いほど、より関連性の高い情報だと判断されています。

このように、Difyは単なる文字列検索ではなく、**ベクトル検索（意味をベクトル化して類似度を測る）**を用いることで、「総理大臣」という文字が含まれていないにもかかわらず、その概念や役割に関連する人物の情報を正確に引き出しているのです。

３、dify上でナレッジを使ったチャットボットを作る

①Dify上でチャットボットを作成する
アプリを作成→最初から作成→チャットボット→アプリ名を入力→「作成」を押す

<img width="164" height="92" alt="image" src="https://github.com/user-attachments/assets/b26d2d4b-ec5e-4dc6-bfa1-716fd230d135" />

<img width="626" height="343" alt="image" src="https://github.com/user-attachments/assets/85fcd517-7868-49cd-8227-24538a456378" />

プロンプトに以下を入力

あなたは佐賀県の歴史に詳しい案内人です。
以下の「コンテキスト」に含まれる情報を最優先に使って質問に答えてください。
コンテキストに情報がない場合は「このナレッジには情報がありません」と答えてください。

②「コンテキスト」の「追加」をおす

<img width="639" height="458" alt="image" src="https://github.com/user-attachments/assets/d8514065-9194-4d65-973c-93dedf8c5e99" />

③参照する知識が選択できるので「佐賀出身の偉人」を選択し、「追加」

<img width="208" height="109" alt="image" src="https://github.com/user-attachments/assets/b83df8e8-7736-4a8c-9392-e4e995028b0c" />

追加されたコンテキストの右側に円ぴーつマークがあらわれるので押すと「ナレッジベースの設定」がでてくるので、「検索設定」を「ハイブリッド検索」にする
<img width="484" height="539" alt="image" src="https://github.com/user-attachments/assets/12c7644c-94be-4ab9-b4ce-897a11e31316" />


４，slack app側の設定をする

Bot TokenをSlack側で発行する

Slack API: Your Apps
 にアクセス
Slackアカウントでログインしてる必要あり

真ん中の 「Create New App」 をクリック

<img width="1105" height="478" alt="image" src="https://github.com/user-attachments/assets/e0db8f53-06b0-478d-8060-71dcc87d405e" />

ポップアップが出たら

「From scratch」 を選ぶ（ゼロから作成）

App Name：わかりやすい名前（例：佐賀偉人Bot）

Pick a workspace to develop your app in：
Botを導入したいSlackワークスペースを選ぶ
<img width="400" height="389" alt="image" src="https://github.com/user-attachments/assets/24264515-6f29-4008-ad93-1ac519f559c2" />

Create App を押すと、アプリが作成される

アプリ管理メニューの左側のバーに「OAuth ＆ Permissons」が表示されるので、押す
<img width="271" height="522" alt="image" src="https://github.com/user-attachments/assets/5101d004-2dfd-428d-a933-63f8fc2adc86" />

Scopes→Add an OAuth Scopeを押す
<img width="529" height="500" alt="image" src="https://github.com/user-attachments/assets/15c97fd7-120a-4992-92dc-a89b353a8647" />

以下の二つを選択し、追加する。
app_mentions:read
　→ Slackで @佐賀偉人Bot と呼ばれたときに反応できる
chat:write
　→ BotがSlackにメッセージを返せる
<img width="457" height="209" alt="image" src="https://github.com/user-attachments/assets/685c16d0-5ea3-494d-9cec-8cedf56926d8" />

追加されると以下のように表示される
<img width="500" height="326" alt="image" src="https://github.com/user-attachments/assets/485ad05e-e395-4ffb-ad06-81b2d5b7f10b" />


次に、左バーの「App Home」を選択する
<img width="752" height="523" alt="image" src="https://github.com/user-attachments/assets/a4dd99d2-ad3a-462a-af1c-a3e6285984c2" />

Your App’s Presence in Slack→App Display Name→Editを押す
<img width="514" height="289" alt="image" src="https://github.com/user-attachments/assets/fa11c5d3-cc47-4847-a901-2251a813889c" />

Display Name (Bot Name)
→ Slackに表示される名前（自由につけてOK）
例：佐賀偉人Bot

Default username
→ Slackで @ で呼び出すときの名前（小文字・英数字のみ）
例：sagaijinbot
を入れて「Add」を押す
<img width="407" height="392" alt="image" src="https://github.com/user-attachments/assets/79d618ac-70dd-4ea3-8cff-7797b93da7c5" />

再度「OAuth & Permissions」に戻る。
<img width="856" height="530" alt="image" src="https://github.com/user-attachments/assets/c0d9906d-1306-409a-bee2-4119811343e2" />

「OAuth TOkens」→「Install to {ワークスペース名}」を押す
<img width="837" height="539" alt="image" src="https://github.com/user-attachments/assets/fbefabb7-8fea-4db8-a906-601a67172731" />

下記のような画面が出てくるので「許可する」を押す
<img width="947" height="419" alt="image" src="https://github.com/user-attachments/assets/f2f8afc1-1646-4bd1-8a6c-d0b4d92b9b78" />

OAuth Tokensの「Bot User OAuth Token」をコピーする（メモ帳などにはりつけて保存しておく）
<img width="808" height="514" alt="image" src="https://github.com/user-attachments/assets/da86261d-dee6-48eb-b35a-29be33496327" />

５、DIfyにスラックボットプラグインをインストールして

①Difyマーケットプレイスに接続する（https://marketplace.dify.ai/）と、以下の画面が表示されるので、検索バーに「Slack Bot」と入力し、Slack Botをクリック。

<img width="656" height="373" alt="image" src="https://github.com/user-attachments/assets/c3cc01f6-04b7-4f07-b5a6-d9afda577c2e" />

②「Install」をクリック

<img width="620" height="294" alt="image" src="https://github.com/user-attachments/assets/fa742279-6151-4b69-9748-5966af2c342b" />

⑥もう一度インストールを押す画面が表示されるのでそれを押すと、下記のようにインストール表示成功画面が出る。

<img width="290" height="173" alt="image" src="https://github.com/user-attachments/assets/ccb8bafa-c698-44cf-8808-33d98cb61661" />

Dify画面右上の「プラグイン」を押して、Slack　Botを選択して押す

<img width="641" height="224" alt="image" src="https://github.com/user-attachments/assets/962da02e-5d94-4b6f-9aae-2200311f23d8" />

右側に画面が表示されるので、「エンドポイント」の「＋」マークを押す

<img width="212" height="117" alt="image" src="https://github.com/user-attachments/assets/5f5217de-de7e-4fd1-a6f4-6199ad7fd49f" />


エンドポイント名
　→ わかりやすい名前をつける（自由）
　例：佐賀偉人Bot

Bot Token
　→ Slackで「Install to Workspace」したときに発行された
　　xoxb-... で始まる Bot User OAuth Token をコピペ

アプリ
　→ Difyで作った「佐賀偉人ナレッジ付きチャットボット」を選択

「保存」ボタンを押す

<img width="329" height="320" alt="image" src="https://github.com/user-attachments/assets/99c88e87-64de-409c-94d8-5712bc2963b0" />

POST URLが発行されるので、https://以降をコピーする
<img width="329" height="223" alt="image" src="https://github.com/user-attachments/assets/756afea6-1a82-4c3e-a85f-e928b1ceabbf" />

Slack APIの管理画面に戻り、Event Subscriptions→Enable EventsをONにする
<img width="1097" height="534" alt="image" src="https://github.com/user-attachments/assets/18ef1a79-69e3-483f-8f82-936b6e144140" />

先ほどDify側でコピペしたPOST URLをはりつけて→Verifiedが表示されればOK
<img width="704" height="443" alt="image" src="https://github.com/user-attachments/assets/192bb98e-1bad-44ff-a01e-8249b3d1496f" />

下にある「Sabscribe to bot events」をクリック
<img width="543" height="450" alt="image" src="https://github.com/user-attachments/assets/58a3f019-4412-4052-89d2-b52443dcea03" />

Add Bot User Eventを押すと選択肢が表れるので、app_mention（@メンションされたとき）
message.im（DM受信）を追加
<img width="488" height="245" alt="image" src="https://github.com/user-attachments/assets/455d583a-174b-4bf0-bb94-3a862e1d839a" />

正しく選べていたら、「Save Changes」を押す
<img width="654" height="491" alt="image" src="https://github.com/user-attachments/assets/ced076b1-eea0-49e3-ad43-04bcaf5a4ef5" />

以下のエラーが出るので（権限（Scopes）を変えたら必ず再インストールが必要）、以下を再度操作。

＜エラー＞
You’ve changed the permission scopes your app uses. Please reinstall your app for these changes to take effect (and if your app is listed in the Slack Marketplace, you’ll need to resubmit it as well).

＜再度操作する内容＞
Slack APIコンソール → OAuth & Permissions
上部の Install to Workspace（または Reinstall to Workspace）→ 許可
画面に出る Bot User OAuth Token（xoxb-…） をコピー
もし前と違うトークンになったら、Dify側のBot Tokenも更新して保存


スラック上でボットを呼び出す
適当なチャンネル（例: #all-my）を開く
/invite @佐賀偉人Bot を実行してBotをそのチャンネルに招待

<img width="848" height="592" alt="image" src="https://github.com/user-attachments/assets/55e62f53-2b66-4e75-8195-88441edebeb7" />

@佐賀偉人Botでメンションして、会話をしてみよう！

<img width="559" height="389" alt="image" src="https://github.com/user-attachments/assets/ba7fb2f9-3f38-4c68-b167-51625e8f7b8d" />

もし途中で躓いたら、GPTやGeminiに操作中の画面の画像を送って、わからないポイントを聞くと教えてくれるよ！



































