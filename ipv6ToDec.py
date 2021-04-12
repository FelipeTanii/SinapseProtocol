''' Felipe Tanii 2021 04 12
File name: ipv6ToDec.py
Sintaxe: import ipv6ToDec as ip   
ip.ipv6Dec(2001:0db8:85a3:08d3:1319:8A2e:0370:7344)
>>> "8193(1) 3512(2) 34211(3) 2259(4) 4889(5) 35374(6) 880(7) 29508(8) "
'''
def abc(abc): # Converte letra hexadecimal para numero decimal
	''' abc("str") >>> int
	'''
	abc = abc.lower()
	if abc == "a":
		abc = 10
	if abc == "b":
		abc = 11
	if abc == "c":
		abc = 12
	if abc == "d":
		abc = 13
	if abc == "e":
		abc = 14
	if abc == "f":
		abc = 15
	return abc

def ipv6Dec(ipv6): # Converte numeros ipv6 para decimal
	'''  ipv6Dec("str") >>> "str"
	'''
	ipv6 += ":"
	n, soma, octe, ipDec = 0, 0, "", ""
	for i in ipv6:
		if i.isalpha() or i.isnumeric():
			octe += i
		if not i.isalpha() and not i.isnumeric():
			n += 1
			if octe[0].isalpha():
				soma += 4096 * abc(octe[0]) 
			else:
				soma += 4096 * int(octe[0]) # 256 * 16 = 4096
			if octe[1].isalpha():
				soma += 256 * abc(octe[1]) 
			else:
				soma += 256 * int(octe[1]) # 16 * 16 = 256
			if octe[2].isalpha():
				soma += 16 * abc(octe[2])
			else:
				soma += 16 * int(octe[2])
			if octe[3].isalpha():
				soma += abc(octe[3])
			else:
				soma += int(octe[3]) 
			ipDec += str(soma) + "(" + str(n) + ") "
			soma, octe = 0, ""
	return ipDec

def test_ipv6Dec():
	ipv6 = "2001:0db8:85a3:08d3:1319:8A2e:0370:7344"
	r = "8193(1) 3512(2) 34211(3) 2259(4) 4889(5) 35374(6) 880(7) 29508(8) "
	#print(ipv6Dec(ipv6),type(ipv6Dec(ipv6)))
	#print(r, type(r))
	if ipv6Dec(ipv6) == r:
		return True
	else:
		return False
#print(test_ipv6Dec())
