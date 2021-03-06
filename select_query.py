class MySelectQuery:
    def __init__(self, param_1):  
        self.param_1 = param_1
    def where(self,column_name,criteria):
        output = []
        file_input = self.param_1.split("\n")
        count = len(file_input)
        for row in file_input:
            if row !="":
                output.append(row.split(","))
        c = 0
        for i in range(len(output[0])):
            if output[0][i] ==column_name:
                c=i
        num = 0
        res = [None]*len(output[0])
        for j in range(count-1):
            if output[j][c] == criteria:
                num = j
        for f in range(len(output[0])):
            res[f] = output[num][f]
        data=[[0]*1]*1 
        for i in range(len(res)):
            string= ",".join(res)
        data[0][0]=string
        return data
#s  = "name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16 1947','University of California, Los Angeles\nMahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9 1969',Louisiana State University\n"
#print(where(s,"name","Alaa Abdelnaby"))
