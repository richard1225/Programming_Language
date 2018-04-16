#! -*- coding:utf-8 -*-
import json
import re

STU_MAX_NO = 0
STU_INFO_LIST = []

def insert():
  name = raw_input("input Name: ").decode("utf-8")
  age = raw_input("input Age: ")
  sex = raw_input("input Sex: ")
  score = raw_input("input Score: ")
  grade = raw_input("input Grage: ")

  global STU_INFO_LIST
  global STU_MAX_NO
  STU_MAX_NO += 1
  stu_info = "no"+":"+str(STU_MAX_NO)+";name"+":"+name+";"+"age"+":"+age+";"+"sex"+":"+sex+";"+"score"+":"+score+";"+"grade"+":"+grade
  STU_INFO_LIST.append(stu_info)
  print "-----------插入成功！-----------"
  print "学号", STU_MAX_NO, "最新的信息如下："
  stu_info = stu_info.split(";")
  for info in stu_info:
    print info.split(":")[0],":",info.split(":")[1]

def delete(stu_no):
  pattern = re.compile("no:"+str(stu_no))
  tmp_list = STU_INFO_LIST[:]
  for stu_info in tmp_list:
    if re.findall(pattern,stu_info):
      STU_INFO_LIST.remove(stu_info)
      print "-----------已删除---------------"
      stu_info = stu_info.split(";")
      for info in stu_info:
        print info.split(":")[0],":",info.split(":")[1]
      

def modify(stu_no):
  print "学号", stu_no, "的信息如下："
  global STU_INFO_LIST
  for stu_info in STU_INFO_LIST:
    if str(stu_no) == stu_info.split(";")[0].split(":")[1]:
      stu_info = stu_info.split(";")
      for info in stu_info:
        print info.split(":")[0],":",info.split(":")[1]

  print "请输入要修改的序号，若需要修改多项，请用空格隔开，如1 3 4\n1: name\n2: age\n3: sex\n4: score\n5: grade\n"
  option = raw_input()  
  option = option.strip()
  opts = option.split(" ")  

  category = {"1":"name", "2":"age", "3":"sex", "4":"score", "5":"grade"}
  stu_list = STU_INFO_LIST[:]
  for stu_info in stu_list:
    if str(stu_no) == stu_info.split(";")[0].split(":")[1]:
      STU_INFO_LIST.remove(stu_info)
      tmp_list = []
      info_list = stu_info.split(";")
      for info in info_list:
        tmp_list.append(info.split(":")[1])
      for opt in opts:
        info = raw_input("input new %s: "%category[opt])
        tmp_list[int(opt)-1] = info
      stu_info = "no"+":"+tmp_list[0]+";name"+":"+tmp_list[1]+";"+"age"+":"+tmp_list[2]+";"+"sex"+":"+tmp_list[3]+";"+"score"+":"+tmp_list[4]+";"+"grade"+":"+tmp_list[5]
      STU_INFO_LIST.append(stu_info)
        
  
  print "-----------修改成功！------------"
  print "学号", stu_no, "最新的信息如下："
  for stu_info in STU_INFO_LIST:
    if str(stu_no) == stu_info.split(";")[0].split(":")[1]:
      stu_info = stu_info.split(";")
      for info in stu_info:
        print info.split(":")[0],":",info.split(":")[1]


def search(stu_no):
  pattern = re.compile("no:"+str(stu_no))
  tmp_list = STU_INFO_LIST[:]
  for stu_info in tmp_list:
    if re.findall(pattern,stu_info):
      print "-----------查询结果如下-----------"
      stu_info = stu_info.split(";")
      for info in stu_info:
        print info.split(":")[0],":",info.split(":")[1]
  

def sort():
  print "-----------排序结果如下-----------"
  tmp_list = STU_INFO_LIST[:]
  pattern = re.compile("score:([0-9]+)")
  while(len(tmp_list) != 0):
    one_time_list = tmp_list[:]
    max_str = ""
    max_score = 0
    for stu_info in one_time_list:
      stu_score = pattern.search(stu_info).group(1)
      if max_score < int(stu_score):
        max_score = int(stu_score)
        max_str = stu_info
    tmp_list.remove(max_str)
    print "学号：", max_str.split(";")[0].split(":")[1] , "姓名：", max_str.split(";")[1].split(":")[1] ,"分数: ", max_score

import os
def manu():
  print "----------------------------------"
  print "请输入对应的数字来选择操作:\n1:增加学生\n2:删除学生\n3:查找学生\n4:修改学生信息\n5:按照学生成绩排序"
  print "----------------------------------"
  option = raw_input()
  os.system('clear')
  if option == "1":
    print "------------正在插入信息-----------"
    insert()
    manu()
  elif option == "2":
    print "------------正在删除信息-----------"
    stu_no=input("请输入学号:")
    delete(stu_no)
    manu()
  elif option == "4" :
    print "------------正在修改信息-----------"
    stu_no=input("请输入学号:")
    modify(stu_no)
    manu()
  elif option ==  "3" :
    print "------------正在查找信息-----------"
    stu_no=input("请输入学号:")
    search(stu_no)
    manu()
  elif option ==  "5" :
    sort()
    manu()


if __name__ == "__main__":
  manu() 
