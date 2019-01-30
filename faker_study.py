# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:42
# @Author  : Felix Wang

from faker import Factory # pip install faker

# zh_CN 表示中国大陆版
fake = Factory().create('zh_CN')
# 产生随机手机号
print(fake.phone_number())
# 产生随机姓名
print(fake.name())
# 产生随机地址
print(fake.address())
# 随机产生国家名
print(fake.country())
# 随机产生国家代码
print(fake.country_code())
# 随机产生城市名
print(fake.city_name())
# 随机产生城市
print(fake.city())
# 随机产生省份
print(fake.province())
# 产生随机email
print(fake.email())
# 产生随机IPV4地址
print(fake.ipv4())
# 产生长度在最大值与最小值之间的随机字符串
print(fake.pystr(min_chars=0, max_chars=8))

# 随机产生车牌号
print(fake.license_plate())

# 随机产生颜色
print(fake.rgb_color())  # rgb
print(fake.safe_hex_color())  # 16进制
print(fake.color_name())  # 颜色名字
print(fake.hex_color()) # 16进制

# 随机产生公司名
print(fake.company())


# 随机产生工作岗位
print(fake.job())
# 随机生成密码
print(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
# 随机生成uuid
print(fake.uuid4())
# 随机生成sha1
print(fake.sha1(raw_output=False))
# 随机生成md5
print(fake.md5(raw_output=False))

# 随机生成女性名字
print(fake.name_female())
# 男性名字
print(fake.name_male())
# 随机生成名字
print(fake.name())

# 生成基本信息
print(fake.profile(fields=None, sex=None))
print(fake.simple_profile(sex=None))

# 随机生成浏览器头user_agent
print(fake.user_agent())

# 随机产生时间
fake.month_name()
# 'September'
fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2010, 7, 21, 18, 52, 43)
fake.time_object(end_datetime=None)
# datetime.time(6, 39, 26)
fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)
# datetime.datetime(2013, 10, 11, 18, 43, 40)
fake.future_date(end_date="+30d", tzinfo=None)
# datetime.date(2018, 7, 8)
fake.date_time(tzinfo=None, end_datetime=None)
# datetime.datetime(2006, 9, 4, 20, 46, 6)
fake.date(pattern="%Y-%m-%d", end_datetime=None)
# '1998-08-02'
fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2018, 6, 8, 9, 56, 24)
fake.timezone()
# 'Africa/Conakry'
fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2017, 6, 27, 21, 18, 28)
fake.month()
# '04'
fake.day_of_week()
# 'Wednesday'
fake.iso8601(tzinfo=None, end_datetime=None)
# '1988-02-28T09:22:29'
fake.time_delta(end_datetime=None)
# datetime.timedelta(10832, 82660)
fake.date_object(end_datetime=None)
# datetime.date(2005, 8, 18)
fake.date_this_decade(before_today=True, after_today=False)
# datetime.date(2015, 1, 5)
fake.date_this_century(before_today=True, after_today=False)
# datetime.date(2000, 6, 1)
fake.date_this_month(before_today=True, after_today=False)
# datetime.date(2018, 6, 13)
fake.am_pm()
# 'AM'
fake.past_datetime(start_date="-30d", tzinfo=None)
# datetime.datetime(2018, 6, 25, 7, 41, 34)
fake.date_this_year(before_today=True, after_today=False)
# datetime.date(2018, 2, 24)
fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
# datetime.datetime(2018, 6, 26, 14, 40, 5)
fake.date_time_ad(tzinfo=None, end_datetime=None)
# datetime.datetime(673, 1, 28, 18, 17, 55)
fake.date_between_dates(date_start=None, date_end=None)
# datetime.date(2018, 6, 26)
fake.future_datetime(end_date="+30d", tzinfo=None)
# datetime.datetime(2018, 7, 4, 10, 53, 6)
fake.century()
# 'IX'
fake.past_date(start_date="-30d", tzinfo=None)
# datetime.date(2018, 5, 30)
fake.time(pattern="%H:%M:%S", end_datetime=None)
# '01:32:14'
fake.day_of_month()
# '19'
fake.unix_time(end_datetime=None, start_datetime=None)
# 1284297794
fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2018, 5, 24, 11, 25, 25)
fake.date_between(start_date="-30y", end_date="today")
# datetime.date(2003, 1, 11)
fake.year()
# '1993'
fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
# <generator object time_series at 0x7f44e702a620>


# 随机产生文件
fake.file_extension(category=None)
# 'xls'
fake.file_name(category=None, extension=None)
# '表示.csv'
fake.file_path(depth=1, category=None, extension=None)
# '/教育/客户.js'
fake.unix_device(prefix=None)
# '/dev/sdf'
fake.unix_partition(prefix=None)
# '/dev/vdf0'
fake.mime_type(category=None)
# 'multipart/form-data'
