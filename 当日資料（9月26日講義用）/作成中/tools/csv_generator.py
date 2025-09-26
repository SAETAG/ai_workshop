#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
汎用CSVデータジェネレーター
リアルなテストデータを生成するためのツール

使用例:
    python csv_generator.py --config sales_config.json --output sales_data.csv --rows 100
"""

import csv
import json
import random
import argparse
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
import numpy as np
from pathlib import Path
import sys

# 日本語サポート
import locale
locale.setlocale(locale.LC_ALL, '')

class DataGenerator:
    """汎用的なデータジェネレータークラス"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        設定を読み込んでジェネレーターを初期化
        
        Args:
            config: 設定辞書
        """
        self.config = config
        self.columns = config['columns']
        self.correlations = config.get('correlations', [])
        self.distributions = config.get('distributions', {})
        self.seed = config.get('seed', None)
        
        if self.seed:
            random.seed(self.seed)
            np.random.seed(self.seed)
    
    def generate_value(self, column_config: Dict[str, Any], row_data: Dict[str, Any] = None) -> Any:
        """
        列の設定に基づいて値を生成
        
        Args:
            column_config: 列の設定
            row_data: 現在の行データ（相関がある場合に使用）
        
        Returns:
            生成された値
        """
        col_type = column_config['type']
        
        if col_type == 'choice':
            # 選択肢から選ぶ
            choices = column_config['choices']
            if isinstance(choices, dict):
                # 重み付き選択
                items = list(choices.keys())
                weights = list(choices.values())
                return np.random.choice(items, p=weights)
            else:
                return random.choice(choices)
        
        elif col_type == 'integer':
            # 整数値
            min_val = column_config.get('min', 0)
            max_val = column_config.get('max', 100)
            distribution = column_config.get('distribution', 'uniform')
            
            if distribution == 'normal':
                # 正規分布
                mean = column_config.get('mean', (min_val + max_val) / 2)
                std = column_config.get('std', (max_val - min_val) / 6)
                value = int(np.random.normal(mean, std))
                return max(min_val, min(max_val, value))
            elif distribution == 'exponential':
                # 指数分布
                scale = column_config.get('scale', 10)
                value = int(np.random.exponential(scale))
                return max(min_val, min(max_val, value))
            else:
                # 一様分布
                return random.randint(min_val, max_val)
        
        elif col_type == 'float':
            # 浮動小数点数
            min_val = column_config.get('min', 0.0)
            max_val = column_config.get('max', 100.0)
            decimals = column_config.get('decimals', 2)
            distribution = column_config.get('distribution', 'uniform')
            
            if distribution == 'normal':
                mean = column_config.get('mean', (min_val + max_val) / 2)
                std = column_config.get('std', (max_val - min_val) / 6)
                value = np.random.normal(mean, std)
                value = max(min_val, min(max_val, value))
            else:
                value = random.uniform(min_val, max_val)
            
            return round(value, decimals)
        
        elif col_type == 'date':
            # 日付
            start_date = datetime.strptime(column_config['start'], '%Y-%m-%d')
            end_date = datetime.strptime(column_config['end'], '%Y-%m-%d')
            days_between = (end_date - start_date).days
            random_days = random.randint(0, days_between)
            random_date = start_date + timedelta(days=random_days)
            
            format_str = column_config.get('format', '%Y-%m-%d')
            return random_date.strftime(format_str)
        
        elif col_type == 'text':
            # テキスト（テンプレートベース）
            templates = column_config.get('templates', ['Sample text {n}'])
            template = random.choice(templates)
            
            # プレースホルダーを置換
            replacements = column_config.get('replacements', {})
            for key, values in replacements.items():
                if isinstance(values, list):
                    value = random.choice(values)
                else:
                    value = values
                template = template.replace(f'{{{key}}}', str(value))
            
            # 行番号を置換
            if row_data:
                template = template.replace('{row_num}', str(row_data.get('_row_num', 0)))
            
            return template
        
        elif col_type == 'id':
            # ID（連番またはUUID風）
            prefix = column_config.get('prefix', '')
            if column_config.get('sequential', False):
                # 連番（行番号を使用）
                if row_data:
                    num = row_data.get('_row_num', 0)
                else:
                    num = 0
                padding = column_config.get('padding', 3)
                return f"{prefix}{str(num).zfill(padding)}"
            else:
                # ランダムID
                length = column_config.get('length', 6)
                chars = column_config.get('chars', '0123456789ABCDEF')
                return prefix + ''.join(random.choices(chars, k=length))
        
        elif col_type == 'calculated':
            # 他の列から計算
            formula = column_config['formula']
            if row_data:
                # 簡易的な式評価（実際の用途では eval は避けるべき）
                # ここでは教育目的のため簡略化
                local_vars = dict(row_data)
                local_vars['random'] = random
                local_vars['np'] = np
                try:
                    return eval(formula, {"__builtins__": {}}, local_vars)
                except:
                    return 0
            return 0
        
        else:
            return "N/A"
    
    def apply_correlations(self, row_data: Dict[str, Any]) -> None:
        """
        相関関係を適用
        
        Args:
            row_data: 行データ
        """
        for correlation in self.correlations:
            source = correlation.get('source')
            target = correlation.get('target')
            rules = correlation.get('rules', {})
            
            if source in row_data:
                source_value = row_data[source]
                if source_value in rules:
                    # ルールに基づいて値を調整
                    target_config = rules[source_value]
                    if isinstance(target_config, dict):
                        # 新しい設定で再生成
                        col_config = next((c for c in self.columns if c['name'] == target), None)
                        if col_config:
                            merged_config = {**col_config, **target_config}
                            row_data[target] = self.generate_value(merged_config, row_data)
                    else:
                        # 直接値を設定
                        row_data[target] = target_config
    
    def generate_row(self, row_num: int) -> Dict[str, Any]:
        """
        1行分のデータを生成
        
        Args:
            row_num: 行番号
        
        Returns:
            生成された行データ
        """
        row_data = {'_row_num': row_num}
        
        # 各列の値を生成
        for column in self.columns:
            col_name = column['name']
            row_data[col_name] = self.generate_value(column, row_data)
        
        # 相関関係を適用
        self.apply_correlations(row_data)
        
        # 内部用のフィールドを削除
        del row_data['_row_num']
        
        return row_data
    
    def generate_dataset(self, num_rows: int) -> List[Dict[str, Any]]:
        """
        データセットを生成
        
        Args:
            num_rows: 生成する行数
        
        Returns:
            生成されたデータセット
        """
        dataset = []
        for i in range(1, num_rows + 1):
            row = self.generate_row(i)
            dataset.append(row)
        
        # 分布調整（必要に応じて）
        if self.distributions:
            dataset = self.adjust_distributions(dataset)
        
        return dataset
    
    def adjust_distributions(self, dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        全体的な分布を調整
        
        Args:
            dataset: データセット
        
        Returns:
            調整済みデータセット
        """
        # ここでは簡略化のため、基本的な調整のみ
        # 実際にはより高度な調整が可能
        return dataset
    
    def save_to_csv(self, dataset: List[Dict[str, Any]], output_path: str) -> None:
        """
        CSVファイルに保存
        
        Args:
            dataset: データセット
            output_path: 出力ファイルパス
        """
        if not dataset:
            print("データセットが空です")
            return
        
        # ヘッダーを列設定から取得
        headers = [col['name'] for col in self.columns]
        
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            for row in dataset:
                # 定義された列のみを出力
                filtered_row = {k: v for k, v in row.items() if k in headers}
                writer.writerow(filtered_row)
        
        print(f"✅ {len(dataset)}行のデータを {output_path} に保存しました")


def load_config(config_path: str) -> Dict[str, Any]:
    """
    設定ファイルを読み込む
    
    Args:
        config_path: 設定ファイルのパス
    
    Returns:
        設定辞書
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='リアルなCSVテストデータを生成します',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 売上データを100行生成
  python csv_generator.py --config configs/sales_config.json --rows 100
  
  # シード値を指定して再現可能なデータを生成
  python csv_generator.py --config configs/review_config.json --rows 50 --seed 42
        """
    )
    
    parser.add_argument(
        '--config', '-c',
        required=True,
        help='設定ファイルのパス (JSON形式)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='出力CSVファイルのパス（省略時は設定ファイルから取得）'
    )
    
    parser.add_argument(
        '--rows', '-r',
        type=int,
        default=20,
        help='生成する行数 (デフォルト: 20)'
    )
    
    parser.add_argument(
        '--seed', '-s',
        type=int,
        help='乱数シード値（再現性のため）'
    )
    
    args = parser.parse_args()
    
    try:
        # 設定を読み込む
        config = load_config(args.config)
        
        # シード値を上書き（指定された場合）
        if args.seed is not None:
            config['seed'] = args.seed
        
        # ジェネレーターを作成
        generator = DataGenerator(config)
        
        # データセットを生成
        dataset = generator.generate_dataset(args.rows)
        
        # 出力パスを決定
        output_path = args.output or config.get('output_file', 'output.csv')
        
        # CSVに保存
        generator.save_to_csv(dataset, output_path)
        
        # サンプル表示
        print("\n📊 生成されたデータのサンプル（最初の3行）:")
        for i, row in enumerate(dataset[:3], 1):
            print(f"\n行 {i}:")
            for key, value in row.items():
                print(f"  {key}: {value}")
        
    except FileNotFoundError:
        print(f"❌ エラー: 設定ファイル '{args.config}' が見つかりません")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ エラー: 設定ファイルのJSON形式が不正です: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ エラー: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()