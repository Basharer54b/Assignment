# Exercise 1.1
"""
في نظام لأحد صالات الانترنت يتم احتساب مبلغ مالي يدفعه الزبائن بناء على عدد الساعات.
وبفرض يتم احتساب 500 ل.س لكل ساعة.

  الموظف  يستخدم الكود التالي ويقوم بإدخال اسم الزبون وعدد الساعات وسعر الساعة الواحدة من أجل حساب المبلغ المطلوب.
 بناء على ماسبق أكمل الكود التالي  لحساب مايتوجب دفعه من قبل كل زبون وإظهار المعلومات على الشاشة.
 بالإضافة إلى كتابة المعلومات في الملف 'Pays.txt'بالشكل التالي:
 |ali|   |5.0 (Hours)|   |2500.0 (Bounds)|
|ahmed|   |2.0 (Hours)|   |1000.0 (Bounds)|
"""
while True:
    name = input('Enter Name: ')
    hours = float(input('Enter Hours: '))
    price =
    pay =
    info = f'|{name}|   |{} (Hours)|   |{} (Bounds)|'
    print(info)
    with open(   ,'a+') as file:
        file.write(info+'\n')
    cmd = input("to exit type 'exit' and press ENTER\nto add new information press only ENTER\n:")
    if cmd.lower() == :
