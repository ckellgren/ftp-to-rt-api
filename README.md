# ftp-to-rt-api
## FTP integration with RT API

#### Follow the format below to add a new location.


Location with up to 3 manually selected sources (via email):
```python
 {   
    'source': 'path to download file',
    'dealer_name': 'sender name',
    'location': 'location_id',
    'template': 'template_id',
    'sms': True #sms
    'autoselect': False,
    'urls': [
        'url_id 1',
        'url_id 2',
        'url_id 3',
    ],
    },
```    
Location with smart-suggested sources (via sms):
```python
    {   
    'source': 'path to download file',
    'dealer_name': 'sender name',
    'location': 'location_id',
    'template': 'template_id',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
```
Note: Email Requests will grab anything in the 'CustomerEmail' column and SMS Requests will grab a value from the 'CustomerCellPhone' column or 'CustomerHomePhone' in the case there is no 'CustomerCellPhone'.
