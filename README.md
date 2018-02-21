# ABOUT:

Variation in names leads to difficulty in identifying a unique person and hence deduplication 
of records is an unsolved challenge. So, to remove the variations and give the unique names
the code has been created. 



# DEPENDENCIES: 

- python3 
- python3 math library
- python3 csv library
- python3 fuzzywuzzy library
- python3 pandas library



# INSTALLING DEPENDENCIES:

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```


# RUNNING THE CODE:
code can be run from linux terminal with command 
```
$ python3 deduplication.py 
```
The required files for it are training_data.csv, test.csv. <br />
With each training example having attribute first name, last name, dob, gender.<br />
The output will be generated in output.csv.<br />
These names can be changed from extdata.py<br />
The output will be the number of unique patients from the input given. <br />

# AUTHOR:
	Amey Muley
  Biotechnology Undergrauate at IIT Guwahati

	
