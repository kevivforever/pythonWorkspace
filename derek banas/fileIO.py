import os

def retrieveFile():
    try:
        bestStudent = {}
        bestStudentStr = "The best Students Ranked \n\n"

        f = open('studentgrades.txt')
    except(IOError), e:
        print "File not found", e
    else:
        for line in f:
            name, grade = line.split()
            bestStudent[grade] = name
        f.close()

        for i in sorted(bestStudent.keys(), reverse=True):
            print bestStudent[i] + ' scored a ' + i
            bestStudentStr += bestStudent[i] + ' scored a ' + i + "\n"
        print "\n"

        print bestStudentStr

        outTOFile = open("studentrank.txt","w")
        outToFile.write(bestStudentStr)
        outToFile.close()

        print "Finished Output"

    return
 
def main():
    retrieveFile()

if __name__ == '__main__':main()
