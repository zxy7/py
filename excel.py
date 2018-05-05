# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import xlwt

def main():
    data = xlrd.open_workbook('a.xls')
    table = data.sheets()[0]
    nrows = table.nrows #行数
    print table
    try:  
        # 创建excel文件  
        filename=xlwt.Workbook()  
        # 给工作表命名，test  
        sheet=filename.add_sheet("test")  
        for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
           print "{title: '"+row[0]+"',"+" key:'"+row[1].lower()+"',width:100},"
          #  print "{title: '"+row[0]+"',"+" key:'"+row[1].lower()+"'},"
          #  print row[1].lower()+":'',"
           sheet.write(rownum,0,"{title: '"+row[0]+"',"+" key:'"+row[1].lower()+"',width:100}")
           sheet.write(rownum,1,row[1].lower()+":'',")
        filename.save("b.xls")  
    except Exception,e:  
        print(str(e)) 

if __name__=="__main__":
    main()