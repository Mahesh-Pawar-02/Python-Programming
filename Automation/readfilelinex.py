import os

def main():

    print("Enter the name of file that you want to reading purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File successfully opend in read mode")

        for line in fobj:
            print(line)
    
        fobj.close()

    else:    
        print("Unable to open as file as file not present in current directory")
        
    
if __name__ == "__main__":
    main()