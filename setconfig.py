import json,os
if not os.path.exists('./config'):
    os.mkdir('./config')
print('请输入名字(每个之间用回车分割)')
in1,l1='',[]
while True:
    in1=input()
    if in1=='stop':
        break
    if len(in1)<4:
        in1=in1+('  '*(4-len(in1)))
        l1.append(in1)
dic={'names':l1}
with open('./config/config.json','w') as f:
    json.dump(dic,f,indent=4)
