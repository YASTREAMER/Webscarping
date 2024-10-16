from searchfunder import searchfunderStart


def main() -> None:
    print(
        "Hello Fall3n. Which website do you want to scrape. \n 1.) SearchFunder \n 2.) Stratista"
    )
    choice = int(input())
    if choice > 2:
        print("Error: Invalid Input")
    elif choice == 1:
        searchfunderStart()
    else:
        pass


if __name__ == "__main__":
    main()
