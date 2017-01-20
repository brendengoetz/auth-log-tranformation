# auth-log-tranformation
Transform data from authentication logs

### Purpose
We currently receive one **80mb** log file per month from our Identity Management team that we use to visualize authentication traffic. These files have over **1 million** rows, and tranformations must be done to:  
  1. reformat the date field into an actual datetime data type (as opposed to a string)  
  2. agregate the authentication records up to a total count by date and hour
