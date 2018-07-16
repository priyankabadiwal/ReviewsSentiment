'''
Json structure of final data
{
	id: {
		avaliable_dates: [{
			date:
			avaliable:
			price:
		}],
		listings: {
			get columns from dataset
		},
		reviews: {

		}
	}
}
'''
import pandas
import os

csv_delimiter = ","

def read_csv(filename):
	df = pandas.read_csv(filename, sep=csv_delimiter)
	return df

def getData(root):
	file_cal = root+"/calendar.csv"
	file_list = root+"/listings.csv"
	# file_neighbourhoods = root+"/neighborhoods.csv"
	file_reviews = root+"/reviews.csv"
	# Reading calendar csv
	df_cal = read_csv(file_cal)
	df_cal_filled = df_cal.fillna("$0")
	df_list = read_csv(file_list)
	# df_neighbourhoods = read_csv(file_neighbourhoods)
	df_reviews = read_csv(file_reviews)
	df_list_index = df_list.set_index('id')
	#Data joined and ready
	df_join_cal = df_cal_filled.join(df_list_index,on="listing_id",lsuffix="_overlap")
	df_join_reviews = df_reviews.join(df_list_index,on="listing_id",lsuffix="_overlap")
	# Write all this to a file


for root, dirs, files in os.walk("contestdata"): 
	if "/" in root:
		print root
		getData(root)



