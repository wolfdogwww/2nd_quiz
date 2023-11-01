student_info = {}

student_info['student_id'] = input("請輸入您的學號：")
student_info['name'] = input("請輸入您的姓名：")
student_info['chinese_score'] = float(input("請輸入您的國文成績："))
student_info['math_score'] = float(input("請輸入您的數學成績："))
student_info['computer_score'] = float(input("請輸入您的電腦成績："))

# 計算總分和平均分數
total_score = student_info['chinese_score'] + student_info['math_score'] + student_info['computer_score']
average_score = total_score / 3

# 判定成績
if average_score >= 60:
    grade_status = "合格"
else:
    grade_status = "不合格"

# 輸出結果
print("------------------------------")
print(f"{student_info['name']}({student_info['student_id']})同學您好：")
print(f"以下是您的各科成績與分數評定", end='\r\n\r\n')
print(f"國文：{student_info['chinese_score']} / 數學：{student_info['math_score']} / 電腦：{student_info['computer_score']}")
print(f"總分：{total_score} / 平均：{round(average_score, 2)}")
print("------------------------------")
print(f"成績判定：{grade_status}")
print()