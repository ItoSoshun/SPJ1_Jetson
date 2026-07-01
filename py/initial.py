import requests

URL = "https://airoco.necolico.jp/data-api/latest?id=CgETViZ2&subscription-key=6b8aa7133ece423c836c38af01c59880"


def main() -> None:
	try:
		res = requests.get(URL, timeout=10)
		res.raise_for_status()
		data = res.json()
	except requests.RequestException as e:
		print(f"API request failed: {e}")
		return
	except ValueError as e:
		print(f"Failed to parse JSON: {e}")
		return

	if not isinstance(data, list) or len(data) < 2 or not isinstance(data[1], dict):
		print(f"Unexpected response format: {data}")
		return

	sensor = data[1]
	co2 = sensor.get("co2")
	name = sensor.get("sensorName")
	print(f"co2={co2},co2_type={type(co2)},name={name}")


if __name__ == "__main__":
	main()