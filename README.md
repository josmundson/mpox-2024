# mpox-2024

#this is a program to plot the rapidly updating sequences released by four US-based cities: Chicago, Los Angeles, NYC, and Seattle, WA

#LA and NYC data come from their public health labs (LA County Public Health Lab and the NYC Public Health Lab

#Due to differences in how these places report their meta data, I use in house python scripts to 1) edit the metadata.tsv file to include the "Los Angeles" as the "division" in the meta data for their sequences (lameta.py) and 2) to pull accession numbers from each city into include-*city* files (include-city.py). I then use cat to combine the files into a large include.txt file and manually add whatever accession is needed for the root

#I altered the run rules (export.smk) to eliminate the production of a colors.tsv file in the /results folder so that I can make a consistent one myself to include 'division' in the final visualization, color the four cities unique colors, and have the remainer of the sequences be gray

#once this is in the /rules folder and the config file is appropriately named and the included.txt is made, it's good to just run on nextstrain build . This will select around 140 global strains to build with the 2000+ local US sequences placed within them

#early in the run, the filtering should show the correct number of sequences from include.txt and an appropriate number from the subsampling. 
