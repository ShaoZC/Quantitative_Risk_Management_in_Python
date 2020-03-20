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
# matplotlib.pyplot.show()



from datetime import datetime

#分析每日贷款金额的走势
loan = LC[['借款成功日期', '借款金额']].copy()
loan['借款日期'] = pandas.to_datetime(loan['借款成功日期'])
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

# 初始评级的数据划分
level_idx = ('A', 'B', 'C', 'D', 'E', 'F')
lev = []
for i in level_idx:
    temp = LC[LC['初始评级'] == i]
    lev.append(temp)

# 借款类型的数据划分
kind_idx = ('电商', 'APP闪电', '普通', '其他')
kind = []
for i in kind_idx:
    temp = LC[LC['借款类型'] == i]
    kind.append(temp)

# 不同借款金额的数据划分
amount_idx = ('0-2000', '2000-3000', '3000-4000', '4000-5000', '5000-6000', '6000+')
amountA = LC.loc[(LC['借款金额'] > 0) & (LC['借款金额'] < 2000)]
amountB = LC.loc[(LC['借款金额'] >= 2000) & (LC['借款金额'] < 3000)]
amountC = LC.loc[(LC['借款金额'] >= 3000) & (LC['借款金额'] < 4000)]
amountD = LC.loc[(LC['借款金额'] >= 4000) & (LC['借款金额'] < 5000)]
amountE = LC.loc[(LC['借款金额'] >= 5000) & (LC['借款金额'] < 6000)]
amountF = LC.loc[(LC['借款金额'] >= 6000)]
amount = (amountA, amountB, amountC, amountD, amountE, amountF)

LC['逾期还款率'] = LC['历史逾期还款期数'] / (LC['历史逾期还款期数'] + LC['历史正常还款期数']) * 100


# 逾期还款率的分析图
def depayplot(i, idx, data, xlabel, title, index):
    depay = []
    for a in data:
        tmp = a[index].mean()
        depay.append(tmp)
    matplotlib.pyplot.subplot(2, 3, i)
    matplotlib.pyplot.bar(idx, depay)
    for (a, b) in zip(idx, depay):
        matplotlib.pyplot.text(a, b + 0.001, '%.2f%%' % b, ha='center', va='bottom', fontsize=10)
    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(index)
    matplotlib.pyplot.title(title)


matplotlib.pyplot.figure(figsize=(15, 10))
index = '逾期还款率'
# 根据初始评级对逾期还款率进行分析
depayplot(1, level_idx, lev, '初始评级', '不同初始评级客户逾期还款率', index)

# 根据年龄对逾期还款率进行分析
depayplot(2, age_idx, age, '年龄', '不同年龄客户逾期还款率', index)

# 根据借款类型对逾期还款率进行分析
depayplot(3, kind_idx, kind, '借款类型', '不同借款类型客户逾期还款率', index)

# 根据性别对逾期还款率进行分析
depayplot(4, sex_idx, sex, '性别', '不同性别客户逾期还款率', index)

# 根据借款金额对逾期还款率进行分析
depayplot(5, amount_idx, amount, '借款金额', '不同借款金额客户逾期还款率', index)

matplotlib.pyplot.show()
