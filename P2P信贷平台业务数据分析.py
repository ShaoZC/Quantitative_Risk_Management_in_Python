import numpy
import pandas
import matplotlib.pyplot

file_LC='data_paipai/LC.csv'
file_LP='data_paipai/LP.csv'

LC=pandas.read_csv(file_LC)
LP=pandas.read_csv(file_LP)

print(LC)
print(LP)


#LC.info()
#LC.describe()
#观察一下年龄分布，最小17岁，最大56岁，平均年龄29岁，33岁以下的占比超过了75%。说明用户整体还是中青年。
#将年龄分为'15-20', '20-25', '25-30', '30-35', '35-40', '40+'比较合理
#观察一下借款金额分布，最小借款金额为100元，最大为50万元，平均值为4424元，低于5230的借款金额占到了75%。
#说明应该是小额借款比较多。将借款金额分为0-2000，2000-3000，3000-4000，4000-5000，5000-6000，6000以上比较合理
#LC['ListingId'].value_counts()
# LP.info()
# LP.describe()
# LP = LP.dropna(how='any')
# LP.info()
# LC = LC.dropna(how='any')
# 数据很干净


#性别分析
male = LC[LC['性别'] == '男']
female = LC[LC['性别'] == '女']
sex = (male,female)
sex_data = (male['借款金额'].sum(), female['借款金额'].sum())
sex_idx = ('男', '女')
matplotlib.pyplot.figure(figsize=(15, 6))
matplotlib.pyplot.subplot(1,3,1)
matplotlib.pyplot.pie(sex_data, labels=sex_idx, autopct='%.1f%%')

#新老客户分析
new = LC[LC['是否首标'] == '是']
old = LC[LC['是否首标'] == '否']
newold_data = (new['借款金额'].sum(), old['借款金额'].sum())
newold_idx = ('新客户', '老客户')
matplotlib.pyplot.subplot(1,3,2)
matplotlib.pyplot.pie(newold_data, labels=newold_idx, autopct='%.1f%%')

#学历分析
ungraduate = LC[LC['学历认证'] == '未成功认证']
graduate = LC[LC['学历认证'] == '成功认证']
education_data = (ungraduate['借款金额'].sum(), graduate['借款金额'].sum())
education_idx = ('大专以下', '大专及以上')
matplotlib.pyplot.subplot(1,3,3)
matplotlib.pyplot.pie(education_data, labels=education_idx, autopct='%.1f%%')
matplotlib.pyplot.show()

#年龄分析
ageA = LC.loc[(LC['年龄'] >= 15) & (LC['年龄'] < 20)]
ageB = LC.loc[(LC['年龄'] >= 20) & (LC['年龄'] < 25)]
ageC = LC.loc[(LC['年龄'] >= 25) & (LC['年龄'] < 30)]
ageD = LC.loc[(LC['年龄'] >= 30) & (LC['年龄'] < 35)]
ageE = LC.loc[(LC['年龄'] >= 35) & (LC['年龄'] < 40)]
ageF = LC.loc[LC['年龄'] >= 40]
age = (ageA, ageB, ageC, ageD, ageE, ageF)
age_total = 0
age_percent =[]
for i in age:
    tmp = i['借款金额'].sum()
    age_percent.append(tmp)
    age_total  += tmp
age_percent /= age_total
age_idx = ['15-20', '20-25', '25-30', '30-35', '35-40', '40+']
matplotlib.pyplot.figure(figsize=(15, 8))
matplotlib.pyplot.bar(age_idx, age_percent)
for (a, b) in zip(age_idx, age_percent):
    matplotlib.pyplot.text(a, b+0.001, '%.2f%%' % (b * 100), ha='center', va='bottom', fontsize=10)
matplotlib.pyplot.show()



from datetime import datetime

#分析每日贷款金额的走势
loan = LC[['借款成功日期', '借款金额']].copy()
loan['借款日期'] = pd.to_datetime(loan['借款成功日期'])
loan1 = loan.pivot_table(index='借款日期', aggfunc='sum').copy()
matplotlib.pyplot.figure(figsize=(15, 6))
matplotlib.pyplot.subplot(1,2,1)
matplotlib.pyplot.plot(loan1)
matplotlib.pyplot.xlabel('日期')
matplotlib.pyplot.ylabel('借款金额')
matplotlib.pyplot.title('每天贷款金额波动图')

#分析每月贷款金额的走势
loan['借款成功月份'] = [datetime.strftime(x, '%Y-%m') for x in loan['借款日期']]
loan2 = loan.pivot_table(index='借款成功月份', aggfunc='sum').copy()
matplotlib.pyplot.subplot(1,2,2)
matplotlib.pyplot.plot(loan2)
matplotlib.pyplot.xlabel('月份')
matplotlib.pyplot.xticks(['2015-01','2015-07','2016-01','2016-07','2017-01'])
matplotlib.pyplot.ylabel('借款金额')
matplotlib.pyplot.title('每月贷款金额波动图')
matplotlib.pyplot.show()

# 对2017年1月的数据继续进行分析，并求出平均值和标准差
loan3 = loan1.loc['2017-01']
avg = loan3['借款金额'].mean()
std = loan3['借款金额'].std()
print(avg, std)