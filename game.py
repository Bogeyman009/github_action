
def game(dict):
    name=str(input())
    for key in dict:
        if(dict[key]==name):
            del dict[key]
            break
    for key in dict:
        print(dict[key],end=" ")

def main():
    dict={"1":"Shroud",
          "2":"Tarik",
          "3":"Som",
          "4":"Timmy"}
    
    game(dict)
    print(dict)

main()