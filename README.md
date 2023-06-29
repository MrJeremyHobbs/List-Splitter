
# Getting Started
Download the script and place it on your harddrive.

Create 2 folders in the same directory as the script:
input 
output

In the input folder place your analytics report. This should be a single-column plain-text file that is tabbed delimtied or comma-seperated. In either case, the extension will be .csv.

Example using dummy data:

MMS Id
984791625320
984791615950
984791635960
984791635970
984791635880

Edit the splitter.py script using a plain-text editor (like Notepad++). At the top of the file, there is a value called number_of_lines_per_file. By default, it's set at 500,000. But, if you find that your exported files are over 10mgbs or wildly under, you can change that value accordingly.

number_of_lines_per_file = 500000

# Running the Script
Run the script.

In your output folder there should now be a series of files called 1_SPLIT.txt, 2_SPLIT.txt, etc, depending on the amount of input data you fed into the script.

You can now take each of these SPLIT files and create sets in Alma.

# Create Sets in Alma
Once you've created a set for each file, you can then go into Alma and begin combining sets 2 by 2 until you end up with a single set of all the MMS IDs that were in the original analytics file.

To make your life easier, name the sets descriptively as you go.

Unfortunately, Alma only supports combining 2 sets at a time (NERS request anyone?), which is why this process is necessary.

For example, you have 5 files.

You create 5 sets in Alma:

SET_1
SET_2
SET_3
SET_4
SET_5

Once you start combining the sets, label them like this:

SET_1 + SET_2
SET_3 + SET_4
SET_5 (no need to combine)

Then:

SET_1 + SET_2 + SET_3 + SET_4
SET_5

Finally:
SET_1 + SET_2 + SET_3 + SET_4 + SET_5

Check the totals of the final set. It should match closely to your original analytics file.

Sometimes the number can be off slightly. Depending on how old your analytics report is, some of the original records in the report may have been deleted and are no longer in Alma.