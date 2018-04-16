#! -*- coding:utf-8 -*-
import json

STU_MAX_NO = 0
STU_INFO_DICT = {}

def insert():
  name = raw_input("input Name: ").decode("utf-8")
  age = raw_input("input Age: ")
  sex = raw_input("input Sex: ")
  score = raw_input("input Score: ")
  grade = raw_input("input Grage: ")
  global STU_INFO_DICT
  global STU_MAX_NO
  STU_MAX_NO += 1
  STU_INFO_DICT[STU_MAX_NO] = { "name":name,"age":age,"sex":sex,"score":score,"grade":grade}  
  print "-----------插入成功！-----------"
  print "学号", STU_MAX_NO, "最新的信息如下："
  for info in STU_INFO_DICT[STU_MAX_NO]:
    print info, ":",  STU_INFO_DICT[STU_MAX_NO][info]


def delete(stu_no):
  global STU_INFO_DICT
  stu_info = STU_INFO_DICT.pop(stu_no)
  for info in stu_info:
    print info, ":", stu_info[info]
  print "-----------已删除---------------"

def modify(stu_no):
  print "学号", stu_no, "的信息如下："
  global STU_INFO_DICT
  for info in STU_INFO_DICT[stu_no]:
    print info, ":", STU_INFO_DICT[stu_no][info]
  print "请输入要修改的序号，若需要修改多项，请用空格隔开，如1 3 4\n1: name\n2: age\n3: sex\n4: score\n5: grade\n"
  option = raw_input()  
  option = option.strip()
  opts = option.split(" ")  

  category = {"1":"name", "2":"age", "3":"sex", "4":"score", "5":"grade"}
  for opt in opts:
    info = raw_input("input new %s"%category[opt])
    STU_INFO_DICT[stu_no][category[opt]] = info
  print "-----------修改成功！------------"
  print "学号", stu_no, "最新的信息如下："
  for info in STU_INFO_DICT[stu_no]:
    print info, ":", STU_INFO_DICT[stu_no][info]


def search(stu_no):
  STU_INFO_DICT[stu_no]
  stu_info = STU_INFO_DICT.pop(stu_no)
  print "-----------查询结果如下-----------"
  for info in stu_info:
    print info, ":", stu_info[info]
  

def sort():
  print "-----------排序结果如下-----------"
  score_dict = {}
  for stu_no in STU_INFO_DICT:
    score_dict[stu_no] = STU_INFO_DICT[stu_no]["score"]
  sort_list = sorted(score_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
  for score_dict in sort_list:
    stu_no = score_dict[0]
    print "学号：", stu_no, "姓名：", STU_INFO_DICT[stu_no]["name"], "分数: ", STU_INFO_DICT[stu_no]['score']

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
