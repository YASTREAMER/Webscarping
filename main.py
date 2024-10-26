from searchfunder import searchfunderStart
from stratista import statistaStart 

def main() -> None:
    print(
        "Hello Fall3n. Which website do you want to scrape. \n 1.) SearchFunder \n 2.) Statista"

    )
    choice = int(input())
    if choice > 2:
        print("Error: Invalid Input")
    elif choice == 1:
        searchfunderStart()
    else:
        statistaStart()


if __name__ == "__main__":
    main()
