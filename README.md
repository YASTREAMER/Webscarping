# Webscarping

## Requirement

To run the script you will need to have selenium and firefox drivers install in an virtual python envoirenment.
To install selenium copy and paste the code:-

    pip install selenium 

Or if you want to have the exact dependenices it is recommended to load the dependenices using [Requirement List](requirements.txt)

    pip install -r requirements.txt

The above method is the preferred method as it allows for the dependenices to not mismatch.

## Edits

Before you run the code for Statista you will have to make some edits in the [This File](const.py)
What you have to do is change the upperlimit and lowerlimit variable in multiple of 100,000 or 200,000. I would recommended to increase it in increament of 100,000 
your computer have 8Gb of ram and 200,000 if your has 16gb. 

    upperlimit=200000 
    lowerlimit=100000 
    
Also there is another variable Increament, I recommend to keep it around 1000 as it allows for 
most of sectors to show below 10,000. 

    Increament = 1000

## Code 

To run the code, enter your virtual envoirenment.Then run the following code

    python3 main.py

The following output will be shown

    Hello all. Which website do you want to scrape. 
    1.) SearchFunder 
    2.) Statista 
    3.) Download Data

### **Warning**
    Dont use 1st and 3rd options as they are not needed right now

It will generate the necessary folders for you. Dont used the 1st and 3rd options as they are not needed anymore
When you choose the 2nd option you will be shown an prompt in the terminal as shown below.

    There is your time to set the download location 

After seeing this just change the download location in the firefox window that opens when you run the script.
Just make sure your system has enough storage for downloading the data.

## Output

The output will be xlsx files that will be downloaded.

<!-- The files generate in [ScrapedDatat](ScrapedData/) will contain the links for the different sectors. The files will be in the format
link-UUID-sectorName.txt -->

If you find any problem or bug in the code please reach out to me.