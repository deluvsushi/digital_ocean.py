# digital_ocean.py
Web-API for [status.digitalocean.com](https://status.digitalocean.com) website to get status of all digitalocean services

## Example
```python
import digital_ocean
digital_ocean = digital_ocean.DigitalOcean()
status = digital_ocean.get_status()
print(status)
```
