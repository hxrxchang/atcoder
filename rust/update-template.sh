#!/bin/bash

# compete.toml のパス
COMPETE_TOML="compete.toml"
# 埋め込むテンプレートファイルのパス
TEMPLATE_RS="./src/main.rs"
# 一時ファイルの名前
TEMP_TOML="${COMPETE_TOML}.tmp"

# template.rs が存在するかチェック
if [ ! -f "$TEMPLATE_RS" ]; then
    echo "エラー: $TEMPLATE_RS が見つかりません。作成してください。"
    exit 1
fi

# compete.toml が存在するかチェック
if [ ! -f "$COMPETE_TOML" ]; then
    echo "エラー: $COMPETE_TOML が見つかりません。"
    echo "cargo compete init を実行して $COMPETE_TOML を作成してください。"
    exit 1
fi

# template.rs の内容を読み込む (改行を保持)
# read -r -d '' は、末尾の改行を含めてファイルの内容を正確に読み込むための安全な方法です
read -r -d '' TEMPLATE_CONTENT < "$TEMPLATE_RS"

# compete.toml を行ごとに処理し、新しい内容を一時ファイルに書き出す
# STATE変数を使って、どのセクションを処理しているかを追跡します
STATE="NORMAL" # NORMAL, IN_TEMPLATE_SECTION

# 一時ファイルを空にし、処理を開始
> "$TEMP_TOML"

while IFS= read -r line; do
    if [[ "$line" =~ ^\[template\] ]]; then
        # [template] セクションの開始を検出したら、新しいテンプレートブロックを挿入
        echo "[template]" >> "$TEMP_TOML"
        echo "src = '''" >> "$TEMP_TOML"
        echo "$TEMPLATE_CONTENT" >> "$TEMP_TOML"
        echo "'''" >> "$TEMP_TOML"
        STATE="IN_TEMPLATE_SECTION"
        continue # この行は処理したので次の行へ
    fi

    # テンプレートセクション内にいる場合
    if [[ "$STATE" == "IN_TEMPLATE_SECTION" ]]; then
        # 既存の src = ... の行はスキップ
        if [[ "$line" =~ ^src[[:space:]]*= ]]; then
            continue
        # 次のセクションが始まったら、状態をリセットし、その行を出力
        elif [[ "$line" =~ ^\[.+\] ]]; then
            echo "$line" >> "$TEMP_TOML"
            STATE="NORMAL"
            continue
        fi
        # テンプレートブロックの内部にある他の行（空行、コメントなど）はスキップ
        if [[ "$line" =~ ^[[:space:]]*$ ]] || [[ "$line" =~ ^# ]]; then
            continue
        fi
    fi

    # 通常の状態の場合、またはテンプレートセクションを抜けた後に、現在の行を出力
    if [[ "$STATE" == "NORMAL" ]]; then
        echo "$line" >> "$TEMP_TOML"
    fi

done < "$COMPETE_TOML"

# 元のファイルを一時ファイルで置き換える
mv "$TEMP_TOML" "$COMPETE_TOML"

echo "$TEMPLATE_RS の内容を $COMPETE_TOML に正常に埋め込みました。"
