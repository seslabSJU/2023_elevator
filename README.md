
| |














|oneM2M<br />Technical Report |oneM2M<br />Technical Report |
|-|-|
|Document Number |oneM2M-TR-0051-V-3.0.0  |
|Document Name: |oneM2M API guide<br /> |
|Date: |2021-05-12 |
|Abstract: |Provides a collection of oneM2M API for guiding developers to develop applications using functionalities provided by a oneM2M service platform |
|Template Version: January 2017 (Do not modify) |Template Version: January 2017 (Do not modify) |











The present document is provided for future development work within oneM2M only. The Partners accept no liability for any use of the present document.

The present document has not been subject to any approval process by the oneM2M Partners Type 1.  Published oneM2M specifications and reports for implementation should be obtained via the oneM2M Partners' Publications Offices.





<br />About oneM2M 

The purpose and goal of oneM2M is to develop technical specifications which address the need for a common M2M Service Layer that can be readily embedded within various hardware and software, and relied upon to connect the myriad of devices in the field with M2M application servers worldwide. 

More information about oneM2M may be found at:  http//www.oneM2M.org

Copyright Notification

(c) 2021, oneM2M Partners Type 1 (ARIB, ATIS, CCSA, ETSI, TIA, TSDSI, TTA, TTC).

All rights reserved.

The copyright and the foregoing restriction extend to reproduction in all media.



Notice of Disclaimer & Limitation of Liability 

The information provided in this document is directed solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendation as to products or vendors is made or should be implied. 

NO REPRESENTATION OR WARRANTY IS MADE THAT THE INFORMATION IS TECHNICALLY ACCURATE OR SUFFICIENT OR CONFORMS TO ANY STATUTE, GOVERNMENTAL RULE OR REGULATION, AND FURTHER, NO REPRESENTATION OR WARRANTY IS MADE OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR AGAINST INFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. NO oneM2M PARTNER TYPE 1 SHALL BE LIABLE, BEYOND THE AMOUNT OF ANY SUM RECEIVED IN PAYMENT BY THAT PARTNER FOR THIS DOCUMENT, WITH RESPECT TO ANY CLAIM, AND IN NO EVENT SHALL oneM2M BE LIABLE FOR LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES. oneM2M EXPRESSLY ADVISES ANY AND ALL USE OF OR RELIANCE UPON THIS INFORMATION PROVIDED IN THIS DOCUMENT IS AT THE RISK OF THE USER.

<br />Contents
Annex A: Example of notification    146
Annex B: Bibliography    166



# 1 Scope
The present document is a collection of the CRUDN messages used for managing some of the main resources defined in oneM2M TS-0001 <a href="#_ref_i.2">[i.2]</a>. It also provides the description and associated flow in basic examples. It aims to use this list as a common sets of APIs to help developers to write applications that can run across different platforms and specific implementations.

When an application developer would need to build software code for managing a specific resource, he could have an immediate access to the list of CRUDN message with description and its associated examples of requests to send and its expected responses. The REST API examples are sorted by resource type and CRUDN operations, which allows a quick and easy access to the information.


# 2 References

## 2.1 Normative references
Normative references are not applicable in the present document.


## 2.2 Informative references
References are either specific (identified by date of publication and/or edition number or version number) or nonspecific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area.


- <a name="_ref_i.1">[i.1]</a>    oneM2M Drafting Rules.
> NOTE:    Available at [http://www.onem2m.org/images/files/oneM2M-Drafting-Rules.pdf](http://www.onem2m.org/images/files/oneM2M-Drafting-Rules.pdf).

- <a name="_ref_i.2">[i.2]</a>    oneM2M TS-0001: "Functional Architecture".
- <a name="_ref_i.3">[i.3]</a>    oneM2M TS-0004: "Service Layer Core protocol Specification".

# 3 Definition of terms, symbols and abbreviations

## 3.1 Terms

Void.


## 3.2 Symbols
Void.


## 3.3 Abbreviations
For the purposes of the present document, the following abbreviations apply:


`ACP    Access Control Policy`  
`AE    Application Entity`  
`AE-ID    Application Entity Identifier`  
`API    Application Programming Interface`  
`CBOR     Concise Binary Object Representation`  
`CRUDN    Create, Retrieve, Update, Delete and Notify operations for REST API`  
`CSE    Common Services Entity`  
`HAIM    Home Appliances Information Model`  
`HTTP    HyperText Transfer Protocol`  
`JSON    JavaScript Object Notation`  
`RCN    Result Content`  
`REST    Representational State Transfer`  
`XML    eXtensible Markup Language`  

# 4 Conventions

The key words "Shall", "Shall not", "May", "Need not", "Should", "Should not" in the present document are to be interpreted as described in the oneM2M Drafting Rules <a href="#_ref_i.1">[i.1]</a>.


# 5 oneM2M REST APIs

## 5.1 Introduction
The major objective of the present document is providing example sets of request and response. The REST APIs that are defined in the present document cover for resources Create, Retrieve, Update and Delete management, subscription/notification, data discovery, etc. Sending the CRUD request to the CSE and getting the response may help user to learn oneM2M specification. 

In the current guide, examples of API are written based on HTTP protocol binding and JSON format. The APIs are written based on release 2a version.

For more references, please refer to clause 2.2.


## 5.2 Short name representation

### 5.2.1 Introduction
oneM2M defines short names for resources and attributes. To encode the message using XML, JSON and CBOR, short names are used. Request or response body which have been formed in short names can reduce the size of the message.


### 5.2.2 Resource type short names
Table 5.2.2-1 shows shot names for the resource type. It includes resource types which are used in the present document. For more information please refer to oneM2M TS-0004 <a href="#_ref_i.2">[i.2]</a>.


**Table 5.2.2-1: Resource type short names**

|Resource Type Name |Short Name |
|-|-|
|accessControlPolicy |acp |
|AE |ae |
|container |cnt |
|contentInstance |cin |
|CSEBase |cb |
|group |grp |
|remoteCSE |csr |
|subscription |sub |
|semanticDescriptor |smd |
|timeSeries |ts |
|timeSeriesInstance |tsi |




### 5.2.3 Resource attribute short names
Table 5.2.3-1 shows shot names for the resource attribute. It includes attributes which are used in the present document. For more information please refer to oneM2M TS-0004 <a href="#_ref_i.2">[i.2]</a>.


**Table 5.2.3-1: Resource attribute short names**

|Attribute Name |Occurs in |Short Name |
|-|-|-|
|accessControlPolicyIDs |All except accessControlPolicy, contentInstance |acpi |
|announcedAttribute |accessControlPolicy, AE, container, contentInstance, group, locationPolicy, mgmtObj, node, remoteCSE, schedule, semanticDescriptor, trafficPattern |aa |
|announceTo |accessControlPolicy, AE, container, contentInstance, group, locationPolicy, mgmtObj, node, remoteCSE, schedule, semanticDescriptor, trafficPattern |at |
|creationTime |All |ct |
|expirationTime |All except contentInstance, CSEBase |et |
|labels |All (optional) |lbl |
|lastModifiedTime |All |lt |
|Link |All |lnk |
|parentID |All |pi |
|resourceID |All |ri |
|resourceType |All |ty |
|stateTag |container, contentInstance, delivery, request |st |
|resourceName |All |rn |
|privileges |accessControlPolicy |pv |
|selfPrivileges |accessControlPolicy |pvs |
|App-ID |AE |api |
|AE-ID |AE |aei |
|appName |AE |apn |
|pointOfAccess |AE, CSEBase, remoteCSE |poa |
|ontologyRef |AE, container, contentInstance, semanticDescriptor. flexContainer, timeSeries |or |
|nodeLink |AE, CSEBase, remoteCSE |nl |
|contentSerialization |AE |csz |
|creator |container, contentInstance, eventConfig, group, pollingChannel, statsCollect, statsConfig, subscription, semanticDescriptor, notificationTargetPolicy, flexContainer, timeSeries |cr |
|maxNrOfInstances |container, timeSeries |mni |
|maxByteSize |container, timeSeries |mbs |
|maxInstanceAge |container, timeSeries |mia |
|currentNrOfInstances |container, timeSeries |cni |
|currentByteSize |container |cbs |
|locationID |container |li |
|disableRetrieval |container |disr |
|contentInfo |contentInstance |cnf |
|contentSize |contentInstance, timeSeriesInstance |cs |
|contentRef |contentInstance |conr |
|containerDefinition |flexContainer |cnd |
|primitiveContent  |request |pc |
|content |contentInstance, timeSeriesInstance |con |
|cseType |CSEBase, remoteCSE |cst |
|CSE-ID |CSEBase, remoteCSE, serviceSubscribedNode |csi |
|supportedResourceType |CSEBase |srt |
|notificationCongestionPolicy |CSEBase |ncp |
|memberType |group |mt |
|currentNrOfMembers |group |cnm |
|maxNrOfMembers |group |mnm |
|memberIDs |group |mid |
|membersAccessControlPolicyIDs |group |macp |
|memberTypeValidated |group |mtv |
|consistencyStrategy |group |csy |
|semanticSupportIndicator |group |ssi |
|notifyAggregation |group |nar |
|groupName |group, subscription |gn |
|CSEBase |remoteCSE |cb |
|M2M-Ext-ID |remoteCSE |mei |
|Trigger-Recipient-ID |remoteCSE |tri |
|requestReachability |remoteCSE |rr |
|triggerReferenceNumber |remoteCSE |trn |
|eventNotificationCriteria |subscription |enc |
|expirationCounter |subscription |exc |
|notificationURI |subscription |nu |
|groupID |subscription |gpi |
|notificationForwardingURI |subscription |nfu |
|batchNotify |subscription |bn |
|rateLimit |subscription |rl |
|preSubscriptionNotify |subscription |psn |
|pendingNotification |subscription |pn |
|notificationStoragePriority |subscription |nsp |
|latestNotify |subscription |ln |
|notificationContentType |subscription |nct |
|notificationEventCat |subscription |nec |
|subscriberURI |subscription |su |
|descriptorRepresentation |semanticDescriptor |dcrp |
|semanticOpExec |semanticDescriptor |soe |
|descriptor |semanticDescriptor |dsp |
|relatedSemantics |semanticDescriptor |rels |
|periodicInterval |timeSeries |pei |
|missingDataDetect |timeSeries |mdd |
|missingDataMaxNr |timeSeries |mdn |
|missingDataList |timeSeries |mdlt |
|missingDataCurrentNr |timeSeries |mdc |
|missingDataDetectTimer |timeSeries |mdt |
|dataGenerationTime |timeSeriesInstance |dgt |
|sequenceNr |timeSeriesInstance |snr |
|e2eSecInfo |CSEBase, remoteCSE, AE |esi |
|supportedReleaseVersions |CSEBase, remoteCSE, AE |srv |
|descriptorRepresentation |semanticDescriptor |dcrp |
|semanticOpExec |semanticDescriptor |soe |
|descriptor |semanticDescriptor |dsp |
|relatedSemantics |semanticDescriptor |rels |
|periodicInterval |timeSeries |pei |
|missingDataDetect |timeSeries |mdd |
|missingDataMaxNr |timeSeries |mdn |
|missingDataList |timeSeries |mdlt |
|missingDataCurrentNr |timeSeries |mdc |
|missingDataDetectTimer |timeSeries |mdt |
|dataGenerationTime |timeSeriesInstance |dgt |
|sequenceNr |timeSeriesInstance |snr |
|e2eSecInfo |CSEBase, remoteCSE, AE |esi |
|supportedReleaseVersions |CSEBase, remoteCSE, AE |srv |




## 5.3 Enumeration data types

### 5.3.0 Introduction
The oneM2M Enumeration Types are based on xs:integer, and the numeric values are interpreted as specified in table 5.3.1-1.


### 5.3.1 m2m:resource Type
The enumeration type of resource Type is used in the Content-Type in the HTTP header of request. Table 5.3.1-1 only has enumeration type for resource Type which are used in the present document. More information can be found in oneM2M TS-0004 <a href="#_ref_i.2">[i.2]</a>.


**Table 5.3.1-: Interpretation of resourceType**

|Value |Interpretation |Note |
|-|-|-|
|1 |accessControlPolicy | |
|2 |AE | |
|3 |container | |
|4 |contentInstance | |
|5 |CSEBase | |
|9 |group | |
|15 |pollingChannel | |
|16 |remoteCSE | |
|23 |subscription | |
|24 |semanticDescriptor | |
|28 |flexContainer | |
|29 |timeSeries | |
|30 |timeSeriesInstance | |




### 5.3.2 m2m:result content
The response format can be changed using resultContent (RCN) parameter. The oneM2M standard defines 8 different result content, but this API guide only deals with result content 0 to 3. Table 5.3.2-1 shows resultContent value and response format matches.


**Table 5.3.2-: Interpretation of resultContent**

|Value |Interpretation |Note |
|-|-|-|
|0 |nothing | |
|1 |attributes | |
|2 |hierarchical address | |
|3 |hierarchical address and attributes | |




# 6 Open API collection

## 6.1 APIs list

### 6.1.1 Introduction
The identifier of the API is constructed with the following format:

API/&lt;RESOURCE_TYPE>/&lt;OPERATION_TYPE>/&lt;NUMBER>_&lt;PERMUTATION>

Specific values are used in the format defined in table 6.1.1-1.


**Table 6.1.1-1: API Id Notation**

|Name |Value |interpretation |
|-|-|-|
|&lt;RESOURCE_TYPE> |CB |CSEBase |
|&lt;RESOURCE_TYPE> |CSR |remoteCSE |
|&lt;RESOURCE_TYPE> |AE |AE |
|&lt;RESOURCE_TYPE> |CONT |container |
|&lt;RESOURCE_TYPE> |CI |contentInstance |
|&lt;RESOURCE_TYPE> |SMD |semanticDescriptor |
|&lt;RESOURCE_TYPE> |DIS |discovery |
|&lt;RESOURCE_TYPE> |SUB |subscription |
|&lt;RESOURCE_TYPE> |GRP |group |
|&lt;RESOURCE_TYPE> |TS |timeSeries |
|&lt;RESOURCE_TYPE> |TSI |timeSeriesInstance |
|&lt;RESOURCE_TYPE> |ACP |accessControlPolicy |
|&lt;RESOURCE_TYPE> |FLX |flexContainer |
|&lt;OPERATION_TYPE> |CRE |CREATE |
|&lt;OPERATION_TYPE> |RET |RETRIEVE |
|&lt;OPERATION_TYPE> |UPD |UPDATE |
|&lt;OPERATION_TYPE> |DEL |DELETE |
|&lt;OPERATION_TYPE> |DIS |DISCOVERY |
|&lt;NUMBER> |001 - 999 |- |
|&lt;PERMUTATION> |short name of attribute or resource type that is used in a request primitive. |A resultContent with its value is presented as a &lt;PERMUTATION><br />RCN1, RCN2, RCN3, RCN4<br />Filter Criteria parameter used in discovery clause is presented as a &lt;PERMUTATION><br />TY, LBL, LVL, CRB, etc. |






## 6.2 API details

### 6.2.1 Introduction
This clause introduces standard APIs to perform CRUD operations on the target resource. Each API has request and response using HTTP binding and JSON serialization, but some resources do not have all CRUD APIs which means that the resource does not support all operations. A result content is only used from 0 to 3 in this clause.


### 6.2.2 Resource Type CSEBase

#### 6.2.2.0 Introduction
A &lt;CSEBase> resource represents a CSE and it is the root for all resources that are residing in the CSE. The &lt;CSEBase>resource does not support the creation, update, and delete operations via API but only supports retrieve operation.


#### 6.2.2.1 API-CB-RET

|<br /><br />API Id |API/CB/RET/001<br />API/CB/RET/001_RCN1 <br />API/CB/RET/001_RCN4 |
|-|-|
|API Name |CSEBase RETRIEVE with or without resultContent parameter |
|Target Resource |&lt;CSEBase> resource of the requested &lt;AE> resource |
|<br />Description |The interface is used to send a &lt;CSEBase> resource RETRIEVE request to CSE, and receive response from the CSE.  |
|<br />Resource Structure<br />before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />    API/CB/RET/001<br />   API/CB/RET/001_RCN1<br /><br /><br />HTTP Request:<br /><br />GET /mn-name?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />Accept: application/json<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2000<br />Content-Length:344<br />Content-Type:application/json<br />X-M2M-Origin:/mnID<br />X-M2M-RVI: 2a<br /><br /><br /><br /><br />{<br />    "m2m:cb": {<br />        "acpi": [<br />            "mnIDAcp"<br />        ],<br />        "csi": "/mnID",<br />        "cst": 2,<br />        "csz": [<br />            "application/xml",<br />            "application/json"<br />        ],<br />        "ct": "20180727T135221",<br />        "lbl": [<br />            "17.0.0+",<br />            "ID-CSE-01"<br />        ],<br />        "lt": "20180727T135221",<br />        "pi": null,<br />        "poa": [<br />            "http://192.168.0.10:8282"<br />        ],<br />        "ri": "mnID",<br />        "rn": "mn-name",<br />        "srt": [<br />            1,<br />            2,<br />            3,<br />            4,<br />            5,<br />            9,<br />            12,<br />            13,<br />            14,<br />            15,<br />            16,<br />            18,<br />            23,<br />            17,<br />            11,<br />            20,<br />            19,<br />            28,<br />            22,<br />            7,<br />            21,<br />            24,<br />            100,<br />            8,<br />            10<br />        ],<br />        "srv": [<br />            "2a"<br />        ],<br />        "ty": 5,<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=4<br /> |<br />   API/CB/RET/001_RCN4<br /><br /><br />HTTP Request:<br /><br />GET /mn-name?rcn=4 HTTP/1.1<br />Host: 192.168.0.10:8282<br />Accept: application/json<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2000<br />Content-Length: 1009<br />Content-Type:application/json<br />X-M2M-Origin:/mnID<br />X-M2M-RVI: 2a<br /><br /><br />{<br />    "m2m:cb": {<br />        "acpi": [<br />            "mnIDAcp"<br />        ],<br />        "csi": "/mnID",<br />        "cst": 2,<br />        "csz": [<br />            "application/xml",<br />            "application/json"<br />        ],<br />        "ct": "20180727T135221",<br />        "lbl": [<br />            "17.0.0+",<br />            "ID-CSE-01"<br />        ],<br />        "lt": "20180727T135221",<br />        "m2m:acp": [<br />            {<br />                "ct": "20180723T141039",<br />                "et": "99991231T235959",<br />                "lbl": [<br />                    "cseAcp"<br />                ],<br />                "lt": "20180723T141039",<br />                "pi": "mnID",<br />                "pv": {<br />                    "acr": [<br />                        {<br />                            "acco": {<br />                                "acip": {<br />                                    "ipv4": [<br />                                        "127.0.0.1/0"<br />                                    ]<br />                                },<br />                                "actw": [<br />                                    "* * * * * *"<br />                                ]<br />                            },<br />                            "acop": 63,<br />                            "acor": [<br />                                "*"<br />                            ]<br />                        }<br />                    ]<br />                },<br />                "pvs": {<br />                    "acr": [<br />                        {<br />                            "acco": {<br />                                "acip": {<br />                                    "ipv4": [<br />                                        "127.0.0.1/0",<br />                                        "127.0.0.1/1"<br />                                    ]<br />                                },<br />                                "actw": [<br />                                    "* * * * * *"<br />                                ]<br />                            },<br />                            "acop": 63,<br />                            "acor": [<br />                                "*"<br />                            ]<br />                        }<br />                    ]<br />                },<br />                "ri": "mnIDAcp",<br />                "rn": "mn-nameAcp",<br />                "ty": 1<br />            }<br />        ],<br />        "m2m:ae": [<br />            {<br />                "aei": "CAE0120180723T1415351396520173012480_cse01",<br />                "api": "A01.com.company.Temp",<br />                "ct": "20180723T141535",<br />                "et": "99991231T235959",<br />                "lbl": [<br />                    "indoor_temp",<br />                    "room_1"<br />                ],<br />                "lt": "20180723T142022",<br />                "pi": "mnID",<br />                "ri": "CAE0120180723T1415351396520173012480_cse01",<br />                "rn": "ae_sensor",<br />                "rr": false,<br />                "ty": 2<br />            }<br />        ],<br />        "pi": null,<br />        "poa": [<br />            "http://192.168.0.10:8282"<br />        ],<br />        "ri": "mnID",<br />        "rn": "mn-name",<br />        "srt": [<br />            1,<br />            2,<br />            3,<br />            4,<br />            5,<br />            9,<br />            12,<br />            13,<br />            14,<br />            15,<br />            16,<br />            18,<br />            23,<br />            17,<br />            11,<br />            20,<br />            19,<br />            28,<br />            22,<br />            7,<br />            21,<br />            24,<br />            100,<br />            8,<br />            10<br />        ],<br />        "ty": 5,<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />    }<br />}<br /><br /> |


### 6.2.3 Resource Type remoteCSE

#### 6.2.3.0 Introduction
The &lt;remoteCSE> resource represents a Registree CSE that is registered into a Registrar CSE, and &lt;remoteCSE> locates directly under the &lt;CSEBase> of the Registrar CSE. Similarly, one &lt;remoteCSE> resource will also be created under the &lt;CSEBase> of the Registree CSE to represent the Registrar CSE when the Registree CSE is successfully registered into the Registrar CSE.


#### 6.2.3.1 API-CSR-CRE

|<br /><br />API Id |API/CSR/CRE/001<br />API/CSR/CRE/001_RCN1 <br />API/CSR/CRE/001_RCN2<br />API/CSR/CRE/001_RCN3 <br />API/CSR/CRE/001_RCN4 |
|-|-|
|API Name |remoteCSE CREATE with or without resultContent parameter |
|Target Resource |&lt;remoteCSE> resource |
|<br />Description |The interface is used to send a &lt;remoteCSE> resource CREATE request to CSE, and receive response from the CSE.  |
|<br /><br />Resource Structure | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=0<br /> |<br />   API/CSR/CRE/001_RCN0<br /><br /><br />HTTP Request:<br /><br />POST /cse-name?rcn=0 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Content-Type:application/json;ty=16<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />   <br />        "m2m:csr": {<br />            "cb": "//192.168.0.50:8080/cse-name2",<br />            "csi": "/cse2ID",<br />            "rn": "cse-name2",<br />            "rr": true<br />              <br />        }<br />   <br />}<br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 201 Created<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />Content-Length:0<br />Content-Type:application/json<br />Content-Location: /cseID/cse2ID<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />    API/CSR/CRE/001<br />   API/CSR/CRE/001_RCN1<br /><br /><br />HTTP Request:<br /><br />POST /cse-name?rcn=1 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Content-Type:application/json;ty=16<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />   <br />        "m2m:csr": {<br />            "cb": "//192.168.56.50:8080/cse-name2",<br />            "csi": "/cse2ID",<br />            "rn": "cse-name2",<br />            "rr": true<br />              <br />        }<br />   <br />}<br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 201 Created<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2001<br />X-M2M-RVI: 2a<br />Content-Length:216<br />Content-Type:application/json<br />Content-Location: /cseID/cse2ID<br /><br /><br /><br />{<br />    "m2m:csr": {<br />        "cb": "//192.168.0.50:8080/cse-name2",<br />        "csi": "/cse2ID",<br />        "ct": "20200604T123044,616218",<br />        "et": "99991231T235959",<br />        "lt": "20200604T123044,616218",<br />        "pi": "ID-CSE-01",<br />        "ri": "cse2ID",<br />        "rn": "cse-name2",<br />        "rr": false,<br />        "ty": 16<br />    }<br />}<br /><br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />   API/CSR/CRE/001_RCN2<br /><br /><br />HTTP Request:<br /><br />POST /cse-name?rcn=2 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Content-Type:application/json;ty=16<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />   <br />        "m2m:csr": {<br />            "cb": "//192.168.0.50:8080/cse-name2",<br />            "csi": "/cse2ID",<br />            "rn": "cse-name2",<br />            "rr": true<br />              <br />        }<br />   <br />}<br /><br />HTTP Response:<br /><br />HTTP/1.1 201 Created<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2001<br />X-M2M-RVI: 2a<br />Content-Length:30<br />Content-Type:application/json<br />Content-Location: /cseID/cse2ID<br /><br />{"m2m:uri":"cse-name/cse-name2"}<br /><br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=3<br /> |<br />   API/CSR/CRE/001_RCN3	<br /><br /><br />HTTP Request:<br /><br />POST /cse-name?rcn=3 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Content-Type:application/json;ty=16<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />   <br />        "m2m:csr": {<br />            "cb": "//192.168.0.50:8080/cse-name2",<br />            "csi": "/cse2ID",<br />            "rn": "cse-name2",<br />            "rr": true<br />              <br />        }<br />   <br />}<br /><br />HTTP Response:<br /><br />HTTP/1.1 201 Created<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2001<br />X-M2M-RVI: 2a<br />Content-Length:264<br />Content-Type:application/json<br />Content-Location: /cseID/cse2ID<br /><br />{<br />    "m2m:rce": {<br />        "m2m:csr": {<br />            "cb": "//192.168.56.2:8282/cse-name2",<br />            "csi": "/cse2ID",<br />            "ct": "20180801T093501",<br />            "et": "99991231T235959",<br />            "lt": "20180801T093501",<br />            "pi": "cseID",<br />            "poa": [<br />                "http://192.168.56.2:8282"<br />            ],<br />            "ri": "cse2ID",<br />            "rn": "cse-name2",<br />            "rr": true,<br />            "ty": 16,<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />        },<br />        "uri": "cse-name/cse-name2"<br />    }<br />}<br /> |




#### 6.2.3.2 API-CSR-RET

|<br />API Id |API/CSR/RET/001<br />API/CSR/RET/001_RCN1  |
|-|-|
|API Name |remoteCSE RETRIEVE with or without resultContent parameter |
|Target Resource |&lt;remoteCSE> resource located under &lt;CSEBase> of the hosting CSE |
|<br /><br />Description |The interface is used to send a &lt;remoteCSE> RETRIEVE request attached with resultContent to a hosting CSE, and the hosting CSE will send back a response containing attributes of the requested &lt;remoteCSE> resource. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />    API/CSR/RET/001<br />   API/CSR/RET/001_RCN1<br /><br /><br />HTTP Request:<br /><br />GET /cse-name/cse-name2?rcn=1 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Accept: application/json<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2000<br />X-M2M-RVI: 2a<br />Content-Length:227<br />Content-Type:application/json<br /><br /><br /><br />{<br />    "m2m:csr": {<br />        "cb": "//192.168.56.2:8282/cse-name2",<br />        "csi": "/cse2ID",<br />        "ct": "20180801T093501",<br />        "et": "99991231T235959",<br />        "lt": "20180801T093501",<br />        "pi": "cseID",<br />        "poa": [<br />            "http://192.168.56.2:8282"<br />        ],<br />        "ri": "cse2ID",<br />        "rn": "cse-name2",<br />        "rr": true,<br />        "ty": 16,<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />    }<br />} |




#### 6.2.3.3 API-CSR-UPD

|<br />API Id |API/CSR/UPD/001<br />API/CSR/UPD/001_RCN0 <br />API/CSR/UPD/001_RCN1 |
|-|-|
|API Name |remoteCSE UPDATE with or without resultContent parameter |
|Target Resource |&lt;remoteCSE> resource located under &lt;CSEBase> of the hosting CSE |
|<br />Description |The interface is used to send a &lt;remoteCSE> UPDATE request attached with resultContent to a hosting CSE, and the hosting CSE will send back a response resultContent. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=0<br /> |<br />    API/CSR/UPD/001_RCN0<br /><br />EXAMPLE:	Demonstrate the update of the &lt;pointOfAccess> attribute of &lt;remoteCSE> resource.<br /><br /><br />HTTP Request:<br /><br />PUT /cse-name/cse-name2?rcn=0 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Content-Type: application/json<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />{<br />    "m2m:csr": {<br />        "poa": ["http://192.168.0.101:8282"]<br />    }<br />}<br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2004<br />X-M2M-RVI: 2a<br />Content-Length:0<br /><br /><br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />    API/CSR/UPD/001<br />   API/CSR/UPD/001_RCN1<br /><br />EXAMPLE:	Demonstrate the update of the &lt;pointOfAccess> attribute of &lt;remoteCSE> resource.<br /><br /><br />HTTP Request:<br /><br />PUT /cse-name/cse-name2?rcn=1 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Accept: application/json<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:csr": {<br />        "poa": ["http://192.168.0.100:8282"]<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2004<br />X-M2M-RVI: 2a<br />Content-Length:251<br />Content-Type:application/json<br /><br />{<br />    "m2m:csr": {<br />        "cb": "//192.168.56.2:8282/cse-name2",<br />        "csi": "/cse2ID",<br />        "ct": "20180801T093501",<br />        "et": "99991231T235959",<br />        "lt": "20180801T095839",<br />        "pi": "cseID",<br />        "poa": [<br />            "http://192.168.0.100:8282"<br />        ],<br />        "ri": "cse2ID",<br />        "rn": "cse-name2",<br />        "rr": true,<br />        "ty": 16<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />    }<br />}<br /> |




#### 6.2.3.4 API-CSR-DEL

|<br /><br />API Id |API/CSR/DEL/001<br />API/CSR/DEL/001_RCN0 <br />API/CSR/DEL/001_RCN1 |
|-|-|
|API Name |remoteCSE DELETE with or without resultContent parameter |
|Target Resource |&lt;remoteCSE> resource located under &lt;CSEBase> of the hosting CSE |
|<br /><br />Description |The interface is used to send a &lt;remoteCSE> DELETE request attached with resultContent set to 0 to the hosting CSE, and the hosting CSE will delete the &lt;remoteCSE> resource and send back a response containing the response status code of the DELETE operation. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=0<br /> |<br />    API/CSR/DEL/001_RCN0<br /><br /><br /><br />HTTP Request:<br /><br />DELETE /cse-name/cse-name2?rcn=0 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Accept: application/json<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2002<br />X-M2M-RVI: 2a<br />Content-Length:0<br /><br /><br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />    API/CSR/DEL/001<br />   API/CSR/DEL/001_RCN1<br /><br /><br /><br />HTTP Request:<br /><br />DELETE /cse-name/cse-name2 HTTP/1.1<br />Host: 192.168.56.102:9011<br />Accept: application/json<br />X-M2M-Origin: C0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />HTTP/1.1 200 OK<br />X-M2M-RI: 1234<br />X-M2M-RSC: 2004<br />X-M2M-RVI: 2a<br />Content-Length:228<br />Content-Type:application/json<br /><br />{<br />    "m2m:csr": {<br />        "cb": "//192.168.56.2:8282/cse-name2",<br />        "csi": "/cse2ID",<br />        "ct": "20180801T093501",<br />        "et": "99991231T235959",<br />        "lt": "20180801T100431",<br />        "pi": "cseID",<br />        "poa": [<br />            "http://192.168.0.101:8282"<br />        ],<br />        "ri": "cse2ID",<br />        "rn": "cse-name2",<br />        "rr": true,<br />        "ty": 16,<br />        "srv": [<br />            "1",<br />            "2",<br />            "2a"<br />        ]<br /><br />    }<br />}<br /> |




### 6.2.4 Resource Type AE
6.2.4.0    Introduction

The &lt;AE> resource represents information about an Application Entity that is registered to a CSE. The originator of an &lt;AE> create request is and only can be an AE. A CSE is not allowed to initiate an &lt;AE> create request. 

The &lt;AE> resource which resides in different kind of nodes such as Application Dedicated Node, Middle Node, Infrastructure Node, etc. An Application Dedicated Node could reside in a constrained M2M device, while a Middle Node could reside in an M2M gateway and an Infrastructure Node could reside in an M2M Service Infrastructure. For example, in smart home scenario, light bulbs are modelled as Application Dedicated Node which communicate with home gateway which is modelled as a Middle Node and in resource registration phase, light bulbs can be registered as an &lt;AE> resource.



OpenAPI repository for &lt;AE> Resource:  

[https://labs.etsi.org/rep/iot/onem2m-api/blob/master/OpenAPI/API-AE.json](https://labs.etsi.org/rep/iot/onem2m-api/blob/master/OpenAPI/API-AE.json)



6.2.4.1    AE CREATE



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871700720></mark>Initial state on CSE:



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871701A30></mark>









Call flow:

<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871703100></mark>



    

Example:



HTTP Request:



POST /csename HTTP/1.1

Host: 192.168.1.30:8080

X-M2M-Origin: CAdmin

Content-Type: application/json;ty=2

X-M2M-RI: 1234

X-M2M-RVI:3



{

    "m2m:ae" : {

        "rn": "temperature",

        "api": "N01.com.company.temperature ",

        "lbl": ["key1", "key2"],

        "rr": true,

        "srv": ["3"],

        "poa": ["http://192.168.1.30:8080"]

        }

}





HTTP Response:



201 Created

content-length: 313 

content-type: application/json 

date: Tue, 30 Mar 2021 15:39:34 GMT 

x-m2m-ri: 1234 

x-m2m-rsc: 2001 

x-m2m-rvi: 3

{

    "m2m:ae": {

        "rn": "temperature",

        "api": "N01.com.company.temperature ",

        "lbl": [

            "key1",

            "key2"

        ],

        "rr": true,

        "srv": [

            "3"

        ],

        "poa": [

            "http://192.168.1.30:8080"

        ],

        "ri": "CAdmin",

        "ct": "20210330T153934,791690",

        "lt": "20210330T153934,791690",

        "et": "20220330T153934,791714",

        "pi": "id-in",

        "ty": 2,

        "aei": "CAdmin"

    }

}







6.2.4.2    AE Retrieve



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871702A20></mark>Initial state on CSE:

<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D8717002C0></mark>



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871700270></mark>









Call flow:





Example:

HTTP Request:



GET /csename/temperature HTTP/1.1

Accept: application/json

Host: 192.168.0.10:8282

X-M2M-Origin: CAdmin

X-M2M-RI:1234

X-M2M-RVI: 3



















HTTP Response:



200 OK

Content-Length:323 

Content-Type:application/json

X-M2M-RI:1234

X-M2M-RVI: 3

X-M2M-RSC:2000

{

    "m2m:ae": {

        "rn": "temperature",

        "api": "N01.com.company.temperature ",

        "lbl": [

            "key1",

            "key2"

        ],

        "rr": true,

        "srv": [

            "3"

        ],

        "poa": [

            "http://192.168.1.30:8080"

        ],

        "ri": "CSUQPRVK06v",

        "ct": "20210407T093125,074401",

        "lt": "20210407T093125,074401",

        "et": "20220407T093125,074426",

        "pi": "id-in",

        "ty": 2,

        "aei": "CSUQPRVK06v"

    }





6.2.4.3    AE Update



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871702020></mark>Initial state on CSE:

<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871700A90></mark>



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871702610></mark>







Call flow:



Example:



HTTP Request:



PUT /csename/temperature HTTP/1.1

Host: 192.168.1.30:8080

X-M2M-Origin: CAdmin

Content-Type:application/json

Accept: application/json

X-M2M-RI: 1234

X-M2M-RVI: 3



{

    "m2m:ae" : {

        "lbl": ["temperature bedroom"],

        "poa": ["http://192.168.1.50:9090"]

        }

}





HTTP Response:



200 OK

Content-Length:330 

Content-Type:application/json

X-M2M-RI:1234

X-M2M-RVI: 3

X-M2M-RSC:2004



{

    "m2m:ae": {

        "rn": "temperature",

        "api": "N01.com.company.temperature ",

        "lbl": [

            "temperature bedroom"

        ],

        "rr": true,

        "srv": [

            "3"

        ],

        "poa": [

            "http://192.168.1.50:9090"

        ],

        "ri": "CSUQPRVK06v",

        "ct": "20210407T093125,074401",

        "lt": "20210407T094636,903417",

        "et": "20220407T093125,074426",

        "pi": "id-in",

        "ty": 2,

        "aei": "CSUQPRVK06v"

    }



6.2.4.3    AE Delete

<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D8716F33D0></mark>Initial state on CSE:

<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D8717002C0></mark>



<mark>unsupported pict element: <Element '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pict' at 0x000002D871700270></mark>













Call flow:







Example:

HTTP Request:



DELETE /csename/temperature HTTP/1.1

Host: 192.168.1.30:8080

X-M2M-Origin: CAdmin

X-M2M-RI:1234

X-M2M-RVI: 3





HTTP Response:



200 OK

Content-Length:0 

Content-Type:application/json

X-M2M-RI:1234

X-M2M-RVI: 3

X-M2M-RSC:2002




### 6.2.5 Resource Type container

#### 6.2.5.0 Introduction
The &lt;container> resource represents a container for data instances. It is used to share information with other entities and potentially to track the data. A &lt;container> resource has no associated content. It has only attributes and child resources.

The &lt;container> resource can be seen as a container of a group of data instances with same characteristics, for example, sensor measurement of temperature, humidity, illumination, CO2, etc. For example, when a temperature sensor is modelled as application dedicated node and registered with an &lt;AE> resource, a &lt;container> resource can be created under the created &lt;AE> as its child resource to contain temperature measurements. Note that &lt;container> resource has no associated content and the real data is contained in a child resource of container called &lt;contentInstance> which will be introduced in clause 6.2.6.


#### 6.2.5.1 API-CONT-CRE

|<br /><br />API Id |API/CONT/CRE/001<br />API/CONT/CRE/001_RCN0<br />API/CONT/CRE/001_RCN1<br />API/CONT/CRE/001_RCN2<br />API/CONT/CRE/001_RCN3 |
|-|-|
|API Name |container CREATE with and without resultContent parameter |
|Target Resource |&lt;AE> resource as a parent resource of the requested &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;container> CREATE request attached with resultContent under the &lt;AE> resource located in the &lt;CSEBase>. The hosting CSE will create the &lt;container> resource under the &lt;AE>, and send back a response according to the configured resultContent. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />No RCN or RCN=1 |<br />    API/CONT/CRE/001<br />   API/CONT/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=3<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "rn": "cont_temp"<br />    }<br />}<br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:265 <br />Content-Location:/mnID/cnt20180406T0857121405855183193600_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br />{<br />    "m2m:cnt": {<br />        "cbs": 0,<br />        "cni": 0,<br />        "ct": "20180406T085712",<br />        "et": "99991231T235959",<br />        "lt": "20180406T085712",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 10000,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T0857121405855183193600_cse01",<br />        "rn": "cont_temp",<br />        "st": 0,<br />        "ty": 3<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=0 |<br />    API/CONT/CRE/001_RCN/0<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=3<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "rn": "cont_temp"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:0 <br />Content-Location:/ mnID/cnt20180406T0922111405855351047681_cse01<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /> |
|<br /><br /><br />Example with <br />RCN=2 |<br />    API/CONT/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=3<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "rn": "cont_temp"<br />    }<br />}<br /><br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:50 <br />Content-Location:/mnID/cnt20180406T0924461405855854609922_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001 <br /><br />{<br />    "m2m:uri": "mn-name/ae_sensor/cont_temp"<br />}<br /> |
|<br /><br /><br />Example with <br />RCN=3 |<br />API/CONT/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=3<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "rn": "cont_temp"<br />    }<br />}<br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:322 <br />Content-Location:/mnID/cnt20180406T0927581405855602828800_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:cnt": {<br />            "cbs": 0,<br />            "cni": 0,<br />            "ct": "20180406T092758",<br />            "et": "99991231T235959",<br />            "lt": "20180406T092758",<br />            "mbs": 60000000,<br />            "mia": 1600,<br />            "mni": 10000,<br />            "pi": "CAE0120180406T0846311405855351047680_cse01",<br />            "ri": "cnt20180406T0927581405855602828800_cse01",<br />            "rn": "cont_temp",<br />            "st": 0,<br />            "ty": 3<br />        },<br />        "uri": "mn-name/ae_sensor/cont_temp"<br />    }<br />}<br /> |




#### 6.2.5.2 API-CONT-RET

|<br /><br />API Id |API/CONT/RET/001<br />API/CONT/RET/001_RCN1<br />API/CONT/RET/001_RCN4 |
|-|-|
|API Name |container RETRIEVE with or without resultContent parameter set |
|Target Resource |Requested &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;container> RETRIEVE request attached with resultContent to the &lt;container> resource located in the &lt;CSEBase>. The hosting CSE will send back a response according to the configured resultContent.  |
|<br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br /><br /><br /><br />Example with <br />No RCN or RCN=1 |<br />API/CONT/RET/001<br />API/CONT/RET/001_RCN/1<br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:265 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br /><br />{<br />    "m2m:cnt": {<br />        "cbs": 0,<br />        "cni": 0,<br />        "ct": "20180406T092758",<br />        "et": "99991231T235959",<br />        "lt": "20180406T092758",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 10000,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T0927581405855602828800_cse01",<br />        "rn": "cont_temp",<br />        "st": 0,<br />        "ty": 3<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with<br />RCN=4<br /><br /> |<br />API/CONT/RET/001_RCN4<br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp?rcn=4 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE3878123815422295646<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />// Container &lt;cont_temp> has 2 child &lt;contentInstance> resources<br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:1347<br />Content-Type:application/json<br />X-M2M-Origin:/mnID<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br /><br />{<br />    "m2m:cnt": {<br />        "cbs": 6,<br />        "cni": 2,<br />        "ct": "20180406T092758",<br />        "et": "99991231T235959",<br />        "lt": "20180406T094838",<br />        "m2m:cin": [<br />            {<br />                "con": "27",<br />                "cs": 3,<br />                "ct": "20180406T094838",<br />                "et": "99991231T235959",<br />                "lt": "20180406T094838",<br />                "pi": "cnt20180406T0927581405855602828800_cse01",<br />                "ri": "cin20180406T0948381405855183193602_cse01",<br />                "rn": "cin20180406T0948381405855183193601_cse01",<br />                "st": 2,<br />                "ty": 4<br />            },<br />            {<br />                "con": "28",<br />                "cs": 3,<br />                "ct": "20180406T094719",<br />                "et": "99991231T235959",<br />                "lt": "20180406T094719",<br />                "pi": "cnt20180406T0927581405855602828800_cse01",<br />                "ri": "cin20180406T0947191405855686755841_cse01",<br />                "rn": "cin20180406T0947191405855686755840_cse01",<br />                "st": 1,<br />                "ty": 4<br />            }<br />        ],<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 10000,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T0927581405855602828800_cse01",<br />        "rn": "cont_temp",<br />        "st": 2,<br />        "ty": 3<br />    }<br />}<br /> |




#### 6.2.5.3 API-CONT-UPD

|<br />API Id |API/CONT/UPD/001<br />API/CONT/UPD/001_RCN0<br />API/CONT/UPD/001_RCN1 |
|-|-|
|API Name |container UPDATE with or without resultContent set |
|Target Resource |Requested &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;container> UPDATE request to the target &lt;container> resource located under the CSE, and the hosting CSE will respond with only the response status code to indicate the UPDATE operation status. |
|<br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />RCN=0<br /><br /><br /> |<br />API/CONT/UPD/001_RCN0<br /><br />HTTP Request:<br />PUT /mn-name/ae_sensor/cont_temp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "mni": 400,<br />        "lbl": ["indoor_temperature"]<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234 <br />X-M2M-RVI: 2a<br />X-M2M-RSC:2004<br /><br /> |
|<br /><br /><br />Example with <br />No RCN or RCN=1<br /><br /><br /> |<br />API/CONT/UPD/001<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_sensor/cont_temp HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Accept: application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "mni": 300,<br />        "lbl": ["indoor_temp"]<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:285 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2004<br /><br />{<br />    "m2m:cnt": {<br />        "cbs": 0,<br />        "cni": 0,<br />        "ct": "20180406T125807",<br />        "et": "99991231T235959",<br />        "lbl": [<br />            "indoor_temp"<br />        ],<br />        "lt": "20180406T130109",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 300,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T1258071405855183193603_cse01",<br />        "rn": "cont_temp",<br />        "st": 1,<br />        "ty": 3<br />    }<br />}<br /> |




#### 6.2.5.4 API-CONT-DEL

|<br />API Id |API/CONT/DEL/001<br />API/CONT/DEL/001_RCN0 |
|-|-|
|API Name |container DELETE with no resultContent (or resultContent set to 0) |
|Target Resource |Requested &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;container> DELETE request to a target &lt;container> resource located under the CSE, and the hosting CSE will respond with only response status code to indicate the DELETE operation status. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />RCN=0<br /><br /><br /> |<br />API/CONT/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /> |
|<br /><br /><br />Example with <br />No RCN or RCN=1<br /><br /><br /> |<br />API/CONT/DEL/001<br />API/CONT/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-Origin:/mnID<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br />{<br />    "m2m:cnt": {<br />        "cbs": 0,<br />        "cni": 0,<br />        "ct": "20180406T125807",<br />        "et": "99991231T235959",<br />        "lbl": [<br />            "indoor_temp"<br />        ],<br />        "lt": "20180406T130330",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 400,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T1258071405855183193603_cse01",<br />        "rn": "cont_temp",<br />        "st": 2,<br />        "ty": 3<br />    }<br />}<br /> |




### 6.2.6 Resource Type contentInstance

#### 6.2.6.0 Introduction
The &lt;contentInstance> resource represents a data instance stored in the &lt;container> resource. Taking a temperature sensor device as an example, the temperature sensor is designed to collect temperature data of environment and in this case, the real temperature data is modelled as a &lt;contentInstance> resource. In details, we assume both the temperature sensor is registered with &lt;AE> resource and a &lt;container> resource is created under the &lt;AE> to store temperature instances, under this consumption, whenever the temperature data is uploaded into a central server, the temperature data has to be denoted as a value of content attribute of &lt;contentInstance> resource.

The &lt;contentInstance> resource cannot be modified once created, and is able to be deleted explicitly by an AE or may be deleted by the platform based on specific policies. If the platform has policies to manage the &lt;contentInstance> resource, these policies are represented by attributes axByteSize, maxNrOfInstances and/or maxInstanceAge attributes in their parent &lt;container> resource.

The &lt;contentInstance> resource inheritances the same access control policies of its parent &lt;container> resource, and does not have its own accessControlPolicyIDs attribute. 


#### 6.2.6.1 API-CI-CRE

|<br /><br />API Id |API/CI/CRE/001<br />API/CI/CRE/001_RCN0<br />API/CI/CRE/001_RCN1<br />API/CI/CRE/001_RCN2<br />API/CI/CRE/001_RCN3 |
|-|-|
|API Name |contentInstance CREATE with or without resultContent parameter |
|Target Resource |The &lt;container> resource as a parent resource of being created &lt;contentInstance> resource |
|<br /><br /><br />Description |The interface is used to send a &lt;contentInstance> CREATE request to the target &lt;container> resource located under the CSE, and the hosting CSE will create a new &lt;contentInstance> under the requested &lt;container>, and send back a response containing only the response status code to indicate the CREATE operation status. |
|<br /><br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />rcn=0 |<br />API/CI/CRE/001_RCN/0    <br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=4<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:0 <br />Content-Location:/mnID/cin20180406T1358251405855267120642_cse01<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /> |
|<br /><br /><br />Example with <br />No RCN<br />or RCN=1 |<br />API/CI/CRE/001<br />API/CI/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=4<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:258 <br />Content-Location:/mnID/cin20180406T1355091405855351047683_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T135509",<br />        "et": "99991231T235959",<br />        "lt": "20180406T135509",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1355091405855351047683_cse01",<br />        "rn": "cin20180406T1355091405855351047682_cse01",<br />        "st": 1,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br />Example with <br />RCN=2 |<br />API/CI/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=4<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:91 <br />Content-Location:/mnID/cin20180406T1400131405855099266562_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:uri": "mn-name/ae_sensor/cont_temp/cin20180406T1400131405855099266561_cse01"<br />}<br /> |
|<br /><br /><br />Example with <br />RCN=3 |<br />API/CI/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />Content-Type: application/json;ty=4<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:356 <br />Content-Location:/mnID/cin20180406T1402131405855770682883_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:cin": {<br />            "con": "20",<br />            "cs": 2,<br />            "ct": "20180406T140213",<br />            "et": "99991231T235959",<br />            "lt": "20180406T140213",<br />            "pi": "cnt20180406T1353041405855518901760_cse01",<br />            "ri": "cin20180406T1402131405855770682883_cse01",<br />            "rn": "cin20180406T1402131405855770682882_cse01",<br />            "st": 4,<br />            "ty": 4<br />        },<br />        "uri": "mn-name/ae_sensor/cont_temp/cin20180406T1402131405855770682882_cse01"<br />    }<br />}<br /> |




#### 6.2.6.2 API-CI-RET

|<br />API Id |API/CI/RET/001_LA<br />API/CI/RET/001_OL<br />API/CI/RET/001_CI |
|-|-|
|API Name |Latest, Oldest or specific contentInstance RETRIEVE |
|Target Resource |&lt;latest>, &lt;oldest> virtual  resources or individual &lt;contentInstance> resource of the requested &lt;container> resource |
|Description |The interface is used to send a &lt;contentInstance> RETRIEVE request to the CSE, and the hosting CSE will send back a response containing the result. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />latest |<br />API/CI/RET/001_LA <br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp/la HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:258 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T140213",<br />        "et": "99991231T235959",<br />        "lt": "20180406T140213",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1402131405855770682883_cse01",<br />        "rn": "cin20180406T1402131405855770682882_cse01",<br />        "st": 4,<br />        "ty": 4<br />    }<br />} |
|<br /><br /><br />Example with <br />oldest |<br />      API/CI/RET/001_OL<br />   <br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp/ol HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:258 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T135509",<br />        "et": "99991231T235959",<br />        "lt": "20180406T135509",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1355091405855351047683_cse01",<br />        "rn": "cin20180406T1355091405855351047682_cse01",<br />        "st": 1,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br />Example with <br />CI name |<br />API/CI/RET/001_CI<br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp/cin20180406T1400131405855099266561_cse01 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:258 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T140013",<br />        "et": "99991231T235959",<br />        "lt": "20180406T140013",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1400131405855099266562_cse01",<br />        "rn": "cin20180406T1400131405855099266561_cse01",<br />        "st": 3,<br />        "ty": 4<br />    }<br />}<br /> |




#### 6.2.6.3 API-CI-DEL

|<br /><br /><br /><br /><br />API Id |API/CI/DEL/001_LA<br />API/CI/DEL/001_LA_RCN0<br /><br />API/CI/DEL/001_OL<br />API/CI/DEL/001_OL_RCN0<br /><br />API/CI/DEL/001_CI<br />API/CI/DEL/001_CI_RCN0 |
|-|-|
|API Name |Latest, Oldest or specific contentInstance DELETE |
|Target Resource |&lt;latest>, &lt;oldest> virtual  resources or individual &lt;contentInstance> resource of the requested &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;container> DELETE request to the CSE, and the hosting CSE will delete the &lt;contentInstance>, and send back a response containing the response status code to indicate the status of the DELETE operation. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />latest<br /><br />(No RCN or RCN=1) |<br />API/CI/DEL/001_LA<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/la HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:258 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T140213",<br />        "et": "99991231T235959",<br />        "lt": "20180406T140213",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1402131405855770682883_cse01",<br />        "rn": "cin20180406T1402131405855770682882_cse01",<br />        "st": 4,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br />Example with <br />latest and RCN=0 |<br />API/CI/DEL/001_LA_RCN0<br /> <br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/la?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /> |
|<br /><br /><br />Example with <br />oldest<br /><br />(No RCN or RCN=1) |<br />API/CI/DEL/001_OL<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/ol HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:258 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T135509",<br />        "et": "99991231T235959",<br />        "lt": "20180406T135509",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1355091405855351047683_cse01",<br />        "rn": "cin20180406T1355091405855351047682_cse01",<br />        "st": 1,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br />Example with <br />oldest and RCN=0 |<br />API/CI/DEL/001_OL_RCN0<br /> <br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/ol?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /><br /> |
|<br /><br /><br />Example with <br />CI name<br /><br />(No RCN or RCN=1) |<br />API/CI/DEL/001_CI<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/cin20180406T1400131405855099266561_cse01 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-Origin:/mnID<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T143434",<br />        "et": "99991231T235959",<br />        "lt": "20180406T143434",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1434341405855518901762_cse01",<br />        "rn": "cin20180406T1434341405855518901761_cse01",<br />        "st": 9,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br />Example with <br />CI name and RCN=0 |<br />API/CI/DEL/001_CI_RCN0    <br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/cin20180406T1400131405855099266561_cse01?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T0846311405855351047680_cse01<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /> |




### 6.2.7 Resource Type semanticDescriptor

#### 6.2.7.0 Introduction
The &lt;semanticDescriptor> resource is used to store a semantic description pertaining to a resource and potentially sub-resources. Such a description may be provided according to ontologies. The semantic information is used by the semantic functionalities of the oneM2M system and is also available to applications or CSEs. 


#### 6.2.7.1 API-SMD-CRE

|<br /><br />API Id |API/SMD/CRE/001<br />API/SMD/CRE/001_RCN0<br />API/SMD/CRE/001_RCN1<br />API/SMD/CRE/001_RCN3 |
|-|-|
|API Name |semanticDescriptor CREATE with or without resultContent parameter |
|Target Resource |The &lt;container> resource as a parent resource of being created &lt;semanticDescriptor> resource |
|<br /><br />Description |The interface is used to send a &lt;semanticDescriptor> CREATE request to the target &lt;container> resource located under the CSE, and the hosting CSE will create a new &lt;semanticDescriptor> under the requested &lt;container>, and send back a response according to the configured resultContent. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br />HTTP Header Information<br /> | |
|RDF content |The RDF content will be encode Base64 in the HTTP payload<br /><br />&lt;?xml version="1.0"?><br />&lt;rdf:RDF xmlns="http://www.onem2m.org/ontology/houses_temperature_example#"<br />     xml:base="http://www.onem2m.org/ontology/houses_temperature_example"<br />     xmlns:temperature_example="http://www.onem2m.org/ontology/temperature_example#"<br />     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"<br />     xmlns:owl="http://www.w3.org/2002/07/owl#"<br />     xmlns:xml="http://www.w3.org/XML/1998/namespace"<br />     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"<br />     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"><br /><br />    &lt;owl:NamedIndividual rdf:about="http://www.onem2m.org/ontology/houses_temperature_example#House1"><br />        &lt;rdf:type rdf:resource="http://www.onem2m.org/ontology/temperature_example#House"/><br />        &lt;temperature_example:hasIndoorTemperature rdf:resource="http://www.onem2m.org/ontology/houses_temperature_example#IndoorTempProperty1"/><br />    &lt;/owl:NamedIndividual><br /><br />    &lt;owl:NamedIndividual   rdf:about="http://www.onem2m.org/ontology/houses_temperature_example#IndoorTempProperty1"><br />        &lt;rdf:type rdf:resource="http://www.onem2m.org/ontology/temperature_example#TemperatureProperty"/><br />        &lt;temperature_example:hasDatatype>xsd:int&lt;/temperature_example:hasDatatype><br />        &lt;temperature_example:hasUnit>Fahrenheit&lt;/temperature_example:hasUnit><br />        &lt;temperature_example:valueIsStoredIn>http://mnprovider.com:9011/mn-name/ae_sensor/cont_temp/la&lt;/temperature_example:valueIsStoredIn><br />    &lt;/owl:NamedIndividual><br />&lt;/rdf:RDF> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/SMD/CRE/001_RCN0<br />    <br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />Content-Type: application/json;ty=24<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:smd" : {<br />        "dcrp"	: "application/rdf+xml:1",<br />        "rn"	: "semantic_describer",<br />        "dsr": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlMSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlIi8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0luZG9vclRlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBlcmF0dXJlUHJvcGVydHkiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+eHNkOmludDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNEYXRhdHlwZT4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzVW5pdD5GYWhyZW5oZWl0PC90ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOnZhbHVlSXNTdG9yZWRJbj5odHRwOi8vbW5wcm92aWRlci5jb206OTAxMS9tbi1uYW1lL2FlX3NlbnNvci9jb250X3RlbXAvbGE8L3RlbXBlcmF0dXJlX2V4YW1wbGU6dmFsdWVJc1N0b3JlZEluPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCjwvcmRmOlJERj4="<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:0 <br />Content-Location:/mnID/CAE0120180404T0830181405122857960960_cse01<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /> |
|Example with no RCN or<br />RCN=1 <br /> |<br />API/SMD/CRE/001<br />API/SMD/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />Content-Type: application/json;ty=24<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:smd" : {<br />        "dcrp"	: "application/rdf+xml:1",<br />        "rn"	: "semantic_describer",<br />        "dsr": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlMSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlIi8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0luZG9vclRlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBlcmF0dXJlUHJvcGVydHkiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+eHNkOmludDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNEYXRhdHlwZT4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzVW5pdD5GYWhyZW5oZWl0PC90ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOnZhbHVlSXNTdG9yZWRJbj5odHRwOi8vbW5wcm92aWRlci5jb206OTAxMS9tbi1uYW1lL2FlX3NlbnNvci9jb250X3RlbXAvbGE8L3RlbXBlcmF0dXJlX2V4YW1wbGU6dmFsdWVJc1N0b3JlZEluPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCjwvcmRmOlJERj4="<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:3480 <br />Content-Location:/mnID/smd20180413T1256011400030218380800_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:smd": {<br />        "ct": "20180413T125601",<br />        "dcrp": "application/rdf+xml:1",<br />        "dsp": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo3NTc5L3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFNlbnNvcjEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVNlbnNvciIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNUZW1wZXJhdHVyZU1lYXN1cmluZ0Z1bmN0aW9uIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBGdW5jdGlvbjEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQoNCiAgICA8b3dsOk5hbWVkSW5kaXZpZHVhbCByZGY6YWJvdXQ9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wRnVuY3Rpb24xIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjVGVtcGVyYXR1cmVNZWFzdXJpbmdGdW5jdGlvbiIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTptZWFzdXJlc1RlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+ICAgDQo8L3JkZjpSREY+DQo=",<br />        "et": "99991231T235959",<br />        "lt": "20180413T125601",<br />        "or": "http://www.onem2m.org/ontology/temperature_example",<br />        "pi": "cnt20180413T0847561400030050526720_cse01",<br />        "ri": "smd20180413T1256011400030218380800_cse01",<br />        "rn": "semantic_describer",<br />        "ty": 24<br />    }<br />}<br /> |
|Example with RCN=3 <br /> |<br />API/SMD/CRE/001<br />API/SMD/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/cont_temp?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />Content-Type: application/json;ty=24<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:smd" : {<br />        "dcrp"	: "application/rdf+xml:1",<br />        "rn"	: "semantic_describer",<br />        "dsr": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlMSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI0hvdXNlIi8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0luZG9vclRlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSI+DQogICAgICAgIDxyZGY6dHlwZSByZGY6cmVzb3VyY2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS90ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBlcmF0dXJlUHJvcGVydHkiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+eHNkOmludDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNEYXRhdHlwZT4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzVW5pdD5GYWhyZW5oZWl0PC90ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOnZhbHVlSXNTdG9yZWRJbj5odHRwOi8vbW5wcm92aWRlci5jb206OTAxMS9tbi1uYW1lL2FlX3NlbnNvci9jb250X3RlbXAvbGE8L3RlbXBlcmF0dXJlX2V4YW1wbGU6dmFsdWVJc1N0b3JlZEluPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCjwvcmRmOlJERj4="<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Length:3480 <br />Content-Location:/mnID/smd20180413T1256011400030218380800_cse01<br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2001<br /><br />{<br />    "m2m:rce": {<br />		"m2m:smd": {<br />			"ct": "20180413T125601",<br />			"dcrp": "application/rdf+xml:1",<br />			"dsp": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo3NTc5L3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFNlbnNvcjEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVNlbnNvciIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNUZW1wZXJhdHVyZU1lYXN1cmluZ0Z1bmN0aW9uIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBGdW5jdGlvbjEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQoNCiAgICA8b3dsOk5hbWVkSW5kaXZpZHVhbCByZGY6YWJvdXQ9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wRnVuY3Rpb24xIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjVGVtcGVyYXR1cmVNZWFzdXJpbmdGdW5jdGlvbiIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTptZWFzdXJlc1RlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+ICAgDQo8L3JkZjpSREY+DQo=",<br />			"et": "99991231T235959",<br />			"lt": "20180413T125601",<br />			"or": "http://www.onem2m.org/ontology/temperature_example",<br />			"pi": "cnt20180413T0847561400030050526720_cse01",<br />			"ri": "smd20180413T1256011400030218380800_cse01",<br />			"rn": "semantic_describer",<br />			"ty": 24<br />		},<br />		"uri": "mn-name/ae_sensor/cont_temp/semantic_describer"<br />	}<br />}<br /> |




#### 6.2.7.2 API-SMD-RET

|API Id |API/SMD/RET/001_RCN1 |
|-|-|
|API Name |SemanticDescriptor RETRIEVE with or without resultContent parameter |
|Target Resource |Requested &lt;semanticDescriptor> resource |
|<br /><br />Description |The interface is used to send a &lt;semanticDescriptor> RETRIEVE request attached with resultContent to the &lt;container> resource located in the &lt;CSEBase>. The hosting CSE will send back a response according to the configured resultContent.  |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />RCN=1<br />or No RCN |<br />API/SMD/RET/001<br />API/SMD/RET/001_RCN1   <br />   <br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/cont_temp/semantic_describer HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0838301405122186544640_cse01<br />Accept: application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:3374 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2000<br /><br />{<br />    "m2m:smd": {<br />        "ct": "20180413T125601",<br />        "dcrp": "application/rdf+xml:1",<br />        "dsp": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo3NTc5L3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFNlbnNvcjEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVNlbnNvciIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNUZW1wZXJhdHVyZU1lYXN1cmluZ0Z1bmN0aW9uIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI1RlbXBGdW5jdGlvbjEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+DQoNCiAgICA8b3dsOk5hbWVkSW5kaXZpZHVhbCByZGY6YWJvdXQ9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wRnVuY3Rpb24xIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjVGVtcGVyYXR1cmVNZWFzdXJpbmdGdW5jdGlvbiIvPg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTptZWFzdXJlc1RlbXBlcmF0dXJlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiLz4NCiAgICA8L293bDpOYW1lZEluZGl2aWR1YWw+ICAgDQo8L3JkZjpSREY+DQo=",<br />        "et": "99991231T235959",<br />        "lt": "20180413T125601",<br />        "or": "http://www.onem2m.org/ontology/temperature_example",<br />        "pi": "cnt20180413T0847561400030050526720_cse01",<br />        "ri": "smd20180413T1256011400030218380800_cse01",<br />        "rn": "semantic_describer",<br />        "ty": 24<br />    }<br />}<br /> |




#### 6.2.7.3 API-SMD-UPD

|<br /><br />API Id |API/SMD/UPD/001<br />API/SMD/UPD/001_RCN0<br />API/SMD/UPD/001_RCN1 |
|-|-|
|API Name |semanticDescriptor UPDATE with or without resultContent set  |
|Target Resource |The &lt; semanticDescriptor > resource located under &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;semanticDescriptor> UPDATE request to the target &lt;container> resource located under the CSE, and the hosting CSE will create a new &lt;semanticDescriptor> under the requested &lt;container>, and send back a response according to the configured resultContent. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />RCN=0<br /><br /><br /> |<br />     API/AE/UPD/001_RCN0<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_sensor/cont_temp/semantic_describer?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:smd" : {<br /><br />        "dsp":<br />" PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo4MjgyL3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KPC9yZGY6UkRGPg==",<br /><br /> "or": "http://www.onem2m.org/ontology/temperature_example2",<br />    <br />}<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2004<br /> |
|<br /><br /><br />Example with <br />RCN=1<br />or No RCN<br /><br /><br /> |<br />    API/AE/UPD/001<br />    API/AE/UPD/001_RCN1<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_sensor/cont_temp/semantic_describer HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:smd" : {<br /><br />        "dsp":<br />" PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo4MjgyL3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KPC9yZGY6UkRGPg==",<br /><br /> "or": "http://www.onem2m.org/ontology/temperature_example2",<br />    <br />}<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:2405 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2004<br /><br />{<br />    "m2m:smd": {<br />        "ct": "20180413T125601",<br />        "dcrp": "application/rdf+xml:1",<br />        "dsp": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo4MjgyL3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KPC9yZGY6UkRGPg==",<br />        "et": "99991231T235959",<br />        "lt": "20180413T150302",<br />        "or": "http://www.onem2m.org/ontology/temperature_example2",<br />        "pi": "cnt20180413T0847561400030050526720_cse01",<br />        "ri": "smd20180413T1256011400030218380800_cse01",<br />        "rn": "semantic_describer",<br />        "ty": 24<br />    }<br />}<br /> |




#### 6.2.7.4 API-SMD-DEL

|<br />API Id |API/SMD/DEL/001<br />API/SMD/DEL/001_RCN0<br />API/SMD/DEL/001_RCN1 |
|-|-|
|API Name |SMD DELETE  |
|Target Resource |The &lt;semanticDescriptor> resource located under the &lt;container> resource |
|<br /><br />Description |The interface is used to send a &lt;semanticDescriptor> DELETE request to the hosting CSE, and the hosting CSE will delete the &lt;semanticDescriptor> and send back a response containing a response status code indicating the DELETE request status. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /> | |
|<br /><br /><br />Example with <br />RCN=0<br /> |<br />API/AE/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/semantic_describer?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:0 <br />X-M2M-RI:1234<br />X-M2M-RSC:2002<br /> |
|<br /><br /><br />Example with <br />RCN=1 or<br />no RCN<br /> |<br />API/SMD/DEL/001<br />API/SMD/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/cont_temp/semantic_describer HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830181405122857960960_cse01<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Length:2299 <br />Content-Type:application/json<br />X-M2M-RI:1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC:2002<br /><br />{<br />    "m2m:smd": {<br />        "ct": "20180413T125601",<br />        "dcrp": "application/rdf+xml:1",<br />        "dsp": "PD94bWwgdmVyc2lvbj0iMS4wIj8+DQo8cmRmOlJERiB4bWxucz0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlIyINCiAgICAgeG1sOmJhc2U9Imh0dHA6Ly93d3cub25lbTJtLm9yZy9vbnRvbG9neS9ob3VzZXNfdGVtcGVyYXR1cmVfZXhhbXBsZSINCiAgICAgeG1sbnM6dGVtcGVyYXR1cmVfZXhhbXBsZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjIg0KICAgICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiDQogICAgIHhtbG5zOm93bD0iaHR0cDovL3d3dy53My5vcmcvMjAwMi8wNy9vd2wjIg0KICAgICB4bWxuczp4bWw9Imh0dHA6Ly93d3cudzMub3JnL1hNTC8xOTk4L25hbWVzcGFjZSINCiAgICAgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSMiDQogICAgIHhtbG5zOnJkZnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDEvcmRmLXNjaGVtYSMiPg0KDQogICAgPG93bDpOYW1lZEluZGl2aWR1YWwgcmRmOmFib3V0PSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UxIj4NCiAgICAgICAgPHJkZjp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L3RlbXBlcmF0dXJlX2V4YW1wbGUjSG91c2UiLz4NCiAgICAgICAgPHRlbXBlcmF0dXJlX2V4YW1wbGU6aGFzSW5kb29yVGVtcGVyYXR1cmUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvaG91c2VzX3RlbXBlcmF0dXJlX2V4YW1wbGUjSW5kb29yVGVtcFByb3BlcnR5MSIvPg0KICAgIDwvb3dsOk5hbWVkSW5kaXZpZHVhbD4NCg0KICAgIDxvd2w6TmFtZWRJbmRpdmlkdWFsIHJkZjphYm91dD0iaHR0cDovL3d3dy5vbmVtMm0ub3JnL29udG9sb2d5L2hvdXNlc190ZW1wZXJhdHVyZV9leGFtcGxlI0luZG9vclRlbXBQcm9wZXJ0eTEiPg0KICAgICAgICA8cmRmOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vd3d3Lm9uZW0ybS5vcmcvb250b2xvZ3kvdGVtcGVyYXR1cmVfZXhhbXBsZSNUZW1wZXJhdHVyZVByb3BlcnR5Ii8+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc0RhdGF0eXBlPnhzZDppbnQ8L3RlbXBlcmF0dXJlX2V4YW1wbGU6aGFzRGF0YXR5cGU+DQogICAgICAgIDx0ZW1wZXJhdHVyZV9leGFtcGxlOmhhc1VuaXQ+RmFocmVuaGVpdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTpoYXNVbml0Pg0KICAgICAgICA8dGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+aHR0cDovL2luLnByb3ZpZGVyLmNvbTo4MjgyL3NlcnZlci90ZW1wc2Vuc29yYWUxL3RlbXBlcmF0dXJlL2xhdGVzdDwvdGVtcGVyYXR1cmVfZXhhbXBsZTp2YWx1ZUlzU3RvcmVkSW4+DQogICAgPC9vd2w6TmFtZWRJbmRpdmlkdWFsPg0KPC9yZGY6UkRGPg==",<br />        "et": "99991231T235959",<br />        "lt": "20180413T151556",<br />        "or": "http://www.onem2m.org/ontology/temperature_example2",<br />        "pi": "cnt20180413T0847561400030050526720_cse01",<br />        "ri": "smd20180413T1256011400030218380800_cse01",<br />        "rn": "semantic_describer",<br />        "ty": 24<br />    }<br />}<br /> |


### 6.2.8 Resource discovery

#### 6.2.8.0 Introduction
The discovery is one of the common service functions which searches information about application and services. An originator can receive the matching information according to the filter criteria, by sending the discovery request. The format of a query string has both target resource address and filter criteria information; e.g. /mn-name?fu=2&ty=2.

The filterUsage can be set to retrieve any preferred format of the discovery response. The filterUsage value is specified in table 6.2.8.0-1. When filterUsage sets to 1, the response of the discovery is represented with a format of the URI list and all URIs of discovered resources is listed in the response. And when filterUsage sets to 2, the response contains attributes of the resources that matched with presented filter criteria conditions. 


**Table 6.2.8.0-1: Interpretation of filterUsage**

|Interpretation |Value |Note |
|-|-|-|
|Discovery Criteria |1 | |
|Conditional Retrieval |2 |Default  |



Filter criteria are set to search the resources with specific conditions. For example, AE resources can be found by setting the resourceType to 2. Some Filter criteria conditions are listed in table 6.2.8.0-2, which is extracted from the table 8.1.2-2 of oneM2M TS-0001 <a href="#_ref_i.2">[i.2]</a>.  


**Table 6.2.8.0-2: Filter criteria conditions**

|Condition tag |Short Name |Multiplicity |Description |
|-|-|-|-|
|Matching Conditions |Matching Conditions |Matching Conditions |Matching Conditions |
|createdBefore |crb |0..1 |The creationTime attribute of the matched resource is chronologically before the specified value. |
|createdAfter |cra |0..1 |The creationTime attribute of the matched resource is chronologically after the specified value. |
|modifiedSince |ms |0..1 |The lastModifiedTime attribute of the matched resource is chronologically after the specified value. |
|unmodifiedSince |us |0..1 |The lastModifiedTime attribute of the matched resource is chronologically before the specified value. |
|stateTagSmaller |sts |0..1 |The stateTag attribute of the matched resource is smaller than the specified value. |
|stateTagBigger |stb |0..1 |The stateTag attribute of the matched resource is bigger than the specified value. |
|expireBefore |exb |0..1 |The expirationTime attribute of the matched resource is chronologically before the specified value. |
|expireAfter |exa |0..1 |The expirationTime attribute of the matched resource is chronologically after the specified value. |
|labels |lbl |0..1 |The labels attribute of the matched resource matches the specified value. |
|resourceType |ty |0..n |The resourceType attribute of the matched resource is the same as the specified value. It also allows differentiating between normal and announced resources. |
|sizeAbove |sza |0..1 |The contentSize attribute of the &lt;contentInstance> matched resource is equal to or greater than the specified value. |
|sizeBelow |szb |0..1 |The contentSize attribute of the &lt;contentInstance> matched resource is smaller than the specified value. |
|Filter Handling Conditions |Filter Handling Conditions |Filter Handling Conditions |Filter Handling Conditions |
|limit |lim |0..1 |The maximum number of resources to be included in the filtering result. This may be modified by the Hosting CSE. When it is modified, then the new value shall be smaller than the suggested value by the Originator. |
|level |lvl |0..1 |The maximum level of resource tree that the Hosting CSE shall perform the operation starting from the target resource (i.e. To parameter). This shall only be applied for Retrieve operation. The level of the target resource itself is zero and the level of the direct children of the target is one. |



As an initial condition to use discovery function, CSEBase need to have resources. Table 6.2.8.0-3 has detailed information of resources which will be used in this clause.


**Table 6.2.8.0-3: Resource Specifications**

|Resource Name |Resource attributes in JSON format |
|-|-|
|CSEBase |{<br />    "m2m:cb": {<br />        "pi": null,<br />        "ty": 5,<br />        "ct": "20180302T070445",<br />        "ri": "CSE9486743758493047362",<br />        "rn": "mn-name",<br />        "lt": "20180302T070445",<br />        "lbl": [<br />            "mn-name"<br />        ],<br />        "cst": 1,<br />        "csi": "/mn-name",<br />        "srt": [<br />            1,<br />            2,<br />            3,<br />            4,<br />            5,<br />            9,<br />            10,<br />            13,<br />            14,<br />            16,<br />            17,<br />            23<br />        ],<br />        "poa": [<br />            "http://192.168.0.10:8282"<br />        ]<br />    }<br />} |
|ae_actuator |{<br />    "m2m:ae": {<br />        "pi": "mnID",<br />        "ty": 2,<br />        "ct": "20180404T083025",<br />        "ri": "CAE0120180404T0830251405122594272800_cse01",<br />        "rn": "ae_actuator",<br />        "lbl": [<br />            "actuator",<br />            "light"<br />        ],<br />        "lt": "20180406T083320",<br />        "et": "20221231T235959",<br />        "api": "A01.com.company.Light",<br />        "aei": "CAE0120180404T0830251405122594272800_cse01",<br />        "rr": false<br />    }<br />} |
|cnt_light1 |{<br />    "m2m:cnt": {<br />        "pi": "CAE0120180404T0830251405122594272800_cse01",<br />        "ty": 3,<br />        "ct": "20180406T085318",<br />        "ri": "cnt20180406T0853181405855183193600_cse01",<br />        "rn": "cont_light1",<br />        "lt": "20180406T085318",<br />        "et": "20201231T235959",<br />        "lbl": [<br />            "indoor_light"<br />            "actuator"<br />            "room1"<br />        ],<br />        "st": 5,<br />        "cr": "S20170717074825768bp2l",<br />        "mni": 10000,<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "cni": 5,<br />        "cbs": 10<br />    }<br />} |
|cnt_light2 |{<br />    "m2m:cnt": {<br />        "pi": "CAE0120180404T0830251405122594272800_cse01",<br />        "ty": 3,<br />        "ct": "20180405T085318",<br />        "ri": "cnt20180406T0853181405855183193600_cse01",<br />        "rn": "cont_light2",<br />        "lt": "20180406T085318",<br />        "et": "20201231T235959",<br />        "lbl": [<br />            "outdoor_light"<br />            "actuator"<br />        ],<br />        "st": 4,<br />        "cr": "S20170717074825768bp2l",<br />        "mni": 10000,<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "cni": 10,<br />        "cbs": 20<br />    }<br />} |
|ae_sensor |{<br />    "m2m:ae": {<br />        "pi": "mnID",<br />        "ty": 2,<br />        "ct": "20180404T083320",<br />        "ri": "CAE0120180404T0833201405122522252800_cse01",<br />        "rn": "ae_sensor",<br />        "lbl": [<br />            "sensor",<br />            "temperature"<br />        ],<br />        "lt": "20180404T083320",<br />        "et": "20221231T235959",<br />        "api": "A01.com.company.Temperature",<br />        "aei": "CAE0120180404T0833201405122522252800_cse01",<br />        "rr": false<br />    }<br />} |
|cnt_temp1 |{<br />    "m2m:cnt": {<br />        "pi": "CAE0120180404T0833201405122522252800_cse01",<br />        "ty": 3,<br />        "ct": "20180406T085712",<br />        "ri": "cnt20180406T0857121405855183193600_cse01",<br />        "rn": "cont_temp1",<br />        "lt": "20180406T085712",<br />        "et": "20201231T235959",<br />        "lbl": [<br />            "indoor_temperature"<br />            "sensor"<br />            "room2"<br />        ],<br />        "st": 8,<br />        "cr": "S20170717074825768bp2l",<br />        "mni": 10000,<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "cni": 10,<br />        "cbs": 20<br />    }<br />} |
|cnt_temp2 |{<br />    "m2m:cnt": {<br />        "pi": "CAE0120180404T0833201405122522252800_cse01",<br />        "ty": 3,<br />        "ct": "20180406T085820",<br />        "ri": "cnt20180406T0858201405855563993600_cse01",<br />        "rn": "cont_temp2",<br />        "lt": "20180406T085820",<br />        "et": "20211231T235959",<br />        "lbl": [<br />            "outdoor_temperature"<br />            "sensor"<br />        ],<br />        "st": 9,<br />        "cr": "S20170717074825768bp2l",<br />        "mni": 10000,<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "cni": 15,<br />        "cbs": 30<br />    }<br />} |




#### 6.2.8.1 API-DIS-TY

|<br />API Id |API/DIS_TY2<br />API/DIS_TY3 |
|-|-|
|API Name |Discovery with resourceType Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the specific resource type. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /> | |
|<br /><br /><br />Example with <br />ty=2 |<br />API/DIS_TY2<br /><br />HTTP Request:<br /><br />GET /mn-name?fu=1&ty=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830251405122594272800_cse01<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_sensor"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />ty=3 |<br />API/DIS_TY3<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&ty=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180404T0830251405122594272800_cse01<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{ <br />    "m2m:uril": [<br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />    ]<br />}<br /> |




#### 6.2.8.2 API-DIS-LBL

|<br />API Id |API/DIS_LBL_ACTUATOR<br />API/DIS_LBL_SENSOR |
|-|-|
|API Name |Discovery with label Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the specific label value. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br />Example with <br />lbl=actuator |<br />API/DIS_LBL_ACTUATOR<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&lbl=actuator HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />lbl=sensor |<br />API/DIS_LBL_SENSOR<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&lbl=sensor HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_sensor",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |




#### 6.2.8.3 API-DIS-LVL

|<br />API Id |API/DIS_LVL1<br />API/DIS_LVL2 |
|-|-|
|API Name |Discovery with level Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the child level value. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />lvl=1 |<br />API/DIS_LVL1<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&lvl=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_sensor"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />lvl=2 |<br />API/DIS_LVL2<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&lvl=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |




#### 6.2.8.4 API-DIS-CRB, API-DIS-CRA

|<br />API Id |API/DIS_CRB<br />API/DIS_CRA |
|-|-|
|API Name |Discovery with createdBefore and createdAfter Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the period of created time. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />crb |<br />API/DIS_CRB<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&crb=20180405T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />cra |<br />API/DIS_CRA<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&cra=20180405T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |




#### 6.2.8.5 API-DIS-STB, API-DIS-STS

|<br />API Id |API/DIS_STB<br />API/DIS_STS |
|-|-|
|API Name |Discovery with stateTagBigger and stateTagSmaller Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the stateTag. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />stb |<br />API/DIS_STB<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&stb=6 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />sts |<br />API/DIS_STS<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&sts=6 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2"<br />}<br /> |




#### 6.2.8.6 API-DIS-SZB, API-DIS-SZA

|<br />API Id |API/DIS_SZB<br />API/DIS_SZA |
|-|-|
|API Name |Discovery with sizeBelow and sizeAbove Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the size of container. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br />Example with <br />szb |<br />API/DIS_SZB<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&szb=15 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator/cnt_light1"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />sza |<br />API/DIS_SZA<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&sza=15 HTTP/1.1<br />Accept: application/json<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |




#### 6.2.8.7 API-DIS-US, API-DIS-MS

|<br />API Id |API/DIS_US<br />API/DIS_MS |
|-|-|
|API Name |Discovery with unmodifiedSince and modifiedSince Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the time of modification. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />us |<br />API/DIS_US<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&us=20180405T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_sensor"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />ms |<br />API/DIS_MS    <br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&ms=20180405T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |




#### 6.2.8.8 API-DIS-EXB, API-DIS-EXA

|<br />API Id |API/DIS_EXB<br />API/DIS_EXA |
|-|-|
|API Name |Discovery with expiredBefore and expiredAfter Filter Criteria condition |
|Target Resource |CSEBase (can be any oneM2M resource primitives) |
|<br />Description |The interface is used to discovery resources that match with the period of expirationTime. If found, the Hosting CSE sends back a response with matched resources. |
|<br /><br /><br /><br />Resource Structure |<br /><br /><br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />exb |<br />API/DIS_EXB<br />    <br />HTTP Request:<br /><br />GET /mn-name?fu=1&exb=20211231T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator/cnt_light1",<br />        "/mn-name/ae_actuator/cnt_light2",<br />        "/mn-name/ae_sensor/cnt_temp1",<br />        "/mn-name/ae_sensor/cnt_temp2"<br />}<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />exa |<br />API/DIS_EXA<br />        <br />HTTP Request:<br /><br />GET /mn-name?fu=1&exa=20211231T235959 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:uril": <br />        "/mn-name/ae_actuator",<br />        "/mn-name/ae_sensor",<br />}<br /> |




### 6.2.9 Resource Type subscription

#### 6.2.9.0 Introduction
The &lt;subscription> resource contains subscription information for its subscribed-to resource. The &lt;subscription> resource created under the subscribed-to resource. Each &lt;subscription> may include notification policies that specify when, and how notification are sent. 


#### 6.2.9.1 API-SUB-CRE

|<br /><br />API Id |API/SUB/CRE/001<br />API/SUB/CRE/001_RCN0<br />API/SUB/CRE/001_RCN1<br />API/SUB/CRE/001_RCN2<br />API/SUB/CRE/001_RCN3 |
|-|-|
|API Name |&lt;subscription> resource CREATE |
|Target Resource |&lt;AE> resource of the requested &lt;subscription> resource |
|<br />Description |The interface is used to send a &lt;subscription> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;subscription> resource and sends back a response. |
|<br /><br />Resource Structure<br />before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/SUB/CRE/001_RCN0<br />    <br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_2">[2]</a><br />        },<br />  	  "nct": 2,<br />	  "nu": ["https://192.168.0.10:8282/notification/handler"],<br />	  "rn": "ae_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/SUB/CRE/001<br />API/SUB/CRE/001_RCN1<br />     <br />HTTP Request:<br /><br />POST /mn-name/ae_actuatorHTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_2">[2]</a><br />        },<br />  	  "nct": 2,<br />	  "nu": [<br />            https://192.168.0.10:8282/notification/handler<br />        ],<br />	  "rn": "ae_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:sub": {<br />        "rn": "ae_sub",<br />        "ty": 23,<br />        "ri": "SUB583675048372974938",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20180302T070445",<br />        "lt": "20180302T070445",<br />        "nu": [<br />            "https://192.168.0.10:8282/notification/handler"<br />        ],<br />        "cnm": 2, <br />        "mnm": 50,<br />        "enc": {<br />               "net": <a href="#_ref_2">[2]</a><br />        },<br />  	   "nct": 2<br />    }<br />} |
|<br /><br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/SUB/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_2">[2]</a><br />        },<br />  	  "nct": 2,<br />	  "nu": [<br />            https://192.168.0.10:8282/notification/handler<br />        ],<br />	  "rn": "ae_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/ae_actuator/ae_sub"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/SUB/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_2">[2]</a><br />        },<br />  	  "nct": 2,<br />	  "nu": [<br />            https://192.168.0.10:8282/notification/handler<br />        ],<br />	  "rn": "ae_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:sub": {<br />        "rn": "ae_sub",<br />        "ty": 23,<br />        "ri": "SUB583675048372974938",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20180302T070445",<br />        "lt": "20180302T070445",<br />        "nu": [<br />            "https://192.168.0.10:8282/notification/handler"<br />        ],<br />        "cnm": 2, <br />        "mnm": 50,<br />        "enc": {<br />               "net": <a href="#_ref_2">[2]</a><br />        },<br />  	   "nct": 2<br />    }<br />}<br /> |




#### 6.2.9.2 API-SUB-RET

|API Id |API/SUB/RET/001<br />API/SUB/RET/001_RCN1 |
|-|-|
|API Name |&lt;subscription> resource RETRIEVE with resultContent set to 1 |
|Target Resource |Requested &lt;subscription> resource |
|Description |The interface is used to send a &lt;subscription> RETRIEVE request attached with resultContent set to 1 to the &lt;subscription> resource hosting CSE and sends back a response. |
|<br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/SUB/RET/001<br /><br />HTTP Request:<br /><br />GET /mn-name/ae_actuator/ae_sub HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:sub": {<br />        "rn": "ae_sub",<br />        "ty": 23,<br />        "ri": "SUB583675048372974938",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20180302T070445",<br />        "lt": "20180302T070445",<br />        "nu": [<br />            "https://192.168.0.10:8282/notification/handler"<br />        ],<br />        "cnm": 2, <br />        "mnm": 50,<br />        "enc": {<br />               "net": <a href="#_ref_2">[2]</a><br />        },<br />  	   "nct": 2<br />    }<br />}<br /> |




#### 6.2.9.3 API-SUB-UPD

|<br />API Id |API/SUB/UPD/001<br />API/SUB/UPD/001_RCN0<br />API/SUB/UPD/001_RCN1 |
|-|-|
|API Name |&lt;subscription> resource UPDATE with resultContent parameter |
|Target Resource |Requested &lt;subscription> resource |
|<br />Description |The interface is used to send a &lt;subscription> UPDATE request attached with resultContent to the Registrar CSE, and the Registrar CSE updates a &lt;subscription> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/SUB/UPD/001_RCN0<br />    <br />HTTP Request:<br /><br />PUT /mn-name/ae_actuator/ae_sub?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "nct": 3<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/SUB/UPD/001<br />API/SUB/UPD/001_RCN1<br />       <br />HTTP Request:<br /><br />PUT /mn-name/ae_actuator/ae_sub HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "nct": 3<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:sub": {<br />        "rn": "ae_sub",<br />        "ty": 23,<br />        "ri": "SUB583675048372974938",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20180302T070445",<br />        "lt": "20180302T070445",<br />        "nu": [<br />            "https://192.168.0.10:8282/notification/handler"<br />        ],<br />        "cnm": 2, <br />        "mnm": 50,<br />        "enc": {<br />               "net": <a href="#_ref_2">[2]</a><br />        },<br />  	   "nct": 3<br />    }<br />}<br /> |




#### 6.2.9.4 API-SUB-DEL

|<br />API Id |API/SUB/DEL/001<br />API/SUB/DEL/001_RCN0<br />API/SUB/DEL/001_RCN1 |
|-|-|
|API Name |&lt;subscription> resource DELETE with resultContent parameter |
|Target Resource |Requested &lt;subscription> resource |
|<br />Description |The interface is used to send a &lt;subscription> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE deletes a &lt;subscription> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=0 |<br />    API/SUB/DEL/001<br />    API/SUB/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_actuator/ae_sub?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1 |<br />API/SUB/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_actuator/ae_sub?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/ae_sub<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:sub": {<br />        "rn": "ae_sub",<br />        "ty": 23,<br />        "ri": "SUB583675048372974938",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20180302T070445",<br />        "lt": "20180302T070445",<br />        "nu": [<br />              "https://192.168.0.10:8282/notification/handler"<br />        ],<br />        "cnm": 2, <br />        "mnm": 50,<br />        "enc": {<br />               "net": <a href="#_ref_2">[2]</a><br />        },<br />  	   "nct": 3<br />    }<br />}<br /> |




### 6.2.10 Resource Type group

#### 6.2.10.0 Introduction
The &lt;group> resource represents a group of resources of the same or mixed types. It basically designed to handle several of resources at the same time. When a request sent through the &lt;group> resource, it distributes the request to each member of the &lt;group> resources, which are indicated by the memberIDs attribute. 


#### 6.2.10.1 API-GRP-CRE

|<br /><br />API Id |API/GRP/CRE/001<br />API/GRP/CRE/001_RCN0<br />API/GRP/CRE/001_RCN1<br />API/GRP/CRE/001_RCN2<br />API/GRP/CRE/001_RCN3 |
|-|-|
|API Name |&lt;group> resource CREATE |
|Target Resource |&lt;AE> resource of the requested &lt;group> resource |
|<br />Description |The interface is used to send a &lt;group> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;group> resource and sends back a response. |
|<br /><br />Resource Structure<br />before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/GRP/CRE/001_RCN0<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=9<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:grp": {<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ],<br />  	  "mt": 3,<br />	  "mnm": 50,<br />	  "rn": "group_lamp"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/GRP/CRE/001<br />API/GRP/CRE/001_RCN1<br />   <br />HTTP Request:<br /><br />POST /mn-name/ae_actuator HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=9<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:grp": {<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ],<br />	  "mt": 3,<br />	  "mnm": 50,<br />	  "rn": "group_lamp"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:grp": {<br />        "rn": "group_lamp",<br />        "ty": 9,<br />        "ri": "GRP792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "mt": 3,<br />        "cnm": 2,<br />        "mnm": 50,<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ]<br />        "mtv": true,<br />        "csy": 1<br />    }<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/GRP/CRE/001_RCN2  <br /><br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=9<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:grp": {<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ],<br /> 	  "mt": 3,<br />	  "mnm": 50,<br />	  "rn": "group_lamp"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/ae_actuator/group_lamp"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/GRP/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_actuator?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=9<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:grp": {<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ],<br />	  "mt": 3,<br />	  "mnm": 50,<br />	  "rn": "group_lamp"<br />      }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:grp": {<br />            "rn": "group_lamp",<br />            "ty": 9,<br />            "ri": "GRP792482146823489621",<br />            "pi": "CAE5630283216026458665",<br />            "ct": "20171212T170445",<br />            "lt": "20171212T170445",<br />            "mt": 3,<br />            "cnm": 2,<br />            "mnm": 50,<br />            "mid": [<br />                "mn-name/ae_actuator/lamp_container1",<br />                "mn-name/ae_actuator/lamp_container2"<br />            ]<br />            "mtv": true,<br />            "csy": 1<br />        }<br />        "uri": "mn-name/ae_actuator/group_lamp"<br />    }<br />}      <br /> |




#### 6.2.10.2 API-GRP-RET

|API Id |API/GRP/RET/001<br />API/GRP/RET/001_RCN1 |
|-|-|
|API Name |&lt;group> resource RETRIEVE with resultContent set to 1 |
|Target Resource |Requested &lt;group> resource |
|Description |The interface is used to send a &lt;group> RETRIEVE request attached with resultContent set to 1 to the &lt;group> resource hosting CSE and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/GRP/RET/001<br />API/GRP/RET/001_RCN1    <br /><br />HTTP Request:<br /><br />GET /mn-name/ae_actuator/group_lamp?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br />{<br />    "m2m:grp": {<br />        "rn": "group_lamp",<br />        "ty": 9,<br />        "ri": "GRP792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "mt": 3,<br />        "cnm": 2,<br />        "mnm": 50,<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ]<br />        "mtv": true,<br />        "csy": 1<br />    }<br />}<br /> |




#### 6.2.10.3 API-GRP-UPD

|<br />API Id |API/GRP/UPD/001<br />API/GRP/UPD/001_RCN0<br />API/GRP/UPD/001_RCN1 |
|-|-|
|API Name |&lt;group> resource UPDATE with resultContent parameter |
|Target Resource |Requested &lt;group> resource |
|<br />Description |The interface is used to send a &lt;group> UPDATE request attached with resultContent to the Registrar CSE, and the Registrar CSE updates a &lt;group> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/GRP/UPD/001_RCN0<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_actuator/group_lamp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:grp": {<br />        "mnm": 100<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/GRP/UPD/001<br />API/GRP/UPD/001_RCN1    <br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_actuator/group_lamp?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />	"m2m:grp": {<br />	        "mnm": 100<br />      }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:grp": {<br />        "rn": "group_lamp",<br />        "ty": 9,<br />        "ri": "GRP792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "mt": 3,<br />        "cnm": 2,<br />        "mnm": 100,<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ]<br />        "mtv": true,<br />        "csy": 1<br />    }<br />}<br /> |




#### 6.2.10.4 API-GRP-DEL

|<br />API Id |API/GRP/DEL/001<br />API/GRP/DEL/001_RCN0<br />API/GRP/DEL/001_RCN1 |
|-|-|
|API Name |&lt;group> resource DELETE with resultContent parameter |
|Target Resource |Requested &lt;group> resource |
|<br />Description |The interface is used to send a &lt;group> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE deletes a &lt;group> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/GRP/DEL/001_RCN0   <br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_actuator/group_lamp?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/GRP/DEL/001<br />API/GRP/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_actuator/group_lamp?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:grp": {<br />        "rn": "group_lamp",<br />        "ty": 9,<br />        "ri": "GRP792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "mt": 3,<br />        "cnm": 2,<br />        "mnm": 100,<br />        "mid": [<br />            "mn-name/ae_actuator/lamp_container1",<br />            "mn-name/ae_actuator/lamp_container2"<br />        ]<br />        "mtv": true,<br />        "csy": 1<br />    }<br />}<br /> |




#### 6.2.10.5 API-GRP-FOPT

|API Id |API/GRP/FOPT/001 |
|-|-|
|API Name |&lt;group> resource  |
|Target Resource |Fopt virtual resource of the  &lt;group> resource |
|<br />Description |The interface is used to send a contentInstance CREATE request to the FanoutOutPoint Virtual resource of a group.<br />As a result, the contentInstances will be created on each container that belonging to this group. |
|<br /><br />Resource Structure<br />before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/GRP/<br /> <br />HTTP Request:<br /><br />POST /mn-name/ae_actuator/ group_lamp/fopt   HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=4<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 Created<br />Content-Location: mn-name/ae_actuator/group_lamp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br /><br />{<br />    "m2m:agr": {<br />        "rsp": [<br />            {<br />                "fr": "/ID-CSE-01/mn-name/ae_actuator/lamp_container1",<br />                "pc": {<br />                    "m2m:cin": {<br />                        "con": "20",<br />                        "cs": 2,<br />                        "ct": "20200609T163651,675786",<br />                        "et": "99991231T235959",<br />                        "lt": "20200609T163651,675786",<br />                        "pi": "cnt20200609T1632571403417286346243_cse01",<br />                        "ri": "cin20200609T1636511403417286346245_cse01",<br />                        "rn": "fopt20200609T1636511403417286346244_cse01",<br />                        "st": 1,<br />                        "ty": 4<br />                    }<br />                },<br />                "rqi": "1234",<br />                "rsc": 2001<br />            },<br />            {<br />                "fr": "/ID-CSE-01/mn-name/ae_actuator/lamp_container2",<br />                "pc": {<br />                    "m2m:cin": {<br />                        "con": "20",<br />                        "cs": 2,<br />                        "ct": "20200609T163651,680775",<br />                        "et": "99991231T235959",<br />                        "lt": "20200609T163651,680775",<br />                        "pi": "cnt20200609T1609261403417286346240_cse01",<br />                        "ri": "cin20200609T1636511403417286346246_cse01",<br />                        "rn": "fopt20200609T1636511403417286346244_cse01",<br />                        "st": 1,<br />                        "ty": 4<br />                    }<br />                },<br />                "rqi": "1234",<br />                "rsc": 2001<br />            }<br />        ]<br />    }<br />}<br /><br /><br /> |




### 6.2.11 Resource Type timeSeries

#### 6.2.11.0 Introduction
The &lt;timeSeries> resource represents a container for Time Series Data Instance. It is used to share information with other entities and potentially to track, detect and report the missing data in Time Series. 


#### 6.2.11.1 API-TS-CRE

|<br /><br />API Id |API/TS/CRE/001<br />API/TS/CRE/001_/RCN0<br />API/TS/CRE/001_/RCN1<br />API/TS/CRE/001_/RCN2<br />API/TS/CRE/001_/RCN3 |
|-|-|
|API Name |&lt;timeSeries> resource CREATE with resultContent parameter |
|Target Resource |&lt;AE> resource of the requested &lt;timeSeries> resource |
|<br />Description |The interface is used to send a &lt;timeSeries> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;timeSeries> resource and sends back a response. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/TS/CRE/001_RCN0<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=29<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "rn": timeSeries_cont,<br />        "pei": 1,<br />        "mdd": true,<br />        "mdt": 5<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/TS/CRE/001<br />API/TS/CRE/001_RCN1<br />    <br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=29<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "rn": timeSeries_cont,<br />        "pei": 1,<br />        "mdd": true,<br />        "mdt": 1<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:ts": {<br />        "rn": "timeSeries_cont",<br />        "ty": 29,<br />        "ri": "TS792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "et": "2021212T170445",<br />        "st": 0,<br />        "mni": 3153600000,<br />        "mbs": 3153600000,<br />        "mia": 31536000,<br />        "cni": 0,<br />        "cbs": 0,<br />        "pei": 1,<br />        "mdd": "true",<br />        "mdn": 1000,<br />        "mdc": 0,<br />        "mdt": 1<br />    }<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/TS/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=29<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "rn": timeSeries_cont,<br />        "pei": 1,<br />        "mdd": true,<br />        "mdt": 1<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont <br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/ae_sensor/timeSeries_cont"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/TS/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=29<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "rn": timeSeries_cont,<br />        "pei": 1,<br />         "mdd": true,<br />         "mdt": 1<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:ts": {<br />            "rn": "timeSeries_cont",<br />            "ty": 29,<br />            "ri": "TS792482146823489621",<br />            "pi": "CAE5630283216026458665",<br />            "ct": "20171212T170445",<br />            "lt": "20171212T170445",<br />            "et": "2021212T170445",<br />            "st": 0,<br />            "mni": 3153600000,<br />            "mbs": 3153600000,<br />            "mia": 31536000,<br />            "cni": 0,<br />            "cbs": 0,<br />            "pei": 1,<br />            "mdd": "ture",<br />            "mdn": 1000,<br />            "mdc": 0,<br />            "mdt": 1<br />        }<br />        "m2m:uri": "mn-name/ae_sensor/timeSeries_cont"<br />    }<br />}      <br /> |




#### 6.2.11.2 API-TS-RET

|API Id |API/TS/CRE/001<br />API/TS/CRE/001_RCN1 |
|-|-|
|API Name |&lt;timeSeries> resource RETRIEVE with resultContent parameter |
|Target Resource |Requested &lt;timeSeries> resource |
|Description |The interface is used to send a &lt;timeSeries> RETRIEVE request attached with resultContent set to 1 to the Registrar CSE and sends back a response. |
|<br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/TS/RET/001<br />API/TS/RET/001_RCN1   <br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:ts": {<br />        "rn": "timeSeries_cont",<br />        "ty": 29,<br />        "ri": "TS792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "et": "2021212T170445",<br />        "st": 0,<br />        "mni": 3153600000,<br />        "mbs": 3153600000,<br />        "mia": 31536000,<br />        "cni": 0,<br />        "cbs": 0,<br />        "pei": 1,<br />        "mdd": "ture",<br />        "mdn": 1000,<br />        "mdc": 0,<br />        "mdt": 1<br />    }<br />}<br /> |




#### 6.2.11.3 API-TS-UPD

|<br />API Id |API/TS/UPD/001<br />API/TS/UPD/001_RCN0<br />API/TS/UPD/001_RCN1 |
|-|-|
|API Name |&lt;timeSeries> resource UPDATE with resultContent parameter |
|Target Resource |Requested &lt;timeSeries> resource |
|<br />Description |The interface is used to send a &lt;timeSeries> UPDATE request attached with resultContent to the Registrar CSE, and the Registrar CSE updates a &lt;timeSeries> resource and sends back a response. |
|<br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/TS/UPD/001_RCN0<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_sensor/timeSeries_cont?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "mdt": 2<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/TS/UPD/001<br />API/TS/UPD/001_RCN1<br /><br />HTTP Request:<br /><br />PUT /mn-name/ae_sensor/timeSeries_cont?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:ts": {<br />        "mdt": 2<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:ts": {<br />        "rn": "timeSeries_cont",<br />        "ty": 29,<br />        "ri": "TS792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "et": "2021212T170445",<br />        "st": 0,<br />        "mni": 3153600000,<br />        "mbs": 3153600000,<br />        "mia": 31536000,<br />        "cni": 0,<br />        "cbs": 0,<br />        "pei": 1,<br />        "mdd": "ture",<br />        "mdn": 1000,<br />        "mdc": 0,<br />        "mdt": 2<br />    }<br />}<br /> |




#### 6.2.11.4 API-TS-DEL

|<br />API Id |API/TS/DEL/001<br />API/TS/DEL/001_RCN0<br />API/TS/DEL/001_RCN1 |
|-|-|
|API Name |&lt;timeSeries> resource DELETE with resultContent parameter |
|Target Resource |Requested &lt;timeSeries> resource |
|<br />Description |The interface is used to send a &lt;timeSeries> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE updates a &lt;timeSeries> resource and sends back a response. |
|<br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=0 |<br />API/TS/DEL/001<br />API/TS/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/timeSeries_cont?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1 |<br />API/TS/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/timeSeries_cont?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:ts": {<br />        "rn": "timeSeries_cont",<br />        "ty": 29,<br />        "ri": "TS792482146823489621",<br />        "pi": "CAE5630283216026458665",<br />        "ct": "20171212T170445",<br />        "lt": "20171212T170445",<br />        "et": "2021212T170445",<br />        "st": 0,<br />        "mni": 3153600000,<br />        "mbs": 3153600000,<br />        "mia": 31536000,<br />        "cni": 0,<br />        "cbs": 0,<br />        "pei": 1,<br />        "mdd": "ture",h<br />        "mdn": 1000,<br />        "mdc": 0,<br />        "mdt": 2<br />    }<br />}<br /> |




### 6.2.12 Resource Type timeSeriesInstance

#### 6.2.12.0 Introduction
The &lt;timeSeriesInstance> resource represents a data instance in the &lt;timeSeries> resource. 


#### 6.2.12.1 API-TSI-CRE

|<br /><br />API Id |API/TSI/CRE/001<br />API/TSI/CRE/001_RCN0<br />API/TSI/CRE/001_RCN1<br />API/TSI/CRE/001_RCN2<br />API/TSI/CRE/001_RCN3 |
|-|-|
|API Name |&lt;timeSeriesInstance> resource CREATE with resultContent parameter |
|Target Resource |&lt;timeSeries> resource of the requested &lt;timeSeriesInstance> resource |
|<br />Description |The interface is used to send a &lt;timeSeriesInstance> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;timeSeriesInstance> resource and sends back a response. |
|<br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/TSI/CRE/001_RCN0<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/timeSeries_cont?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=30<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:tsi": {<br />        "dgt": "20180307T123456",<br />        "con": "DATA_TACK"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/TSI/CRE/001<br />API/TSI/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/timeSeries_cont HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=30<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "dgt": "20180307T123456",<br />        "con": "DATA_TACK"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont<br />Content-Type: application/json<br />X-M2M-Origin: CAE5630283216026458665<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "ty": 30,<br />        "pi": "CAE5630283216026458665",<br />        "ri": "TSI840674869203617594",<br />        "ct": "20180307T012211",<br />        "lt": "20180307T012211",<br />        "et": "20210307T012211",<br />        "dgt": "20180307T123456"<br />        "con": "DATA_TACK",<br />        "cs": 9,<br />        "st": 7<br />    }<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/TSI/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/timeSeries_cont?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=30<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "dgt": "20180307T123456",<br />        "con": "DATA_TACK"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/ae_sensor/timeSeries_cont/tsi_value1"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/TSI/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name/ae_sensor/timeSeries_cont?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=30<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "dgt": "20180307T123456",<br />        "con": "DATA_TACK"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:tsi": {<br />            "rn": "tsi_value1",<br />            "ty": 30,<br />            "pi": "CAE5630283216026458665",<br />            "ri": "TSI840674869203617594",<br />            "ct": "20180307T012211",<br />            "lt": "20180307T012211",<br />            "et": "2n0210307T012211",<br />            "dgt": "20180307T123456"<br />            "con": "DATA_TACK",<br />            "cs": 9,<br />            "st": 7<br />        }<br />    "m2m:uri": "mn-name/ae_sensor/timeSeries_cont/tsi_value1"<br />    }<br />}      <br /> |




#### 6.2.12.2 API-TSI-RET

|API Id |API/TSI/RET/001<br />API/TSI/RET/001_RCN1 |
|-|-|
|API Name |&lt;timeSeriesInstance> resource RETRIEVE with resultContent parameter |
|Target Resource |Requested &lt;timeSeriesInstance> resource |
|<br />Description |The interface is used to send a &lt;timeSeriesInstance> RETRIEVE request attached with resultContent set to 1 to the Registrar CSE and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/TSI/RET/001<br />API/TSI/RET/001_RCN1<br /><br />HTTP Request:<br /><br />GET /mn-name/ae_sensor/timeSeries_cont/tsi_value1?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "ty": 30,<br />        "pi": "CAE5630283216026458665",<br />        "ri": "TSI840674869203617594",<br />        "ct": "20180307T012211",<br />        "lt": "20180307T012211",<br />        "et": "2n0210307T012211",<br />        "dgt": "20180307T123456"<br />        "con": "DATA_TACK",<br />        "cs": 9,<br />        "st": 7<br />    }<br />}<br /> |




#### 6.2.12.3 API-TSI-UPD

|API Id |API/TSI/UPD |
|-|-|
|API Name |&lt;timeSeriesInstance> resource UPDATE |
|Target Resource |Requested &lt;timeSeriesInstance> resource |
|Description |Update operation is not allowed in &lt;timeSeriesInstance> resource |




#### 6.2.12.4 API-TSI-DEL

|<br />API Id |API/TSI/DEL/001<br />API/TSI/DEL/001_RCN0<br />API/TSI/DEL/001_RCN1 |
|-|-|
|API Name |&lt;timeSeriesInstance> resource DELETE with resultContent parameter |
|Target Resource |Requested &lt;timeSeriesInstance> resource |
|<br />Description |The interface is used to send a &lt;timeSeriesInstance> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;timeSeriesInstance> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=0 |<br />API/TSI/DEL/001<br />API/TSI/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/timeSeries_cont/tsi_value1?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1 |<br />API/TSI/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/ae_sensor/timeSeries_cont/tsi_value1?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/ae_sensor/timeSeries_cont/tsi_value1<br />Content-Type: application/json<br />X-M2M-Origin: CAE5630283216026458665<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:tsi": {<br />        "rn": "tsi_value1",<br />        "ty": 30,<br />        "pi": "CAE5630283216026458665",<br />        "ri": "TSI840674869203617594",<br />        "ct": "20180307T012211",<br />        "lt": "20180307T012211",<br />        "et": "2n0210307T012211",<br />        "dgt": "20180307T123456"<br />        "con": "DATA_TACK",<br />        "cs": 9,<br />        "st": 7<br />    }<br />}<br /> |




### 6.2.13 Resource Type accessControlPolicy

#### 6.2.13.0 Introduction
The &lt;accessControlPolicy> resource is defined to contain a set of access control rules defining for which entities have which privilege to perform operations such as CREATE, RETRIEVE, UPDATE and DELETE. The allowed operations are defined by an attribute accessControlOperations that associated with each &lt;accessControlPolicy> resource. 


#### 6.2.13.1 API-ACP-CRE

|<br /><br />API Id |API/ACP/CRE/001<br />API/ACP/CRE/001_RCN0<br />API/ACP/CRE/001_RCN1<br />API/ACP/CRE/001_RCN2<br />API/ACP/CRE/001_RCN3 |
|-|-|
|API Name |&lt;accessControlPolicy> resource CREATE with resultContent parameter |
|Target Resource |&lt;CSEBase> of the requested &lt;accessControlPolicy> resource |
|<br />Description |The interface is used to send a &lt;accessControlPolicy> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;accessControlPolicy> resource, and sends back a response. |
|<br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/ACP/CRE/001_RCN0<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=1<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "rn": "accessControlPolicy",<br />        "et" : "20201221T064952",<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "CAE1", "CAE2" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                     "acco" : [],<br />                     "acop" : 63,<br />                     "acor" : [ "all" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/ACP/CRE/001<br />API/ACP/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=1<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "rn": "accessControlPolicy",<br />        "et" : "20201221T064952",<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "CAE1", "CAE2" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "all" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:acp": {<br />        "rn": "accessControlPolicy",<br />        "ty": 1,<br />        "ri": "ACP503720698362418574",<br />        "pi": "mnID",<br />        "ct": "20180308T115922",<br />        "lt": "20180308T115922",<br />        "et": "20201221T064952",<br />        "pv": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE1",<br />                        "CAE2"<br />                    ]<br />                }<br />            ]<br />        },<br />        "pvs": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "all"<br />                    ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/ACP/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=1<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "rn": "accessControlPolicy",<br />        "et" : "20201221T064952",<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "CAE1", "CAE2" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "all" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/accessControlPolicy"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/ACP/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=1<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "rn": "accessControlPolicy",           <br />        "et" : "20201221T064952",<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "CAE1", "CAE2" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                    "acco" : [],<br />                    "acop" : 63,<br />                    "acor" : [ "all" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:rce": {<br />        "m2m:acp": {<br />            "rn": "accessControlPolicy",<br />            "ty": 1,<br />            "ri": "ACP503720698362418574",<br />            "pi": "mnID",<br />            "ct": "20180308T115922",<br />            "lt": "20180308T115922",<br />            "et": "20201221T064952",<br />            "pv": {<br />                "acr": [<br />                    {<br />                        "acco": [],<br />                        "acop": 63,<br />                        "acor": [<br />                            "CAE1",<br />                            "CAE2"<br />                        ]<br />                    }<br />                ]<br />            },<br />            "pvs": {<br />                "acr": [<br />                    {<br />                        "acco": [],<br />                        "acop": 63,<br />                        "acor": [<br />                            "all"<br />                        ]<br />                    }<br />                ]<br />            }<br />            "m2m:uri": "mn-name/accessControlPolicy"<br />        }<br />    }<br />}  <br /> |




#### 6.2.12.2 API-ACP-RET

|API Id |API/ACP/RET/001<br />API/ACP/RET/001_RCN1 |
|-|-|
|API Name |&lt;accessControlPolicy> resource RETRIEVE with resultContent parameter |
|Target Resource |&lt;CSEBase> of the requested &lt;accessControlPolicy> resource |
|<br />Description |The interface is used to send a &lt;accessControlPolicy> RETRIEVE request attached with resultContent set to 1 to the Registrar CSE and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/ACP/RET/001<br />API/ACP/RET/001_RCN1<br /><br />HTTP Request:<br /><br />GET /mn-name/accessControlPolicy?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:acp": {<br />        "rn": "accessControlPolicy",<br />        "ty": 1,<br />        "ri": "ACP503720698362418574",<br />        "pi": "mnID",<br />        "ct": "20180308T115922",<br />        "lt": "20180308T115922",<br />        "et": "20201221T064952",<br />        "pv": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE1",<br />                        "CAE2"<br />                    ]<br />                }<br />            ]<br />        },<br />        "pvs": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "all"<br />                    ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /> |




#### 6.2.12.3 API-ACP-UPD

|<br />API Id |API/ACP/UPD/001<br />API/ACP/UPD/001_RCN0<br />API/ACP/UPD/001_RCN1 |
|-|-|
|API Name |&lt;accessControlPolicy> resource UPDATE with resultContent parameter |
|Target Resource |&lt;accessControlPolicy> resource |
|<br />Description |The interface is used to send a &lt;accessControlPolicy> UPDATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;accessControlPolicy> resource and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/ACP/UPD/001_RCN0<br /><br />HTTP Request:<br /><br />PUT /mn-name/accessControlPolicy?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acor" : [ "CAE_A", "CAE_B" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                    "acor" : [ "CAE_C", "CAE_D" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/ACP/UPD/001<br />API/ACP/UPD/001_RCN1<br /><br />HTTP Request:<br /><br />PUT /mn-name/accessControlPolicy?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:acp" : {<br />        "pv" : {<br />            "acr" : [<br />                {<br />                    "acor" : [ "CAE_A", "CAE_B" ]<br />                }<br />            ]<br />        },<br />        "pvs" : {<br />            "acr" : [<br />                {<br />                    "acor" : [ "CAE_C", "CAE_D" ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:acp": {<br />        "rn": "accessControlPolicy",<br />        "ty": 1,<br />        "ri": "ACP503720698362418574",<br />        "pi": "mnID",<br />        "ct": "20180308T115922",<br />        "lt": "20180308T115922",<br />        "et": "20201221T064952",<br />        "pv": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE_A",<br />                        "CAE_B"<br />                    ]<br />                }<br />            ]<br />        },<br />        "pvs": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE_C",<br />                        "CAE_D"<br />                    ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /> |




#### 6.2.12.4 API-ACP-DEL

|<br />API Id |API/ACP/DEL/001<br />API/ACP/DEL/001_RCN0<br />API/ACP/DEL/001_RCN1 |
|-|-|
|API Name |&lt;accessControlPolicy> resource DELETE with resultContent parameter |
|Target Resource |&lt;accessControlPolicy> resource |
|<br />Description |The interface is used to send a &lt;accessControlPolicy> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;accessControlPolicy> resource and sends back a response.  |
|<br /><br /><br /><br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=0 |<br />API/ACP/DEL/001<br />API/ACP/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/accessControlPolicy?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1 |<br />API/ACP/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/accessControlPolicy?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/accessControlPolicy<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:acp": {<br />        "rn": "accessControlPolicy",<br />        "ty": 1,<br />        "ri": "ACP503720698362418574",<br />        "pi": "mnID",<br />        "ct": "20180308T115922",<br />        "lt": "20180308T115922",<br />        "et": "20201221T064952",<br />        "pv": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE_A",<br />                        "CAE_B"<br />                    ]<br />                }<br />            ]<br />        },<br />        "pvs": {<br />            "acr": [<br />                {<br />                    "acco": [],<br />                    "acop": 63,<br />                    "acor": [<br />                        "CAE_C",<br />                        "CAE_D"<br />                    ]<br />                }<br />            ]<br />        }<br />    }<br />}<br /> |




### 6.2.14 Resource Type flexContainer

#### 6.2.14.0 Introduction
The &lt;flexContainer> resource type is a customizable container for data instances. While &lt;contentInstance> save the data in content attribute, &lt;flexContainer> resource type directly contains the data in the attribute. Since it can have any attribute name, it may be a solution for saving custom data which is defined by the developer or manufacturer. 

The CRUD examples in this clause are written based on the parking lot implementation. As custom attributes, availableSpotNumber, totalSpotNumber are made to save data for the parking lot.


#### 6.2.14.1 API-FLX-CRE

|<br /><br />API Id |API/FLX/CRE/001<br />API/FLX/CRE/001_RCN0<br />API/FLX/CRE/001_RCN1<br />API/FLX/CRE/001_RCN2<br />API/FLX/CRE/001_RCN3 |
|-|-|
|API Name |&lt;flexContainer> resource CREATE with resultContent parameter |
|Target Resource |&lt;CSEBase> of the requested &lt;flexContainer> resource |
|<br />Description |The interface is used to send a &lt;flexContainer> CREATE request attached with resultContent to the Registrar CSE, and the Registrar CSE creates a &lt;flexContainer> resource, and sends back a response. |
|<br />Resource Structure before Sending Request | |
|<br /><br /><br /><br /><br />Call Flow |<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/FLX/CRE/001_RCN0<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=28<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot": {<br />        "rn": "yt_lot_1",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/FLX/CRE/001<br />API/FLX/CRE/001_RCN1<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=28<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot": {<br />        "rn": "yt_lot_1",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /><br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:sc_offLot": {<br />        "pi": "CAE5630283216026458665",<br />        "ri": "FLX37696264720673421",<br />        "ty": 28,<br />        "ct": "20181019T045127",<br />        "st": 15878,<br />        "rn": "yt_lot_1",<br />        "lt": "20181207T002422",<br />        "et": "20211019T045127",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=2<br /> |<br />API/FLX/CRE/001_RCN2<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=2 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=28<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot": {<br />        "rn": "yt_lot_1",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /><br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{<br />    "m2m:uri": "mn-name/yt_lot_1"<br />}<br /> |
|<br /><br /><br /><br />Example with <br />RCN=3 |<br />API/FLX/CRE/001_RCN3<br /><br />HTTP Request:<br /><br />POST /mn-name?rcn=3 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=28<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot": {<br />        "rn": "yt_lot_1",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /><br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /><br />{  <br />    "m2m:rce":{  <br />        "m2m:sc_offLot":{  <br />           "pi":"CAE5630283216026458665",<br />           "ri":"FLX37696264720673421",<br />           "ty":28,<br />           "ct":"20181019T045127",<br />           "st":15878,<br />           "rn":"yt_lot_1",<br />           "lt":"20181207T002422",<br />           "et":"20211019T045127",<br />           "lbl":[  <br />              "sc"<br />           ],<br />           "cnd":"http://developers.iotocean.org/schema/offStreetParking.xsd",<br />           "type":"OffStreetParking",<br />           "category":"lot_1",<br />           "geolocation":[  <br />              37.4114423,<br />              127.1293735<br />           ],<br />           "name":"parkingLot_1",<br />           "availableSpotNumber":"3",<br />           "totalSpotNumber":"110"<br />        }<br />     },<br />     "m2m:uri":"mn-name/yt_lot_1"<br />} <br /> |




#### 6.2.14.2 API-FLX-RET

|API Id |API/FLX/RET/001<br />API/FLX/RET/001_RCN1 |
|-|-|
|API Name |&lt;flexContainer> resource RETRIEVE with resultContent parameter |
| Target Resource |&lt;CSEBase> of the requested &lt;flexContainer> resource |
|<br />Description |The interface is used to send a &lt;flexContainer> RETRIEVE request attached with resultContent set to 1 to the Registrar CSE and sends back a response. |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /> <br /> |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/FLX/RET/001<br />API/FLX/RET/001_RCN1<br /><br />HTTP Request:<br /><br />GET /mn-name/yt_lot_1?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /><br />{<br />    "m2m:sc_offLot": {<br />        "pi": "CAE5630283216026458665",<br />        "ri": "FLX37696264720673421",<br />        "ty": 28,<br />        "ct": "20181019T045127",<br />        "st": 15878,<br />        "rn": "yt_lot_1",<br />        "lt": "20181207T002422",<br />        "et": "20211019T045127",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "3",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /> |




#### 6.2.14.3 API-FLX-UPD

|<br />API Id |API/FLX/UPD/001<br />API/FLX/UPD/001_RCN0<br />API/FLX/UPD/001_RCN1 |
|-|-|
|API Name |&lt;flexContainer> resource UPDATE with resultContent parameter |
|Target Resource |&lt;flexContainer> resource |
|<br />Description |The interface is used to send a &lt;flexContainer> UPDATE request attached with resultContent to the Registrar CSE, and the Registrar CSE updates a &lt;flexContainer> resource and sends back a response. |
|<br />Resource Structure before Sending Request<br /><br /> | |
|<br /><br /><br /><br /><br />Call Flow | |
|<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br />Example with <br />RCN=0 |<br />API/FLX/UPD/001_RCN0<br /><br />HTTP Request:<br /><br />PUT /mn-name/yt_lot_1?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot" : {<br />        "availableSpotNumber": "40",<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />no RCN or<br />RCN=1 |<br />API/FLX/UPD/001<br />API/FLX/UPD/001_RCN1<br /><br />HTTP Request:<br /><br />PUT /mn-name/yt_lot_1?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sc_offLot" : {<br />        "availableSpotNumber": "40",<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:sc_offLot": {<br />        "pi": "CAE5630283216026458665",<br />        "ri": "FLX37696264720673421",<br />        "ty": 28,<br />        "ct": "20181019T045127",<br />        "st": 15878,<br />        "rn": "yt_lot_1",<br />        "lt": "20181207T052435",<br />        "et": "20211019T045127",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "40",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /> |




#### 6.2.14.4 API-FLX-DEL

|<br />API Id |API/FLX/DEL/001<br />API/FLX/DEL/001_RCN0<br />API/FLX/DEL/001_RCN1 |
|-|-|
|API Name |&lt;flexContainer> resource DELETE with resultContent parameter |
|Target Resource |&lt;flexContainer> resource |
|<br />Description |The interface is used to send a &lt;flexContainer> DELETE request attached with resultContent to the Registrar CSE, and the Registrar CSE deletes a &lt;flexContainer> resource and sends back a response.  |
|<br /><br /><br /><br />Resource Structure before Sending Request |<br /><br /> |
|<br /><br /><br /><br /><br />Call Flow |<br /> |
|<br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br />Example with <br />no RCN or<br />RCN=0 |<br />API/FLX/DEL/001<br />API/FLX/DEL/001_RCN0<br /><br />HTTP Request:<br /><br />DELETE /mn-name/yt_lot_1?rcn=0 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /> |
|<br /><br /><br /><br /><br /><br />Example with <br />RCN=1 |<br />API/FLX/DEL/001_RCN1<br /><br />HTTP Request:<br /><br />DELETE /mn-name/yt_lot_1?rcn=1 HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Location: mn-name/yt_lot_1<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2002<br /><br />{<br />    "m2m:sc_offLot": {<br />        "pi": "CAE5630283216026458665",<br />        "ri": "FLX37696264720673421",<br />        "ty": 28,<br />        "ct": "20181019T045127",<br />        "st": 15878,<br />        "rn": "yt_lot_1",<br />        "lt": "20181207T052435",<br />        "et": "20211019T045127",<br />        "lbl": [<br />            "sc"<br />        ],<br />        "cnd": "http://developers.iotocean.org/schema/offStreetParking.xsd",<br />        "type": "OffStreetParking",<br />        "category": "lot_1",<br />        "geolocation": [<br />             37.4114423,<br />             127.1293735<br />        ],<br />        "name": "parkingLot_1",<br />        "availableSpotNumber": "40",<br />        "totalSpotNumber": "110"<br />    }<br />}<br /> |




# Annex A: Example of notification

# A.1 Notification API

## A.1.0 Introduction
The notify operation is used for notify any event. AE or CSE which has privilege to make a &lt;subscription> resource as a child resource of the subscribed-to resource. The &lt;subscription> resource includes notification policies that specify which, when, and how notifications are sent. 

In this clause, notification examples are provided for the understanding of notification procedure. Especially, examples have different notificationEnentType in the eventNotificationCriteria. The notificationEventType value is specified in table A.1.0-1 and set when notification is sent. 


**Table A.1.0-1: Interpretation of notificationEventType**

|Value |Interpretation |Note |
|-|-|-|
|1 |Update_of_Resource |Default |
|2 |Delete_of_Resource | |
|3 |Create_of_Direct_Child_Resource | |
|4 |Delete_of_Direct_Child_Resource | |




## A.1.1 API-NOTI-NET1

|API Id |API/NOTI/NET1/STEP01<br />API/NOTI/NET1/STEP02<br />API/NOTI/NET1/STEP03 |API/NOTI/NET1/STEP01<br />API/NOTI/NET1/STEP02<br />API/NOTI/NET1/STEP03 |
|-|-|-|
|API Name |Notification procedure when the &lt;subscription> resource has notificationEventType set to 1(Hosting CSE sends notification when the subscribed-to resource has been updated) |Notification procedure when the &lt;subscription> resource has notificationEventType set to 1(Hosting CSE sends notification when the subscribed-to resource has been updated) |
|Target Resource |Update Target: Requested &lt;container> resource <br />Notification Target: originator |Update Target: Requested &lt;container> resource <br />Notification Target: originator |
|<br />Description |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 1 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends an UPDATE request to the &lt;container> resource. The Registrar CSE updates a &lt;container> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as update succeed. The originator sends back an ACK message. |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 1 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends an UPDATE request to the &lt;container> resource. The Registrar CSE updates a &lt;container> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as update succeed. The originator sends back an ACK message. |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET1/STEP01<br />    <br />HTTP Request:<br /><br />POST /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_1">[1]</a><br />        },<br />        "nu": ["AE1"],<br />        "rn": "cont_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/cont_temp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br />Resource Structure<br />before Sending Request |		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET1/STEP02<br /><br />HTTP Request:<br /><br />PUT /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T08463114<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cnt": {<br />        "mni": "300"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:cnt": {<br />        "cbs": 10,<br />        "cni": 0,<br />        "ct": "20180406T125807",<br />        "et": "99991231T235959",<br />        "lbl": [<br />            "indoor_temp"<br />        ],<br />        "lt": "20180406T130109",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 300,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T1258071405855183193603_cse01",<br />        "rn": "cont_temp",<br />        "st": 1,<br />        "ty": 3<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br />Resource Structure<br />before Sending Request |		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET1/STEP03<br />    <br />HTTP Request:<br /><br />POST HTTP/1.1<br />Accept: application/json<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: mn-name<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sgn": {<br />        "sur": " mn-name/cont_temp/cont_sub",<br />        "nev": {<br />            "net":1,<br />            "rep": {<br />                "m2m:cnt": {<br />                    "cbs": 10,<br />                    "cni": 0,<br />                    "ct": "20180406T125807",<br />                    "et": "99991231T235959",<br />                    "lbl": [<br />                        "indoor_temp"<br />                    ],<br />                    "lt": "20180406T130109",<br />                    "mbs": 60000000,<br />                    "mia": 1600,<br />                    "mni": 300,<br />                    "pi": "CAE0120180406T0846311405855351047680_cse01",<br />                    "ri": "cnt20180406T1258071405855183193603_cse01",<br />                    "rn": "cont_temp",<br />                    "st": 1,<br />                    "ty": 3<br />                }<br />             }<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /> |




## A.1.2 API-NOTI-NET2

|API Id |API/NOTI/NET2/STEP01<br />API/NOTI/NET2/STEP02<br />API/NOTI/NET2/STEP03 |API/NOTI/NET2/STEP01<br />API/NOTI/NET2/STEP02<br />API/NOTI/NET2/STEP03 |
|-|-|-|
|API Name |Notification procedure when the &lt;subscription> resource has notificationEventType set to 2(Hosting CSE sends notification when the subscribed to resource has been deleted) |Notification procedure when the &lt;subscription> resource has notificationEventType set to 2(Hosting CSE sends notification when the subscribed to resource has been deleted) |
|Target Resource |Delete Target: Requested &lt;container> resource <br />Notification Target: originator |Delete Target: Requested &lt;container> resource <br />Notification Target: originator |
|<br />Description |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 2 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends a DELETE request to the &lt;container> resource. The Registrar CSE deletes a &lt;container> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as delete succeed. The originator sends back an ACK message. |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 2 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends a DELETE request to the &lt;container> resource. The Registrar CSE deletes a &lt;container> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as delete succeed. The originator sends back an ACK message. |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET2/STEP01<br />    <br />HTTP Request:<br /><br />POST /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_2">[2]</a><br />        },<br />        "nu": ["AE1"],<br />        "rn": "cont_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/cont_temp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET2/STEP02<br />    <br />HTTP Request:<br /><br />DELETE /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T08463114<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:cnt": {<br />        "cbs": 10,<br />        "cni": 0,<br />        "ct": "20180406T125807",<br />        "et": "99991231T235959",<br />        "lbl": [<br />            "indoor_temp"<br />        ],<br />        "lt": "20180406T130109",<br />        "mbs": 60000000,<br />        "mia": 1600,<br />        "mni": 300,<br />        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />        "ri": "cnt20180406T1258071405855183193603_cse01",<br />        "rn": "cont_temp",<br />        "st": 1,<br />        "ty": 3<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |Resource Structure<br />before Sending Request | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET2/STEP03<br />    <br />HTTP Request:<br /><br />POST HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: mn-name<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sgn": {<br />        "sur": " mn-name/cont_temp/cont_sub",<br />        "nev": {<br />            "net":2,<br />                "rep": {<br />                    "m2m:cnt": {<br />                        "cbs": 10,<br />                        "cni": 0,<br />                        "ct": "20180406T125807",<br />                        "et": "99991231T235959",<br />                        "lbl": [<br />                            "indoor_temp"<br />                        ],<br />                        "lt": "20180406T130109",<br />                        "mbs": 60000000,<br />                        "mia": 1600,<br />                        "mni": 300,<br />                        "pi": "CAE0120180406T0846311405855351047680_cse01",<br />                        "ri": "cnt20180406T1258071405855183193603_cse01",<br />                        "rn": "cont_temp",<br />                        "st": 1,<br />                        "ty": 3<br />                }<br />             }<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /> |




## A.1.3 API-NOTI-NET3

|API Id |API/NOTI/NET3/STEP01<br />API/NOTI/NET3/STEP02<br />API/NOTI/NET3/STEP03 |API/NOTI/NET3/STEP01<br />API/NOTI/NET3/STEP02<br />API/NOTI/NET3/STEP03 |
|-|-|-|
|API Name |Notification procedure when the &lt;subscription> resource has notificationEventType set to 3 (Hosting CSE sends notification when the direct child resource has been created) |Notification procedure when the &lt;subscription> resource has notificationEventType set to 3 (Hosting CSE sends notification when the direct child resource has been created) |
|Target Resource |Create &lt;contentIntance> target: Requested &lt;container> resource <br />Notification Target: originator |Create &lt;contentIntance> target: Requested &lt;container> resource <br />Notification Target: originator |
|<br />Description |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 3 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends a CREATE request of the &lt;contentInstance> resource to the &lt;container> resource. The Registrar CSE creates a &lt;contentInstance> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as create succeed. The originator sends back an ACK message. |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 3 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends a CREATE request of the &lt;contentInstance> resource to the &lt;container> resource. The Registrar CSE creates a &lt;contentInstance> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as create succeed. The originator sends back an ACK message. |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET3/STEP01<br />    <br />HTTP Request:<br /><br />POST /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />	"m2m:sub": {<br />             "enc": {<br />                   "net": <a href="#_ref_3">[3]</a><br />             },<br />	       "nu": ["AE1"],<br />	       "rn": "cont_sub"<br />      }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/cont_temp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET3/STEP02<br />    <br />HTTP Request:<br /><br />POST /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T08463114<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:cin": {<br />        "con": "20"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T135509",<br />        "et": "99991231T235959",<br />        "lt": "20180406T135509",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1355091405855351047683_cse01",<br />        "rn": "cin20180406T1355091405855351047682_cse01",<br />        "st": 1,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |Resource Structure<br />before Sending Request | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET3/STEP03<br />    <br />HTTP Request:<br /><br />POST HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: mn-name<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sgn": {<br />        "sur": " mn-name/cont_temp/cont_sub",<br />        "nev": {<br />            "net":3,<br />            "rep": {<br />                "m2m:cin": {<br />                    "con": "20",<br />                    "cs": 2,<br />                    "ct": "20180406T135509",<br />                    "et": "99991231T235959",<br />                    "lt": "20180406T135509",<br />                    "pi": "cnt20180406T1353041405855518901760_cse01",<br />                    "ri": "cin20180406T1355091405855351047683_cse01",<br />                    "rn": "cin20180406T1355091405855351047682_cse01",<br />                    "st": 1,<br />                    "ty": 4<br />                }<br />            }<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /> |




## A.1.4 API-NOTI-NET4

|API Id |API/NOTI/NET4/STEP01<br />API/NOTI/NET4/STEP02<br />API/NOTI/NET4/STEP03 |
|-|-|
|API Name |Notification procedure when the &lt;subscription> resource has notificationEventType set to 4(Hosting CSE sends notification when the direct child resource has been deleted) |
|Target Resource |Delete &lt;contentIntance> target: Requested &lt;container> resource <br />Notification Target: originator |
|<br />Description |Figure below depicts the procedure for notification. <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Initial condition: MN(Hosting CSE) has a &lt;container> resource. At the same time, &lt;container> resource has &lt;contentInstance> resource as a direct child resource. The originator is AE1 in this clause, but can be CSE.<br /><br />Step 01: The originator sends a &lt;subscription> resource CREATE request to the &lt;container> resource on the Registrar CSE. In the request, notificationEventType set to 4 and notificationURI attribute set to originator. The Registrar CSE creates a &lt;subscription> resource and sends back a response.<br />Step 02: An AE2 sends a DELETE request of the &lt;contentInstance> resource to the &lt;container> resource. The Registrar CSE deletes a &lt;contentInstance> resource and sends back a response.<br />Step 03: The Hosting CSE sends notification as soon as delete succeed. The originator sends back an ACK message. |



|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br />Resource Structure<br />before Sending Request |<br />		 |
|-|-|-|
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br />HTTP Header Information<br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 01<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET4/STEP01<br /><br />HTTP Request:<br /><br />POST /mn-name/cont_temp? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE5630283216026458665<br />Content-Type: application/json;ty=23<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sub": {<br />        "enc": {<br />            "net": <a href="#_ref_4">[4]</a><br />        },<br />        "nu": ["AE1"],<br />        "rn": "cont_sub"<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />201 Created<br />Content-Location: mn-name/cont_temp<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2001<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br />Resource Structure<br />before Sending Request |<br />		 |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br />HTTP Header Information<br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 02<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET4/STEP02<br /><br />HTTP Request:<br /><br />DELETE /mn-name/cont_temp/ci_temp_value1? HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: CAE0120180406T08463114<br />Content-Type: application/json<br />Accept: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br /><br />HTTP Response:<br /><br />200 OK<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2004<br /><br />{<br />    "m2m:cin": {<br />        "con": "20",<br />        "cs": 2,<br />        "ct": "20180406T135509",<br />        "et": "99991231T235959",<br />        "lt": "20180406T135509",<br />        "pi": "cnt20180406T1353041405855518901760_cse01",<br />        "ri": "cin20180406T1355091405855351047683_cse01",<br />        "rn": "cin20180406T1355091405855351047682_cse01",<br />        "st": 1,<br />        "ty": 4<br />    }<br />}<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |Resource Structure<br />before Sending Request | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Call Flow | |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br />HTTP Header Information<br /><br /><br /> |<br /> |
|<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Step 03<br /><br /> |<br /><br /><br /><br /><br /><br />Example |<br />API/NOTI/NET4/STEP03<br /><br />HTTP Request:<br /><br />POST HTTP/1.1<br />Host: 192.168.0.10:8282<br />X-M2M-Origin: mn-name<br />Content-Type: application/json<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br /><br />{<br />    "m2m:sgn": {<br />        "sur": " mn-name/cont_temp/cont_sub",<br />        "nev": {<br />            "net":4,<br />            "rep": {<br />                "m2m:cin": {<br />                    "con": "20",<br />                    "cs": 2,<br />                    "ct": "20180406T135509",<br />                    "et": "99991231T235959",<br />                    "lt": "20180406T135509",<br />                    "pi": "cnt20180406T1353041405855518901760_cse01",<br />                    "ri": "cin20180406T1355091405855351047683_cse01",<br />                    "rn": "cin20180406T1355091405855351047682_cse01",<br />                    "st": 1,<br />                    "ty": 4<br />                }<br />            }<br />        }<br />    }<br />}<br /><br /><br />HTTP Response:<br /><br />200 OK<br />X-M2M-RI: 1234<br />X-M2M-RVI: 2a<br />X-M2M-RSC: 2000<br /> |




# Annex B: Bibliography

- oneM2M TS-0009: "HTTP Protocol Binding".
- oneM2M TS-0011: "Common Terminology".

# History

|Draft history (to be removed on publication) |Draft history (to be removed on publication) |Draft history (to be removed on publication) |
|-|-|-|
|V3.0.0.0 |2021-05-12 |Initial Draft V3.0.0.0<br />Implemented contribution agreed at TDE49.4<br />TDE-2021-0015-TR-0051_API-AE |





|Publication history |Publication history |Publication history |
|-|-|-|
|V0.0.6 |August 2020 |Partners pre-processing done by editHelp!<br />e-mail:  |
|V2.0.0 |November 2020 |Final version |
| | | |
| | | |
| | | |
