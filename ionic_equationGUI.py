import tkinter as tk
import random
import time

# イオン式の辞書を作成する
ionic_equations = {
    # 一価陽イオン
    "水素イオン": "H+",
    "リチウムイオン": "Li+",
    "ナトリウムイオン": "Na+",
    "カリウムイオン": "K+",
    "銅(I)イオン": "Cu+",
    "銀イオン": "Ag+",
    "アンモニウムイオン": "NH4+",
    "オキソニウムイオン": "H3O+",
    #二価陽イオン
    "マグネシウムイオン": "Mg2+",
    "カルシウムイオン": "Ca2+",
    "バリウムイオン": "Ba2+",
    "亜鉛イオン": "Zn2+",
    "スズ(Ⅱ)イオン": "Sn2+",
    "鉛イオン": "Pb2+",
    "銅(II)イオン": "Cu2+",
    "鉄(II)イオン": "Fe2+",
    "マンガンイオン": "Mn2+",
    # 三価陽イオン
    "アルミニウムイオン": "Al3+",
    "クロム(III)イオン": "Cr3+",
    "鉄(III)イオン": "Fe3+",
    # 一価陰イオン
    "フッ化物イオン": "F-",
    "塩化物イオン": "Cl-",
    "臭化物イオン": "Br-",
    "ヨウ化物イオン": "I-",
    "水酸化物イオン": "OH-",
    "硝酸イオン": "NO3-",
    "酢酸イオン": "CH3COO-",
    "炭酸水素イオン": "HCO3-",
    "シアン化物イオン": "CN-",
    # 二価陰イオン
    "酸化物イオン": "O2-",
    "硫化物イオン": "S2-",
    "硫酸イオン": "SO42-",
    "炭酸イオン": "CO32-",
    "亜硫酸イオン": "SO32-",
    # 三価陰イオン
    "リン酸イオン": "PO43-",
    # 他のイオン式を追加する
}


# 正解をチェックする関数
def check_answer(event=None):  # event引数を追加
    user_input = entry.get()
    correct_answer = ionic_equations.get(name_label['text'])
    if user_input == correct_answer:
        result_label.config(text="正解!")
    else:
        result_label.config(text=f"不正解! イオン式: {correct_answer}")
    root.update_idletasks()  # 現在の変更を画面に反映
    time.sleep(2)  # 2秒間待機
    new_problem()  # 新しい問題を自動で出す

# 新しい問題を出す関数
def new_problem():
    global name_label
    name = random.choice(list(ionic_equations.keys()))
    name_label.config(text=name)
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUIを作成する
root = tk.Tk()
root.title("イオン式クイズ")
root.geometry("190x90")

# イオンの日本語名を表示するラベル
name_label = tk.Label(root, text=random.choice(list(ionic_equations.keys())), font=("Helvetica", 18))
name_label.pack()

# ユーザーの入力を受け取るエントリー
entry = tk.Entry(root, font=("Helvetica", 17))
entry.pack()
entry.bind('<Return>', check_answer)  # Enterキーにcheck_answer関数をバインド

# 結果を表示するラベル
result_label = tk.Label(root, text="", font=("Helvetica", 16 ))
result_label.pack()

# 新しい問題を出す
new_problem()

# GUIを実行する
root.mainloop()