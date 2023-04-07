class userDS:
    def quanQual(data):
        quant=[]
        qual=[]
        for columnNames in data.columns:
            if(data[columnNames].dtype=='O'):
                qual.append(columnNames)
            else:
                quant.append(columnNames)
        return  quant,qual


    def freqTable(data,columnName):
        import pandas as pd
        freqTable= pd.DataFrame(columns= ["Unique_Values","Frequency","Relative_Frequency","CumSum"])
        freqTable["Unique_Values"]= data[columnName].value_counts().index
        freqTable["Frequency"]= data[columnName].value_counts().values
        freqTable["Relative_Frequency"]= freqTable["Frequency"]/freqTable["Unique_Values"].count()
        freqTable["CumSum"]= freqTable["Relative_Frequency"].cumsum()
        return freqTable
    
    
    def Univariant(data,quant):
        import pandas as pd
        import numpy as np
        lesser=[]
        greater=[]
        descriptive= pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%","99%","100%","Min","Max","IQR",'1.5Rule','Lesser',
                                    'Greater','Skew','Kurtosis','var','std'],columns=quant)
        for columnNames in quant:
            descriptive[columnNames]["Mean"]=data[columnNames].mean()
            descriptive[columnNames]["Median"]=data[columnNames].median()
            descriptive[columnNames]["Mode"]=data[columnNames].mode()[0]
            descriptive[columnNames]["25%"]=data.describe()[columnNames]["25%"]
            descriptive[columnNames]["50%"]=data.describe()[columnNames]["50%"]
            descriptive[columnNames]["75%"]=data.describe()[columnNames]["75%"]
            descriptive[columnNames]["99%"]=np.percentile(data[columnNames],99)
            descriptive[columnNames]["100%"]=data.describe()[columnNames]["max"]
            descriptive[columnNames]["Min"]= data[columnNames].min()
            descriptive[columnNames]["Max"]= data[columnNames].max()
            descriptive[columnNames]["IQR"]=descriptive[columnNames]["75%"]-descriptive[columnNames]["25%"]
            descriptive[columnNames]["1.5Rule"]= 1.5*descriptive[columnNames]["IQR"]
            descriptive[columnNames]["Lesser"]=descriptive[columnNames]["25%"]-descriptive[columnNames]["1.5Rule"]
            descriptive[columnNames]["Greater"]=descriptive[columnNames]["75%"]+descriptive[columnNames]["1.5Rule"]
            descriptive[columnNames]["Skew"]= data[columnNames].skew()
            descriptive[columnNames]["Kurtosis"]= data[columnNames].kurtosis()
            descriptive[columnNames]["var"]= data[columnNames].var()
            descriptive[columnNames]["std"]= data[columnNames].std()
            
        return descriptive
    
  
    def findoutliaercolumn(data,quant):
        import pandas as pd
        import numpy as np
        descriptive= pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%","99%","100%","Min","Max","IQR",'1.5Rule','Lesser',
                                    'Greater'],columns=quant)
        lesser=[]
        greater=[]
        for columnNames in quant:
            descriptive[columnNames]["25%"]=data.describe()[columnNames]["25%"]
            descriptive[columnNames]["50%"]=data.describe()[columnNames]["50%"]
            descriptive[columnNames]["75%"]=data.describe()[columnNames]["75%"]
            descriptive[columnNames]["99%"]=np.percentile(data[columnNames],99)
            descriptive[columnNames]["100%"]=data.describe()[columnNames]["max"]
            descriptive[columnNames]["Min"]= data[columnNames].min()
            descriptive[columnNames]["Max"]= data[columnNames].max()
            descriptive[columnNames]["IQR"]=descriptive[columnNames]["75%"]-descriptive[columnNames]["25%"]
            descriptive[columnNames]["1.5Rule"]= 1.5*descriptive[columnNames]["IQR"]
            descriptive[columnNames]["Lesser"]=descriptive[columnNames]["25%"]-descriptive[columnNames]["1.5Rule"]
            descriptive[columnNames]["Greater"]=descriptive[columnNames]["75%"]+descriptive[columnNames]["1.5Rule"]
            if (descriptive[columnNames]["Min"]<descriptive[columnNames]["Lesser"]):
                lesser.append(columnNames)
                print("Lesser Outliear: ",[columnNames])
            if (descriptive[columnNames]["Max"]>descriptive[columnNames]["Greater"]):
                greater.append(columnNames)
                print("Greater Outliear: ",[columnNames])
        return lesser,greater   
        
 
    def replaceoutliaer(data,quant):
        import pandas as pd
        import numpy as np
        descriptive= pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%","99%","100%","Min","Max","IQR",'1.5Rule','Lesser',
                                    'Greater'],columns=quant)
        lesser=[]
        greater=[]
        for columnNames in quant:
            descriptive[columnNames]["25%"]=data.describe()[columnNames]["25%"]
            descriptive[columnNames]["50%"]=data.describe()[columnNames]["50%"]
            descriptive[columnNames]["75%"]=data.describe()[columnNames]["75%"]
            descriptive[columnNames]["99%"]=np.percentile(data[columnNames],99)
            descriptive[columnNames]["100%"]=data.describe()[columnNames]["max"]
            descriptive[columnNames]["Min"]= data[columnNames].min()
            descriptive[columnNames]["Max"]= data[columnNames].max()
            descriptive[columnNames]["IQR"]=descriptive[columnNames]["75%"]-descriptive[columnNames]["25%"]
            descriptive[columnNames]["1.5Rule"]= 1.5*descriptive[columnNames]["IQR"]
            descriptive[columnNames]["Lesser"]=descriptive[columnNames]["25%"]-descriptive[columnNames]["1.5Rule"]
            descriptive[columnNames]["Greater"]=descriptive[columnNames]["75%"]+descriptive[columnNames]["1.5Rule"]
            if (descriptive[columnNames]["Min"]<descriptive[columnNames]["Lesser"]):
                lesser.append(columnNames)
                #print("Lesser Outliear: ",[columnNames])
            if (descriptive[columnNames]["Max"]>descriptive[columnNames]["Greater"]):
                greater.append(columnNames)
                #print("Greater Outliear: ",[columnNames])
        for columnNames in lesser:
            data[columnNames][data[columnNames] < descriptive[columnNames]["Lesser"]] = descriptive[columnNames]["Lesser"]
            #f=data[columnNames][data[columnNames]< descriptive[columnNames]["Lesser"]]
            #print (f)
        for columnNames in greater:
            data[columnNames][data[columnNames] > descriptive[columnNames]["Greater"]] = descriptive[columnNames]["Greater"]       

    def stdNBGraph(dataset):
            import seaborn as sns
            mean= dataset.mean()
            std= dataset.std()
            z_score= [((j-mean)/std) for j in dataset]
            sns.distplot(z_score,kde=True)        
 
    def get_pdf_probability(dataset,startrange,endrange):
        import matplotlib.pyplot as plt
        from scipy.stats import norm
        import seaborn as sns
        #startrange=40
        #endrange=90
        ax= sns.distplot(dataset,kde=True,kde_kws={'color':'blue'},color='Green')
        plt.axvline(startrange,color='red')
        plt.axvline(endrange,color='red')
        #generate a sample to get the Mean & Std
        sample= dataset
        sample_mean=sample.mean()
        sample_std=sample.std()
        print('Mean=%.3f,Standard Deviasion=%.3f' %(sample_mean,sample_std))
        #define the distriibution
        dist= norm(sample_mean,sample_std)
        #Sample Probability of a range of outcomes
        #values= [value for value in range(startrange,endrange)]
        #values
        probablity=[dist.pdf(value) for value in range(startrange,endrange)]
        probs= sum(probablity)
        probs
        print("The area between the range({},{}):{}".format(startrange,endrange,probs))
        return probs