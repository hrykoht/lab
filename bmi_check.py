# -*- coding: utf-8 -*-

# ユーザが入力した値が小数に変換可能かを判定する
def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

# ユーザ入力(身長)
height = input("身長を入力してください(cm):")

# ユーザ入力(身長)が小数に変換できない値だった場合は終了する
if not is_num(height):
   print("身長の入力は数字(cm)でお願いします")
   input()
   print("入力エラーのため終了します")
   exit()

# ユーザ入力(体重)
weight = input("体重を入力してください(kg):")

# ユーザ入力(体重)が小数に変換できない値だった場合は終了する
if not is_num(weight):
   print("体重の入力は数字(kg)でお願いします")
   input()
   print("入力エラーのため終了します")
   exit()

# ユーザ入力は文字列入力のため小数に変換
height = float(height)
weight = float(weight)

# BMI値を計算する
bmi = weight / pow (height,2)
bmi = bmi * 10000
    
# BMI値をユーザに通知する（小数点以下第1位までを出力する）
print('あなたの BMI 値は {:.1f} です'.format(bmi))

# BMI値によって通知メッセージを分岐する
if bmi < 18.5:
    print('すこし痩せすぎのようです')

elif 18.5 <= bmi < 25.0:
    print('標準的な体型です')

elif 25.0 <= bmi < 30.0:
    print('すこし肥満傾向にあるようです')
    print('生活習慣を見直しましょう')

else:
    print('高度な肥満です')
    print('最寄りの病院に相談しましょう')
