import json
import requests
import base64
import os,time
import phonenumbers
from phonenumbers import timezone

def lambda_handler(event, context):
   ## print (event)
    
##Getting Calling Number from Connect
    e164num = event['Details']['Parameters']['ANI']
    orinumber =e164num[3:]
    ##orinumber = phonenumbers.parse(e164num,None)
    ##orinumber= phonenumbers.format_number(e164num, phonenumbers.PhoneNumberFormat.NATIONAL)
    
##defining parameters for Authentication
    params={
        "grant_type":"password",
        "client_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "client_secret" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "username":"apiuser@mindstretcher.com",
        "password" :"mslc2021"
    }
##Getting access token
    r=requests.post("https://login.salesforce.com/services/oauth2/token",params=params);
    access_token=r.json().get("access_token")
    instance_url=r.json().get("instance_url")

##creating instance URL   
    url = instance_url+'/services/data/v46.0/query/'
    
##Updating the number format
    orinumber =str(orinumber)
    ##orinumber =str(phonenumbers.parse(orinumber, None).national_number)
    number = '\''+orinumber+'\''

    
##Creating the Query  
    query = 'SELECT Primary_Name__c, ID, Primary_Email__c  FROM Student__c WHERE Contact_number__c = '+number
    parameters = {'q':query}
    headers = {'Authorization':'Bearer '+ access_token}
    r = requests.get(url =url, headers = headers, params=parameters)
    data =r.json()
    NumberofRecords = data['totalSize']
    
    
##check whether is there any contacts

    if NumberofRecords>0:
        CallingName = data['records'][0]['Primary_Name__c'] 
        StudentOID = data["records"][0]['Id']
        ContactEmail = data['records'][0]['Primary_Email__c']
        response_to_connect = {"CallingName":CallingName, "StudentOID":StudentOID, "ContactEmail":ContactEmail, "NumberofRecords":NumberofRecords}
        return (response_to_connect)
    

    else:
        response_to_connect = {"NumberofRecords":NumberofRecords}
        print(response_to_connect)
        return (response_to_connect)
                
    
