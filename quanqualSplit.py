class userDS:
        def quanQual(data):
            quant=[]
            qual=[]
            for columnNames in data.columns:
                #print("for loop",columnNames)
                if(data[columnNames].dtype=='O'):
                    qual.append(columnNames)
                else:
                    quant.append(columnNames)
            return  quant,qual
