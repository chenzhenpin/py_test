
#coding=utf-8
# import dns.resolver
# domain = raw_input('Please input an domain: ')
# cname = dns.resolver.query(domain, 'CNAME') #指定查询类型为CNAME记录
# for i in cname.response.answer : #结果将回应cname后的目标域名
	# for j in i.items :
		# print j.to_text()
import dns.resolver
domain = raw_input('Please input an domain: ')
MX = dns.resolver.query(domain, 'MX')  #指定查询类型为MX记录
for i in MX:
#遍历回应结果， 输出MX记录的preference及exchanger信息
	print 'MX preference =', i.preference, 'mail exchanger =', i.exchange