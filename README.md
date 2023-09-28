# Votes and supporters data frame

The idea of this module is to process the files in CSV format and return a pandas dataframe to answer the questions of how many legislators supported/opposed a bill, how many bills a legislator support/opposed, querying by bill, by leglislator and returning lists of bill, leglislators or simply the count of votes.

## Todo list

Wrap everything into a simple Flask server and enable a web service to answer it

Since the volume of data shouldn't be much large (not so many votes a legislator would vote after all) I would create a S3 bucket and monitor any new upload of change in the csv files. This could be a very neaty AWS Lambda.
