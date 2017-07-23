# Log Analysis Project
## Synopsis
This is an internal reporting tool for a newspaper website that will use information from the database to discover what kind of articles the site's readers like.
## Installation
This project runs on a VM which has Python3 and PostgreSQL installed. To access this VM,
### Install VirtualBox
Install the platform package for your operating system from [here](https://www.virtualbox.org/wiki/Downloads)
### Install Vagrant
Install the version for your operating system from [here](https://www.vagrantup.com/downloads.html)
### Download the VM configuration
Download and unzip the following folder: [FSND-virtual-machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) or Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm
### Start the VM
From the terminal, inside the vagrant subdirectory, run the command **vagrant up**
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM!
### Download the SQL schema
Download the data at [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To load the data, use the command **psql -d news -f newsdata.sql**.
## Running the project
* Run the following CREATE VIEW queries in the **news** database:
    * CREATE VIEW counterrors AS 
    (SELECT time::date, COUNT(*) AS nooferrors
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY time::date);
    * CREATE VIEW countrequests AS
    (SELECT time::date, COUNT(*) AS allrequests
    FROM log
    GROUP BY time::date);
    * CREATE VIEW finalpercents AS 
    (SELECT counterrors.time::date, ROUND(CAST((counterrors.nooferrors*100/CAST(countrequests.allrequests AS FLOAT)) AS NUMERIC), 2) AS percent
    FROM counterrors, countrequests
    WHERE counterrors.time::date = countrequests.time::date;
* Run the python file named NewsData with python3
## License
This software is released under the MIT License, see LICENSE.txt.
