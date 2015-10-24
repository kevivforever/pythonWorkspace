classes = {"English III": "Ms. Lapan",
         "Precalculus": "Mrs. Gideon",
         "Music Theory":"Mr. Davis",
         "Biotechnology":"Ms. Palmer",
         "Principles of Technology I":"Ms. Garcia",
         "Latin II":"Mrs. Barnett",
         "AP US History":"Ms. Johannessen",
         "Business Computer Infomation Systems":" Mr. James"}

subjects = classes.keys()
teacher = classes.values()

def print_schedule():
    for i in range(1,9):
        sub = subjects[i-1]
        teach = teacher[i-1]
        print "|%d|%36s|%15s|" % (i,sub,teach)
        
def print_border_line():
    for i in range(0,54):
        if i == 0 or i == 53:
            print "+",
        else:
            print "-",

def main():
    print_border_line()
    print
    print_schedule()
    print_border_line()



if __name__ == '__main__': main()
    
