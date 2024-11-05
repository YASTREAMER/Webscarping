from searchfunder import searchfunderStart
from stratista import statistaStart 
from downloadFile import mainDownload
import os 

def main() -> None:

    print(
        "Hello all. Which website do you want to scrape. \n 1.) SearchFunder \n 2.) Statista \n 3.) Download Data"

    )
    choice = int(input())
    if choice > 3:
        print("Error: Invalid Input")
    elif choice == 1:
        searchfunderStart()
    elif choice == 2:
        folderGen()
        statistaStart()
    else:
        mainDownload()

def folderGen()-> None:
    if not os.path.exists("ScrapedData"):
        os.mkdir("ScrapedData")
    if not os.path.exists("DownloadFolder"):
        os.mkdir("DownloadFolder")

if __name__ == "__main__":
    main()
