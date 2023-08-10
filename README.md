# checkip
Send an alert with the Elasticsearch Webcrawler or other connector's IP changes. 


Create a new webcrawler instance either pointed to 
```
{"processors": [
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
      }
       ]
}
```
