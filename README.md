# checkip
Send an alert when an Elastic Cloud's Webcrawler or other Search connector's IP changes. 


* Create a new webcrawler instance "checkip"

![Alt text](/img/setup1.png?raw=true "Create webcrawler")

* Either with the domain:
```http://ip.4ndata.com/``` or your local instance of checkip.py

![Alt text](/img/setup2.png?raw=true "Set domain")

* Once created, adapt the ingest pipeline by customizing it.
* Uncheck all ML processing options

![Alt text](/img/setup3.png?raw=true "Uncheck ML options")


* Adapt the 'search-checkip@custom' ingest pipeline by selecting edit->Manage-Edit

![Alt text](/img/setup4.png?raw=true "Uncheck ML options")

![Alt text](/img/setup5.png?raw=true "Uncheck ML options")

* Select Import Processor and add the processors stanza below

```
{
  "processors": [
       {
         "fingerprint": {
           "fields": ["body_content"]
         }
       },
       {
        "set": {
          "field": "_id",
          "value": "{{fingerprint}}"
        }
      },
      {
        "set": {
          "field": "@timestamp",
          "value": "{{last_crawled_at}}"
        }
      }
  ]
}
```

![Alt text](/img/setup6.png?raw=true "Uncheck ML options")

* Select 'load and overwrite' and then Save Pipeline

* Navigate back to Enterprise Search->Content->Elasticsearch indices->search-checkip

* Select 'Scheduling', 'Enable recurring crawls', 'Interval 24 hours'

![Alt text](/img/setup7.png?raw=true "Uncheck ML options")

* Select 'Crawl', 'crawl all domains' to create crawl initially. 

* Confirm you have one document in the index by selecting 'documents'

![Alt text](/img/setup8.png?raw=true "Uncheck ML options")

### Create Alert

* Navigate to Security->Alerts

![Alt text](/img/alert1.png?raw=true "Uncheck ML options")

* Select 'manage rules' then 'Create New Alert'

* Select 'New Terms', remove existing index patterns and add 'search-checkip' index

![Alt text](/img/alert2.png?raw=true "Uncheck ML options")

* Set the 'Custom Query' to 'body_content.enum: *' and 'Fields' and 'Continue'

![Alt text](/img/alert3.png?raw=true "Uncheck ML options")
![Alt text](/img/alert4.png?raw=true "Uncheck ML options")

* Set the name, description, severity

![Alt text](/img/alert5.png?raw=true "Uncheck ML options")

$ Set the 'Schedule' 24 hrs, 1 hour look back, the Continue

![Alt text](/img/alert6.png?raw=true "Uncheck ML options")

* Select whatever action you prefer, then 'Create & enable rule' to complete the setup










