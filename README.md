# TRIAGE WRITER
#### Video Demo: https://youtu.be/2kF_nM6SE1g
#### Description:

```
This application is designed to assist in mass casualty incidents (MCI). As a paramedic, I created this tool to be beneficial in my profession. During an MCI, it is crucial to triage victims due to the typically overwhelming number of casualties compared to the available emergency personnel on the scene. Therefore, it is essential to allocate emergency resources in a way that maximizes the number of victims receiving the best possible care under those conditions. Unfortunately, it is often impossible to help everyone affected by an MCI. Without triage Emergency services might focus on someone gravely wounded with little chance of recovery, while others with initially less severe conditions could deteriorate to a point where they become unsavable. Triage involves a straightforward algorithm that we use to evaluate the victims' conditions. Various triage algorithms are employed worldwide, but this application contains the generally accepted outcomes of triage, categorizing victims into four groups based on the urgency of their conditions.

Currently, we use paper charts to mark victims and their priority levels. However, in our daily operations, we utilize tablets to write reports. This makes the application practical, as we already have the tablets in use, and there is ongoing discussion about transitioning all MCI documentation to digital formats. Thus, the development of this app is both logical and timely.

The project directory contains multiple files:

- requirements.txt
- classes.py
- project.py
- test_project.py
```

#### Intended method of usage:
```
The program was exported to an executable via pyinstaller.

After starting the program, the first and only thing to do is to input Triage Crew ID. In the region where I work we identify crews either by their number which is made up from three digits(e.g. 123) or by three capital letters followed by a space and the three numbers described earlier (e.g. ABC 123). These represent call signs of the crews.

It is necessary to first input the Crew ID. Only after that other buttons are enabled. While inputin the ID the user has the option to delete what he inputed (in case he has made a mistake), or to submit what is inputed. If the inputed value does not match the expected input, nothing happens. After a valid input has been confirmed, the ID area is disabled and Start and End triage buttons are enabled.

At this point it is either possible to start the triage process or to exist the application.

Once Start triage button is pressed, the coloured buttons that represent the triage categories are enabled. After each click on those buttons, the Victims triaged counter is updated by one and data is stored into a temp victims.csv file. This file contains the id of the victim, time and date of triage and the assigned colour.

After the triage is finished, user can press the End triage button. This exits the application, reads the csv file, creates a triage report pdf file from it and lastly deletes the temporary csv file.
```

## requirements.txt
This file lists all pip installable requirements as per CS50 Python final project specification. In this application, the requirements.txt contain only one thig:
- fpdf
## classes.py
This file was supposed to contain more classes to be imported to the main project file to make it manageable in size. I have however ported some of the functionality originally made as object to the main() function of the project file.

As it stands, there is only one class in the classes.py file, which is Victim. This class represents a victim that a paramedic or a first responder would care for on scene of an MCI. The Victim class has multiple parametres that it can store.
- time
- date
- colour

Date and time are obtained by the datetime library. Colour is given by the choice the user makes. There are four possible colours:
- Green
- Yellow
- Red
- Black

The colour represent how serious is the injury of the victim. Green, MINOR, victims are able to walk. Yellow, DELAYED victims that are not able to walk but their injuries aren't too serious. Red, IMMEDIATE, victims have serious injuries that require immediate attention and intervention. Black, EXPECTANT, victims are beyond saving with the limited manpower available at the scene.

A new instance of this class is created in the main project.py directory on each itteration of the use loop.
## project.py
Project.py is the main directory of the program. It contains a class Home_screen within which there is most of the functionality of the application. That mostly consists of the GUI which was made using tkinter library. There is also a main function that initiates an instance of the Home_screen class, which basically starts the application. Lastly, there are three functions defined after the main function, which are:
- Print_to_pdf
- Make_csv
- Check_victims_and_print
### Home_screen class
The Home_screen class represents the biggest part of the application. It contains all of the GUI and most of the functionality of the application.

The __init__ within the Home_screen class contains a few variables that are inputed or generated while the program runs. These are:
- Triage Crew ID
- Number of triaged victims

After that, within __init__, the window size is initialized, and there ale all of the button placements.

Later, within the Home_screen class, there are all of the functions that the buttons in this program have and some more. Those are:

- enter (Which registers when the user presses the Return key and gives it the same functionality as pressing the Submit button)
- fnc_delete_btn (Deletes all that has been inputed in the Crew ID input textbox - in case there was an error and the user spotted it)
- fnc_submit_btn (Function for the submit button. It uses RegEx to only accept given values, prompts the user for confirmation of press, then it assigns a value of the Crew ID variable and changes the state of the input textbox, the input related buttons and the Start and End triage buttons)
- fnc_start_triage_btn (This function firstly calls another function, the fnc_create instance, which creates the first instance of the Victim class, then it disables it self (the Start triage button) and enables the coloured buttons)
- fnc_end_triage_btn (Prompts the user whether he really wants to quit. This functionality is the same for this button and for quitting the application via pressing X. This works through "self.window.protocol("WM_DELETE_WINDOW", self.fnc_end_triage_btn)" expression in the __init__ method within the Home_screen class. If the user confirms that he wants to quit, Check_victims_and_print function is called and then the GUI is destroyed)

Then there are four functions for the coloured buttons. They are all very similar in functionality. The only difference is what colour they assing to the current instance of Victim class. In general, they all increment the number of already triaged victims by one, they assing a colour to the current instance of Victim, and then they all call fnc_update, fnc_victim_save and fnc_create_instance which are described bellow.

- fnc_create_instance (Creates a new instance of Victim class. This is done for the first time by the Start triage button, which is after that disabled. Later, it is done by the coloured buttons)
- fnc_victim_save (This function calls a Make_csv function which is described bellow.)
- fnc_update(This functions updates the Already triaged victims text within the GUI to the current value of already triaged victims)

The following functions are all placed bellow main, in the main part of the code.
- Print_to_pdf (This function imports the temporary .csv file and reads it before it is deleted. It counts the triaged victims and with some other collected data (like the Triage crew ID) prints it all to a pdf file as a Triage report.)
- Make_csv (This function creates the temporary .csv file and ads data to it on every itteration of the app, meaning after every colour button press a new row is added. The created .csv file contains four columns of data: id, date, time, colour. These are used by the Print_to_pdf function above)
- Check_victims_and_print (This function checks, whether there is a victims.csv file that is required for the creation of the pdf report. If there is none, meaning the user ended the application before he pressed Start triage button, nothing happens, and the application exits. If there however is one, Print_to_pdf is called and then the victims.csv is deleted.)
## test_project.py
The test file contains three test functions for functions defined after main. They are:

- test_Print_to_pdf
- test_Make_csv
- test_Check_victims_and_print

All of the test functions use @pytest.fixture method because they test succesfull generation of files which need to be tested and subsequently deleted.

