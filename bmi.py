
weight = int(input('体重は？(kg)'))
height = int(input('身長は？(cm)')) * 0.01
bmi = round(weight / (height ** 2), 2)
print(bmi)

if bmi < 18.5:
    print('痩せ型')
elif 18.5 < bmi < 25:
    print('普通体重')
else:
    print('肥満')

app_weight = round((height ** 2) * 22)
print('適正体重は{}kg'.format(app_weight))
