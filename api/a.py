import requests

def main():
	res=requests.get("https://www.googleapis.com/youtube/v3/channels")
	data=res.json()
	a=data["error"]["code"]
	a+=a
	print(f"doubled error code is {a}")

if __name__=="__main__":
	main()