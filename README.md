# auth-log-tranformation
This python script transforms data from authentication logs

### Purpose
We currently receive one **80mb** log file per month from our Identity Management team that we use to visualize authentication traffic in Tableau, and compare it to web traffic from other sources. These files have over **1 million** rows, and transformations must be done to:  
  1. reformat the timestamp field into an actual timestamp data type (as opposed to a string)  
  2. aggregate the authentication records up to a total count by date and hour

### Next Steps
This is a great start, but I would like to create a mostly-automated workflow that:
  1. Places the log file into a network directory on a scheduled basis
  2. Runs a scheduled job to execute this python script on those files
  3. Appends the new, aggregated data set to a master file
  4. Updates a Tableau Data Extract based on the master file 
