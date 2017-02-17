# auth-log-tranformation
Transform data from authentication logs

### Purpose
We currently receive one **80mb** log file per month from our Identity Management team that we use to visualize authentication traffic. These files have over **1 million** rows, and tranformations must be done to:  
  1. reformat the date field into an actual datetime data type (as opposed to a string)  
  2. agregate the authentication records up to a total count by date and hour

### Next Steps
Create a mostly-automated workflow that:
  1. Places the log file into a network directory on a scheduled basis
  2. Runs a scheduled job to execute this python script
  3. Appends the new, aggregated data set to a maseter file
  4. Updates a Tableau Data Extract based on the master file 
