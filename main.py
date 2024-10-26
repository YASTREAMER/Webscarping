from searchfunder import searchfunderStart
from stratista import statistaStart 
import os 

def main() -> None:

    print(
        "Hello all. Which website do you want to scrape. \n 1.) SearchFunder \n 2.) Statista"

    )
    choice = int(input())
    if choice > 2:
        print("Error: Invalid Input")
    elif choice == 1:
        searchfunderStart()
    else:
        folderGen()
        statistaStart()

def folderGen()-> None:
    if not os.path.exists("ScrapedData"):
        os.mkdir("ScrapedData")

if __name__ == "__main__":
    main()
