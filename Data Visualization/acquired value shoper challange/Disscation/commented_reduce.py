"""	Function to reduce the data (loc_transactions) to a file (loc_reduced). 
	Needs loc_offers to know which transactions matter (are on offer). """

def reduce_data(loc_offers, loc_transactions, loc_reduced):
  #start a counter for progress reporting
  start = datetime.now()
  #get all categories and companies on offer in dictionaries
  offers_cat = {}
  offers_co = {}
  #for numbered (enumerated) line in offers file
  for e, line in enumerate( open(loc_offers) ):
    #add 2nd and 4th column value to the dictionary
    offers_cat[ line.split(",")[1] ] = 1
    offers_co[ line.split(",")[3] ] = 1
  #open an output file, name 'loc_reduced', writing binary
  with open(loc_reduced, "wb") as outfile:
    #go through transactions file and reduce
	#keep a counter
    reduced = 0
	#for enumerated line in huge transaction file
    for e, line in enumerate( open(loc_transactions) ):
	  #first time we write the header
      if e == 0:
        outfile.write( line ) #print header
      else:
	    #else we only write when the transaction category ID [3] or company ID [4] 
		#is inside one of the dictionaries we created from the offers file.
        if line.split(",")[3] in offers_cat or line.split(",")[4] in offers_co:
		  #write the transaction record to the outfile (reduced file)
          outfile.write( line )
		  #increment our counter (number of reduced files written)
          reduced += 1
      #progress report (once every 5000000 lines)
      if e % 5000000 == 0:
        print e, reduced, datetime.now() - start
  #final report
  print e, reduced, datetime.now() - start