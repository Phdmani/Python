# Python
This code allows you to get a url link from a CSV file and lets you download it. You can also name the downloaded file from the csv file. It goes by rows so the url and the file name must be on the same row.It skips the header of the file.You can replace URL_in_Csv with the the row in which the urls are found with row[#]. SO if your url downloads an mp3 and the URLs is on the first column and the name in the second, the 14th line would read :      
urllib.request.urlretrieve(row[0], row[1]+'.mp3')
You can also download the files to a specific folder like this:
urllib.request.urlretrieve(row[0], "/home/user/Downloads/mp3/"+row[1]+'.mp3')  


