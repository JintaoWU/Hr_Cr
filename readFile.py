import os

#将csv格式读成字典
def read_csv_to_dic(path):
    tmp = open(path, 'r')

    dic = {}
    label = []
    index = 1
    for line in tmp:
        att = line.split(',')
        if index == 1:
            label = att
            label[-1] = label[-1].strip()
            for e in label:
                dic[e] = []
        else:
            for i in range(len(label)):
                if att[i].strip('\n') == '':
                    continue
                dic[label[i]].append(att[i].strip())
        index = index + 1
    return dic

#获取Cr，Hr的字典数据
def get_Cr_Hr(dir):
    Cr={}
    Hr={}
    for f in os.listdir(dir):
        path = dir + f

        if 'Cr' in f:
            Cr = read_csv_to_dic(path)
        elif 'Hr' in f:
            Hr = read_csv_to_dic(path)
        else:
            print("Wrong Data!!!")
    return Cr,Hr

#写入文件
def write_result(dir):
    Cr, Hr = get_Cr_Hr(dir)
    w=open('result.txt','w')

    for k,v in Cr.items():
        CrTmp=Cr[k]
        HrTmp=Hr[k]
        if len(CrTmp)!=len(HrTmp):
            print("size not same!!!")
        else:
            for i in range(len(CrTmp)):
                s=CrTmp[i]+"\t"+HrTmp[i]+"\t"+k+"\n"
                w.write(s)
    w.close()


dir = './files/'
write_result(dir)




