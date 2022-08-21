from requests import get


class DigitalOcean:
	def __init__(self):
		self.api = "https://status.digitalocean.com/api/v2"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_summary(self):
		return get(
			f"{self.api}/summary.json",
			headers=self.headers).json()
	
	def get_status(self):
		return get(
			f"{self.api}/status.json",
			headers=self.headers).json()
	
	def get_components(self):
		return get(
			f"{self.api}/components.json",
			headers=self.headers).json()
	
	def get_all_incidents(self):
		return get(
			f"{self.api}/incidents.json",
			headers=self.headers).json()
	
	def get_unresolved_incidents(self):
		return get(
			f"{self.api}/incidents/unresolved.json",
			headers=self.headers).json()
	
	def get_upcoming_scheduled_maintenances(self):
		return get(
			f"{self.api}/scheduled-maintenances/upcoming.json",
			headers=self.headers).json()
			
	def get_active_scheduled_maintenances(self):
		return get(
			f"{self.api}/scheduled-maintenances/active.json",
			headers=self.headers).json()
			
	def get_all_scheduled_maintenances(self):
		return get(
			f"{self.api}/scheduled-maintenances.json",
			headers=self.headers).json()
