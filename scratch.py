# -*-coding:utf-8-*-
import numpy as np
import tushare as ts
print('#一次性获取全部日k线数据')
a=ts.get_hist_data('600848')#一次性获取全部日k线数据
print('a=',a.head())

print('设定历史数据的时间')
b=ts.get_hist_data('600848',start='2015-01-05',end='2019-01-09')
print('b=',b)

# c1=ts.get_hist_data('600848', ktype='W') #获取周k线数据
# c2=ts.get_hist_data('600848', ktype='M') #获取月k线数据
# c3=ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
# c4=ts.get_hist_data('600848', ktype='15') #获取15分钟k线数据
# c5=ts.get_hist_data('600848', ktype='30') #获取30分钟k线数据
# c6=ts.get_hist_data('600848', ktype='60') #获取60分钟k线数据
# c7=ts.get_hist_data('sh'） #获取上证指数k线数据，其它参数与个股一致，下同
# c8=ts.get_hist_data('sz'） #获取深圳成指k线数据
# c9=ts.get_hist_data('hs300'）#获取沪深300指数k线数据
# c10=ts.get_hist_data('sz50'）#获取上证50指数k线数据
# c11=ts.get_hist_data('zxb'）#获取中小板指数k线数据
# c12=ts.get_hist_data('cyb'）#获取创业板指数k线数据


print('一次性获取当前交易所有股票的行情数据（如果是节假日，即为上一交易日，结果显示速度取决于网速）')
# d=ts.get_today_all()
# print('d=',d)


# print("行业分类")
# e=ts.get_industry_classified(0)
# print('e=',e.head())
#
# print('概念分类')
# f=ts.get_concept_classified(0)
# print('f=',f.head())
#
print('沪深300成份及权重')
g=ts.get_hs300s()
print('g=',g.head())


print('#获取2014年第3季度的现金流量数据')
h=ts.get_cashflow_data(2014,3)
print('h=',h.head())