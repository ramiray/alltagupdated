from pprint import pprint
import pandas as pd
import boto3
import json
from botocore.exceptions import ClientError


client = boto3.client('resourcegroupstaggingapi', )
df=pd.DataFrame({'ResourceARN':[],'Key':[],'Value':[]}) 
df1=pd.DataFrame({'ResourceARN':[]}) 
client = boto3.client('resourcegroupstaggingapi', region_name='ap-southeast-2')
paginator = client.get_paginator('get_resources')
pages= paginator.paginate()


for page in pages:
    resources=page['ResourceTagMappingList']
    for resource in resources:
        arn=resource.get('ResourceARN')
        tags=resource.get('Tags')
        #print(arn,tags)
        if tags==[]:
            df1.loc[len(df.index)]=[arn]
            df1.to_csv('Untaggedresources.csv',index=False)


        for i,tags in enumerate(resource.get('Tags')):
        
            #print(tags)
            
            if tags['Key'] == "env" or tags['Value'] == " ":
                #print(arn,tags)
                df.loc[len(df.index)]=[arn,tags['Key'],tags['Value']]

            #if i==0:
            #    df.loc[len(df.index)]=[arn,tags['Key'],tags['Value']]
            #else:
            #    df.loc[len(df.index)]=['',tags['Key'],tags['Value']]
        
df.to_csv('Outputfiletest.csv')

    