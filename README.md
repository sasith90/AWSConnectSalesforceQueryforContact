# AWSConnectSalesforceQueryforContact
This Lambda python code will connect Salesforce via Conencted APP and Query Contact based on Contact Number
Variables to change

ANI - AWS Connect Invoke Lambda input paramater
   params={
        "grant_type":"password",
        "client_id":"Conencted APP Client ID",
        "client_secret" : "AAConnected App secret",
        "username":"aSalesforce login username",
        "password" :"mSalesforce Login password"
    }
  Salesforce Object Values 
    - Primary_Name__c, 
    - ID, 
    - Primary_Email__c  
    Salesforce Object Class 
    - Student__c 
    Salesforce Match Attribute (this is the attribute that you are going to check)
    - Contact_number__c
   
   AWS Connect external Attributes 
   - CallingName
   - StudentOID
   - ContactEmail
   - NumberofRecords
