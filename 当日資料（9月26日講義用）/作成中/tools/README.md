# CSVデータジェネレーター

## 概要

AIで生成するデータは「嘘っぽく」なりがちです。そこで、統計的な分布やビジネスロジックを組み込んだPythonプログラムで、よりリアルなテストデータを生成するツールを作成しました。

## 特徴

- 🎲 **統計的分布**: 正規分布、指数分布、重み付き選択など
- 🔗 **相関関係**: 列間の論理的な関連性を定義可能
- 📝 **JSON設定**: データ構造を外部設定ファイルで管理
- 🌱 **再現性**: シード値で同じデータを再生成可能
- 🎯 **汎用性**: 様々なタイプのデータに対応

## インストール

```bash
# 必要なライブラリをインストール
pip install numpy
```

## 使い方

### 基本的な使い方

```bash
# レビューデータを20行生成（デフォルト）
python csv_generator.py --config configs/review_config.json

# 売上データを100行生成
python csv_generator.py --config configs/sales_config.json --rows 100

# 出力ファイル名を指定
python csv_generator.py --config configs/tourist_config.json --output my_data.csv --rows 50

# シード値を指定（再現可能なデータ生成）
python csv_generator.py --config configs/sales_config.json --rows 100 --seed 42
```

### コマンドラインオプション

| オプション | 短縮形 | 説明 | デフォルト |
|:-----------|:-------|:-----|:-----------|
| --config | -c | 設定ファイルのパス（必須） | - |
| --output | -o | 出力CSVファイル名 | 設定ファイルで指定 |
| --rows | -r | 生成する行数 | 20 |
| --seed | -s | 乱数シード（再現性のため） | なし |

## 設定ファイルの構造

### 基本構造

```json
{
  "name": "データセット名",
  "description": "説明",
  "output_file": "出力ファイル名.csv",
  "seed": null,
  "columns": [...],
  "correlations": [...]
}
```

### 列（columns）の定義

#### 1. choice型（選択肢から選ぶ）

```json
{
  "name": "product_name",
  "type": "choice",
  "choices": ["商品A", "商品B", "商品C"]
}
```

重み付き選択：
```json
{
  "name": "store_location",
  "type": "choice",
  "choices": {
    "佐賀市": 0.35,
    "唐津市": 0.25,
    "鳥栖市": 0.20
  }
}
```

#### 2. integer型（整数）

```json
{
  "name": "quantity",
  "type": "integer",
  "min": 1,
  "max": 100,
  "distribution": "normal",
  "mean": 50,
  "std": 15
}
```

分布タイプ：
- `uniform`: 一様分布（デフォルト）
- `normal`: 正規分布
- `exponential`: 指数分布

#### 3. float型（浮動小数点数）

```json
{
  "name": "temperature",
  "type": "float",
  "min": -5.0,
  "max": 35.0,
  "decimals": 1,
  "distribution": "normal",
  "mean": 20.0,
  "std": 8.0
}
```

#### 4. date型（日付）

```json
{
  "name": "visit_date",
  "type": "date",
  "start": "2024-01-01",
  "end": "2024-12-31",
  "format": "%Y-%m-%d"
}
```

#### 5. text型（テンプレートベースのテキスト）

```json
{
  "name": "review_text",
  "type": "text",
  "templates": [
    "{quality}で{emotion}。",
    "{feature}が{evaluation}です。"
  ],
  "replacements": {
    "quality": ["良い", "普通", "悪い"],
    "emotion": ["満足", "普通", "不満"],
    "feature": ["味", "香り", "見た目"],
    "evaluation": ["最高", "良い", "普通"]
  }
}
```

#### 6. id型（ID生成）

```json
{
  "name": "customer_id",
  "type": "id",
  "prefix": "CUS",
  "sequential": true,
  "padding": 5
}
```

#### 7. calculated型（計算値）

```json
{
  "name": "total_amount",
  "type": "calculated",
  "formula": "quantity * unit_price"
}
```

### 相関関係（correlations）の定義

列間の論理的な関係を定義できます：

```json
{
  "correlations": [
    {
      "source": "product_name",
      "target": "unit_price",
      "rules": {
        "高級品": {"min": 10000, "max": 50000},
        "普通品": {"min": 1000, "max": 10000}
      }
    }
  ]
}
```

## 提供されている設定ファイル

### 1. review_config.json（レビューデータ）
- 商品レビューのテキストと評価
- 評価に応じたレビュー内容の変化
- 正規分布による評価の分布

### 2. sales_config.json（売上データ）
- 日次の売上トランザクション
- 商品と価格の相関
- 年齢層と支払方法の相関

### 3. tourist_config.json（観光客データ）
- 観光客の属性と行動
- 出身地と滞在日数の相関
- グループサイズと消費額の相関

## カスタム設定の作成

新しいデータタイプを作成する場合：

1. `configs/`ディレクトリに新しいJSONファイルを作成
2. 必要な列を定義
3. 相関関係を設定（オプション）
4. ジェネレーターを実行

例：`configs/my_custom_data.json`
```json
{
  "name": "カスタムデータ",
  "output_file": "custom.csv",
  "columns": [
    {
      "name": "id",
      "type": "id",
      "prefix": "ID",
      "sequential": true
    },
    {
      "name": "value",
      "type": "integer",
      "min": 0,
      "max": 100
    }
  ]
}
```

## 統計的分布の活用

### 正規分布の使い方
- 自然なばらつきを表現（身長、体重、テストの点数など）
- `mean`（平均）と`std`（標準偏差）で制御

### 指数分布の使い方
- 待ち時間や間隔を表現（購入間隔、故障までの時間など）
- `scale`パラメータで分布を調整

### 重み付き選択
- 現実的な比率を再現（地域別の顧客分布など）
- 合計が1.0になるように重みを設定

## トラブルシューティング

### エラー: ModuleNotFoundError: No module named 'numpy'
```bash
pip install numpy
```

### 文字化けする場合
- 出力ファイルはUTF-8 with BOMで保存されます
- Excelで開く際は「データ」→「テキストファイル」から開いてください

### データが偏っている
- 設定ファイルの`distribution`や`mean`、`std`を調整
- `seed`値を変更して異なるパターンを試す

## 高度な使い方

### バッチ処理
```bash
# 複数のデータセットを一度に生成
for config in configs/*.json; do
    python csv_generator.py --config "$config" --rows 100
done
```

### 大量データの生成
```bash
# 10万行のデータを生成（メモリに注意）
python csv_generator.py --config configs/sales_config.json --rows 100000
```

### プログラムから利用
```python
from csv_generator import DataGenerator, load_config

# 設定を読み込み
config = load_config('configs/sales_config.json')

# ジェネレーターを作成
generator = DataGenerator(config)

# データを生成
dataset = generator.generate_dataset(100)

# CSVに保存
generator.save_to_csv(dataset, 'output.csv')
```

## なぜプログラムで生成するのか？

### AIによる生成の問題点
- パターンが単調になりがち
- 論理的な矛盾が発生しやすい
- 統計的な分布が不自然

### プログラムによる生成の利点
- **制御可能**: 正確な分布と相関を定義
- **再現性**: シード値で同じデータを再生成
- **拡張性**: 新しいロジックを簡単に追加
- **高速**: 大量データも瞬時に生成
- **品質**: ビジネスルールを確実に適用

## ライセンス

教育目的で自由に使用・改変可能です。

## 作成者

SAGA Creative Link Workshop のために作成